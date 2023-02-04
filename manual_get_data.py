"""Retrive data from degreeworks and facotrs in 2FA."""
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import privateInfo


def manual_endpoints():
    """something descriptive when this is done."""
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options)

    # max screen
    driver.maximize_window()

    # go to where
    driver.get(
        "https://login.wayne.edu/" +
        "?destination_url=https%3A%2F%2Facademica.aws.wayne.edu%2Fcas%2Flogin%3Fservice%3D" +
        "https%253A%252F%252Fdegreeworks.wayne.edu%253A443%252Flogin%252Fcas")

    # find html id password and usrename
    username = driver.find_element("id", "accessid")
    password = driver.find_element("id", "passwd")

    # my info sent into the driver
    username.send_keys("hh8001")
    password.send_keys(privateInfo.getPass())

    # loginbutton clicky
    driver.find_element("id", "login-button").click()
    time.sleep(2)
    driver.find_element(
        "xpath", "//*[@id=\"idDiv_SAOTCS_Proofs\"]/div[1]/div/div").click()
    # microsoft 2fa code
    code = input("code: ")
    driver.find_element(
        "xpath", "//*[@id=\"idTxtBx_SAOTCC_OTC\"]").send_keys(code)
    driver.find_element(
        "xpath", "//*[@id=\"idSubmit_SAOTCC_Continue\"]").click()
    # authentication finished, endpoints available
    time.sleep(10)
    driver.get("https://degreeworks.wayne.edu/worksheets/WEB31")

    time.sleep(500000)


if __name__ == "__main__":
    manual_endpoints()
