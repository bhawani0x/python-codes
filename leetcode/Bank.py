class Bank:
    def __init__(self):
        self.accounts = {}
        self.loans = {"Personal Loan": 9.0, "Home Loan": 8.25, "Student Loan": 12.20, "Gold Loan": 9.75}
        self.min_balance = {'saving': 10000.0, 'checking': 7000.0, 'current': 5500.0}
        self.fine = {'saving': 4000.0, 'checking': 2500.0, 'current': 1000.0}
        self.credit_card = {'Bronze': 10.12, 'Silver': 11.35, 'Gold': 18.39, 'Platinum': 24.48}

    def create_account(self, account_number, account_holder_name, account_type, initial_balance, credit_card_type):
        """
        Return account log details of customer
        Format: {account_number: {Name: account_holder_name, account:account_type, balance: initial_balance, credit_card: credit_card_type}}
        """
        account_details = {
            "Name": account_holder_name,
            "account": account_type,
            "balance": initial_balance,
            "credit_card": credit_card_type
        }
        self.accounts[account_number] = account_details
        print (self.accounts[account_number])
        return self.accounts

    def display_account_balance(self, account_number):
        """
        Return the available balance of the account
        """
        return self.accounts.get(account_number, {}).get('balance', None)

    def check_minimal_balance(self, account_number):
        """
        Check if the account has minimum balance or not, if not then fine should be returned in the
        format->  fine: amount
        """
        account_details = self.accounts.get(account_number, {})
        account_type = account_details.get('account', '')
        current_balance = account_details.get('balance', 0.0)

        if current_balance < self.min_balance.get(account_type, 0.0):
            return 'Yes'
        else:
            return 'No'

    def request_loan(self, account_number, loan_amount, loan_type):
        """
        Return the status of the loan request which means to check if loan amount can be approved or not.
        Removing the loan amount from your balance amount should not leave your account with 0 balance
        """
        account_details = self.accounts.get(account_number, {})
        current_balance = account_details.get('balance', 0.0)

        if current_balance - loan_amount >= 0:
            # Approve loan
            self.accounts[account_number]['balance'] -= loan_amount
            return 'Approved'
        else:
            return 'Not Approved'

    def calculate_emi(self, loan_amount, loan_type, duration):
        """
        Return EMI based on loan. if EMI amount is removed from the balance, your account should not have 0 balance.
        """
        interest_rate = self.loans.get(loan_type, 0.0)
        emi_amount = (loan_amount + (loan_amount * interest_rate / 100)) / duration
        return emi_amount

    def transfer_money(self, sender_account, receiver_account, amount):
        """
        Return account balance of both accounts after money transfer and check for minimum balance in account
        """
        sender_balance = self.accounts.get(sender_account, {}).get('balance', 0.0)
        receiver_balance = self.accounts.get(receiver_account, {}).get('balance', 0.0)

        if sender_balance >= amount:
            sender_balance -= amount
            receiver_balance += amount
            self.accounts[sender_account]['balance'] = sender_balance
            self.accounts[receiver_account]['balance'] = receiver_balance

            sender_fine = self.check_minimal_balance(sender_account)
            receiver_fine = self.check_minimal_balance(receiver_account)

            return {'sender_balance': sender_balance, 'receiver_balance': receiver_balance,
                    'sender_fine': sender_fine, 'receiver_fine': receiver_fine}
        else:
            return {'status': 'Insufficient Balance'}

    def credit_card_payment(self, account_number, amount):
        """
        Return the remaining balance after making the credit card bill payment.
        If the credit card bill is greater than the account balance, return the total amount to be paid,
        including the remaining credit card bill amount with interest and
        the fine if the amount is less than the pre-defined minimum balance.
        """
        account_details = self.accounts.get(account_number, {})
        current_balance = account_details.get('balance', 0.0)
        credit_card_type = account_details.get('credit_card', '')
        interest_rate = self.credit_card.get(credit_card_type, 0.0)

        if current_balance >= amount:
            current_balance -= amount
            self.accounts[account_number]['balance'] = current_balance

            if current_balance < self.min_balance.get(credit_card_type, 0.0):
                fine = self.fine.get(credit_card_type, 0.0)
                return {'remaining_balance': current_balance, 'fine': fine}
            else:
                return {'remaining_balance': current_balance}
        else:
            extra = amount - current_balance
            interest_imposed = (extra * interest_rate) / 100
            total_amount_to_pay = amount + interest_imposed

            return {'total_amount_to_pay': total_amount_to_pay}

    def debit_card_payment(self, account_number, amount):
        """
        Return balance after debit card payment and check for minimum balance in account 
        """
        account_details = self.accounts.get(account_number, {})
        current_balance = account_details.get('balance', 0.0)

        if current_balance >= amount:
            current_balance -= amount
            self.accounts[account_number]['balance'] = current_balance

            account_fine = self.check_minimal_balance(account_number)

            return {'remaining_balance': current_balance, 'account_fine': account_fine}
        else:
            return {'status': 'Insufficient Balance'}

    def monthly_investment(self, account_number, investment_amount):
        """
        Return balance after paying all monthly investments and check for minimum balance in account
        """
        account_details = self.accounts.get(account_number, {})
        current_balance = account_details.get('balance', 0.0)

        if current_balance >= investment_amount:
            current_balance -= investment_amount
            self.accounts[account_number]['balance'] = current_balance

            account_fine = self.check_minimal_balance(account_number)

            return {'remaining_balance': current_balance, 'account_fine': account_fine}
        else:
            return {'status': 'Insufficient Balance'}


b = Bank()
b.create_account(6721, "Jane Smith",'saving', 50000.0, 'Bronze'),{6721:{"Name":"Jane Smith","account":"saving","balance":50000.0,"credit_card":"Bronze"}}
b.check_minimal_balance(6721)