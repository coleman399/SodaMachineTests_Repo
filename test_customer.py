import  unittest
from coins import Coin, Quarter
from soda_machine import SodaMachine
from wallet import Wallet
from customer import Customer
from cans import Can
from backpack import Backpack
class TestGetWalletCoin(unittest.TestCase):

    def setUp(self):
        self.wallet = Wallet()
        

    def test_get_wallet_coin(self):
        """Verify that each type of coin can be returned from wallet"""
        wallet = self.wallet.money
        
        for coin in range(0, len(wallet)):
            with self.subTest("Subtest", coin = coin):
                # . Test each type of coin can be returned from wallet
                if wallet[coin] != None:
                    can_be_returned = True
                else:
                    can_be_returned = False
                #  Test that passing in a string that is not a valid coin name will return None
                if wallet[coin].name == 'Quarter' or wallet[coin].name == 'Dime' or wallet[coin].name == 'Nickel' or wallet[coin].name == 'Penny':
                    proper_name = True
                else:
                    proper_name = False
                
        if can_be_returned and proper_name == True:
            result = True
        else:
            result = False

        print(can_be_returned, proper_name)
        self.assertTrue(result)


class test_add_coins_to_wallet(unittest.TestCase):

    def setUp(self):
        self.wallet = Wallet()
        self.quarter = Quarter()
        self.customer = Customer()

    def test_add_coins_to_wallet(self):
        """Verify that adding coins increases the length of money list"""
        wallet = []
        wallet.append(self.quarter)
        wallet.append(self.quarter)
        wallet.append(self.quarter)

        result = self.customer.add_coins_to_wallet(wallet)
        if len(wallet) == 3:
            return True
        else:
            return False

        if len(wallet) == 3:
            wallet.append()
            if len(wallet)==3:
                return True
            else:
                return False
                
        self.assertEqual(True, True)
    
class add_can_to_backpack(unittest.TestCase):

    def setUp(self):
        self.can = Can('Cola', 0.60)
        self.backpack = Backpack()
        

    def test_add_can_to_backpack(self):
        purchased_cans = []
        purchased_cans.append('Cola')
        answer = ''
        if (len(purchased_cans)) == 1:
            answer = True
        else:
            answer = False

        self.assertEqual(answer, True)
        




        
if __name__ == '__main__':
    unittest.main()


