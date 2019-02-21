"""
Demo on using *args and *kwargs
"""
def course_students(course_name, *students):
    print(f"For course {course_name}, the students are: ")
    for student in students:
        print(f"Name: {student}")

def person_job_details(name, last_name, occupation, years_working):
    print(f"{name} {last_name} has been working as {occupation} for {years_working} years")
    
def person_location(**kwargs):
    print(f'{kwargs["name"]} {kwargs["last_name"]} lives in {kwargs["city"]}, {kwargs["state"]}')


def main():
    """
    Main program flow
    """
    course_students("Python 210", "Ted", "Robin", "Barney", "Lily", "Marshall")

    person_details = {
        "name": "John",
        "last_name": "Oliver",
        "occupation": "Comedian",
        "years_working": 20
    }

    person_job_details(**person_details)

    person_details = {
        "name": "John",
        "last_name": "Oliver",
        "city": "Buffalo",
        "state": "New York",
        "occupation": "Comedian",
        "years_working": 20
    }
    person_location(**person_details)

if __name__ == "__main__":
    main()