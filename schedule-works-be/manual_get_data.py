"""Retrive data from degreeworks and facotrs in 2FA."""
import time
import json
import os
import click
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
# import privateInfo
import devolpment_shortcut


@click.command()
@click.option(
    "--sid",
    "-s",
    metavar="STRING",
    help="Student ID.",
)
@click.option(
    "--passwd",
    "-p",
    metavar="STRING",
    help="Password for logging in.",
)
def get_json_data(sid, passwd):
    """Provide json data by providing studentID and password."""
    sid, passwd = sid.strip("'"), passwd.strip("'")
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )

    # max screen
    driver.maximize_window()

    # go to where
    driver.get("https://login.wayne.edu/")

    # find html id password and usrename
    username = driver.find_element("id", "accessid")
    password = driver.find_element("id", "passwd")

    # my info sent into the driver
    username.send_keys(sid)
    password.send_keys(passwd)

    # loginbutton clicky

    driver.find_element("id", "login-button").click()
    time.sleep(2)
    if "microsoft" in driver.current_url:
        driver.find_element("xpath", '//*[@id="idDiv_SAOTCS_Proofs"]/div[1]').click()
        # microsoft 2fa code
        while True:
            with open(
                "C:/Program Files/ScheduleWorks/schedule-works-be/2fa_code.txt",
                "r",
                encoding="utf-8",
            ) as infile:
                file_data = infile.read()
            if "done" in file_data:
                break
            time.sleep(5)
        code = re.findall("[+-]?\d+\.?\d*", file_data)
        driver.find_element("xpath", '//*[@id="idTxtBx_SAOTCC_OTC"]').send_keys(code)
        driver.find_element("xpath", '//*[@id="idSubmit_SAOTCC_Continue"]').click()

    # authentication finished, endpoints available
    time.sleep(2)
    driver.get("https://degreeworks.wayne.edu/worksheets/WEB31")
    time.sleep(2)
    driver.get("https://degreeworks.wayne.edu/api/students/myself")
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, features="lxml")
    dict_from_json = json.loads(soup.find("body").text)
    if not os.path.exists("C:/Program Files/ScheduleWorks/data"):
        os.makedirs("C:/Program Files/ScheduleWorks/data")

    with open(
        "C:/Program Files/ScheduleWorks/data/userData.json", "w+", encoding="utf-8"
    ) as outfile:
        json.dump(dict_from_json, outfile, indent=4)
    user_info = devolpment_shortcut.extract_user_info()
    audit_url = (
        "https://degreeworks.wayne.edu/api/audit?studentId={sid}"
        + "&school={school}"
        + "&degree={degree}"
        + "&is-process-new=false"
        + "&audit-type=AA"
        + "&auditId="
        + "&include-inprogress=true"
        + "&include-preregistered=true"
        + "&aid-term="
    ).format(sid=user_info["id"], school=user_info["level"], degree=user_info["degree"])
    driver.get(audit_url)
    soup = BeautifulSoup(driver.page_source, features="lxml")
    dict_from_json = json.loads(soup.find("body").text)
    with open(
        "C:/Program Files/ScheduleWorks/data/classData.json", "w+", encoding="utf-8"
    ) as outfile:
        json.dump(dict_from_json, outfile, indent=4)

    driver.close()
    devolpment_shortcut.view_course_history()
    devolpment_shortcut.view_degree_requirements()


if __name__ == "__main__":
    get_json_data()
