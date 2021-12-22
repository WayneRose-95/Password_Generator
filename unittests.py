from password_generator import Random_Password
import unittest 

class Test_Password_Generator(unittest.TestCase):

    def setUp(self):
        self.test_password = Random_Password()

    def test_get_user_input(self):
        test_user_input = self.test_password.get_user_input()

        self.assertIsInstance(test_user_input, int)

    def test_create_the_password(self):
        sample_password = self.test_password.create_the_password(10)
        self.assertIsInstance(sample_password, str)

    def test_choose_again_True(self):
        sample_input = self.test_password.choose_again()
        self.assertTrue(sample_input)

    def test_choose_again_False(self):
        sample_input = self.test_password.choose_again()
        self.assertFalse(sample_input)

    def tearDown(self):
        del self.test_password
        
unittest.main(argv=[''], verbosity=2, exit=False)