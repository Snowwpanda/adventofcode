# Advent Must Go On 🎄

A Streamlit-based coding challenge platform where you can create puzzles, add solutions, and share challenges with friends!

## Features

- 📝 **Problem Management**: Automatically loads problems from a simple folder structure
- 💡 **Example Cases**: Show visible examples to help users understand the problem
- 🔒 **Hidden Tests**: Secret test cases to validate complete solutions
- 🏆 **Leaderboard**: Track scores and compete with friends
- 📊 **Progress Tracking**: Monitor your submission history and improvement
- ✅ **Automatic Validation**: Solutions are automatically tested against all cases
- 🎯 **Scoring System**: Get points based on how many tests you pass

## Quick Start

### Installation

1. **Install dependencies:**
   ```bash
   pip install streamlit
   ```

2. **Run the app:**
   ```bash
   cd advent_must_go_on
   streamlit run app.py
   ```

3. **Open your browser** to the URL shown (usually http://localhost:8501)

## Creating a New Problem

### Folder Structure

Each problem should have its own folder in the `problems/` directory:

```
problems/
└── your_problem_name/
    ├── problem_description.md    # Problem statement (Markdown)
    ├── example_1.txt              # Visible example input
    ├── example_2.txt              # Another example
    ├── test_1.txt                 # Hidden test case 1
    ├── test_2.txt                 # Hidden test case 2
    ├── test_3.txt                 # Hidden test case 3
    └── solutions/
        └── solution.py            # Your official solution
```

### Step-by-Step Guide

1. **Create a problem folder:**
   ```
   problems/my_cool_problem/
   ```

2. **Write the problem description** (`problem_description.md`):
   ```markdown
   # My Cool Problem
   
   ## Description
   Explain what needs to be solved...
   
   ## Input Format
   Describe the input...
   
   ## Output Format
   Describe expected output...
   ```

3. **Add example files** (`example_1.txt`, `example_2.txt`, etc.):
   - These are **visible** to users
   - Help users understand the input format
   - Users can see the expected output

4. **Add test files** (`test_1.txt`, `test_2.txt`, etc.):
   - These are **hidden** from users
   - Used to validate the complete solution
   - Users only see how many they passed

5. **Write the official solution** (`solutions/solution.py`):
   ```python
   def solve(input_text: str) -> str:
       """
       Your solution to the problem.
       
       Args:
           input_text: The input as a string
           
       Returns:
           The answer as a string
       """
       # Your solution code here
       result = do_something(input_text)
       return str(result)
   ```

### Important Notes

- The solution **must** have a function called `solve`
- `solve` takes the input as a **string**
- `solve` must **return a string**
- The system uses your solution to generate expected outputs automatically
- Make sure your solution works correctly - it defines what's "correct"!

## Example Problem: Sum of Numbers

Here's what a complete problem looks like:

**Folder:** `problems/sum_of_numbers/`

**problem_description.md:**
```markdown
# Sum of Numbers

Calculate the sum of all numbers in the input, one per line.
```

**example_1.txt:**
```
1
2
3
```

**test_1.txt:**
```
100
200
300
```

**solutions/solution.py:**
```python
def solve(input_text: str) -> str:
    lines = input_text.strip().split('\n')
    total = sum(int(line.strip()) for line in lines if line.strip())
    return str(total)
```

## How It Works

### For Problem Creators

1. Add your problem folder with all files
2. Write your official solution in `solutions/solution.py`
3. The system automatically:
   - Loads your problem
   - Runs your solution on all examples and tests
   - Stores the expected outputs
   - Makes it available in the app

### For Problem Solvers

1. Enter your name in the sidebar
2. Select a problem
3. Read the description and study examples
4. Write your solution (must be a `solve` function)
5. Test with examples first (optional)
6. Submit for full testing
7. Get scored based on tests passed!

### Scoring

- **Example tests**: Visible inputs/outputs (help you understand)
- **Hidden tests**: Validate your complete solution
- **Score**: (Tests Passed / Total Tests) × 100
- **100% = Complete** ✅
- Best score per problem is saved

## File Structure

```
advent_must_go_on/
├── app.py                          # Main Streamlit application
├── src/
│   ├── problem_loader.py           # Loads problems from folders
│   └── scoring.py                  # Manages scores and leaderboard
├── problems/
│   ├── sum_of_numbers/             # Example problem 1
│   │   ├── problem_description.md
│   │   ├── example_1.txt
│   │   ├── example_2.txt
│   │   ├── test_1.txt
│   │   ├── test_2.txt
│   │   ├── test_3.txt
│   │   └── solutions/
│   │       └── solution.py
│   └── fibonacci_finder/           # Example problem 2
│       └── ...
├── data/
│   ├── scores.json                 # User scores (auto-generated)
│   └── submissions.json            # Submission history (auto-generated)
└── README.md                       # This file
```

## Tips for Creating Good Problems

1. **Clear Description**: Make sure the problem is well-explained
2. **Good Examples**: Provide 2-3 examples that cover different cases
3. **Edge Cases**: Include tests for edge cases (empty input, large numbers, etc.)
4. **Difficulty Range**: Mix easy and hard test cases
5. **Test Your Solution**: Make sure your official solution is correct!

## Customization

### Adding Problem Metadata

You can extend the `Problem` class in `src/problem_loader.py` to add:
- Difficulty levels
- Point values
- Time limits
- Memory limits
- Tags/categories

### Styling

Edit the Streamlit app (`app.py`) to customize:
- Colors and themes
- Page layout
- Icons and emojis
- Competition rules

### Data Storage

Currently uses JSON files in `data/`:
- `scores.json`: Best scores per user per problem
- `submissions.json`: Complete submission history

You can extend this to use a database for more users.

## Deployment

### Local Network (Share with friends on same network)

```bash
streamlit run app.py --server.address 0.0.0.0
```

Friends can access at: `http://your-ip:8501`

### Streamlit Cloud (Public hosting)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy!

### Custom Server

Use Docker or any Python hosting service. The app is fully self-contained.

## Troubleshooting

**Problem not showing up?**
- Check folder is in `problems/` directory
- Ensure `problem_description.md` exists
- Check console for error messages

**Solution not working?**
- Make sure function is named `solve`
- Check it accepts string input
- Check it returns string output
- Test locally in Python first

**Scores not saving?**
- Check `data/` folder exists
- Ensure write permissions
- Look for errors in console

## Advanced Features

### Multiple Solutions

You can add alternative solutions for testing:
```
solutions/
├── solution.py          # Official solution
├── solution_fast.py     # Optimized version
└── solution_simple.py   # Readable version
```

Only `solution.py` is used by the system.

### Problem Templates

Create a `_template/` folder with boilerplate files for quick problem creation.

### Batch Testing

You can test all problems at once:
```python
from src.problem_loader import ProblemLoader

loader = ProblemLoader()
for problem in loader.get_all_problems():
    print(f"Testing {problem.problem_id}...")
    # Your test code here
```

## Contributing

Feel free to:
- Add new problems
- Improve the UI
- Add new features
- Fix bugs

## License

This project is open source and available for personal and educational use.

## Credits

Inspired by [Advent of Code](https://adventofcode.com/) - an awesome annual coding challenge!

---

**Happy Coding! 🚀**
