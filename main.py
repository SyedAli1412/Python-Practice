from PythonPractice.BinaryOperators.binary_operators import BinaryOperators
from PythonPractice.EnumsSwitchProblems.enums_switch_problems import Switch
from PythonPractice.GroupByFunctions.group_by_functions import GroupBy
from PythonPractice.Recursion.recursion import Recursion
# from PythonPractice.Polymorphism.method_overloading import Calculator
from PythonPractice.Polymorphism.method_overriding import Calculator
from PythonPractice.Polymorphism.method_overriding_inheritance import Animal, Goat
from PythonPractice.data.data import Data


class Main:

    @staticmethod
    def main():
        # Testing of Group By Functions class
        # group_by = GroupBy(records=Data.criminals_records,number_data=Data.numberData)
        # print("Result:", group_by.check_prime())

        # Testing of Enums Switch Problems Class
        # switch = Switch(bootcamp_languages=Data.bootcamp_languages)
        # print('Result:', switch.lang_matcher())

        # Testing of Binary Operators Class
        # operators = BinaryOperators(number1=10, number2=12, operation='COMPLEMENT')
        # print("Result:", operators.operation_result())

        # Testing Recursion
        recursion = Recursion()
        print("Result:", recursion.binary_search(array=[1, 3, 5, 9, 2], target=9))

        # Testing Polymorphism
        # calc = Calculator()
        # print("Result:", calc.mortgage_calculation(loan_amount=30000, loan_term=30))
        # animal = Animal()
        # goat = Goat()
        # print("Animal Sound:", animal.make_sound())
        # print("Goat Sound:", goat.make_sound())



if __name__ == '__main__':
    main = Main()
    main.main()
