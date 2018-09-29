import pytest
import unittest

class VendingMachine:
    def __init__(self):
        self.receipt_amount = 0

    def click(self):
        if self.receipt_amount >= 100:
            return "コーラ"
        else:
            return None
    
    def insert(self, coin: int):
        self.receipt_amount += coin

class TestVendingMachine(unittest.TestCase):
    def test_ボタンを押すとコーラが出る(self):
        vending_machine = VendingMachine()

        assert vending_machine.click() == None

        vending_machine.insert(100)
        assert vending_machine.click('コーラ') == 'コーラ'


if __name__ == "__main__":
    unittest.main()
