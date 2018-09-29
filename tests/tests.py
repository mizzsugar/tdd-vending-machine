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
            return True
        else:
            return False


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
            if self.cola.can_buy(self.receipt_amount):
                return self.cola
            return None
        elif beverage == self.oolong.name:
            if self.oolong.can_buy(self.receipt_amount):
                return self.oolong
            return None
        elif beverage == self.redbull.name:
            if self.redbull.can_buy(self.receipt_amount):
                return self.redbull
            return None
        else:
            return None
    
    def insert(self, coin: int):
        self.receipt_amount += coin
        
        if self.cola.can_buy(self.receipt_amount):
            self.lightened.append(self.cola.name)
        if self.oolong.can_buy(self.receipt_amount):
            self.lightened.append(self.oolong.name)
        if self.redbull.can_buy(self.receipt_amount):
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

    def test_0円入れるとレッドブルが出でない(self):
        vending_machine = VendingMachine()

        assert vending_machine.click("レッドブル") == None

    def test_100円入れるとレッドブルが出でない(self):
        vending_machine = VendingMachine()

        vending_machine.insert(100)
        assert vending_machine.click("レッドブル") == None

    def test_200円入れるとレッドブルが出る(self):
        vending_machine = VendingMachine()

        vending_machine.insert(200)
        assert vending_machine.click("レッドブル") == vending_machine.redbull

    def test_お金を入れるとボタンが光る(self):
        vending_machine = VendingMachine()
        vending_machine.insert(100)

        expect = ["コーラ", "ウーロン茶"]
        actual = vending_machine.lightened
        assert expect == actual

    def test_100円と50円と500円と10円を入れられる(self):
        vending_machine = VendingMachine()

        yen100 = Yen(100)
        yen50 = Yen(50)
        yen500 = Yen(500)
        yen10 = Yen(10)

        vending_machine.insert(yen100)

        assert  vending_machine.receipt_amount == 100


if __name__ == "__main__":
    unittest.main()
