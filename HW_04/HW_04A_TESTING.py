import unittest
from HW_04A_ekocibelli import get_user_data, get_user_id


class Test_Github_Data(unittest.TestCase):

    def test_not_valid_user(self):
        self.assertEqual(get_user_data("ekocibel"), "User ekocibel does not exist.")

    def test_valid_user(self):
        self.assertEqual(get_user_data('richkempinski'),
                         {'Mocks': 10,
                          'Project1': 2,
                          'hellogitworld': 30,
                          'helloworld': 6,
                          'threads-of-life': 1})


if __name__ == '__main__':
    print('Running HW_04A_TESTING.py testing suite...')
    unittest.main(exit=False, verbosity=2)