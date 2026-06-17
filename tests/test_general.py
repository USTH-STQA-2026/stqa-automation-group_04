"""
Logout & Language Tests (*Kiểm thử Đăng xuất & Chuyển ngôn ngữ*) — Library Book Borrowing System (*Hệ thống Mượn sách thư viện*)

Students must complete ALL 2 test cases in this file.
(*Sinh viên cần hoàn thành TẤT CẢ 2 test case trong file này.*)

Hints (*Gợi ý*):
    - Use login() helper to log in (*Dùng login() helper để đăng nhập*)
    - Logout button: 'flt-semantics[role="button"]:has-text("Đăng xuất")'
      (*Nút Đăng xuất*)
    - Language switch EN button: 'flt-semantics[role="button"]:has-text("EN")'
      (*Nút chuyển ngôn ngữ EN*)
    - After logout: page returns to login (has "Đăng nhập" button and "Email" input)
      (*Sau đăng xuất: trang quay về login*)
    - After switching to EN: text "Logout", "Borrow", "Search", "Library" may appear
      (*Sau chuyển EN: text tiếng Anh có thể xuất hiện*)
"""
import os
import time
import pytest
from conftest import (
    enable_flutter_semantics, flutter_fill, flutter_click_button,
    login, SCREENSHOT_DIR,
)


def test_logout(page, test_config):
    """TC-11: Logout success"""

    # [R] Reachability
    login(page, test_config)
    enable_flutter_semantics(page)

    page.wait_for_timeout(1000)

    # [I] Click Đăng xuất
    logout_btn = page.locator(
        'flt-semantics[role="button"]:has-text("Đăng xuất")'
    )

    assert logout_btn.count() > 0, \
        "Logout button not found"

    logout_btn.first.click()

    # Chờ hệ thống xử lý đăng xuất
    page.wait_for_timeout(3000)
    enable_flutter_semantics(page)

    # Chụp minh chứng
    page.screenshot(
        path=os.path.join(
            SCREENSHOT_DIR,
            "logout_success.png"
        )
    )

    # [R✓] Verify quay về màn hình login
    sem_text = " ".join(
        page.locator("flt-semantics").all_text_contents()
    )

    has_login = "Đăng nhập" in sem_text
    has_email = "Email" in sem_text

    assert has_login or has_email, \
        "Logout failed - login page not displayed"

def test_switch_language_to_english(page, test_config):
    """TC-12: Switch language to English"""

    # [R] Reachability
    login(page, test_config)
    enable_flutter_semantics(page)

    page.wait_for_timeout(1000)

    # [I] Chuyển sang tiếng Anh
    en_btn = page.locator(
        'flt-semantics[role="button"]:has-text("EN")'
    )

    assert en_btn.count() > 0, \
        "EN button not found"

    en_btn.first.click()

    # Chờ giao diện cập nhật
    page.wait_for_timeout(2000)
    enable_flutter_semantics(page)

    # Chụp minh chứng
    page.screenshot(
        path=os.path.join(
            SCREENSHOT_DIR,
            "switch_language_en.png"
        )
    )

    # [R✓] Verify
    sem_text = " ".join(
        page.locator("flt-semantics").all_text_contents()
    )

    has_logout = "Logout" in sem_text
    has_borrow = "Borrow" in sem_text
    has_library = "Library" in sem_text

    assert has_logout or has_borrow or has_library, \
        "Language was not switched to English"