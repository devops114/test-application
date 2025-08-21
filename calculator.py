def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

# Test the functions
if __name__ == "__main__":
    print("Testing calculator...")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 6 = {multiply(4, 6)}")
    
    # This will sometimes fail randomly (30% chance)
    import random
    if random.random() < 0.3:
        print("10 / 0 = ", end="")
        try:
            result = divide(10, 0)
            print(result)
        except ValueError as e:
            print(f"ERROR: {e}")
            exit(1)  # Exit with error code
    else:
        result = divide(10, 2)
        print(f"10 / 2 = {result}")
    
    print("All tests completed successfully!")
    exit(0)  # Success exit code
