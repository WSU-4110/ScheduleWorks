"""Retrive data from degreeworks and facotrs in 2FA."""
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import privateInfo
import devolpment_shortcut


def two_fa(sid,passwd):
    """something descriptive when this is done."""
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options)

    # max screen
    driver.maximize_window()

    # go to where
    driver.get(
        "https://login.wayne.edu/")

    # find html id password and usrename
    username = driver.find_element("id", "accessid")
    password = driver.find_element("id", "passwd")

    # my info sent into the driver
    username.send_keys(sid)
    password.send_keys(passwd)

    # loginbutton clicky
    driver.find_element("id", "login-button").click()
    time.sleep(1)
    
    driver.find_element(
        "xpath", "//*[@id=\"idDiv_SAOTCS_Proofs\"]/div[1]/div/div").click()
    # microsoft 2fa code
    time.sleep(10)
    code = input("code: ")
    driver.find_element(
        "xpath", "//*[@id=\"idTxtBx_SAOTCC_OTC\"]").send_keys(code)
    driver.find_element(
        "xpath", "//*[@id=\"idSubmit_SAOTCC_Continue\"]").click()
    
    # authentication finished, endpoints available

    time.sleep(3)
    driver.get("https://degreeworks.wayne.edu/worksheets/WEB31")
    time.sleep(3)
    driver.get("https://degreeworks.wayne.edu/api/students/myself")
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, features="lxml")
    dict_from_json = json.loads(soup.find("body").text)

    if not os.path.exists('data'):
        os.makedirs('data')

    with open("data/userData.json", 'w+', encoding="utf-8") as outfile:
        json.dump(dict_from_json, outfile, indent=4)

    user_info = devolpment_shortcut.extract_user_info()

    audit_url = ("https://degreeworks.wayne.edu/api/audit?studentId={sid}" +
                 "&school={school}" +
                 "&degree={degree}" +
                 "&is-process-new=false" +
                 "&audit-type=AA" +
                 "&auditId=" +
                 "&include-inprogress=true" +
                 "&include-preregistered=true" +
                 "&aid-term=").format(
        sid=user_info["id"], school=user_info["level"], degree=user_info["degree"])

    driver.get(audit_url)
    soup = BeautifulSoup(driver.page_source, features="lxml")
    dict_from_json = json.loads(soup.find("body").text)
    with open("data/classData.json", 'w+', encoding="utf-8") as outfile:
        json.dump(dict_from_json, outfile, indent=4)

def login_only(sid,passwd):
    """something descriptive when this is done."""
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options)

    # max screen
    driver.maximize_window()

    # go to where
    driver.get(
        "https://login.wayne.edu/")

    # find html id password and usrename
    username = driver.find_element("id", "accessid")
    password = driver.find_element("id", "passwd")

    # my info sent into the driver
    username.send_keys(sid)
    password.send_keys(passwd)

    # loginbutton clicky
    driver.find_element("id", "login-button").click()
    time.sleep(1)
    # authentication finished, endpoints available

    time.sleep(3)
    driver.get("https://degreeworks.wayne.edu/worksheets/WEB31")
    time.sleep(3)
    driver.get("https://degreeworks.wayne.edu/api/students/myself")
    time.sleep(3)

    soup = BeautifulSoup(driver.page_source, features="lxml")
    dict_from_json = json.loads(soup.find("body").text)

    if not os.path.exists('data'):
        os.makedirs('data')

    with open("data/userData.json", 'w+', encoding="utf-8") as outfile:
        json.dump(dict_from_json, outfile, indent=4)

    user_info = devolpment_shortcut.extract_user_info()

    audit_url = ("https://degreeworks.wayne.edu/api/audit?studentId={sid}" +
                 "&school={school}" +
                 "&degree={degree}" +
                 "&is-process-new=false" +
                 "&audit-type=AA" +
                 "&auditId=" +
                 "&include-inprogress=true" +
                 "&include-preregistered=true" +
                 "&aid-term=").format(
        sid=user_info["id"], school=user_info["level"], degree=user_info["degree"])

    driver.get(audit_url)
    soup = BeautifulSoup(driver.page_source, features="lxml")
    dict_from_json = json.loads(soup.find("body").text)
    with open("data/classData.json", 'w+', encoding="utf-8") as outfile:
        json.dump(dict_from_json, outfile, indent=4)


if __name__ == "__main__":
    two_fa("ha5135",privateInfo.getPass())
    devolpment_shortcut.view_degree_requirements()
    devolpment_shortcut.view_course_history()
