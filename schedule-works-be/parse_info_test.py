import unittest
from unittest.mock import mock_open, patch
import parse_info
import json


class TestParseInfo(unittest.TestCase):

    def setUp(self):
        self.json_data = {
            "classInformation": {
                "classArray": [
                    {
                        "discipline": "CSCI",
                        "number": "101",
                        "credits": "4"
                    }
                ]
            },
            "blockArray": [
                {
                    "title": "Core",
                    "percentComplete": "0",
                    "ruleArray": [
                        {
                            "label": "Course 1",
                            "percentComplete": "100",
                            "requirement": {
                                "courseArray": [
                                    {
                                        "discipline": "CSCI",
                                        "number": "101"
                                    }
                                ]
                            },
                            "classesAppliedToRule": {
                                "classArray": [
                                    {
                                        "discipline": "CSCI",
                                        "number": "101",
                                        "credits": "4",
                                        "letterGrade": "A",
                                        "percentComplete": "100"
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }
        self.file_content = '{"field": "value"}'

 def test_idk(self):
        # Set up test data
        mock_data = {
            "classInformation": {
                "classArray": [
                    {"discipline": "A", "number": "101", "credits": "3"},
                    {"discipline": "B", "number": "201", "credits": "4"},
                ]
            },
            "blockArray": [
                {
                    "ifPart": {},
                    "elsePart": {
                        "ruleArray": [
                            {
                                "classesAppliedToRule": {
                                    "classArray": [
                                        {
                                            "discipline": "A",
                                            "number": "101",
                                            "credits": "3",
                                            "percentComplete": "100",
                                            "letterGrade": "A",
                                        },
                                        {
                                            "discipline": "B",
                                            "number": "201",
                                            "credits": "4",
                                            "percentComplete": "50",
                                            "letterGrade": "B",
                                        },
                                    ]
                                }
                            }
                        ]
                    },
                }
            ]
        }
        # Set up mock open method to return mock data
        with patch("builtins.open", mock_open(read_data=json.dumps(mock_data))):
            # Call the function
            parse_info.idk()
            # Check that output.json was written with the expected output
            with open("data/output.json") as f:
                output = json.load(f)
                self.assertEqual(
                    output,
                    {
                        "Course History": {
                            "A": {"101": 3},
                            "B": {"201": 4},
                        },
                        "Tot_credits": 7,
                        "Course Requirements": [
                            {
                                "discipline": "B",
                                "number": "201",
                                "credits": "4",
                                "percentComplete": "50",
                                "letterGrade": "B",
                            }
                        ],
                    },
                )
    @patch('parse_info.open')



def test_course_requirements(self, mock_file):
        mock_file.return_value.__enter__.return_value = self.json_data
        parse_info.course_requirements()

        expected_output = {
            "requirements": {
                "Core": {
                    "percentComplete": "0",
                    "requiredCourses": [{"discipline": "CSCI", "number": "101"}]
                }
            }
        }

        with open("C:/Program Files/ScheduleWorks/data/requirements.json") as f:
            content = f.read()
            self.assertEqual(json.loads(content), expected_output)

@patch('parse_info.open', mock_open(read_data=file_content), create=True)
@patch('json.dump')
    def test_idk(self, mock_dump):
        parse_info.idk()

        expected_output = {
            "Course History": {
                "CSCI": {
                    "101": 4
                }
            },
            "Tot_credits": 4,
            "Course Requirements": []
        }
        mock_dump.assert_called_once_with(expected_output, mock_open(), indent=4)
