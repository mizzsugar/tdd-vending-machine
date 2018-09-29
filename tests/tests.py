import pytest
import unittest

class VendingMachine:
    def __init__(self):
        self.receipt_amount = 0

    def click(self, beverage=None):
        if beverage is None:
            return None
        elif self.receipt_amount >= 100:
            return beverage
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

    def test_ボタンを押すとウーロン茶が出る(self):
        vending_machine = VendingMachine()

        assert vending_machine.click() == None

        vending_machine.insert(100)
        assert vending_machine.click("ウーロン茶") == "ウーロン茶"

    def test_200円入れるとレッドブルが出る(self):
        vending_machine = VendingMachine()

        assert vending_machine.click("レッドブル") == None

        vending_machine.insert(100)
        assert vending_machine.click("レッドブル") == None

        vending_machine.insert(100)
        assert vending_machine.click("レッドブル") == "レッドブル"

if __name__ == "__main__":
    unittest.main()
