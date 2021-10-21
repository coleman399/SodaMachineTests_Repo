import unittest
from unittest import result
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
    
    def test_get_quarter_from_register(self):
        """make sure quarter got removed from register list and return the same coin"""
        quarter = Quarter()
        results = 0
        compared_coin = self.soda_machine.get_coin_from_register(quarter.name)
        if compared_coin.name == quarter.name:
            results += 1
        self.assertEqual(1, results)

    def test_get_dime_from_register(self):
        """make sure dime got removed from register list and return the same coin"""
        dime = Dime()
        results = 0
        compared_coin = self.soda_machine.get_coin_from_register(dime.name)
        if compared_coin.name == dime.name:
            results += 1
        self.assertEqual(1, results)

    def test_get_nickel_from_register(self):
        """make sure nickel got removed from register list and return the same coin"""
        nickel = Nickel()
        results = 0
        compared_coin = self.soda_machine.get_coin_from_register(nickel.name)
        if compared_coin.name == nickel.name:
            results += 1
        self.assertEqual(1, results)
 
    def test_get_penny_from_register(self):
        """make sure penny got removed from register list and return the same coin"""
        penny = Penny()
        results = 0
        compared_coin = self.soda_machine.get_coin_from_register(penny.name)
        if compared_coin.name == penny.name:
            results += 1
        self.assertEqual(1, results)

class TestRegisterHasCoin(unittest.TestCase):
    """test register_has_coin method in SodaMachine Class"""
    def setUp(self):
        self.soda_machine = SodaMachine()
    
    def test_register_has_quarter(self):
        """make sure quarter returns true"""
        quarter = Quarter()
        results = 0
        compared_coin = self.soda_machine.register_has_coin(quarter.name)
        if compared_coin == True:
            results += 1
        self.assertEqual(1, results)

    def test_register_has_dime(self):
        """make sure dime returns true"""
        dime = Dime()
        results = 0
        compared_coin = self.soda_machine.register_has_coin(dime.name)
        if compared_coin == True:
            results += 1
        self.assertEqual(1, results)

    def test_register_has_nickel(self):
        """make sure nickel returns true"""
        nickel = Nickel()
        results = 0
        compared_coin = self.soda_machine.register_has_coin(nickel.name)
        if compared_coin == True:
            results += 1
        self.assertEqual(1, results)
                
    def test_register_has_penny(self):
        """make sure penny returns true"""
        penny = Penny()
        results = 0
        compared_coin = self.soda_machine.register_has_coin(penny.name)
        if compared_coin == True:
            results += 1
        self.assertEqual(1, results)

    def test_register_does_not_have_nonsense(self):
        """make sure nonsense returns false"""
        nonsense_coin = "nonsense coin"
        results = 0
        compared_coin = self.soda_machine.register_has_coin(nonsense_coin)
        if compared_coin == False:
            results += 1
        self.assertEqual(1, results)

class TestDetermineChangeValue(unittest.TestCase):
    """test determine_change_value method in SodaMachine Class"""
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_determine_higher_payment(self):
        """test with total payment higher, test with select_soda_price higher, test with two equal values"""
        higher_payment = self.soda_machine.determine_change_value(10, 5)
        result = None
        if higher_payment == 5:
            result = True
        else:
            result = False
        self.assertTrue(result)

    def test_determine_higher_price(self):
        """test with total payment higher, test with select_soda_price higher, test with two equal values"""
        higher_price = self.soda_machine.determine_change_value(5, 10)
        result = None
        if higher_price == -5:
            result = True
        else:
            result = False
        self.assertTrue(result)

    def test_determine_equal_pay(self):
        """test with total payment higher, test with select_soda_price higher, test with two equal values"""
        equal_pay = self.soda_machine.determine_change_value(5, 5)
        result = None
        if equal_pay == 0:
            result = True
        else:
            result = False
        self.assertTrue(result)

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
        coin_list = []
        coin_list.append(self.quarter)
        coin_list.append(self.dime)
        coin_list.append(self.nickel)
        coin_list.append(self.penny)
        result = None
        if self.soda_machine.calculate_coin_value(coin_list) == .41:
            result = True
        else:
            result = False
        self.assertTrue(result)

    def test_calculate_coin_value(self):
        """Pass in an empty list. Ensure the returned value is 0"""
        coin_list = []
        result = None
        if self.soda_machine.calculate_coin_value(coin_list) == 0:
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

    def test_get_inventory_cola(self):
        """pass in cola, ensure the returned can has the same name"""
        cola = Cola()
        results = 0
        compared_can = self.soda_machine.get_inventory_soda(cola.name)
        if compared_can.name == cola.name:
            results += 1
        self.assertEqual(1, results)

    def test_get_inventory_orange_soda(self):
        """pass in orange soda, ensure the returned can has the same name"""
        orange_soda = OrangeSoda()
        results = 0
        compared_can = self.soda_machine.get_inventory_soda(orange_soda.name)
        if compared_can.name == orange_soda.name:
            results += 1
        self.assertEqual(1, results)

    def test_get_inventory_root_beer(self):
        """pass in root beer, ensure the returned can has the same name"""
        rootbeer = RootBeer()
        results = 0
        compared_can = self.soda_machine.get_inventory_soda(rootbeer.name)
        if compared_can.name == rootbeer.name:
            results += 1
        self.assertEqual(1, results)

    def test_get_inventory_cola(self):
        """pass in “Mountain Dew” and ensure None is returned"""
        mountain_dew = "Mountain Dew"
        results = 0
        compared_can = self.soda_machine.get_inventory_soda(mountain_dew)
        if compared_can == None:
            results += 1
        self.assertEqual(1, results)

class TestReturnInventory(unittest.TestCase):
    """test the return_inventory method in the SodaMachine Class"""
    def setUp(self):
        self.soda_machine = SodaMachine()
        self.cola = Cola()

    def test_return_inventory(self):
        """Instantiate a can and pass it into the method. Test that the len of self.inventory is now 31"""
        results = None
        self.soda_machine.return_inventory(self.cola)
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
        coin_list = [self.quarter, self.dime, self.nickel, self.penny]
        result = None
        self.soda_machine.deposit_coins_into_register(coin_list)
        if len(self.soda_machine.register) == 92:
            result = True
        else:
            result = False
        self.assertTrue(result)    

if __name__ == '__main__':
    unittest.main()
