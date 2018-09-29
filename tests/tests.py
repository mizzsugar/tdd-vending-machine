import pytest
import unittest

class VendingMachine:
    def __init__(self):
        self.receipt_amount = 0

    def cola(self):
        if self.receipt_amount >= 100:
            return 'コーラ'
        else:
            return None

    def oolong(self):
        if self.receipt_amount >= 100:
            return 'ウーロン茶'
        else:
            return None
        
    def redbull(self):
        if self.receipt_amount >= 200:
            return 'レッドブル'
        else:
            return None


    def click(self, beverage=None):
        if beverage is None:
            return None
        elif beverage ==  "コーラ":
            return self.cola()
        elif beverage ==  "ウーロン茶":
            return self.oolong()
        elif beverage ==  "レッドブル":
            return self.redbull()                 
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
