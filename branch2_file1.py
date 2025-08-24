# Branch 2 - File 1
# This file exists only in branch 2

def welcome_message():
    return "Welcome to branch 2!"

def multiply_numbers(x, y):
    return x * y

def get_user_info(user_id):
    return {
        "id": user_id,
        "branch": "branch-2",
        "status": "active"
    }

if __name__ == "__main__":
    print(welcome_message())
    print(f"Product of 4 and 7: {multiply_numbers(4, 7)}")
    print(get_user_info(123))