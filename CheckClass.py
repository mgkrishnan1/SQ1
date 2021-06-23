class CheckClass:
    @staticmethod
    def checkValue(value):
        if type(value) not in [int, float]:
            raise TypeError("Not a valid value type.")
        if value > 0:
            return 1
        elif value == 0:
            return 0
        else:
            return -1
