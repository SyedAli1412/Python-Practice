class Calculator:
    # Mortgage Calculation if all loan_amount, interest_rate, loan_term is provided
    # In python multiple methods with same names are not allowed even if their params are different
    # So we will use this method in order to achieve polymorphism by setting default interest_rate=0.5
    # Incase user not provides then calculation will be done by 0.5 else with users provided interest rate
    # Non-default parameter doesn't follow default parameter
    # One more note if we define the method with this same name then our code of previous method will be totally
    # overriden with new method but with different params
    def mortgage_calculation(self, loan_amount, loan_term, interest_rate=0.5):
        monthly_interest_rate = interest_rate / 100 / 12
        num_payments = loan_term * 12
        mortgage_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** num_payments) / \
                           ((1 + monthly_interest_rate) ** num_payments - 1)

        return mortgage_payment



