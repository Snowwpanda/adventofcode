"""
Official solution for Sum of Numbers problem.
This solution is used to generate expected outputs for test cases.
"""

def solve(input_text: str) -> str:
    """
    Calculate the sum of all numbers in the input.
    
    Args:
        input_text: String containing numbers, one per line
        
    Returns:
        String representation of the sum
    """
    lines = input_text.strip().split('\n')
    total = 0
    
    for line in lines:
        line = line.strip()
        if line:  # Ignore empty lines
            total += int(line)
    
    return str(total)
