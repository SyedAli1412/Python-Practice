from group_by_functions import GroupBy
from enums_switch_problems import Switch
from binary_operators import BinaryOperators
from recursion import Recursion
from data.data import Data


class Main:

    def main(self):
        # Testing of Group By Functions class
        # group_by = GroupBy(records=Data.criminals_records,number_data=Data.numberData)
        # print("Result:", group_by.max_value())

        # Testing of Enums Switch Problems Class
        # switch = Switch(bootcamp_languages=Data.bootcamp_languages)
        # print('Result:', switch.lang_matcher())

        # Testing of Binary Operators Class
        # operators = BinaryOperators(number1=10, number2=12, operation='COMPLEMENT')
        # print("Result:", operators.operation_result())

        # Testing Recursion
        recursion = Recursion()
        print("Result:", recursion.binary_search(array=[1, 3, 5, 9, 2], target=9))


if __name__ == '__main__':
    main = Main()
    main.main()
