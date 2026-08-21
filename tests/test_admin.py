import pytest
from playwright.sync_api import expect

from utils.configreader import ConfigReader
from utils.logger import Logger
from utils.screenshot import ScreenshotUtil
from pages.loginpage import LoginPage
from pages.navigationpage import NavigationPage
from pages.adminpage import AdminPage
from utils.testdatagenerator import TestDataGenerator

@pytest.mark.login
  
def test_naviage_page(logged_in_page):
     
     nav = NavigationPage(logged_in_page)
     nav.navigate_to_admin()
     expect(logged_in_page.get_by_role("heading", name="Admin")).to_be_visible()
     ScreenshotUtil.capture(logged_in_page,"admin_page")

def test_adding_user(logged_in_page):
     username = TestDataGenerator.random_username()
     pwd = TestDataGenerator.random_password()
     empname = TestDataGenerator.random_employee_prefix()
     nav = NavigationPage(logged_in_page)
     nav.navigate_to_admin()
     admin = AdminPage(logged_in_page)

     admin.add_userbutton()
     admin.add_user(empname,username,pwd)  

     expect(logged_in_page.get_by_role("heading" ,name="Admin")).to_be_visible()
     admin.search_user(username)
     ScreenshotUtil.capture(logged_in_page,f"user_create_{username}")

def test_delete_user(logged_in_page):
     nav = NavigationPage(logged_in_page)
     nav.navigate_to_admin()
     admin = AdminPage(logged_in_page)
     admin.add_userbutton()
     username = TestDataGenerator.random_username()
     pwd = TestDataGenerator.random_password()
     empname = TestDataGenerator.random_employee_prefix()     
     admin.add_user(empname,username,pwd)
     admin.search_user(username)
     admin.delete_user(username)
     ScreenshotUtil.capture(logged_in_page,f"user_deleted_{username}")

    
    



    

    
