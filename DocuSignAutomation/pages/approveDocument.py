import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Approve_Documnets():
    def __init__(self, driver):
        self.driver = driver

        # Elements:
        self.manage_tab = "button[data-qa='header-MANAGE-tab-button']"
        self.action_required = "button[data-qa='action-required-count']"

    def approve_document(self):
        pass
