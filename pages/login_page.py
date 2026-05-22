from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email = page.locator("#email")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-btn")
        self.error = page.locator("#login-error")
        
    def open(self, base_url: str):
        self.page.goto(base_url)

    def login(self, email: str, password: str):
        self.email.fill(email)
        self.password.fill(password)
        self.login_button.click()

    def verify_error(self, message: str):
        expect(self.error).to_have_text(message)