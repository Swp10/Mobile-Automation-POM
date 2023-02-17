from selenium.webdriver.common.by import By
from .base_page import Page

class LaunchPage:

    def login_with_existing_account(self):
        self.click_on_element(self.By.ID, "com.example.path:id/btn_log_in").click()

    def create_new_account(self):
        self.click_on_element(self.By.ID, "com.example.path:id/action").click()
