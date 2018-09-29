import pytest
import unittest

class VendingMachine:
    def click(self):
        return "コーラ"

class TestVendingMachine(unittest.TestCase):
    def test_ボタンを押すとコーラが出る(self):
        vending_machine = VendingMachine()

        assert vending_machine.click() == None

        vending_machine.insert(100)
        assert vending_machine.click() == 'コーラ'


if __name__ == "__main__":
    unittest.main()
