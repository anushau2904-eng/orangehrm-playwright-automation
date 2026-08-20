from pages.basepage import BasePage

class LoginPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.txt_username = self.page.get_by_placeholder("Username")
        self.txt_password = self.page.get_by_placeholder("Password")
        self.btn_login_button = self.page.get_by_role("button",name="Login")

    def login(self, username, password):
        self.txt_username.fill(username)
        self.txt_password.fill(password)
        self.btn_login_button.click()