from rearrange import rearrange_name
import unittest


class TestRearrange(unittest.TestCase):

    def setUp(self):
        print("new test {} initiated!".format(self._testMethodName))
        return super().setUp()

    def tearDown(self):
        print("success" if self._outcome.success else "failed")
        return super().tearDown()

    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"

        # assertEqual: verify what we expected is exactly equal to what we got
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        self.assertEqual(rearrange_name(""), "")

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_hyphenated_first_name(self):
        self.assertEqual(rearrange_name("Picard, Jean-Luc"), "Jean-Luc Picard")

    def test_invalid_input(self):
        # Verifies if TypeError or AttributeError is raised 
        # when the wrong data type is passed
        # into the function
        with self.assertRaises((TypeError, AttributeError)):
            rearrange_name(1234)

        with self.assertRaises((TypeError, AttributeError)):
            rearrange_name(["Ho", "ho", "ho"])

        with self.assertRaises((TypeError, AttributeError)):
            rearrange_name(None)
    

# Run the test
unittest.main()