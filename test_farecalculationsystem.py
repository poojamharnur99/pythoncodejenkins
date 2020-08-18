#unit testing for railway fare calculation
import unittest
import farecalculationsystem #import program module which calculate amount to pay to book ticket

class TestFarecalculationsystem(unittest.TestCase):
    # test case 1
    # test case to check fare for 5 passanger and second class
    def test_farecalculationsystem(self):
        result = farecalculationsystem.calculare_fare(5,2) #test case to check fare for 5 passanger and general  class
        self.assertEqual(result, 1545)

    # test case 2
    # test case to check fare for 5 passanger and first class
    def test_farecalculationsystem2(self):
        result = farecalculationsystem.calculare_fare(5, 1)  # test case to check fare for 5 passanger and first class
        self.assertEqual(result, 2100)

    # test case 3
    # test case to check fare for 5 passanger and invalid choise for class
    def test_farecalculationsystem3(self):
        result = farecalculationsystem.calculare_fare(5, 7)  # test case to check fare for 5 passanger and invalid  class choise
        self.assertEqual(result, 0)

    # test case 4
    # test case to check fare for if number of passanger is not integer input
    def test_farecalculationsystem4(self):
        result = farecalculationsystem.calculare_fare('five', 7)  # test case to check fare for 5 passanger and invalid  class choise
        self.assertEqual(result, None)

    # test case 5
    # test case to check fare for if choise for class is not integer input
    def test_farecalculationsystem5(self):
        result = farecalculationsystem.calculare_fare(3,'two')  # test case to check fare for 5 passanger and invalid  class choise
        self.assertEqual(result, None)

    # test case 6
    # test case to check fare for if choise for class is not integer input
    def test_farecalculationsystem6(self):
        result = farecalculationsystem.calculare_fare('three','one')  # test case to check fare for 5 passanger and invalid  class choise
        self.assertEqual(result, None)




if __name__ == '__main__':
    unittest.main()
