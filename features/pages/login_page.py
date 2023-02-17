from features.credentials import EMAIL, PASSWORD
from features.pages.base_page import Page
from selenium.webdriver.common.by import By

class LoginPage(Page):

    def login_with_email_and_password(self):
        if not EMAIL or not PASSWORD:
            raise Exception("No credentials found!")

        self.driver.findElement(By.ID, "com.example.path:id/account_edit").sendKeys(EMAIL)
        self.driver.findElement(By.ID, "com.example.path:id/password_edit").sendKeys(PASSWORD)
        self.driver.find_element(By.ID, "com.example.path:id/action").click()
