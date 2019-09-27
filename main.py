import unittest
import student_code

class SetupTest(unittest.TestCase):
    def test1(self):
        result = student_code.hello_world()
        print(result)
        self.assertTrue(result, "wrong!")

if __name__ == '__main__':
    unittest.main()
