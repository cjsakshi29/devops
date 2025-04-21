"""
Simple Calculator: Performs basic arithmetic operations
including addition, subtraction, multiplication, and division.
"""
def add(a, b):
    """Returns the sum of a and b."""
    return a + b

def subtract(a, b):
    """Returns the result of a - b."""
    return a - b

def multiply(a, b):
    """Returns the product of a and b."""
    return a * b

def divide(a, b):
    """Returns the result of a / b, or an error if dividing by zero."""
    if b == 0:
        return "Error! Division by zero."
    return a / b

def main():
    """Main function to execute the calculator operations."""
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Addition: {add(a, b)}")
    print(f"Subtraction: {subtract(a, b)}")
    print(f"Multiplication: {multiply(a, b)}")
    print(f"Division: {divide(a, b)}")

if __name__ == "__main__":
    main()
