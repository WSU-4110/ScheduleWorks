import pytest
import nub as nu


# 1
def test_get_terms():
    nub = nu.Nub("https://registration.wayne.edu/StudentRegistrationSsb/ssb")
    terms = nub.get_terms(maximum=5)
    assert len(terms) == 5


# 2
def test_get_terms_large():
    nub = nu.Nub("https://registration.wayne.edu/StudentRegistrationSsb/ssb")
    terms = nub.get_terms(maximum=1000)
    assert len(terms) < 1000


# 3
def test_term():
    nub = nu.Nub("https://registration.wayne.edu/StudentRegistrationSsb/ssb")
    nub.set_term("202301")
    assert nub.term == "202301"


# 4
def test_enable_search():
    nub = nu.Nub("https://registration.wayne.edu/StudentRegistrationSsb/ssb")
    nub.set_term("202301")
    with pytest.raises(Exception):
        nub.get_prerequistes(2200, "CSC")


# 5
def test_conversion():
    nub = nu.Nub("https://registration.wayne.edu/StudentRegistrationSsb/ssb")
    nub.set_term("202301")
    assert nub.convert_to_codes([[{"course": "Computer Science", "code": "2200"}]]) == [
        [{"course": "CSC", "code": "2200"}]
    ]


# 6
def test_code():
    nub = nu.Nub("https://registration.wayne.edu/StudentRegistrationSsb/ssb")
    nub.set_term("202301")
    assert nub.get_subject_code("Computer Science") == [
        {"code": "CSC", "description": "Computer Science"}
    ]


# 7
def test_prereq():
    nub = nu.Nub("https://registration.wayne.edu/StudentRegistrationSsb/ssb")
    nub.set_term("202301")
    nub.enable_search()
    assert nub.get_prerequistes("CSC", "2200") == [
        [{"course": "CSC", "code": "1500"}],
        [{"course": "CSC", "code": "2110"}],
        [{"course": "MAE", "code": "2010"}],
        [{"course": "BE", "code": "1200"}],
    ]
    nub.close_session()


# Run all tests
if __name__ == "__main__":
    pytest.main()
