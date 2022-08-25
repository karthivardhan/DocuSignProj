import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Approve_Documnets():
    def __init__(self, driver):
        self.driver = driver

        # Elements:
        self.manage_tab = "button[data-qa='header-MANAGE-tab-button']"
        self.action_required = "button[data-qa='action-required-count']"
        self.sign_button = "(//*[contains(@class,'olv-button')])[4]"
        self.continue_button = "action-bar-btn-continue"
        self.navigate_option = "navigate-btn"
        self.sign_option = "//*[contains(@class,'signature-tab-content')]"
        self.signing_reason = "signingReason"
        self.select_signing_reason = "//*[contains(text(),'I approve')]"
        self.dialog_submit = "button[data-qa='dialog-submit']"
        self.cfr_continue = "button[data-qa='cfr-continue']"
        self.finish_button = "button[data-qa='slide-up-bar-finish-button']"
        self.no_thanks_button = "button[data-qa='sign-next-no-thanks']"
        self.complete_sign = "action-bar-btn-signing-complete"

    def approve_document(self):
        self.driver.find_element('css selector', self.action_required).click()
        time.sleep(5)
        self.driver.find_element('xpath', self.sign_button).click()
        time.sleep(10)

    def sign(self):
        self.driver.find_element('id', self.continue_button).click()
        self.driver.find_element('id', self.navigate_option).click()
        self.driver.find_element('xpath', self.sign_option).click()
        main_window = self.driver.window_handles
        for handle in self.driver.window_handles:
            if handle != main_window:
                popup = handle
                self.driver.switch_to.window(popup)
        drop_down = self.driver.find_element('id', self.signing_reason)
        select_method = Select(drop_down)
        select_method.select_by_visible_text('I approve this document')
        # self.driver.find_element('xpath', self.select_signing_reason).click()
        self.driver.find_element('css selector', self.dialog_submit).click()
        time.sleep(5)
        # self.driver.switch_to.window(main_window)
        # time.sleep(5)
        # main_window2 = self.driver.window_handles
        # for handle2 in self.driver.window_handles:
        #     if handle2 != main_window2:
        #         popup = handle2
        #         self.driver.switch_to.window(popup)

        # my_alert2 = self.driver.switch_to.alert
        # text = my_alert2.text
        # assert text == 'Select Continue to be taken to a secure login page to enter your credentials'
        # print(my_alert2)
        self.driver.find_element('css selector', self.cfr_continue).click()
        time.sleep(5)
        # self.driver.switch_to.window(main_window2)
        # time.sleep(5)

        all_windows = self.driver.window_handles
        current_window = all_windows[0]
        new_window = all_windows[1]
        self.driver.switch_to.window(new_window)
        time.sleep(10)

    def complete_sign(self):
        self.driver.find_element('css selector', self.finish_button).click()
        self.driver.find_element('css selector', self.no_thanks_button)
        # self.driver.find_element('id', self.complete_sign)