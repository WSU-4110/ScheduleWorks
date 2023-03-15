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


def idk():
    # Open jsonfile
    open_f = open("data.json")
    data = json.load(open_f)

    # Grab discipline from course and course requirements
    courses = {}
    # store list of course req
    course_req = {}

    # Show all keys
    print(data.keys())

    ## Iterate over each course
    # Key of classinformation->class array
    for course in data["classInformation"]["classArray"]:  # extract
        discipline = course["discipline"]
        number = course["number"]
        credits = int(course["credits"])
        # if to check if discipline is available
        if discipline not in courses:
            courses[discipline] = {}
        if number not in courses[discipline]:
            courses[discipline][number] = credits

    # Key of blockarray that contains classesAppliedtoRule and class array
    for course in data["blockArray"]:
        else_part = course.get("ifPart", {}).get("elsePart", {})
        rule_array = else_part.get("ruleArray", [])
        for rule in rule_array:
            for class_info in rule.get("classesAppliedToRule", {}).get(
                "classArray", []
            ):
                discipline = class_info["discipline"]
                number = class_info["number"]
                credits = int(class_info["credits"])
                if discipline not in courses:
                    courses[discipline] = {}
                if number not in courses[discipline]:
                    courses[discipline][number] = credits

    # get course req
    # Iterate through blockArray
    for course in data["blockArray"]:
        else_part = course.get("ifPart", {}).get("elsePart", {})
        rule_array = else_part.get("ruleArray", [])
        for rule in rule_array:
            for class_info in rule.get("classesAppliedToRule", {}).get(
                "classArray", []
            ):
                if (
                    class_info["letterGrade"] == "INPR"
                    or class_info["percentComplete"] != "100"
                    or class_info["percentComplete"] == "0"
                ):
                    course_req.append(class_info)
                discipline = class_info["discipline"]
                number = class_info["number"]
                credits = int(class_info["credits"])
                if discipline not in courses:
                    courses[discipline] = {}
                if number not in courses[discipline]:
                    courses[discipline][number] = credits

    # calculate total
    Tot_credits = sum(sum(courses[discipline].values()) for discipline in courses)

    # Write the output to a JSON file(output)
    with open("data/output.json", "w") as f:
        json.dump(
            {
                "Course History": courses,
                "Tot_credits": Tot_credits,
                "Course Requirements": course_req,
            },
            f,
            indent=4,
        )


if __name__ == "__main__":
    course_requirements()
