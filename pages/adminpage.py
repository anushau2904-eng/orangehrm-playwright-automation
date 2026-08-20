from playwright.sync_api import expect
from pages.basepage import BasePage


class AdminPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.btn_adding_user = page.get_by_role("button" , name= "Add")
        self.drop_user_role = page.locator(".oxd-select-text").nth(0)
        self.drop_status = page.locator(".oxd-select-text").nth(1)
        self.input_emp_name = page.get_by_placeholder("Type for hints...")
        self.input_username = page.locator("//label[text()='Username' and contains(@class,'oxd-input-field-required')]"
        "/parent::div/following-sibling::div//input")
        self.input_pwd = page.locator("input[type='password']").nth(0)
        self.input_confirm_pwd = page.locator("input[type='password']").nth(1)
        self.btn_save = page.get_by_role("button", name = "Save")
        self.btn_cancel = page.get_by_role("button" , name= "Cancel")
        self.input_serach_user = page.locator("//label[text()='Username' and not(contains(@class,'oxd-input-field-required'))]"
        "/parent::div/following-sibling::div//input")
        self.btn_search = page.get_by_role("button",name="Search")
        self.btn_confirm_delete = page.get_by_role("button", name="Yes, Delete")

    def add_userbutton(self):
        self.btn_adding_user.click()

    # def select_user_role(self,Role):
    #     self.drop_user_role.click()
    #     self.page.get_by_role("listbox").get_by_text(Role).click  

    
    def select_employee(self, empname):
        self.input_emp_name.fill(empname)
        self.page.wait_for_timeout(1000)              
        dropdown = self.page.locator("[role='listbox']")
        expect(dropdown).to_be_visible()
        dropdown.locator("div").first.click()       
        
        
    def add_user(self,userrole,status,empname,username,pwd):
        self.drop_user_role.click()
        self.page.get_by_role("option", name=userrole).click()
        self.drop_status.click()
        self.page.get_by_role("option", name=status).click()
        self.select_employee(empname)
        self.input_username.fill(username)
        self.input_pwd.fill(pwd)
        self.input_confirm_pwd.fill(pwd)
        self.btn_save.click()
           
        
    
    def search_user(self,username):
        self.input_serach_user.fill(username)
        self.btn_search.click()

    def get_user_row(self, username):
        return self.page.get_by_role("row").filter(has_text = username)

    def delete_user(self,username):
        row=self.get_user_row(username)
        expect(row).to_be_visible()
        row.locator("button").first.click()
        expect(self.btn_confirm_delete).to_be_visible()
        self.btn_confirm_delete.click()


    # def get_user_row(self,username):
    #     return self.page.locator(f"//div[@role='row'][.//*[contains(text(),'{username}')]]")

    # def verify_user_exists(self, username):
    #     return self.get_user_row(username)
    
    # def delete_user(self,username):
    #     row=self.get_user_row(username)
    #     expect(row).to_be_visible()
    #     row.locator("button").first.click()

    # def confirm_delete(self):
    #     expect(self.Confirm_Delete_button).to_be_visible()
    #     self.Confirm_Delete_button.click()    
    



          
               
         
    