import privateInfo
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def retrive_data():

    chrome_options = Options()
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--headless")
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
    with open("data/userData.json", 'w+') as outfile:
        json.dump(dict_from_json, outfile, indent=4)
    audit_url = "https://degreeworks.wayne.edu/api/audit?studentId={sid}&school={school}&degree={degree}&is-process-new=false&audit-type=AA&auditId=&include-inprogress=true&include-preregistered=true&aid-term=".format(
        sid="004878839", school="UG", degree="BSCS")
    # driver.get(audit_url)
    # time.sleep(30)


def extract_user_info():
    with open('data/userData.json') as f:
        user_data = json.load(f)
    print(user_data["_embedded"]["students"][0]["id"])
    print(user_data["_embedded"]["students"][0]["goals"][0]["school"]["key"])
    print(user_data["_embedded"]["students"][0]["goals"][0]["degree"]["key"])


retrive_data()
