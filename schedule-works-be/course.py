"""Course class for easy information access."""


class Course:
    """An object used to store relevant class information manage them easily."""

    def __init__(self, course_json):
        """Initialize a course object from json data."""
        self.course_json = course_json

    def __repr__(self):
        return str(
            "Course Object: "
            + " "
            + self.get_course_subject()
            + self.get_course_number()
            + " "
            + self.get_times()[0]
            + "-"
            + self.get_times()[1]
        )

    def get_id(self):
        return self.course_json["id"]

    def get_term(self):
        return self.course_json["term"]

    def get_term_name(self):
        return self.course_json["termDesc"]

    def get_reference_number(self):
        return self.course_json["courseReferenceNumber"]

    def get_course_number(self):
        return self.course_json["courseNumber"]

    def get_course_subject(self):
        return self.course_json["subject"]

    def get_campus(self):
        return self.course_json["campusDescription"]

    def get_course_type(self):
        """Lecture or lab section."""
        return self.course_json["scheduleTypeDescription"]

    def get_course_title(self):
        return self.course_json["courseTitle"]

    def get_credits(self):
        return self.course_json["credits"]

    def def_get_enrollment_capacity(self):
        return self.course_json["maximumEnrollment"]

    def def_get_open_seats(self):
        return self.course_json["seatsAvailable"]

    def get_wait_capacity(self):
        return self.course_json["waitCapacity"]

    def get_wait_available(self):
        return self.course_json["waitAvailable"]

    def is_linked(self):
        return self.course_json["isSectionLinked"]

    def get_facualty(self):
        return self.course_json["faculty"]

    def get_times(self) -> list:
        return [
            self.course_json["meetingsFaculty"][0]["meetingTime"]["beginTime"],
            self.course_json["meetingsFaculty"][0]["meetingTime"]["endTime"],
        ]

    def get_dates(self) -> list:
        return [
            self.course_json["meetingsFaculty"][0]["meetingTime"]["startDate"],
            self.course_json["meetingsFaculty"][0]["meetingTime"]["endDate"],
        ]

    def get_dates(self) -> list:
        return [
            self.course_json["meetingsFaculty"][0]["meetingTime"]["startDate"],
            self.course_json["meetingsFaculty"][0]["meetingTime"]["endDate"],
        ]

    def get_campus_code(self):
        return self.course_json["meetingsFaculty"]["meetingTime"]["campus"]

    def get_days(self) -> dict:
        mon = self.course_json["meetingsFaculty"][0]["meetingTime"]["monday"]
        tue = self.course_json["meetingsFaculty"][0]["meetingTime"]["tuesday"]
        wed = self.course_json["meetingsFaculty"][0]["meetingTime"]["wednesday"]
        thur = self.course_json["meetingsFaculty"][0]["meetingTime"]["thursday"]
        fri = self.course_json["meetingsFaculty"][0]["meetingTime"]["friday"]
        dates = {
            "monday": mon,
            "tuesday": tue,
            "wednesday": wed,
            "thursday": thur,
            "friday": fri,
        }

        return dates


def main():
    """Example usage."""
    data = {
        "id": 482685,
        "term": "202309",
        "termDesc": "Fall 2023",
        "courseReferenceNumber": "14098",
        "partOfTerm": "FT",
        "courseNumber": "2200",
        "subject": "CSC",
        "subjectDescription": "Computer Science",
        "sequenceNumber": "001",
        "campusDescription": "Main Campus",
        "scheduleTypeDescription": "Lecture",
        "courseTitle": "Computer Science II",
        "creditHours": 4,
        "maximumEnrollment": 48,
        "enrollment": 48,
        "seatsAvailable": 0,
        "waitCapacity": 0,
        "waitCount": 0,
        "waitAvailable": 0,
        "crossList": None,
        "crossListCapacity": None,
        "crossListCount": None,
        "crossListAvailable": None,
        "creditHourHigh": 4,
        "creditHourLow": 0,
        "creditHourIndicator": "OR",
        "openSection": False,
        "linkIdentifier": "AO",
        "isSectionLinked": True,
        "subjectCourse": "CSC2200",
        "faculty": [],
        "meetingsFaculty": [
            {
                "category": "01",
                "class": "net.hedtech.banner.student.schedule.SectionSessionDecorator",
                "courseReferenceNumber": "14098",
                "faculty": [],
                "meetingTime": {
                    "beginTime": "1430",
                    "building": "MAIN",
                    "buildingDescription": "Old Main",
                    "campus": "MAI",
                    "campusDescription": "Main Campus",
                    "category": "01",
                    "class": "net.hedtech.banner.general.overall.MeetingTimeDecorator",
                    "courseReferenceNumber": "14098",
                    "creditHourSession": 4.0,
                    "endDate": "12/19/2023",
                    "endTime": "1545",
                    "friday": False,
                    "hoursWeek": 2.5,
                    "meetingScheduleType": "LCT",
                    "meetingType": "CLAS",
                    "meetingTypeDescription": "Class",
                    "monday": True,
                    "room": "1168",
                    "saturday": False,
                    "startDate": "08/28/2023",
                    "sunday": False,
                    "term": "202309",
                    "thursday": False,
                    "tuesday": False,
                    "wednesday": True,
                },
                "term": "202309",
            }
        ],
        "reservedSeatSummary": None,
        "sectionAttributes": None,
        "instructionalMethod": "TR",
        "instructionalMethodDescription": "Traditional - Face to Face",
    }
    thing = Course(data)
    print(thing.get_days())


if __name__ == "__main__":
    main()
