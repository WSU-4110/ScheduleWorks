import json

# Open jsonfile
open_f = open("data.json")
data = json.load(open_f)

# Grab discipline from course and course requirements
courses = {}
# store list of course req
course_req = {}

# Show all keys
#print(data.keys())

# Iterate over each course
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


for course in data["inProgress"]["classArray"]:
    discipline = course["discipline"]
    number = course["number"]
    credits = int(course["credits"])
    # if to check if discipline is available
    if discipline not in course_req:
        course_req[discipline] = {}
    course_req[discipline][number] = credits


# calculate total 
Tot_credits = sum(sum(courses[discipline].values()) for discipline in courses)

# Write the output to a JSON file(output)
with open("output.json", "w") as f:
    json.dump({"Course History": courses, "Tot_credits": Tot_credits, "Course Requirements": course_req}, f, indent=4)