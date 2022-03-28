class Calculator:

    def __init__(self, input1, input2):
        self.input1 = input1
        self.input2 = input2 
    
    # add
    def adder(self):
        return self.input1 + self.input2

    # subtract
    def subtractor(self):
        return self.input1 - self.input2

    # multiply
    def multiplier(self):
        return self.input1 * self.input2

    # divide
    def divider(self):
        return self.input1 / self.input2

    # clear and reset to 0
    def clear(self):
        self.input1 = 0
        self.input2 = 0

# receiving input from user
firstNum = int(input("Enter first number: "))
secondNum = int(input("Enter second number: "))

# passing the parameters into Calculator() class
calc = Calculator(firstNum, secondNum)

# print the values given in each calculation
print("Addition: ", calc.adder())
print("Subtraction: ", calc.subtractor())
print("Multiplication: ", calc.multiplier())
print("Division: ", calc.divider())
calc.clear()
print("Clear: ", calc.input1, calc.input2)