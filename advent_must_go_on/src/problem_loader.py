"""
Problem Loader Module
Automatically discovers and loads problems from the problems folder structure.
"""
import os
from pathlib import Path
from typing import List, Dict, Optional
import importlib.util


class Problem:
    """Represents a coding challenge problem."""
    
    def __init__(self, problem_id: str, path: Path):
        self.problem_id = problem_id
        self.path = path
        self.title = problem_id.replace('_', ' ').title()
        
        # Load problem description
        description_path = path / "problem_description.md"
        self.description = ""
        if description_path.exists():
            with open(description_path, 'r', encoding='utf-8') as f:
                self.description = f.read()
        
        # Load examples
        self.examples = self._load_test_files("example")
        
        # Load test cases
        self.tests = self._load_test_files("test")
        
        # Load solution
        self.solution_func = self._load_solution()
        
        # Calculate expected outputs
        self.expected_outputs = self._calculate_expected_outputs()
    
    def _load_test_files(self, prefix: str) -> List[Dict[str, str]]:
        """Load all test files with the given prefix."""
        test_files = []
        
        # Find all files matching pattern (example_1.txt, example_2.txt, etc.)
        for file in sorted(self.path.glob(f"{prefix}_*.txt")):
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            test_files.append({
                'name': file.stem,
                'content': content,
                'path': str(file)
            })
        
        return test_files
    
    def _load_solution(self) -> Optional[callable]:
        """Load the solution function from solutions/solution.py."""
        solution_path = self.path / "solutions" / "solution.py"
        
        if not solution_path.exists():
            return None
        
        try:
            spec = importlib.util.spec_from_file_location("solution", solution_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            
            if hasattr(module, 'solve'):
                return module.solve
            else:
                print(f"Warning: No 'solve' function found in {solution_path}")
                return None
        except Exception as e:
            print(f"Error loading solution from {solution_path}: {e}")
            return None
    
    def _calculate_expected_outputs(self) -> Dict[str, str]:
        """Calculate expected outputs for all test cases using the solution."""
        expected = {}
        
        if self.solution_func is None:
            return expected
        
        # Calculate for examples
        for example in self.examples:
            try:
                result = self.solution_func(example['content'])
                expected[example['name']] = str(result)
            except Exception as e:
                print(f"Error calculating expected output for {example['name']}: {e}")
                expected[example['name']] = f"Error: {str(e)}"
        
        # Calculate for tests
        for test in self.tests:
            try:
                result = self.solution_func(test['content'])
                expected[test['name']] = str(result)
            except Exception as e:
                print(f"Error calculating expected output for {test['name']}: {e}")
                expected[test['name']] = f"Error: {str(e)}"
        
        return expected
    
    def validate_solution(self, user_func: callable) -> Dict[str, any]:
        """Validate a user's solution against test cases."""
        results = {
            'examples_passed': 0,
            'examples_total': len(self.examples),
            'tests_passed': 0,
            'tests_total': len(self.tests),
            'details': []
        }
        
        # Test examples
        for example in self.examples:
            try:
                user_output = str(user_func(example['content']))
                expected_output = self.expected_outputs.get(example['name'], '')
                passed = user_output == expected_output
                
                if passed:
                    results['examples_passed'] += 1
                
                results['details'].append({
                    'name': example['name'],
                    'type': 'example',
                    'passed': passed,
                    'expected': expected_output,
                    'got': user_output
                })
            except Exception as e:
                results['details'].append({
                    'name': example['name'],
                    'type': 'example',
                    'passed': False,
                    'expected': self.expected_outputs.get(example['name'], ''),
                    'got': f"Error: {str(e)}"
                })
        
        # Test cases
        for test in self.tests:
            try:
                user_output = str(user_func(test['content']))
                expected_output = self.expected_outputs.get(test['name'], '')
                passed = user_output == expected_output
                
                if passed:
                    results['tests_passed'] += 1
                
                results['details'].append({
                    'name': test['name'],
                    'type': 'test',
                    'passed': passed,
                    'expected': expected_output,
                    'got': user_output
                })
            except Exception as e:
                results['details'].append({
                    'name': test['name'],
                    'type': 'test',
                    'passed': False,
                    'expected': self.expected_outputs.get(test['name'], ''),
                    'got': f"Error: {str(e)}"
                })
        
        # Calculate score
        total_tests = results['examples_total'] + results['tests_total']
        total_passed = results['examples_passed'] + results['tests_passed']
        results['score'] = (total_passed / total_tests * 100) if total_tests > 0 else 0
        
        return results


class ProblemLoader:
    """Loads all problems from the problems directory."""
    
    def __init__(self, problems_dir: str = "problems"):
        self.problems_dir = Path(problems_dir)
        self.problems: Dict[str, Problem] = {}
        self.load_problems()
    
    def load_problems(self):
        """Discover and load all problems from the problems directory."""
        if not self.problems_dir.exists():
            print(f"Problems directory not found: {self.problems_dir}")
            return
        
        # Find all subdirectories in problems/
        for problem_dir in sorted(self.problems_dir.iterdir()):
            if problem_dir.is_dir():
                problem_id = problem_dir.name
                try:
                    problem = Problem(problem_id, problem_dir)
                    self.problems[problem_id] = problem
                    print(f"Loaded problem: {problem_id}")
                except Exception as e:
                    print(f"Error loading problem {problem_id}: {e}")
    
    def get_problem(self, problem_id: str) -> Optional[Problem]:
        """Get a specific problem by ID."""
        return self.problems.get(problem_id)
    
    def get_all_problems(self) -> List[Problem]:
        """Get all loaded problems."""
        return list(self.problems.values())
    
    def get_problem_ids(self) -> List[str]:
        """Get list of all problem IDs."""
        return sorted(self.problems.keys())
