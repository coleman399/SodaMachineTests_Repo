import unittest
from coins import Quarter, Dime, Nickel, Penny
from cans import Cola, OrangeSoda, RootBeer

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
        can_be_returned = None
        proper_name = None
        expected_result = [True, False]
        result = []
        dime = Dime()
        quarter = Quarter()
        nickel = Nickel()
        penny = Penny()
        counter = 0
        # Test each type of coin can be returned from register
        while self.soda_machine.get_coin_from_register(quarter) == 'Quarter' :
            counter += 1
        while self.soda_machine.get_coin_from_register(dime) == 'Dime' :
            counter += 1
        while self.soda_machine.get_coin_from_register(nickel) == 'Nickel' :
           counter += 1
        while self.soda_machine.get_coin_from_register(penny) == 'Penny':
            counter += 1
        #  Test that passing in a string that is not a valid coin name will return None
        if self.soda_machine.get_coin_from_register("Made up Soda Name") == None:
            proper_name = True
        else:
            proper_name = False
    
        if counter == 88:
            can_be_returned = True
        else:
            can_be_returned = False
        
        result = [proper_name, can_be_returned]

        self.assertEquals(expected_result, result)

class TestRegisterHasCoin(unittest.TestCase):
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
                if self.soda_machine.register_has_coin(register[coin].name) == True:
                    continue
                else:
                    counter += 1 

        
        if counter > 0:
            proper_name = False
                
        self.assertTrue(proper_name) 

class TestDetermineChangeValue(unittest.TestCase):
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
        
        self.assertEqual(expected_result, result)

class TestCalculateCoinValue(unittest.TestCase):
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

class TestGetInventorySoda(unittest.TestCase):
    """test the get_inventory_soda method in the SodaMachine Class"""
    def setUp(self):
        self.soda_machine = SodaMachine()
        self.cola = Cola()
        self.orange_soda = OrangeSoda()
        self.root_beer = RootBeer()

    def test_get_inventory_soda(self):
        """pass in each of the 3 soda names, ensure the returned can has the same name"""
        """pass in “Mountain Dew” and ensure None is returned"""
        cola = self.cola.name
        orange_soda = self.orange_soda.name
        root_beer = self.root_beer.name
        mountain_dew = "Mountain Dew"
        soda_list = [cola, orange_soda, root_beer, mountain_dew]
        expected_results = [True, True, True, False]
        results = []

        for soda in soda_list:
            if self.soda_machine.get_inventory_soda(soda) != None:
                test_soda = self.soda_machine.get_inventory_soda(soda)
                if soda == test_soda.name:
                    results.append(True)
                else:
                    results.append(False)
            else:
                    results.append(False)   
        
        self.assertEqual(expected_results, results)

class TestReturnInventory(unittest.TestCase):
    """test the return_inventory method in the SodaMachine Class"""
    def setUp(self):
        self.soda_machine = SodaMachine()
        self.cola = Cola()

    def test_return_inventory(self):
        """Instantiate a can and pass it into the method. Test that the len of self.inventory is now 31"""
        cola = self.cola
        results = None
        self.soda_machine.return_inventory(cola)
        if len(self.soda_machine.inventory) == 31:
            results = True
        else:
            results = False

        self.assertTrue(results)

class TestDepositCoinsIntoRegister(unittest.TestCase):
    """test the deposit_coins_into_register method in SodaMachine Class"""
    def setUp(self):
        self.soda_machine = SodaMachine()
        self.quarter = Quarter()
        self.dime = Dime()
        self.nickel = Nickel()
        self.penny = Penny()
    
    def test_deposit_coins_into_register(self):
        """Instantiate each of the 4 coins and append them to a list. Pass the list into the function, ensure the len of self.register is 92"""
        quarter = self.quarter
        dime = self.dime
        nickel = self.nickel
        penny = self.penny
        coin_list = [quarter, dime, nickel, penny]
        result = None

        self.soda_machine.deposit_coins_into_register(coin_list)

        if len(self.soda_machine.register) == 92:
            result = True
        else:
            result = False

        self.assertTrue(result)    

if __name__ == '__main__':
    unittest.main()
