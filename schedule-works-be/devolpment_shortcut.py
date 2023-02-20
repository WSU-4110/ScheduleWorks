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
    time.sleep(59999)
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


def extract_user_info() -> dict:
    """Extract user information from json file and returns relavant information in a dict."""
    try:
        with open(
            "C:/Program Files/ScheduleWorks/data/userData.json", encoding="utf-8"
        ) as file:
            user_data = json.load(file)
    except FileNotFoundError as error:
        raise error
    user_information = {}
    user_information["name"] = user_data["_embedded"]["students"][0]["name"]
    user_information["term_code"] = user_data["_embedded"]["students"][0]["activeTerm"]
    user_information["id"] = user_data["_embedded"]["students"][0]["id"]
    user_information["level"] = user_data["_embedded"]["students"][0]["goals"][0][
        "school"
    ]["key"]
    user_information["degree"] = user_data["_embedded"]["students"][0]["goals"][0][
        "degree"
    ]["key"]

    try:
        with open(
            "C:/Program Files/ScheduleWorks/data/userData.txt", "w+", encoding="utf-8"
        ) as file:
            file.write(
                user_information["name"]
                + "\n"
                + user_information["term_code"]
                + "\n"
                + user_information["id"]
                + "\n"
                + user_information["level"]
                + "\n"
                + user_information["degree"]
            )
    except FileNotFoundError as error:
        raise error

    return user_information


def view_course_history():
    """Extract course history from json audit file."""
    try:
        with open(
            "C:/Program Files/ScheduleWorks/data/classData.json", encoding="utf-8"
        ) as file:
            audit_data = json.load(file)
    except FileNotFoundError as error:
        raise error

    try:
        with open(
            "C:/Program Files/ScheduleWorks/data/courseHistory.txt",
            "w+",
            encoding="utf-8",
        ) as file:
            for course in audit_data["classInformation"]["classArray"]:
                print(
                    f"{course['discipline']:<5}",
                    f"{course['number']:<5}",
                    f"{course['credits']:<3}",
                    f"{course['courseTitle']:<30}",
                    f"'Passed:' {course['passed']:<8}",
                )
                file.write(
                    f"{course['discipline']:<5}"
                    + f"{course['number']:<5}"
                    + f"{course['credits']:<3}"
                    + f"{course['courseTitle']:<30}"
                    + f"'Passed:' {course['passed']:<8}\n"
                )
    except FileNotFoundError as error:
        raise error


def view_degree_requirements():
    """Extract degree requirments from json audit file."""
    try:
        with open(
            "C:/Program Files/ScheduleWorks/data/classData.json", encoding="utf-8"
        ) as file:
            audit_data = json.load(file)
    except FileNotFoundError as error:
        raise error

    try:
        with open(
            "C:/Program Files/ScheduleWorks/data/degreeRequirments.txt",
            "w+",
            encoding="utf-8",
        ) as file:
            for degree_block_requirement in audit_data["blockArray"]:
                print(degree_block_requirement["title"])
                file.write(degree_block_requirement["title"] + "\n")

    except FileNotFoundError as error:
        raise error


# def refresh_data():
#     """Use retrive_data with my own cookies for quick access when I need to refresh data."""
#     retrive_data(
#         privateInfo.get_refresh_token(),
#         privateInfo.get_x_auth(),
#         "%20Mazen%20A%20Mirza",
#     )


if __name__ == "__main__":
    # refresh_data()
    view_course_history()
    view_degree_requirements()
    # extract_user_info()
