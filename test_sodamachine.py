import  unittest
from soda_machine import SodaMachine

class TestFillRegister(unittest.TestCase):
    """Tests for SodaMachine's fill_register function"""

    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_fill_register(self):
        """Verify proper amount of coins are being added to register list"""
        self.register = self.soda_machine.register

        quarters = 0
        dimes = 0
        nickels = 0
        pennies = 0
 
        print(f"The length of register equals {len(self.register)}")
        for coin in range(0, len(self.register)):
            with self.subTest("Subtest", coin = coin):
                # supposed to be 8 quarters
                if self.register[coin].name == 'Quarter':
                    quarters += 1  
                # supposed to be 10 dimes
                elif self.register[coin].name == 'Dime':
                    dimes += 1
                # supposed to be 20 nickels
                elif self.register[coin].name == 'Nickel':
                    nickels += 1
                #should be 50 pennies
                else:
                    pennies += 1
        
        expected_result = [8, 10, 20, 50]
        result = [quarters, dimes, nickels, pennies]

        self.assertEqual(expected_result, result)
                        
if __name__ == '__main__':
    unittest.main()
