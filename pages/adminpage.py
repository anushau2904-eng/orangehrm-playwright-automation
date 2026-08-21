from playwright.sync_api import expect
from pages.basepage import BasePage
import random


class AdminPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.btn_adding_user = page.get_by_role("button" , name= "Add")
        self.drop_user_role = page.locator(".oxd-select-text").nth(0)
        self.drop_status = page.locator(".oxd-select-text").nth(1)
        self.input_emp_name = page.get_by_placeholder("Type for hints...")
        self.input_username = page.locator("//label[text()='Username']"
        "/parent::div/following-sibling::div//input")
        self.input_pwd = page.locator("input[type='password']").nth(0)
        self.input_confirm_pwd = page.locator("input[type='password']").nth(1)
        self.btn_save = page.get_by_role("button", name = "Save")
        self.btn_cancel = page.get_by_role("button" , name= "Cancel")
        self.input_serach_user = page.locator("//label[text()='Username']"
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
                     
        dropdown = self.page.locator("[role='listbox']")
        expect(dropdown).to_be_visible()
        searching = dropdown.get_by_text("Searching....", exact=True)
        expect(searching).to_be_hidden()
        option = dropdown.locator(".oxd-autocomplete-option").first
        expect(option).to_be_visible()
        option.click()
        
    def select_role(self):
        self.drop_user_role.click()       
        dropdown = self.page.get_by_role("listbox")
        expect(dropdown).to_be_visible()
        role = random.choice(["Admin", "ESS"])
        option = dropdown.get_by_role("option", name=role, exact=True)
        expect(option).to_be_visible()
        option.click()
        expect(self.drop_user_role).to_contain_text(role)
        

    def select_status(self):
        self.drop_status.click()
        dropdown = self.page.get_by_role("listbox")
        expect(dropdown).to_be_visible()
        status = random.choice(["Enabled", "Disabled"])
        option = dropdown.get_by_role("option", name=status, exact=True)
        expect(option).to_be_visible()
        option.click()
        expect(self.drop_status).to_contain_text(status)
        
   
        
        
    def add_user(self,empname,username,pwd):
        self.select_role()
        self.select_status()
        self.select_employee(empname)
        # expect(self.input_username).to_be_visible()
        self.input_username.fill(username)
        expect(self.input_username).to_have_value(username)
        self.input_pwd.fill(pwd)
        expect(self.input_pwd).to_have_value(pwd)
        self.input_confirm_pwd.fill(pwd)
        expect(self.input_confirm_pwd).to_have_value(pwd)
        expect(self.btn_save).to_be_enabled()
        self.btn_save.click()
           
        
    
    def search_user(self,username):
        expect(self.input_serach_user).to_be_visible()
        expect(self.input_serach_user).to_be_enabled()
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
    



          
               
         
    