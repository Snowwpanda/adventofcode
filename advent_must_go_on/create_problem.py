"""
Helper script to create a new problem with boilerplate files.
Usage: python create_problem.py problem_name
"""
import sys
import os
from pathlib import Path


def create_problem(problem_name: str):
    """Create a new problem folder with boilerplate files."""
    
    # Sanitize problem name
    problem_name = problem_name.lower().replace(' ', '_')
    
    # Create problem directory
    base_dir = Path(__file__).parent / "problems" / problem_name
    if base_dir.exists():
        print(f"❌ Problem '{problem_name}' already exists!")
        return
    
    base_dir.mkdir(parents=True)
    solutions_dir = base_dir / "solutions"
    solutions_dir.mkdir()
    
    print(f"✅ Created problem directory: {base_dir}")
    
    # Create problem_description.md
    description_template = f"""# {problem_name.replace('_', ' ').title()}

## Problem Description

[Describe what needs to be solved]

## Input Format

- [Describe the input format]

## Output Format

- [Describe the expected output]

## Example

**Input:**
```
[example input]
```

**Output:**
```
[example output]
```

## Explanation

[Explain the solution to the example]

## Notes

- [Any additional notes or constraints]
"""
    
    with open(base_dir / "problem_description.md", 'w') as f:
        f.write(description_template)
    print("✅ Created problem_description.md")
    
    # Create example files
    for i in range(1, 3):
        example_file = base_dir / f"example_{i}.txt"
        with open(example_file, 'w') as f:
            f.write("[Add example input here]\n")
        print(f"✅ Created example_{i}.txt")
    
    # Create test files
    for i in range(1, 4):
        test_file = base_dir / f"test_{i}.txt"
        with open(test_file, 'w') as f:
            f.write("[Add test input here]\n")
        print(f"✅ Created test_{i}.txt")
    
    # Create solution template
    solution_template = '''"""
Official solution for {problem_title}.
This solution is used to generate expected outputs for test cases.
"""

def solve(input_text: str) -> str:
    """
    Solve the problem.
    
    Args:
        input_text: The input as a string
        
    Returns:
        The solution as a string
    """
    # TODO: Implement your solution here
    
    # Example: Parse input
    lines = input_text.strip().split('\\n')
    
    # TODO: Process the input
    result = "not implemented"
    
    # Return result as string
    return str(result)
'''
    
    with open(solutions_dir / "solution.py", 'w') as f:
        f.write(solution_template.format(problem_title=problem_name.replace('_', ' ').title()))
    print("✅ Created solutions/solution.py")
    
    print(f"""
🎉 Problem '{problem_name}' created successfully!

Next steps:
1. Edit problem_description.md with your problem statement
2. Add example inputs to example_1.txt, example_2.txt
3. Add test inputs to test_1.txt, test_2.txt, test_3.txt
4. Implement your solution in solutions/solution.py
5. Run 'streamlit run app.py' to see your problem!

📁 Location: {base_dir}
""")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_problem.py <problem_name>")
        print("Example: python create_problem.py sum_of_numbers")
        sys.exit(1)
    
    problem_name = sys.argv[1]
    create_problem(problem_name)
