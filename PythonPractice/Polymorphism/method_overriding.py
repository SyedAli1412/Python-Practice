class Calculator:

    # Our code of previous method will be totally
    # overriden with new method but with different params
    def mortgage_calculation(self, loan_amount, loan_term, interest_rate):
        monthly_interest_rate = interest_rate / 100 / 12
        num_payments = loan_term * 12
        mortgage_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments) / \
                           ((1 + monthly_interest_rate) ** num_payments - 1)

        return mortgage_payment

    # This method has overriden previous one and now previous one will not be accessible on making instance
    def mortgage_calculation(self, loan_amount, loan_term):
        monthly_interest_rate = 4.0 / 100 / 12
        num_payments = loan_term * 12
        mortgage_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments) / \
                           ((1 + monthly_interest_rate) ** num_payments - 1)

        return mortgage_payment



