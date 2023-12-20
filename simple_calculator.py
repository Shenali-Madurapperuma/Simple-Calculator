# Declare a list to store the previous operations

calculation_history = []

# Define the Arithmetic Operation

def add(num1, num2):
  return num1 + num2

def subtract (num1, num2):
  return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        print("float division by zero")
        return None
    return num1 / num2

def power(num1, num2):
    return num1 ** num2

def remainder(num1, num2):
    if num2 == 0:
        print("Float Modulo by zero")
        return None
    return num1 % num2


# Assign Arithmetic Operations

def select_op(choice):

  if choice == '#':
    return -1

  elif choice == '$':
    return 0

  elif choice == '?':
    history()

  elif choice == '+':
    return add

  elif choice == '-':
    return subtract

  elif choice == '*':
    return multiply

  elif choice == '/':
    return divide

  elif choice == '^':
    return power

  elif choice == '%':
    return remainder

  else:
    print("Unrecognized operation")

def history():
  if not calculation_history:
    print("No past calculations to show")
  else:
    for operation in calculation_history:
      print(operation)


# Main Loop

while True:
  print("\n\n***********************")
  print("*  SIMPLE CALCULATOR  *")
  print("***********************\n\n")
  print(" Select operation.")
  print("--------------------\n")
  print("1. Add      : + ")
  print("2. Subtract : - ")
  print("3. Multiply : * ")
  print("4. Divide   : / ")
  print("5. Power    : ^ ")
  print("6. Remainder: % ")
  print("7. Terminate: # ")
  print("8. Reset    : $ ")
  print("9. History  : ? \n")
  
  # take input from the user

  choice = input("Enter choice (+ , - , * , / , ^ , % , # , $ , ?): ")
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()

  if (choice in ('+','-','*','/','^','%')):

    try:
      num1s = input("Enter first number: ")
      if num1s.endswith('$'):
        continue
      if num1s.endswith('#'):
        print("Done. Terminating")
        exit()
      num1 = float(num1s)
    except ValueError:
      print("Not a valid number,please enter again")
      continue
    
    try:
      num2s = input("Enter second number: ")
      if num2s.endswith('$'):
        continue
      if num2s.endswith('#'):
        print("Done. Terminating")
        exit() 
      num2 = float(num2s)
    except ValueError:
      print("Not a valid number,please enter again")
      continue

    result = 0.0
    last_calculation = ""
    op_function = select_op(choice)
    result = op_function(num1, num2)

    if result is not None:
      print(f"{num1} {choice} {num2} = {result}")
    else:
      print(f"{num1} {choice} {num2} = None")

    last_calculation =  "{0} {1} {2} = {3}".format(num1, choice, num2, result) 
    
    # Save the calculation history
    calculation_history.append(last_calculation)
    


  

