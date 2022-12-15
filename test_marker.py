import allure
import pytest
import webdrivermanager
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def get_data():
    return [
        ("usertest", "shaikfaruk"),
        ("paste", "shaik@123")

    ]


@pytest.mark.parametrize("username,password", get_data())
def test_dologin(username,password):
  print(username,"----",password)
  driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
  driver.get("http://www.google.com")
  allure.attach(driver.get_screenshot_as_png(),name="test_dologin",attachment_type=AttachmentType.PNG)

# @pytest.fixture(scope="module")
# def setup():
#     print("db connection")
#     yield
#     print("db colsed")
#
#
# @pytest.fixture(scope="function")
# def before():
#     print("login")
#     yield
#     print("enter")
#
#
# def test(setup, before):
#     print("do login")
#
#
# @pytest.mark.functional
# def test_login():
#     print("hello")
#
#
# @pytest.mark.regression
# def test_logout():
#     print("logout")
#
#
# @pytest.mark.functional
# def test_compose():
#     print("compose")
#
#
# @pytest.mark.skip
# def test_skip():
#     print("skipping test")