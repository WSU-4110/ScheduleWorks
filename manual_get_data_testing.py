import unittest
import manual_get_data as get_json_data

class test_manual_get_data(unittest.TestCase):

    def set_manual_get_data():
        sid = 'gy3531'
        passwd = 'password123'

    def test_get_json_data(self, sid, passwd):
        actualsid = sid
        actualpasswd = passwd
        expectedsid = 'gy3531'
        expectedpasswd = 'password123'
        sid.assertEqual(expectedsid, actualsid)
        passwd.assertEqual(expectedpasswd, actualpasswd)
        

if __name__ == '__main__':
    unittest.main()