"""
Provide access to data retrival from degreeworks using tokens as well as data parsing methods.

Uses selenium to retrive data and beautifulSoup to parse it.
"""
import time
import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# import privateInfo


def retrive_data(refresh_token: str, token: str, name: str) -> None:
    """Retrive data given certain cookie information to shortcut 2FA."""
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )
    # max screen
    driver.maximize_window()
    driver.get("https://degreeworks.wayne.edu/favicon.ico")
    driver.delete_all_cookies()
    driver.add_cookie({"name": "REFRESH_TOKEN", "value": refresh_token})
    driver.add_cookie({"name": "X-AUTH-TOKEN", "value": token})
    driver.add_cookie({"name": "NAME", "value": name})

    driver.get("https://degreeworks.wayne.edu/api/students/myself")
    soup = BeautifulSoup(driver.page_source, features="lxml")
    dict_from_json = json.loads(soup.find("body").text)

    if not os.path.exists("C:/Program Files/ScheduleWorks/data"):
        os.makedirs("C:/Program Files/ScheduleWorks/data")

    with open(
        "C:/Program Files/ScheduleWorks/data/userData.json", "w+", encoding="utf-8"
    ) as outfile:
        json.dump(dict_from_json, outfile, indent=4)

    user_info = extract_user_info()

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
    view_course_history()
    view_degree_requirements()




# def refresh_data():
#     """Use retrive_data with my own cookies for quick access when I need to refresh data."""
#     retrive_data(
#         privateInfo.get_refresh_token(),
#         privateInfo.get_x_auth(),
#         "%20Mazen%20A%20Mirza",
#     )


if __name__ == "__main__":
    return
    # refresh_data()
    # view_course_history()
    # view_degree_requirements()
    # extract_user_info()
