"""Wrapper class to maintain cookies from NU Banner API."""
import re
import requests
from bs4 import BeautifulSoup
import dgraph
import parse_info


class Nub:
    """
    Wrapper api for NU Banner.

    https://jennydaman.gitlab.io/nubanned/dark.html

    """

    def __init__(self, base_url) -> None:
        """Set required variables."""
        self.base_url = base_url
        self.term = ""
        self.session = None

    def get_terms(self, maximum=100, offset=1, search_term=""):
        """
        Generate a list of semesters and their term codes that are available to be viewed.

        Args:
        offset: starting index (default 1).
        maximum: number of semesters to return.
        searchTerm: keyword to filter by.
        """
        url = (
            self.base_url + f"/classSearch/getTerms?"
            f"offset={offset}"
            f"&max={maximum}"
            f"&searchTerm={search_term}"
        )
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return [{"Error": response.status_code}]
        return response.json()

    def set_term(self, term: str) -> None:
        """
        Set the term for lookups.

        Args:
        Term is a numeric string given from get_terms().
        """
        self.term = term
        return True

    def get_subject_code(self, search_term, maximum=10, offset=1):
        """
        Generate a list of subjects and their codes using a filter.

        Args:
        term
        offset: starting index (default 1).
        maximum: number of semesters to return.
        searchTerm: keyword to filter by.
        """
        url = (
            self.base_url + "/classSearch/get_subject"
            f"?offset={offset}"
            f"&max={maximum}"
            f"&searchTerm={search_term}"
            f"&term={self.term}"
        )
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return [{"Error": response.status_code}]

        return response.json()

    def enable_search(self):
        """Enable search cookies with a valid code. Required after setting term."""
        url = self.base_url + "/term/search"
        header = {
            "Content-Type": "application/x-www-form-urlencoded;charset=UT",
        }

        body = {
            "term": self.term,
            "studyPath": "",
            "studyPathText": "",
            "startDatepicker": "",
            "endDatepicker": "",
        }
        with requests.Session() as ses:
            response = ses.post(url, timeout=10, data=body, headers=header)
            self.session = ses

        if response.status_code != 200:
            return [{"Error": response.status_code}]

        return response.json()

    def reset_search(self):
        """Reset form data for clean search."""
        url = self.base_url + "/classSearch/resetDataForm"
        self.session.post(url)

    def look_up(self, subject_code):
        """Search for a course given its subject code."""
        self.reset_search()
        url = (
            self.base_url + "/searchResults/searchResults?"
            f"txt_subject={subject_code}"
            f"&txt_term={self.term}"
            "&startDatepicker="
            "&endDatepicker="
            "&pageOffset=0"
            "&pageMaxSize=5000"
            "&sortColumn=subjectDescription"
            "&sortDirection=asc"
        )
        response = self.session.get(url)

        if response.status_code != 200:
            return [{"Error": response.status_code}]

        return response.json()

    def get_course_reference(self, subject_code, course_code):
        """Return class code for accessing its details."""
        self.reset_search()
        url = (
            self.base_url + "/searchResults/searchResults?"
            f"txt_subject={subject_code}"
            f"&txt_term={self.term}"
            f"&txt_courseNumber={course_code}"
            "&startDatepicker="
            "&endDatepicker="
            "&pageOffset=0"
            "&pageMaxSize=5000"
            "&sortColumn=subjectDescription"
            "&sortDirection=asc"
        )
        response = self.session.get(url, timeout=10)
        if response.status_code != 200:
            return [{"Error": response.status_code}]
        if response.json()["totalCount"] <= 0:
            return [{"Error": "Cannot find class"}]

        course_reference_number = response.json()["data"][0]["courseReferenceNumber"]
        return course_reference_number

    def clean_prereq_list(self, prereq_table):
        """Parse data from html source code."""
        course_prereq_list = []
        word = ""

        text_tokens = str(prereq_table).split(" ")

        # parsing courses from trash
        for i, word in enumerate(text_tokens):
            # print(text_tokens[i])
            if text_tokens[i] == "Course":
                i += 3
                saved_current_index = len(course_prereq_list)
                course_prereq_list.append("")
                while not text_tokens[i].isnumeric():
                    if (
                        "Attributes" in text_tokens[i]
                    ):  # english 3060 made me put this here i dont know why
                        break
                    course_prereq_list[saved_current_index] += text_tokens[i] + " "
                    i += 1
                if text_tokens[i].isnumeric():
                    course_prereq_list[saved_current_index] += text_tokens[i]
            elif "or" in text_tokens[i]:
                course_prereq_list.append("or")

        # cleaning up repeating or statements
        for i, word in enumerate(course_prereq_list):
            if (
                word == "or"
                and (
                    i + 1 < len(course_prereq_list)
                    and course_prereq_list[i + 1] != "or"
                )
                or i == len(course_prereq_list) - 1
            ):
                course_prereq_list.pop(i)

        course_prereq_dict = []

        i = 0
        or_counter = 0
        while i < len(course_prereq_list):
            if course_prereq_list[i] != "or":
                or_counter = 0
                course_prereq_dict.append(
                    [
                        {
                            "course": re.sub(
                                r"[^a-zA-Z ]+", "", course_prereq_list[i]
                            ).strip(),
                            "code": re.findall(r"\d+", course_prereq_list[i])[0],
                        }
                    ]
                )
            else:
                or_counter += 2
                # print(i - or_counter, course_prereq_dict, course_prereq_list[i + 1])
                # use or here to ignore "or masters"
                # use or here to ignore "or atribute in xyz"
                if (
                    course_prereq_list[i + 1] == "or"
                    or "Attributes" not in course_prereq_list[i + 1]
                ):
                    break  # check english 3010 and BE1200 for example
                course_prereq_dict[i - or_counter].append(
                    {
                        "course": re.sub(
                            r"[^a-zA-Z ]+", "", course_prereq_list[i + 1]
                        ).strip(),
                        "code": re.findall(r"\d+", course_prereq_list[i + 1])[0],
                    }
                )
                i += 1  # skipping course that was just added
            i += 1  # increment for while
        return self.convert_to_codes(course_prereq_dict)

    def convert_to_codes(self, course_prereq_dict):
        """Converts a class into its simlplified code."""
        known_conversion = {}
        for course_set in course_prereq_dict:
            for course_data in course_set:
                course_name = course_data["course"]
                if course_name in known_conversion:
                    course_data["course"] = known_conversion[course_name]
                else:
                    code = self.get_subject_code(course_name)[0]["code"]
                    known_conversion[course_name] = code
                    course_data["course"] = code
        return course_prereq_dict

    def get_prerequistes(self, subject_code, course_code):
        """Obtain an array with course prequeistes given a course code and id."""
        course_reference_number = self.get_course_reference(subject_code, course_code)
        url = self.base_url + "/searchResults/getSectionPrerequisites"
        body = {"term": self.term, "courseReferenceNumber": course_reference_number}
        html_response = requests.post(url, data=body, timeout=20)
        if html_response.status_code != 200:
            return ["Error"]
        parsed_html = BeautifulSoup(html_response.content, features="lxml")
        prereq_table = parsed_html.body.find("table")

        return self.clean_prereq_list(prereq_table)

    def make_adjancancy_mtrx(self):
        """Produce an adjancancy matrix for courses still in progress."""
        adjancancy_mtrx = []
        course_list_degree = parse_info.get_courses()
        for course_degree in course_list_degree:
            # print(course_degree)
            course_preqs = self.get_prerequistes(
                course_degree.split(" ")[0], course_degree.split(" ")[1]
            )
            if course_preqs and course_preqs[0] == "Error":
                continue
            for required_courses in course_preqs:
                course = dict(
                    required_courses[0]
                )  # linting caught some error without this here
                adjancancy_mtrx.append(
                    [
                        course_degree,
                        course["course"] + course["code"],
                    ]
                )
        return adjancancy_mtrx

    def make_adjancancy_mtrx_full(self):
        """Produce an adjancancy matrix for all courses in a degree."""
        adjancancy_mtrx = []
        course_list_degree = parse_info.get_all_courses()
        for course_degree in course_list_degree:
            # print(course_degree)
            course_preqs = self.get_prerequistes(
                course_degree.split(" ")[0], course_degree.split(" ")[1]
            )
            if course_preqs and course_preqs[0] == "Error":
                continue
            for required_courses in course_preqs:
                course = dict(required_courses[0])
                adjancancy_mtrx.append(
                    [
                        course_degree,
                        course["course"] + course["code"],
                    ]
                )
        return adjancancy_mtrx

    def search_class(self, subject_code, course_code):
        self.reset_search()
        url = (
            self.base_url + "/searchResults/searchResults?"
            f"txt_subject={subject_code}"
            f"&txt_term={self.term}"
            f"&txt_courseNumber={course_code}"
            "&startDatepicker="
            "&endDatepicker="
            "&pageOffset=0"
            "&pageMaxSize=5000"
            "&sortColumn=subjectDescription"
            "&sortDirection=asc"
        )
        response = self.session.get(url, timeout=10)
        if response.status_code != 200:
            return [{"Error": response.status_code}]
        if response.json()["totalCount"] <= 0:
            return [{"Error": "Cannot find class"}]

        data = response.json()["data"]
        print(len(data))
        print(data[0].keys())

    
        # pprint.pprint(response.json())


def main():
    """Give an example use case."""
    nub = Nub("https://registration.wayne.edu/StudentRegistrationSsb/ssb")
    print(nub.get_terms(maximum=5))
    nub.set_term("202309")
    nub.enable_search()
    nub.search_class("CSC", "2200")
    # graph = dgraph.Dgraph()
    # print(nub.make_adjancancy_mtrx())
    # graph.add_edges_from(nub.make_adjancancy_mtrx())
    # graph.save_graph("graph_small", dpi=600)
    # graph.add_edges_from(nub.make_adjancancy_mtrx_full())
    # graph.save_graph("graph_full", dpi=600)


if __name__ == "__main__":
    main()
