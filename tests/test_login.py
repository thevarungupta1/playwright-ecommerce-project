import allure

from pages.login_page import LoginPage

@allure.feature("Login")
@allure.story("Valid Login")
def test_valid_login(page, base_url):
    login_page = LoginPage(page)

    with allure.step("Open login page"):
        login_page.open(base_url)

    with allure.step("Login with valid credentials"):
        login_page.login("admin@test.com", "Admin@123");


@allure.feature("Login")
@allure.story("InValid Login")
def test_invalid_login(page, base_url):
    login_page = LoginPage(page)
   
    login_page.open(base_url)   
    login_page.login("wrong@test.com", "Admin@123");
    login_page.verify_error("Invalid email or password")


    