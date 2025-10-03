def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform a basic arithmetic operation on two numbers.

    Args:
        num1 (float): First number.
        num2 (float): Second number.
        operation (str): One of 'add', 'subtract', 'multiply', 'divide'.

    Returns:
        float or str: Result of the operation, or an error message string
                      for division by zero or invalid operation.
    """
    op = (operation or "").strip().lower()

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
