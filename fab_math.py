"TDD function"
import math

def my_fabs(number):
    """
    
    """
    if not number:
        raise TypeError("Invalid input")
    if not isinstance(number, int):
        raise TypeError("Input should be int")
    return math.fabs(number)