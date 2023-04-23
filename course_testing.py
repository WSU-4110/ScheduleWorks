import unittest
import course as Course

class Test_course(unittest.TestCase):

    def set_course():
        attribute_list = ["this", "is", "a", "test"]
        passed = True
        name = "Test Name"
        credit = 21
        discipline = "Test discipline"
        number = 70
        term = str(498)
        block_requirement_id = "Test block"
        course = "Test course"

    def test___init__(self,
                 attribute_list:list,
                 passed:bool,
                 name:str,
                 credit:int,
                 discipline:str,
                 number:int,
                 term:str(),
                 block_requirement_id:str) -> None:
        
        actualattribute_list = attribute_list
        actualpassed = passed
        actualname = name
        actualcredit = credit
        actualdiscipline = discipline
        actualnumber = number
        actualterm = term
        actualblock_requirement_id = block_requirement_id
        expectedattribute_list = ["this", "is", "a", "test"]
        expectedpassed = True
        expectedname = "Test Name"
        expectedcredit = 21
        expecteddiscipline = "Test discipline"
        expectednumber = 70
        expectedterm = str(498)
        expectedblock_requirement_id = "Test block"
        attribute_list.assertEqual(expectedattribute_list, actualattribute_list)
        passed.assertEqual(expectedpassed, actualpassed)
        name.assertEqual(expectedname, actualname)
        credit.assertEqual(expectedcredit, actualcredit)
        discipline.assertEqual(expecteddiscipline, actualdiscipline)
        number.assertEqual(expectednumber, actualnumber)
        term.assertEqual(expectedterm, actualterm)
        blocked_requirement_id.assertEqual(expectedblocked_requirement_id, actualblocked_requirement_id)
        
    def test_add_req(self,course):
        actualcourse = course
        expectedcourse = "Test course"
        course.assertEqual(expectedcourse, actualcourse)
        

if __name__ == '__main__':
    unittest.main()