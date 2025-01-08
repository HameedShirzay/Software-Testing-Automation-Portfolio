from pages.login_page import LoginPage


def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.click_login_icon()
    login_page.login('hameedshirzay1@gmail.com', "1d3f1db63842ba")

    # Validate login success (modify based on your application behavior)
    assert "Market Mate" in driver.title

