
import unittest

import Bank


class Test(unittest.TestCase):
    def test_validation10(self):
        b = Bank()
        self.assertEquals(b.create_account(6721, "Jane Smith",'saving', 50000.0, 'Bronze'),{6721:{"Name":"Jane Smith","account":"saving","balance":50000.0,"credit_card":"Bronze"}})

    def test_validation11(self):
        b = Bank()
        self.assertEquals(b.check_minimal_balance(6721), 'Yes')

    def test_validation12(self):
        b = Bank()
        self.assertEquals(b.request_loan(6721, 45000.0, 'Gold Loan'),"Approved")

    def test_validation13(self):
        b = Bank()
        self.assertEquals(b.calculate_emi(45000.0, 'Gold Loan', 5),9877.5)

    def test_validation14(self):
        b = Bank()
        self.assertEquals(b.credit_card_payment(6721, 4000.0),46000.0)

    def test_validation20(self):
        b = Bank()
        self.assertEquals(b.create_account(7380, "Mary Jones", 'current', 65000.0, 'Silver'), {
            7380: {"Name": "Mary Jones", "account": "current", "balance": 65000.0, "credit_card": "Silver"}})

    def test_validation21(self):
        b = Bank()
        self.assertEquals(b.debit_card_payment(7380, 30000.0), 35000.0)

    def test_validation22(self):
        b = Bank()
        self.assertEquals(b.monthly_investment(7380, 30000.0), 5000.0)

    def test_validation23(self):
        b = Bank()
        self.assertEquals(b.check_minimal_balance(7380), {'fine': 1000.0})

    def test_validation24(self):
        b = Bank()
        self.assertEquals(b.request_loan(7380, 3500.0, 'Personal Loan'), "Approved")





    # def test_validation30(self):
    #     b = Bank()
    #     self.assertEquals(b.create_account(5827, "Tara Green",'checking', 75000.0, 'Platinum'),{5827:{"Name":"Tara Green","account":"checking","balance":75000.0,"credit_card":"Platinum"}})

    # def test_validation31(self):
    #     b = Bank()
    #     self.assertEquals(b.transfer_money(5827, 7380, 35700.0),{7380:{"balance":39700.0}, 5827:{"balance":39300.0}})

    # def test_validation32(self):
    #     b = Bank()
    #     self.assertEquals(b.debit_card_payment(5827, 34900.0),4400.0)

    # def test_validation33(self):
    #     b = Bank()
    #     self.assertEquals(b.check_minimal_balance(5827),{'fine':2500.0})

    # def test_validation34(self):
    #     b = Bank()
    #     self.assertEquals(b.credit_card_payment(5827, 6000.0), {'default':4491.68})
