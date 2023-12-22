theProblem = str(input("Enter: "))
signs = ['+', '-', '/', '*']

for sign in signs:
  if sign in theProblem:
    disect = theProblem.split(sign)
    operand1 = float(disect[0])
    operand2 = float(disect[1])
    
    
    if sign == '+':
      result = operand1+operand2
    elif sign == '-':
      result = operand1-operand2
    elif sign == '/':
      if operand2 == 0:
        print("Invalid Denominator")
        break
      else:
        result = operand1/operand2
    elif sign == '*':
      result = operand1*operand2
    print("Result: ", result)
    
    
else:
  print("No valid Operators in the Entered Problem")
