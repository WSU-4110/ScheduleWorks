"""Wrapper class to maintain cookies from NU Banner API"""
import requests


class Nub:
    """
    Wrapper api for NU Banner.
    https://jennydaman.gitlab.io/nubanned/dark.html

    """

    def __init__(self, base_url) -> None:
        self.base_url = base_url
        self.term = ""

    def get_terms(self, maximum=25, offset=0, search_term=""):
        """
        Generate a list of semesters and their term codes that are available to be viewed.

        Args:
        offset: starting index (default 1).
        maximum: number of semesters to return.
        searchTerm: keyword to filter by.
        """
        url = (
            self.base_url
            + f"/classSearch/getTerms?offset={offset}&max={maximum}&searchTerm={search_term}"
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

    def get_subject_code(self, maximum=10, offset=1, search_term=""):
        """
        Generate a list of subjects and their codes using a filter.

        Args:
        term
        offset: starting index (default 1).
        maximum: number of semesters to return.
        searchTerm: keyword to filter by.
        """
        url = (
            self.base_url
            + f"/classSearch/get_subject?offset={offset}&max={maximum}&searchTerm={search_term}&term={self.term}"
        )
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return [{"Error": response.status_code}]

        return response.json()

    def enable_search(self):
        """
        Enable search cookies with a valid code. Takes no args.

        """
        url = self.base_url + f"/term/search"
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

    def look_up(self, subject_code):
        """Search for a course given its subject code."""

        url = (
            self.base_url
            + f"/searchResults/searchResults?txt_subject={subject_code}&txt_term={self.term}&startDatepicker=&endDatepicker=&pageOffset=0&pageMaxSize=5000&sortColumn=subjectDescription&sortDirection=asc"
        )
        print(url)
        response = self.session.get(
            url,
        )

        if response.status_code != 200:
            return [{"Error": response.status_code}]

        return response.json()


def main():
    """Example usage."""
    pre_reqs = Nub("https://registration.wayne.edu/StudentRegistrationSsb/ssb")
    print(pre_reqs.get_terms())
    pre_reqs.set_term("202301")
    pre_reqs.enable_search()
    lookup = pre_reqs.look_up("CSC")
    print(lookup)


if __name__ == "__main__":
    main()
