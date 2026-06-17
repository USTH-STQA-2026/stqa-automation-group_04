"""
Search & Filter Tests (*Kiểm thử Tìm kiếm & Lọc sách*) — Library Book Borrowing System (*Hệ thống Mượn sách thư viện*)

Students must complete ALL 4 test cases in this file.
(*Sinh viên cần hoàn thành TẤT CẢ 4 test case trong file này.*)

Hints (*Gợi ý*):
    - After logging in, use flutter_fill() to type into the search box
      (*Sau khi đăng nhập, dùng flutter_fill() để nhập vào ô tìm kiếm*)
    - Search box aria-label: "Tìm kiếm theo tên sách hoặc tác giả..."
    - Category filter aria-label: "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)"
    - Each book card has role="group" and aria-label containing book info
      (*Mỗi card sách có role="group" và aria-label chứa thông tin sách*)
    - Use login() helper from conftest.py to log in before testing
      (*Dùng login() helper từ conftest.py để đăng nhập trước khi test*)
"""
import os
import time
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    login, SCREENSHOT_DIR,
)


def test_search_book_by_name(page, test_config):
    """TC-04: Search book by name – results found"""

    # [R] Reachability: Đăng nhập và vào màn hình danh sách sách
    login(page, test_config)

    # [I] Infection: Nhập từ khóa tìm kiếm
    flutter_fill(
        page,
        "Tìm kiếm theo tên sách hoặc tác giả...",
        "Flutter"
    )

    # [P] Propagation: Chờ kết quả tìm kiếm cập nhật
    page.wait_for_timeout(1000)

    # Chụp ảnh minh chứng
    page.screenshot(
        path=os.path.join(
            SCREENSHOT_DIR,
            "search_book_by_name.png"
        )
    )

    # [R✓] Revealability: Kiểm tra có sách Flutter xuất hiện
    flutter_books = page.locator(
        'flt-semantics[aria-label*="Flutter"]'
    )

    assert flutter_books.count() > 0, \
        "No books containing 'Flutter' were found in search results"

def test_search_book_no_result(page, test_config):
    """
    TC-05: Verify search returns no results for a non-existent keyword.
    """

    # [R] Reachability
    login(page, test_config)
    enable_flutter_semantics(page)

    # [I] Infection: nhập từ khóa không tồn tại
    flutter_fill(
        page,
        "Tìm kiếm theo tên sách hoặc tác giả...",
        "xyz_khong_ton_tai_12345"
    )

    page.wait_for_timeout(2000)

    # Chụp minh chứng
    page.screenshot(
        path=os.path.join(
            SCREENSHOT_DIR,
            "search_book_no_result.png"
        )
    )

    # [R✓] Revealability
    books = page.locator(
        'flt-semantics[role="group"][aria-label*="Mã: BOOK"]'
    )

    assert books.count() == 0, \
        "Search returned books for a non-existent keyword"

def test_filter_by_category(page, test_config):
    """TC-06: Filter books by category 'Công nghệ'"""

    # [R] Reachability: Đăng nhập vào hệ thống
    login(page, test_config)

    # [I] Infection: Nhập bộ lọc thể loại
    flutter_fill(
        page,
        "Lọc theo thể loại (VD: Công nghệ, Kinh tế...)",
        "Công nghệ"
    )

    # Chờ kết quả lọc cập nhật
    page.wait_for_timeout(1000)

    # Chụp ảnh minh chứng
    page.screenshot(
        path=os.path.join(
            SCREENSHOT_DIR,
            "filter_by_category.png"
        )
    )

    # [R✓] Revealability: Lấy danh sách sách sau khi lọc
    books = page.locator(
        'flt-semantics[role="group"][aria-label*="Mã: BOOK"]'
    )

    book_count = books.count()

    assert book_count > 0, \
        "No books were displayed after filtering by category"

    for i in range(book_count):
        book_info = books.nth(i).get_attribute("aria-label")

        assert "Công nghệ" in book_info, \
            f"Book does not belong to 'Công nghệ' category: {book_info}"


def test_search_by_author(page, test_config):
    """TC-07: Search book by author name"""

    # [R] Reachability: Đăng nhập vào hệ thống
    login(page, test_config)

    # [I] Infection: Nhập tên tác giả cần tìm
    flutter_fill(
        page,
        "Tìm kiếm theo tên sách hoặc tác giả...",
        "Nguyễn Minh Đức"
    )

    # Chờ kết quả tìm kiếm cập nhật
    page.wait_for_timeout(1000)

    # Chụp ảnh minh chứng
    page.screenshot(
        path=os.path.join(
            SCREENSHOT_DIR,
            "search_by_author.png"
        )
    )

    # [R✓] Revealability: Kiểm tra có kết quả chứa tên tác giả
    author_books = page.locator(
        'flt-semantics[aria-label*="Nguyễn Minh Đức"]'
    )

    assert author_books.count() > 0, \
        "No books by author 'Nguyễn Minh Đức' were found"
