class BasePage:

    def __init__(self, page):
        self.page = page

    def get_title(self):
        return self.page.title()

    def get_url(self):
        return self.page.url

    def refresh(self):
        self.page.reload()

    def go_back(self):
        self.page.go_back()

    def go_forward(self):
        self.page.go_forward()

    def wait_for_page_load(self):
        self.page.wait_for_load_state("load")

    def take_screenshot(self, path):
        self.page.screenshot(path=path)