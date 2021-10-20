

from typing import Counter
import  unittest
from soda_machine import SodaMachine


class TestFillRegister(unittest.TestCase):
    """Tests for SodaMachine's fill_register function"""

    def setUp(self):
        """Sets up testing environment by instantiation of a sodamachine"""
        self.soda_machine = SodaMachine()

    def test_fill_register(self):
        """Verify proper amount of quarters are being added to list"""
        expected_result = [8, 10, 20, 50]
        quarters = 0
        dimes = 0
        nickels = 0
        pennies = 0
       

        register = self.soda_machine.register
        print ('register)
        # for i in len(register):
        #     # supposed to be 8 quarters
        #     if register[i] == 'Quarter':
        #         quarters += 1  
        #     # supposed to be 10 dimes
        #     elif register[i] is 'Dime':
        #         dimes += 1
        #     # supposed to be 20 nickels
        #     elif register[i] is 'Nickel':
        #         nickels += 1
        #     #should be 50 pennies
        #     else:
        #         pennies += 1

        result = [quarters, dimes, nickels, pennies]
        
        #self.assertEqual(expected_result, result)
                        
if __name__ == '__main__':
    unittest.main()