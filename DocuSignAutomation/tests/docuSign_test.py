from pages import constants as constants
from pages.loginPage import Login_Page
from pages.homePage import Home_Page
from tests.conftest import Scroll
from pages.addSign import Add_Sign
from pages.approveDocument import Approve_Documnets
import pytest


@pytest.mark.usefixtures("test_setup")
class TestNew():
    def test_loginPage(self):
        driver = self.driver
        self.driver.get(constants.baseUrl)
        login = Login_Page(driver)
        login.login_page(constants.senderEmail, constants.senderPassword)
        home = Home_Page(driver)
        home.upload_documents(
            constants.approver1Name, constants.approver1Email, constants.approver2Name, constants.approver2Email,
            True)
        scroll = Scroll(driver)
        scroll.scroll_page()
        sign = Add_Sign(driver)
        sign.add_sign()
        
        # Upload pdf file
        home = Home_Page(driver)
        home.upload_documents(
            constants.approver1Name, constants.approver1Email, constants.approver2Name, constants.approver2Email)
        # scroll = Scroll(driver)
        # scroll.scroll_page()
        sign = Add_Sign(driver)
        sign.add_sign()
        scroll = Scroll(driver)
        scroll.logout()

        # Login as approver1
        self.driver.get(constants.baseUrl)
        login = Login_Page(driver)
        login.login_page(constants.approver1Email, constants.approver1Password)
        approve = Approve_Documnets(driver)
        approve.approve_document()
        login = Login_Page(driver)
        login.login_page(constants.approver1Email, constants.approver1Password)
        sign = Approve_Documnets(driver)
        sign.sign()
        login = Login_Page(driver)
        login.login_page(constants.approver1Email, constants.approver1Password)
        complete = Approve_Documnets(driver)
        complete.complete_sign()