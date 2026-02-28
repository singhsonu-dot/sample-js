# Functions for arithmetic operations
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0: return "Error: Division by zero"
    return x / y

def calculator():
    while True: # Continuous loop until exit
        print("\n1.Add, 2.Sub, 3.Mul, 4.Div, 5.Exit")
        choice = input("Enter choice (1-5): ")
        if choice == '5': break
        
        if choice in ('1', '2', '3', '4'):
            try:
                n1 = float(input("First number: ")) # User input conversion
                n2 = float(input("Second number: "))
                ops = {'1': add(n1, n2), '2': subtract(n1, n2), 
                       '3': multiply(n1, n2), '4': divide(n1, n2)}
                print("Result:", ops[choice])
            except ValueError:
                print("Invalid input.")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    calculator()
