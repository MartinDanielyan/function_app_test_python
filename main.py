"""
This is a simple Python function app.
It contains a single function to be tested.
"""

def add_numbers(a, b):
    """
    Returns the sum of two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b

# This is a basic example. In a real function app, this might be triggered
# by an HTTP request, a message queue, or a scheduled event.
if __name__ == "__main__":
    result = add_numbers(5, 3)
    print(f"The result of adding 5 and 3 is: {result}")
