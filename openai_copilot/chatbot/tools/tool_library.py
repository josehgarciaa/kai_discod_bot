from Tools import function_to_schema, python_type_to_json_type 


def get_weather(
    location: str,
    *,
    units: str = "celsius"
) -> float:
    """
    Get the current temperature for a given location.

    Args:
        location (str): City and country (e.g. "Bogotá, Colombia").
        units (str, optional): Temperature scale (default "celsius").

    Returns:
        float: The current temperature in the requested units.
    """
    # ... your implementation ...
    return 21.0





# Test it:
def sum_two_numbers(number1: float, number2: float) -> float:
    """
    Sum two numbers.

    Args:
        number1 (float): The first number to sum.
        number2 (float): The second number to sum.

    Returns:
        float: The sum.
    """
    return number1 + number2

