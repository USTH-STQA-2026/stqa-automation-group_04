"""
Borrow & Return Tests (*Kiểm thử Mượn & Trả sách*) — Library Book Borrowing System (*Hệ thống Mượn sách thư viện*)

Students must complete ALL 3 test cases in this file.
(*Sinh viên cần hoàn thành TẤT CẢ 3 test case trong file này.*)

Hints (*Gợi ý*):
    - Use login() helper to log in (*Dùng login() helper để đăng nhập*)
    - "Mượn / Trả" tab: role="tab", aria-label="Mượn / Trả"
    - Available books have "Có sẵn" in aria-label, borrowed books have "Đang mượn"
      (*Sách "Có sẵn" có aria-label chứa "Có sẵn", sách "Đang mượn" chứa "Đang mượn"*)
    - Borrow button: 'flt-semantics[role="button"]:has-text("Mượn sách này")'
      (*Nút mượn*)
    - After clicking "Mượn sách này", a confirmation dialog appears — click "Mượn" again
      (*Sau khi click "Mượn sách này" sẽ hiện dialog xác nhận — cần click nút "Mượn" lần nữa*)
    - Return button: 'flt-semantics[role="button"]:has-text("Trả sách")'
      (*Nút trả*)
"""
import os
import time
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    login, SCREENSHOT_DIR,
)
def test_borrow_book(page, test_config):
    """TC-08: Borrow an available book"""

    # [R] Reachability
    login(page, test_config)
    enable_flutter_semantics(page)

    page.wait_for_timeout(1000)

    # [I] Click nút "Mượn sách này"
    borrow_buttons = page.locator(
        'flt-semantics[role="button"]:has-text("Mượn sách này")'
    )

    assert borrow_buttons.count() > 0, \
        "No borrow button found"

    borrow_buttons.first.click()

    # Chờ dialog xác nhận
    page.wait_for_timeout(1000)
    enable_flutter_semantics(page)

    # Kiểm tra dialog xuất hiện
    sem_text = " ".join(
        page.locator("flt-semantics").all_text_contents()
    )

    assert "Xác nhận mượn sách" in sem_text, \
        "Borrow confirmation dialog not displayed"

    # Click nút xác nhận "Mượn"
    confirm_btn = page.locator(
        'flt-semantics[role="button"]:text-is("Mượn")'
    )

    assert confirm_btn.count() > 0, \
        "Confirm button not found"

    confirm_btn.first.click()

    page.wait_for_timeout(2000)
    enable_flutter_semantics(page)

    # Chụp minh chứng
    page.screenshot(
        path=os.path.join(
            SCREENSHOT_DIR,
            "borrow_book.png"
        )
    )

    # [R✓] Verify kết quả
    sem_text = " ".join(
        page.locator("flt-semantics").all_text_contents()
    )

    has_borrowed = "Đang mượn" in sem_text
    has_success = "thành công" in sem_text.lower()

    assert has_borrowed or has_success, \
        "Borrow operation failed"
def test_view_borrowed_books(page, test_config):
    """TC-09: View borrowed books list (*Xem danh sách sách đang mượn — tab Mượn / Trả*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → switch to "Mượn / Trả" tab → verify borrowed books are shown.
        (*Đăng nhập → chuyển sang tab "Mượn / Trả" → kiểm tra có sách đang mượn.*)

    Hints (*Gợi ý*):
        - Click tab: page.locator('flt-semantics[role="tab"][aria-label="Mượn / Trả"]')
        - Verify: books with "Đang mượn" in aria-label, or "Trả sách" button exists
          (*Kiểm tra: có sách với aria-label chứa "Đang mượn" hoặc có nút "Trả sách"*)
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")


def test_return_book(page, test_config):
    """TC-10: Return a borrowed book (*Trả sách đang mượn*)

    🔴 NOT COMPLETED (*CHƯA HOÀN THÀNH*)

    Description (*Mô tả*):
        Log in → go to "Mượn / Trả" tab → click "Trả sách" → verify book is returned.
        (*Đăng nhập → tab "Mượn / Trả" → click "Trả sách" → kiểm tra sách được trả.*)

    Hints (*Gợi ý*):
        - Switch to "Mượn / Trả" tab (*Chuyển tab "Mượn / Trả"*)
        - Find return button: page.locator('flt-semantics[role="button"]:has-text("Trả sách")')
          (*Tìm nút "Trả sách"*)
        - Click and verify status change or success message
          (*Click và kiểm tra sách chuyển trạng thái hoặc có thông báo thành công*)
    """
    # TODO: Students implement here (Sinh viên viết code ở đây)
    pytest.skip("Not implemented — student must complete (Chưa hoàn thành)")
