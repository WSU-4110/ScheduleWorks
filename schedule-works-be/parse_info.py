"""Functions for parsing large json user data into readable parts."""
import json


def course_requirements():
    """Parse course requirments for classes still needed for degree."""
    try:
        with open(
            "C:/Program Files/ScheduleWorks/data/classData.json", encoding="utf-8"
        ) as file:
            audit_data = json.load(file)
    except FileNotFoundError as error:
        raise error

    degree_requirements = {}

    for block in audit_data["blockArray"]:
        requirement_title = block["title"]
        degree_requirements[requirement_title] = {
            "percentComplete": block["percentComplete"],
            "requiredCourses": [],
        }
        for course in block["ruleArray"]:
            course_name = course["label"]
            if course_name != "IF Statement" and course["percentComplete"] == "0":
                degree_requirements[requirement_title]["requiredCourses"].append(
                    course.get("requirement").get("courseArray")[0]
                )
    try:
        with open(
            "C:/Program Files/ScheduleWorks/data/requirements.json",
            "w+",
            encoding="utf-8",
        ) as outfile:
            json.dump({"requirements": degree_requirements}, outfile, indent=4)
    except FileNotFoundError as error:
        raise error


def view_course_history():
    """Extract course history from json audit file."""
    try:
        with open(
            "C:/Program Files/ScheduleWorks/data/classData.json", encoding="utf-8"
        ) as file:
            audit_data = json.load(file)
    except FileNotFoundError as error:
        raise error

    courses_passed_list = []

    for course in audit_data["classInformation"]["classArray"]:
        courses_passed_list.append(
            {
                "courseTitle": course["courseTitle"],
                "discipline": course["discipline"],
                "number": course["number"],
                "credits": course["credits"],
                "passed": course["passed"],
                "inProgress": course["inProgress"],
                "attributeArray": course["attributeArray"],
            }
        )
        # TODO
        # manage a list of known attriubutes
        # clean out DWSISKEY and other ? attributes (idk what 2YR means)
        # remove attribute list from first append, clean right after and then
        # courses_passed_list[-1]["attributeArray"]:cleaned_attribute_list

    try:
        with open(
            "C:/Program Files/ScheduleWorks/data/courseHistory.json",
            "w+",
            encoding="utf-8",
        ) as outfile:
            json.dump(courses_passed_list, outfile, indent=4)
    except FileNotFoundError as error:
        raise error


def get_courses():
    """Retrives required courses that have yet to be taken."""
    try:
        with open(
            "C:/Program Files/ScheduleWorks/data/requirements.json",
            encoding="utf-8",
        ) as file:
            audit_data = json.load(file)
    except FileNotFoundError as error:
        raise error
    course_list = []
    for discipline in audit_data["requirements"]:
        required_courses = audit_data["requirements"][discipline]["requiredCourses"]
        if required_courses:
            # only accesses the first element in the list does not work with or's
            for course_dict in required_courses:
                # course_name_id = course_list[0]
                course_list.append(
                    course_dict["discipline"] + " " + course_dict["number"]
                )
    return course_list


def get_all_courses():
    """Gives all the courses required by a degree inlcuding those taken and those yet to be taken."""
    course_list = get_courses()

    try:
        with open(
            "C:/Program Files/ScheduleWorks/data/courseHistory.json",
            encoding="utf-8",
        ) as file:
            course_history = json.load(file)
    except FileNotFoundError as error:
        raise error

    for course in course_history:
        course_list.append(course["discipline"] + " " + course["number"])

    return course_list


def get_courses_taken() -> list:
    """Get all the courses taken or currently registered for."""
    try:
        with open(
            "C:/Program Files/ScheduleWorks/data/courseHistory.json",
            encoding="utf-8",
        ) as file:
            course_history = json.load(file)
    except FileNotFoundError as error:
        raise error
    courses_taken = []
    for course in course_history:
        courses_taken.append(course["discipline"] + " " + course["number"])
    return courses_taken


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


def course_history_txt():
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
        ) as outfile:
            for course in audit_data["classInformation"]["classArray"]:
                outfile.write(
                    f"{course['discipline']}\n"
                    + f"{course['number']}\n"
                    + f"{course['credits']}\n"
                    + f"{course['courseTitle']}\n"
                    + f"'Passed:' {course['passed']}\n"
                )
    except FileNotFoundError as error:
        raise error
    

def course_history_txt():
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
        ) as outfile:
            for course in audit_data["classInformation"]["classArray"]:
                outfile.write(
                    f"{course['discipline']}\n"
                    + f"{course['number']}\n"
                    + f"{course['credits']}\n"
                    + f"{course['courseTitle']}\n"
                    + f"'Passed:' {course['passed']}\n"
                )
    except FileNotFoundError as error:
        raise error
    
# def schedules_txt():

#     try:
#         with open(
#             "C:/Program Files/ScheduleWorks/data/courseHistory.txt",
#             "w+",
#             encoding="utf-8",
#         ) as outfile:
#             for course in audit_data["classInformation"]["classArray"]:
#                 outfile.write(
#                     f"{course['discipline']}\n"
#                     + f"{course['number']}\n"
#                     + f"{course['credits']}\n"
#                     + f"{course['courseTitle']}\n"
#                     + f"'Passed:' {course['passed']}\n"
#                 )
#     except FileNotFoundError as error:
#         raise error




if __name__ == "__main__":
    course_history_txt()
