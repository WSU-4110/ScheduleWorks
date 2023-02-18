import json

#Open jsonfile
open_f=open('data.json')
data = json.load(open_f)



#Grab discipline from key course
courses = {}

#Show all keys
print(data.keys())

## Iterate over each course
#Key of classinformation->class array
for course in data["classInformation"]["classArray"]: #extract
                discipline = course["discipline"]
                number = course["number"]
                credits = int(course["credits"])
                #if to check if discipline is available
                if discipline not in courses:
                    courses[discipline] = {}
                if number not in courses[discipline]:
                     courses[discipline][number] = credits


#Key of blockarray that contains classesAppliedtoRule and class arrar
for course in data["blockArray"]["classesAppliedToRule. "]: #extract
        for class_info in course["classesAppliedToRule"]["classArray"]:
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
with open("output.json", "w") as f:
    json.dump({"courses": courses, "Tot_credits": Tot_credits}, f, indent=4) 

