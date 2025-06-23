import sys

def main():
   a = 0
   symbols = ["+", "-", "*", "/"]
   while True:

#First number
    try:
        a = int(input("First number: "))
    except ValueError:
       print("Not an Integer")
       continue
       
#Operator
    print("""
1.Addition ---> "+"
2.Subtraction ---> "-"
3.Multiplication ---> "*"
4.Division ---> "/"
""")
    
    operator = input("Operator: ")
    if operator not in symbols:
       print("Invalid Operator")
       continue

#Second number
    try:
        b = int(input("\nSecond number: "))
    except ValueError:
       print("Not an Integer")
       continue
       
#Calulation
    if operator == "+":
       print(f"Result: {a} + {b} = {add(a, b)}")
    elif operator == "-":
       print(f"Result: {a} - {b} = {sub(a, b)}")
    elif operator == "*":
       print(f"Result: {a}*{b} = {mul(a, b)}")
    elif operator == "/":
       print(f"Result: {a}/{b} = {div(a, b)}")

    #continue calculating
    while True:
        cont = input("Do you want to continue? (y/n): ").lower()
        if cont == "n":
            sys.exit("Thank You!")
        elif cont == "y":
            break
        else:
            print("Invalid response")

#addition
def add(a, b):
   return a + b

#subtraction
def sub(a, b):
   return a - b

#multiplication
def mul(a, b):
   return a*b

#division
def div(a, b):
   if b == 0:
      return "Cannot divide by zero"
   return a/b
   
if __name__ == "__main__":
   main()