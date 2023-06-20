class Recursion:

    def pow(self, base, exp):
        if exp == 0:
            return -1
        elif exp < 0:
            return 1 / self.pow(base, -exp)
        else:
            return base * self.pow(base, exp - 1)

    def fac(self, number):
        if number == 0:
            return 1
        else:
            return number * self.fac(number-1)

    def binary_search(self, array, target):
        low = 0
        high = len(array) - 1
        return self.__binary_search_recursive(array, target, low, high)

    def __binary_search_recursive(self, array, target, low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if array[mid] == target:
            return array[mid]
        elif array[mid] < target:
            return self.__binary_search_recursive(array, target, mid + 1, high)
        else:
            return self.__binary_search_recursive(array, target, low, mid - 1)

