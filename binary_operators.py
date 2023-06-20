from enums.enums import OperationsEnum


class BinaryOperators:
    def __init__(self, number1, number2, operation):
        self.number1 = number1
        self.number2 = number2
        self.operation = operation

    def __type_checker(self):
        if type(self.number1) and type(self.number2) is not int:
            raise ValueError('Type of numbers should be integer')
        return self.number1, self.number2

    def operation_result(self):
        numbers = self.__type_checker()
        if numbers:
            if self.operation == OperationsEnum.AND.value:
                return numbers[0] & numbers[1]
            elif self.operation == OperationsEnum.OR.value:
                return numbers[0] | numbers[1]
            elif self.operation == OperationsEnum.XOR.value:
                return numbers[0] ^ numbers[1]
            elif self.operation == OperationsEnum.COMPLEMENT.value:
                return ~numbers[0]
            elif self.operation == OperationsEnum.LEFTSHIFT.value:
                return numbers[0] << 2
            elif self.operation == OperationsEnum.RIGHTSHIFT.value:
                return numbers[0] >> 2
