from pages.basepage import BasePage

class NavigationPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.adming_menu = self.page.get_by_role("link", name="Admin")

    def navigate_to_admin(self):
        self.adming_menu.click()
        