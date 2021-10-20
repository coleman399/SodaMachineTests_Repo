import unittest
from wallet import Wallet

class TestFillWallet(unittest.TestCase):
    """tests for test length of money list in wallet"""

    def setUp(self):
        self.wallet = Wallet()
    
    def test_fill_wallet(self):

        wallet = self.wallet.money
        im_paid = None

        if len(wallet) == 88:
            im_paid = True
        else:
            im_paid = False

        self.assertEqual(True, im_paid)

if __name__ == '__main__':
    unittest.main()


