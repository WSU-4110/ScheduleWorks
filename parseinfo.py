import json

#Open jsonfile
open_f=open('data.json')
data = json.load(open_f)


#Hold courses in each category for grad requiremnt
MATH_courses = []
PHY_courses = []
CS_courses = []
GE_courses = []

## Iterate over each course
for course in data ['classesAppliedToRule']:
    # Extract course properties
    name = course['name']
    number = code.split()[1]
    discipline = code.split()[0]
    category = course['category'] 
    credits = course['credits'] 
    code = course['code']
 

   

    # Categorize course by discipline and number
    if discipline == 'MATH':
        MATH_courses.append({
            'name': name,
            'discipline': discipline,
            'number': number,
            'category': category,
            'credits': credits
        })

    elif discipline == 'PHYS':
        PHY_courses.append({
            'name': name,
            'discipline': discipline,
            'number': number,
            'category': category,
            'credits': credits
        })
    elif discipline == 'CSC':
        CS_courses.append({
            'name': name,
            'discipline': discipline,
            'number': number,
            'category': category,
            'credits': credits
        })
    else:
        GE_courses.append({
            'name': name,
            'discipline': discipline,
            'number': number,
            'category': category,
            'credits': credits
        })

# Calculate total number of credits 
TOT_credits = sum([course['credits'] for course in CS_courses])

# Create a dictionary with all categorized courses and total credits
output_data = {
    'Math courses': MATH_courses,
    'Physics courses': PHY_courses,
    'Computer Science courses': CS_courses,
    'General Education courses': GE_courses,
    'Total credits needed for a degree': TOT_credits
}

# Write the output to a JSON 
with open('output.json', 'w') as f:
    json.dump(output_data, f, indent=4)