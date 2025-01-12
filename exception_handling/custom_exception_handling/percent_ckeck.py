class PercentCheck(Exception):
    """Exception raised for percentage check errors. """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
  

# creating a function to check the percentage of a number
def check_percentage(num):
    if num < 0:
        raise PercentCheck("number entered can not be negative")
    elif num > 100:
        raise PercentCheck("number entered can not be greater than 100")
    else:
        return (num/100)*100
    
try :
    num = int(input("Enter your marks: "))
    check_percentage(num)
    print(f"Your percentage is {check_percentage(num)}%")
except PercentCheck as e:
    print(f"Error: {e}")
    
