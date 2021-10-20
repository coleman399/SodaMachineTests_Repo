import  unittest
from coins import Quarter
from coins import Dime
from coins import Nickel
from coins import Penny
from soda_machine import SodaMachine

class TestFillRegister(unittest.TestCase):
    """tests for SodaMachine's fill_register function"""

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_fill_register(self):
        """verify proper amount of coins are being added to register list"""
        register = self.soda_machine.register

        quarters = 0
        dimes = 0
        nickels = 0
        pennies = 0
 
        print(f"The length of the register is {len(register)}.")
        for coin in range(0, len(register)):
            with self.subTest("Subtest", coin = coin):
                # supposed to be 8 quarters
                if register[coin].name == 'Quarter':
                    quarters += 1  
                # supposed to be 10 dimes
                elif register[coin].name == 'Dime':
                    dimes += 1
                # supposed to be 20 nickels
                elif register[coin].name == 'Nickel':
                    nickels += 1
                #should be 50 pennies
                else:
                    pennies += 1
        
        expected_result = [8, 10, 20, 50]
        result = [quarters, dimes, nickels, pennies]

        self.assertEqual(expected_result, result)

class TestFillInventory(unittest.TestCase):
    """test fill_inventory method in SodaMachine Class"""

    def setUp(self):
        self.soda_machine = SodaMachine()
    
    def test_fill_inventory(self):
        """verify proper amount of cans are added to inventory list"""
        inventory = self.soda_machine.inventory

        cola = 0
        orange_soda = 0
        root_beer = 0

        print(f"The length of the inventory is {len(inventory)}.")

        for can in range(0, len(inventory)):
            with self.subTest("Subtest", can = can):
                # supposed to be 10 Cola
                if inventory[can].name == 'Cola':
                    cola += 1
                # supposed to be 10 Orange Soda
                elif inventory[can].name == 'Orange Soda':
                    orange_soda += 1
                # supposed to be 10 Root Beer
                else:
                    root_beer += 1

        expected_result = [10, 10, 10]
        result = [cola, orange_soda, root_beer]

        self.assertEqual(expected_result, result)

class TestGetCoinFromRegister(unittest.TestCase):
    """test get_coin_from_register method in SodaMachine Class"""
    
    def setUp(self):
        self.soda_machine = SodaMachine()
    
    def test_get_coin_from_register(self):
        """make sure coin got removed from register list and return the same coin"""
        register = self.soda_machine.register
        can_be_returned = None
        proper_name = None

        print(f"The length of the inventory is {len(register)}.")
        for coin in range(0, len(register)):
            with self.subTest("Subtest", coin = coin):
                # . Test each type of coin can be returned from register
                if register[coin] != None:
                    can_be_returned = True
                else:
                    can_be_returned = False
                #  Test that passing in a string that is not a valid coin name will return None
                if register[coin].name == 'Quarter' or register[coin].name == 'Dime' or register[coin].name == 'Nickel' or register[coin].name == 'Penny':
                    proper_name = True
                else:
                    proper_name = False
                
        if can_be_returned and proper_name == True:
            result = True
        else:
            result = False

        print(can_be_returned, proper_name)
        self.assertTrue(result)

class RegisterHasCoin(unittest.TestCase):
    """test register_has_coin method in SodaMachine Class"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_register_has_coin(self):
        """test that each type of coin will return True, Test that a non-valid coin name will return False"""
        register = self.soda_machine.register
        counter = 0
        proper_name = True

        for coin in range(0, len(register)):
            with self.subTest("Subtest", coin = coin):
                # supposed to be 8 quarters
                if register[coin].name == 'Quarter' or register[coin].name == 'Dime' or register[coin].name == 'Nickel' or register[coin].name == 'Penny':
                    continue
                else:
                    counter += 1 
        
        if counter > 0:
            proper_name = False
                
        self.assertTrue(proper_name) 

class DetermineChangeValue(unittest.TestCase):
    """test determine_change_value method in SodaMachine Class"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_determine_change_value(self):
        """test with total payment higher, test with select_soda_price higher, test with two equal values"""
        higher_payment = self.soda_machine.determine_change_value(10, 5)
        higher_price = self.soda_machine.determine_change_value(5, 10)
        equal_pay = self.soda_machine.determine_change_value(5, 5)
        expected_result = [True, True, True]
        result = []
        
        if higher_payment == 5:
            result.append(True)
        else:
            result.append(False)
        
        if higher_price == -5:
            result.append(True)
        else:
            result.append(False)
        
        if equal_pay == 0:
            result.append(True)
        else:
            result.append(False)
        
        print(result)
        self.assertEqual(expected_result, result)

class CalculateCoinValue(unittest.TestCase):
    """test calculate_coin_value method in SodaMachine Class"""
    def setUp(self):
        self.soda_machine = SodaMachine()
        self.quarter = Quarter()
        self.dime = Dime()
        self.nickel = Nickel()
        self.penny = Penny()

    def test_calculate_coin_value(self):
        """instantiate each of the 4 coin types and append them to a list. Pass the list into this function, ensure the returned values is .41"""
        """Pass in an empty list. Ensure the returned value is 0"""
        quarter = self.quarter
        dime = self.dime
        nickel = self.nickel
        penny = self.penny

        coin_list = []
        coin_list.append(quarter)
        coin_list.append(dime)
        coin_list.append(nickel)
        coin_list.append(penny)

        result = None

        if self.soda_machine.calculate_coin_value(coin_list) == .41:
            result = True
        else:
            result = False
        
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
