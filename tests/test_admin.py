import pytest
from playwright.sync_api import expect

from utils.configreader import ConfigReader
from utils.excelreader import ExcelReader
from utils.logger import Logger
from utils.screenshot import ScreenshotUtil
from pages.loginpage import LoginPage
from pages.navigationpage import NavigationPage
from pages.adminpage import AdminPage

@pytest.mark.login
  
def test_naviage_page(logged_in_page):
     
     nav = NavigationPage(logged_in_page)
     nav.navigate_to_admin()
     expect(logged_in_page.get_by_role("heading", name="Admin")).to_be_visible()
     ScreenshotUtil.capture(logged_in_page,"admin_page")

def test_adding_user(logged_in_page):
     
     users = ExcelReader.get_user_data("userdata.xlsx")
     user = users[0]
     userrole = user["Role"]
     status  = user["Status"]
     empname = user["empname"]
     username = user["Username"]
     pwd = user["Password"]
     nav = NavigationPage(logged_in_page)
     nav.navigate_to_admin()
     admin = AdminPage(logged_in_page)

     admin.add_userbutton()
     admin.add_user(userrole,status,empname,username,pwd)     
     
     

     
     expect(logged_in_page.get_by_role("heading" ,name="Admin")).to_be_visible()
     admin.search_user(username)
     ScreenshotUtil.capture(logged_in_page,f"user_create_{username}")

def test_delete_user(logged_in_page):
     nav = NavigationPage(logged_in_page)
     nav.navigate_to_admin()
     admin = AdminPage(logged_in_page)
     admin.add_userbutton()
     users = ExcelReader.get_user_data("userdata.xlsx")
     user = users[1]
     userrole = user["Role"]
     status = user["Status"]
     empname = user["empname"]
     username = user["Username"]
     pwd = user["Password"]
     admin.add_user(userrole, status,empname,username,pwd)
     admin.delete_user(username)
     ScreenshotUtil.capture(logged_in_page,f"user_deleted_{username}")

    
    

# def create_user(page):
#     admin = AdminPage(page)
#     users = ExcelReader.get_user_data("userdata.xlsx")
#     for user in users:
#         admin.add_button()
#         admin.add_user(user["role"],
#             user["status"],
#             user["employee_name"],
#             user["username"],
#             user["password"])
#     ScreenshotUtil.capture(page,f"user created :{user["username"]}")


    

    
