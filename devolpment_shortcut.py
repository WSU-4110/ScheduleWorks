"""
Provide access to data retrival from degreeworks using tokens as well as data parsing methods.
Uses selenium to retrive data and beautifulSoup to parse it.
"""

import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import privateInfo


def retrive_data():
    """Retrive data given certain cookie information to shortcut 2FA."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options)

    # max screen
    driver.maximize_window()
    driver.get("https://degreeworks.wayne.edu/favicon.ico")
    driver.delete_all_cookies()
    driver.add_cookie(
        {'name': 'REFRESH_TOKEN', 'value': privateInfo.get_refresh_token()})
    driver.add_cookie(
        {'name': 'X-AUTH-TOKEN', 'value': privateInfo.get_x_auth()})
    driver.add_cookie(
        {'name': 'NAME', 'value': '%20Mazen%20A%20Mirza'})

    driver.get("https://degreeworks.wayne.edu/api/students/myself")
    soup = BeautifulSoup(driver.page_source, features="lxml")
    dict_from_json = json.loads(soup.find("body").text)
    with open("data/userData.json", 'w+', encoding="utf-8") as outfile:
        json.dump(dict_from_json, outfile, indent=4)

    user_info = extract_user_info()

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


def extract_user_info():
    """Extract user information from json file and returns relavant information in a dict."""
    try:
        with open('data/userData.json', encoding="utf-8") as file:
            user_data = json.load(file)
    except FileNotFoundError as error:
        raise error
    user_information = {}
    user_information["name"] = user_data["_embedded"]["students"][0]["name"]
    user_information["term_code"] = user_data["_embedded"]["students"][0]["activeTerm"]
    user_information["id"] = user_data["_embedded"]["students"][0]["id"]
    user_information["level"] = user_data["_embedded"]["students"][0]["goals"][0]["school"]["key"]
    user_information["degree"] = user_data["_embedded"]["students"][0]["goals"][0]["degree"]["key"]
    return user_information


if __name__ == "__main__":
    retrive_data()
    # extract_user_info()
