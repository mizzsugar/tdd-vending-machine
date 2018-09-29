import pytest
import unittest

"""
TODO: 

[x] 100円でコーラを買う
    [x] 0円でコーラは買えない
[x] 200円でレッドブルを買う
    [x] 0円でレッドブルは買えない
"""

class Beverage:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def can_buy(self, receipt_amount):
        if receipt_amount >= self.price:
            return self
        else:
            print("お金が足りません")
            return None


class VendingMachine:
    cola    = Beverage("コーラ", 100)
    oolong  = Beverage("ウーロン茶", 100)
    redbull = Beverage("レッドブル", 200)


    def __init__(self):
        self.receipt_amount = 0
        self.lightened = []

    def click(self, beverage:str=None):
        if beverage is None:
            return None
        elif beverage == self.cola.name:
            return self.cola.can_buy(self.receipt_amount)
        elif beverage == self.oolong.name:
            return self.oolong.can_buy(self.receipt_amount)
        elif beverage == self.redbull.name:
            return self.redbull.can_buy(self.receipt_amount)
        else:
            return None
    
    def insert(self, coin: int):
        self.receipt_amount += coin
        
        if self.cola.can_buy(self.receipt_amount) != None:
            self.lightened.append(self.cola.name)
        if self.oolong.can_buy(self.receipt_amount) != None:
            self.lightened.append(self.oolong.name)
        if self.redbull.can_buy(self.receipt_amount) != None:
            self.lightened.append(self.redbull.name)

    

class TestVendingMachine(unittest.TestCase):
    def test_ボタンを押すとコーラが出る(self):
        vending_machine = VendingMachine()

        assert vending_machine.click() == None

        vending_machine.insert(100)
        assert vending_machine.click('コーラ') == vending_machine.cola

    def test_ボタンを押すとウーロン茶が出る(self):
        vending_machine = VendingMachine()

        assert vending_machine.click() == None

        vending_machine.insert(100)
        assert vending_machine.click("ウーロン茶") == vending_machine.oolong

    def test_200円入れるとレッドブルが出る(self):
        vending_machine = VendingMachine()

        assert vending_machine.click("レッドブル") == None

        vending_machine.insert(100)
        assert vending_machine.click("レッドブル") == None

        vending_machine.insert(100)
        assert vending_machine.click("レッドブル") == vending_machine.redbull

    def test_お金を入れるとボタンが光る(self):
        vending_machine = VendingMachine()
        vending_machine.insert(100)

        expect = ["コーラ", "ウーロン茶"]
        actual = vending_machine.lightened
        assert expect == actual


if __name__ == "__main__":
    unittest.main()
