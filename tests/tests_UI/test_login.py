
def test_login_success(page_logged):
    assert "OrangeHRM" in page_logged.page.title()

