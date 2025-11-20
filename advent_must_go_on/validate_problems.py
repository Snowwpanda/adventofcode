"""
Validate problems to ensure they are correctly configured.
Usage: python validate_problems.py
"""
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from problem_loader import ProblemLoader


def validate_problems():
    """Validate all problems in the problems directory."""
    
    print("🔍 Validating problems...\n")
    
    loader = ProblemLoader("problems")
    problems = loader.get_all_problems()
    
    if not problems:
        print("❌ No problems found in 'problems/' directory")
        print("   Create a problem using: python create_problem.py <problem_name>")
        return False
    
    all_valid = True
    
    for problem in problems:
        print(f"📦 Problem: {problem.problem_id}")
        print(f"   Title: {problem.title}")
        
        # Check description
        if problem.description:
            print(f"   ✅ Description: {len(problem.description)} characters")
        else:
            print(f"   ⚠️  Description: Missing or empty")
        
        # Check examples
        if problem.examples:
            print(f"   ✅ Examples: {len(problem.examples)} found")
            for example in problem.examples:
                if example['name'] in problem.expected_outputs:
                    output = problem.expected_outputs[example['name']]
                    print(f"      • {example['name']}: Expected output = '{output}'")
                else:
                    print(f"      ⚠️  {example['name']}: No expected output")
        else:
            print(f"   ⚠️  Examples: None found (add example_1.txt, example_2.txt, etc.)")
        
        # Check tests
        if problem.tests:
            print(f"   ✅ Tests: {len(problem.tests)} found")
            for test in problem.tests:
                if test['name'] in problem.expected_outputs:
                    output = problem.expected_outputs[test['name']]
                    print(f"      • {test['name']}: Expected output = '{output}'")
                else:
                    print(f"      ⚠️  {test['name']}: No expected output")
        else:
            print(f"   ⚠️  Tests: None found (add test_1.txt, test_2.txt, etc.)")
        
        # Check solution
        if problem.solution_func:
            print(f"   ✅ Solution: Found and loaded")
            
            # Test the solution on examples
            try:
                for example in problem.examples:
                    result = problem.solution_func(example['content'])
                    print(f"      • Tested on {example['name']}: Success")
            except Exception as e:
                print(f"   ❌ Solution Error: {e}")
                all_valid = False
        else:
            print(f"   ❌ Solution: Not found or invalid")
            print(f"      Add solutions/solution.py with a 'solve' function")
            all_valid = False
        
        print()
    
    print("=" * 60)
    if all_valid:
        print("✅ All problems validated successfully!")
    else:
        print("⚠️  Some problems have issues. Please fix them.")
    
    return all_valid


def test_problem(problem_id: str):
    """Test a specific problem with sample solution."""
    
    loader = ProblemLoader("problems")
    problem = loader.get_problem(problem_id)
    
    if not problem:
        print(f"❌ Problem '{problem_id}' not found")
        return
    
    print(f"🧪 Testing problem: {problem.title}\n")
    
    if not problem.solution_func:
        print("❌ No solution found to test against")
        return
    
    print("Examples:")
    for example in problem.examples:
        try:
            result = problem.solution_func(example['content'])
            expected = problem.expected_outputs.get(example['name'], 'N/A')
            match = "✅" if str(result) == str(expected) else "❌"
            print(f"  {match} {example['name']}")
            print(f"     Input: {example['content'][:50]}...")
            print(f"     Expected: {expected}")
            print(f"     Got: {result}")
        except Exception as e:
            print(f"  ❌ {example['name']}: Error - {e}")
    
    print("\nHidden Tests:")
    for test in problem.tests:
        try:
            result = problem.solution_func(test['content'])
            expected = problem.expected_outputs.get(test['name'], 'N/A')
            match = "✅" if str(result) == str(expected) else "❌"
            print(f"  {match} {test['name']}: {expected}")
        except Exception as e:
            print(f"  ❌ {test['name']}: Error - {e}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Test specific problem
        problem_id = sys.argv[1]
        test_problem(problem_id)
    else:
        # Validate all problems
        validate_problems()
