# Branch 1 - File 1
# This file exists only in branch 1

def greeting():
    return "Hello from branch 1!"

def calculate_sum(a, b):
    return a + b

if __name__ == "__main__":
    print(greeting())
    print(f"Sum of 5 and 3: {calculate_sum(5, 3)}")