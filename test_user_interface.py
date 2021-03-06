import unittest
from cans import Cola, OrangeSoda, RootBeer
from coins import Nickel, Penny, Quarter, Dime
from user_interface import display_payment_value, get_unique_can_names, try_parse_int, validate_coin_selection, validate_main_menu

class TestUserInterface(unittest.TestCase):

    def test_validate_main_menu_selection_1(self):
        """Test to validate main menu selection works"""
        answer = False
        if validate_main_menu(1)== (True, 1):
            answer = True
        self.assertEqual(answer, True)

    def test_validate_main_menu_selection_2(self):
        """Test to validate main menu selection works"""
        answer = False
        if validate_main_menu(2)== (True, 2):
            answer = True
        self.assertEqual(answer, True)

    def test_validate_main_menu_selection_3(self):
        """Test to validate main menu selection works"""
        answer = False
        if validate_main_menu(3)== (True, 3):
            answer = True
        self.assertEqual(answer, True)

    def test_validate_main_menu_selection_4(self):
        """Test to validate main menu selection works"""
        answer = False
        if validate_main_menu(4)== (True, 4):
            answer = True
        self.assertEqual(answer, True)

    def test_validate_main_menu_selection_8(self):
        """Test to validate main menu doesn't accept incorrect input"""
        answer = False
        if validate_main_menu(8)== (False, None):
            answer = True
        self.assertEqual(answer, True)

    def test_try_parse_int_num(self):
        """Ensure integer is returned as input"""
        answer = False
        if try_parse_int(10) == 10:
            answer = True
        self.assertEqual(answer, True)
    def test_try_parse_int_string(self):
        """Ensure string retuns 0"""
        answer = False
        if try_parse_int('hello') == 0:
            answer = True
        self.assertEqual(answer, True)

    def test_get_unique_can_names(self):
        """Ensures can list will populate only once with each can"""
        get_unique_can_names('')
        self.cola = Cola()
        self.orange_soda = OrangeSoda()
        self.root_beer = RootBeer()
        soda_list = []
        answer = True
        for i in range (1, 3):
            soda_list.append(self.cola)
            soda_list.append(self.orange_soda)
            soda_list.append(self.root_beer)
        print(soda_list)
        if len(get_unique_can_names(soda_list)) == 3:
            answer = True
        self.assertEqual(answer, True)

    def test_get_unique_can_names_empty(self):
        """Ensures empty input does not add anything to the list"""
        empty_list = []
        answer = False
        if get_unique_can_names(empty_list) == []:
            answer = True

        self.assertEqual(answer, True)

    def test_display_payment_value(self):
        """Tests to ensure the currency is assigned the correct value"""
        self.quarter = Quarter()
        self.dime = Dime()
        self.nickel = Nickel()
        self.penny = Penny()
        coin_list = [self.quarter, self.dime, self.nickel, self.penny]
        if display_payment_value(coin_list) == 0.41:
            answer = True
        self.assertEqual(answer, True)
    
    
    def test_display_payment_value_empty_list(self):
        """tests to ensure the returned value of empty list is 0"""
        empty_list = []
        if display_payment_value(empty_list) == 0:
            answer = True
        self.assertEqual(answer, True)
            
    def test_validate_quarter_selection(self):
        """Tests to ensure appropriate value is returend"""
        answer = False
        if validate_coin_selection(1) == (True, "Quarter"):
            answer = True
        self.assertEqual(answer, True)

    def test_validate_dime_selection(self):
        """Tests to ensure appropriate value is returend"""
        answer = False
        if validate_coin_selection(2) == (True, "Dime"):
            answer = True
        self.assertEqual(answer, True)

    def test_validate_nickel_selection(self):
        """Tests to ensure appropriate value is returend"""
        answer = False
        if validate_coin_selection(3) == (True, "Nickel"):
            answer = True
        self.assertEqual(answer, True)

    def test_validate_nickel_selection(self):
        """Tests to ensure appropriate value is returend"""
        answer = False
        if validate_coin_selection(4) == (True, "Penny"):
            answer = True
        self.assertEqual(answer, True)

    def test_validate_nickel_selection(self):
        """Tests to ensure appropriate value is returend"""
        answer = False
        if validate_coin_selection(5) == (True, "Done"):
            answer = True
        self.assertEqual(answer, True)
        
    def test_validate_othervalue_selection(self):
        """Tests to ensure appropriate value is returend"""
        answer = False
        if validate_coin_selection(42) == (False, None):
            answer = True
        self.assertEqual(answer, True)

        


if __name__ == '__main__':
    unittest.main()
