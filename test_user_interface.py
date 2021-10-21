from unittest import result
from cans import Cola, OrangeSoda, RootBeer
import unittest
from coins import Nickel, Penny, Quarter, Dime

from user_interface import display_payment_value, get_unique_can_names, try_parse_int, validate_main_menu

class TestUserInterface(unittest.TestCase):

    def test_validate_main_menu(self):
        """Test to make sure only 1-4 return values"""
        #self.main_menu = validate_main_menu('')
        validate_main_menu('')
        answer = 1
        check_answer = 5
        for i in range (1, 4):
            if validate_main_menu(i) == (True, 1) or (True, 2) or (True, 3) or (True, 4):
                answer += 1
        if validate_main_menu(8) == (False, None):
            answer += 1
        self.assertEqual(answer, check_answer)
        

    def test_try_parse_int(self):
        """Ensure integer is returned as input and string retuns 0"""
        string_input = ('hello')
        try_parse_int('')
        try_parse_int(10)
        try_parse_int(string_input)

    def test_get_unique_can_names(self):
        get_unique_can_names('')
        self.cola = Cola()
        self.orange_soda = OrangeSoda()
        self.root_beer = RootBeer()
        soda_list = []
        empty_list = []
        result_list = []
        expected_answer = [1, 1]
        for i in range (1, 3):
            soda_list.append(self.cola)
            soda_list.append(self.orange_soda)
            soda_list.append(self.root_beer)
        print(soda_list)
        if len(get_unique_can_names(soda_list)) == 3:
            result_list.append(1)
        if get_unique_can_names(empty_list) == []:
            result_list.append(1)

        self.assertEqual(expected_answer, result_list)

    def test_display_payment_value(self):
        self.quarter = Quarter()
        self.dime = Dime()
        self.nickel = Nickel()
        self.penny = Penny()
        result_list = []
        empty_list = []
        expected_answer = [1, 1]
        coin_list = [self.quarter, self.dime, self.nickel, self.penny]
        if display_payment_value(coin_list) == 0.41:
            result_list.append(1)
        if display_payment_value(empty_list) == 0:
            result_list.append(1)
        self.assertEqual(expected_answer, result_list)
            
    def test_validate_coin_selection(self):
        result_list = []
        expected_list = [1,1,1,1,1,0]
        i = 1
        for i in range (1, 6):
            if validate_main_menu(i) == (True, "Quarter") or (True, "Dime") or (True, "Nickel") or (True, "Penny") or (True, "Done"):
                result_list.append(1)
        if validate_main_menu(42) == (False, None):
            result_list.append(0)

        self.assertEqual(expected_list, result_list)


if __name__ == '__main__':
    unittest.main()