import math

def sin_deg(x):
    """
    Calculate sin(x) where x is in degree.
    """
    radians = math.radians(x)
    return math.sin(radians)

# Example usage
x = 45
result = sin_deg(x)
print(f"sin({x}) = {result}")\
