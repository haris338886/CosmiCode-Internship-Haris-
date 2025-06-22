def add(x, y):
    """Addition function"""
    return x + y

def subtract(x, y):
    """Subtraction function"""
    return x - y

def multiply(x, y):
    """Multiplication function"""
    return x * y

def divide(x, y):
    """Division function"""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    """Exponentiation function"""
    return x ** y

def modulus(x, y):
    """Modulus/remainder function"""
    if y == 0:
        return "Error! Division by zero."
    return x % y

def calculator():
    """Main calculator function"""
    print("\nBasic Math Operations Calculator")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exponentiation (^)")
    print("6. Modulus (%)\n")
    
    while True:
        try:
            choice = input("Enter operation number (1-6) or 'q' to quit: ")
            
            if choice.lower() == 'q':
                print("Exiting calculator...")
                break
                
            if choice not in ['1', '2', '3', '4', '5', '6']:
                print("Invalid input! Please enter a number between 1-6.")
                continue
                
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"Result: {num1} ^ {num2} = {power(num1, num2)}")
            elif choice == '6':
                print(f"Result: {num1} % {num2} = {modulus(num1, num2)}")
                
        except ValueError:
            print("Invalid input! Please enter numeric values.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    calculator()