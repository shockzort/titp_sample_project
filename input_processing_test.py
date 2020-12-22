import unittest
import compute_user_function as cus
import user_prompt as up
import datetime
import random
import string


def get_random_int_number(left, right):
    return random.randint(left, right)


def get_random_float_number(left, right):
    return random.gauss(left, right)


def get_random_string(length):
    if length > 1:
        return ''.join(random.choice(string.ascii_lowercase +
                                     string.ascii_uppercase +
                                     string.digits)
                       for _ in range(length))

    if length == 1:
        return ''.join(random.choice(string.ascii_lowercase +
                                     string.ascii_uppercase)
                       for _ in range(length))


# Basic tests to check for correct falue parsing
class TestParsingMethods(unittest.TestCase):
    random.seed(datetime.datetime.now())

    def test_parsing_empty_symbol(self):
        success, result = up.try_parse_arg('')
        self.assertEqual(success, False)

    def test_parsing_symbol(self):
        success, result = up.try_parse_arg(get_random_string(1))
        self.assertEqual(success, False)

    def test_parsing_string(self):
        success, result = up.try_parse_arg(get_random_string(10))
        self.assertEqual(success, False)

    def test_parsing_int_neg(self):
        success, result = up.try_parse_arg(get_random_int_number(-10, -1))
        self.assertEqual(success, True)

    def test_parsing_int_pos(self):
        success, result = up.try_parse_arg(get_random_int_number(1, 10))
        self.assertEqual(success, True)

    def test_parsing_int_random(self):
        success, result = up.try_parse_arg(get_random_int_number(-10, 10))
        self.assertEqual(success, True)

    def test_parsing_int_zero(self):
        success, result = up.try_parse_arg(0)
        self.assertEqual(success, True)

    def test_parsing_int_small(self):
        success, result = up.try_parse_arg(int(up.min_value))
        self.assertEqual(success, True)

    def test_parsing_int_big(self):
        success, result = up.try_parse_arg(int(up.max_value))
        self.assertEqual(success, True)

    def test_parsing_float_neg(self):
        success, result = up.try_parse_arg(get_random_float_number(-10.0, -1.0))
        self.assertEqual(success, True)

    def test_parsing_float_pos(self):
        success, result = up.try_parse_arg(get_random_float_number(1.0, 10.0))
        self.assertEqual(success, True)

    def test_parsing_float_random(self):
        success, result = up.try_parse_arg(get_random_float_number(-10.0, 10.0))
        self.assertEqual(success, True)

    def test_parsing_float_zero(self):
        success, result = up.try_parse_arg(0.0)
        self.assertEqual(success, True)

    def test_parsing_float_small(self):
        success, result = up.try_parse_arg(up.min_value)
        self.assertEqual(success, True)

    def test_parsing_float_big(self):
        success, result = up.try_parse_arg(up.max_value)
        self.assertEqual(success, True)


# Basic tests to check for non processed exceptions when handling computations
class TestComputationMethods(unittest.TestCase):
    random.seed(datetime.datetime.now())

    def test_compute_zero(self):
        result = cus.compute_function(0.0, 0.0)
        self.assertEqual(len(result) > 0, True)

    def test_compute_zero_pos(self):
        result = cus.compute_function(0.0, up.max_value)
        self.assertEqual(len(result) > 0, True)

    def test_compute_pos_zero(self):
        result = cus.compute_function(up.max_value, 0.0)
        self.assertEqual(len(result) > 0, True)

    def test_compute_zero_neg(self):
        result = cus.compute_function(0.0, -up.max_value)
        self.assertEqual(len(result) > 0, True)

    def test_compute_nrg_zero(self):
        result = cus.compute_function(-up.max_value, 0.0)
        self.assertEqual(len(result) > 0, True)

    def test_compute_small(self):
        result = cus.compute_function(up.min_value, up.min_value)
        self.assertEqual(len(result) > 0, True)

    def test_compute_small_big(self):
        result = cus.compute_function(up.min_value, up.max_value)
        self.assertEqual(len(result) > 0, True)

    def test_compute_big_small(self):
        result = cus.compute_function(up.max_value, 1.0e-35)
        self.assertEqual(len(result) > 0, True)

    def test_compute_big(self):
        result = cus.compute_function(up.max_value, up.max_value)
        self.assertEqual(len(result) > 0, True)

    def test_compute_neg(self):
        result = cus.compute_function(get_random_float_number(-10.0, -1.0),
                                      get_random_float_number(-10.0, -1.0))
        self.assertEqual(len(result) > 0, True)

    def test_compute_pos(self):
        result = cus.compute_function(get_random_float_number(1.0, 10.0),
                                      get_random_float_number(1.0, 10.0))
        self.assertEqual(len(result) > 0, True)

    def test_compute_pos_neg(self):
        result = cus.compute_function(get_random_float_number(1.0, 10.0),
                                      get_random_float_number(-10.0, -1.0))
        self.assertEqual(len(result) > 0, True)

    def test_compute_neg_pos(self):
        result = cus.compute_function(get_random_float_number(-10.0, -1.0),
                                      get_random_float_number(1.0, 10.0))
        self.assertEqual(len(result) > 0, True)

    def test_compute_random(self):
        result = cus.compute_function(get_random_float_number(-10.0, 10.0),
                                      get_random_float_number(-10.0, 10.0))
        self.assertEqual(len(result) > 0, True)

    def test_compute_random_big(self):
        result = cus.compute_function(get_random_float_number(-up.max_value, up.max_value),
                                      get_random_float_number(-up.max_value, up.max_value))
        self.assertEqual(len(result) > 0, True)


if __name__ == '__main__':
    unittest.main()
