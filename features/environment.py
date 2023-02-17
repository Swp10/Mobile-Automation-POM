from appium import webdriver
from app.application import Application
from .pages.launch_page import LaunchPage

desired_caps = {
    "appium:deviceName": "Nexus_5X",
    "platformName": "Android",
    "appium:platformVersion": "12.0",
    "appium:app": "/Users/Apps/com.example.path.apk",
    "appium:automationName": "uiautomator2"
}

driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_caps)


def before_feature(context, feature):
    context.driver.implicitly_wait(30)
    context.app = Application(context.driver)


def after_feature(context, feature):
    context.driver.quit()
