"""
Official solution for Fibonacci Finder problem.
"""

def solve(input_text: str) -> str:
    """
    Find the Nth Fibonacci number.
    
    Args:
        input_text: String containing a single integer N
        
    Returns:
        String representation of F(N)
    """
    n = int(input_text.strip())
    
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    
    # Calculate iteratively
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    
    return str(curr)
