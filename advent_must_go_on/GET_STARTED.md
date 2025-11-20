# 🚀 GET STARTED IN 5 MINUTES

## Step 1: Install and Run (2 minutes)

### Option A: Use the Startup Script (Easiest!)

**Windows:**
```
Double-click start.bat
```

**Mac/Linux:**
```bash
chmod +x start.sh
./start.sh
```

### Option B: Manual Start

```bash
# Install Streamlit
pip install streamlit

# Run the app
streamlit run app.py
```

Your browser will automatically open to `http://localhost:8501`

---

## Step 2: Try the Examples (1 minute)

1. **Enter your name** in the sidebar
2. **Click "Sum Of Numbers"** problem
3. **Read the problem** description
4. **Try solving it!**

Example solution:
```python
def solve(input_text: str):
    lines = input_text.strip().split('\n')
    total = sum(int(line.strip()) for line in lines if line.strip())
    return str(total)
```

Copy this into the editor, click "Submit Solution", and see it work!

---

## Step 3: Create Your Own Problem (2 minutes)

### Quick Way:

```bash
python create_problem.py your_problem_name
```

This creates a complete problem folder with templates!

### Then edit these files:

1. **problem_description.md** - Write your challenge
   ```markdown
   # Your Problem
   Calculate something cool!
   ```

2. **example_1.txt** - Add example input
   ```
   5
   10
   15
   ```

3. **test_1.txt** - Add test input
   ```
   100
   200
   ```

4. **solutions/solution.py** - Write solution
   ```python
   def solve(input_text: str) -> str:
       # Your solution
       return str(result)
   ```

**Refresh the app** and your problem appears!

---

## 🎉 That's it!

You now have a working coding challenge platform!

## Next Steps

### Share with Friends
```bash
streamlit run app.py --server.address 0.0.0.0
```
Give them your IP: `http://YOUR_IP:8501`

### Add More Problems
```bash
python create_problem.py problem_2
python create_problem.py problem_3
```

### Validate Everything Works
```bash
python validate_problems.py
```

---

## Common Questions

**Q: How do I create a new problem?**
```bash
python create_problem.py my_problem
```

**Q: How do I test if my problem works?**
```bash
python validate_problems.py my_problem
```

**Q: Where are scores saved?**
→ In `data/scores.json` (auto-created)

**Q: Can friends on my network access it?**
→ Yes! Use `--server.address 0.0.0.0` when starting

**Q: How do I deploy publicly?**
→ See `DEPLOYMENT.md` for options

---

## File Structure (Quick Reference)

```
advent_must_go_on/
├── app.py                    ← Main app
├── start.bat / start.sh      ← Double-click to start!
├── create_problem.py         ← Create new problems
├── validate_problems.py      ← Test problems
│
├── problems/                 ← Add problem folders here
│   ├── sum_of_numbers/      ← Example 1
│   └── fibonacci_finder/    ← Example 2
│
├── data/                     ← Scores saved here (auto)
│
└── 📚 Documentation
    ├── README.md            ← Full guide
    ├── QUICKSTART.md        ← Quick reference
    ├── PROJECT_OVERVIEW.md  ← How it all works
    └── DEPLOYMENT.md        ← How to deploy
```

---

## Problem Folder Structure

```
problems/your_problem/
├── problem_description.md    ← The challenge
├── example_1.txt            ← Visible example
├── example_2.txt            ← Another example
├── test_1.txt               ← Hidden test
├── test_2.txt               ← Hidden test
├── test_3.txt               ← Hidden test
└── solutions/
    └── solution.py          ← Your solution
```

---

## The Solution Function

Every problem needs this in `solutions/solution.py`:

```python
def solve(input_text: str) -> str:
    """
    Your solution function.
    
    Args:
        input_text: The input as a string
        
    Returns:
        The answer as a string
    """
    # Your code here
    result = do_something(input_text)
    return str(result)  # Must return string!
```

**Important:**
- Function MUST be called `solve`
- Takes string input
- Returns string output

---

## Example: Creating "Double Numbers"

**1. Create problem:**
```bash
python create_problem.py double_numbers
```

**2. Edit problem_description.md:**
```markdown
# Double Numbers

Multiply each number by 2.

## Input
Numbers, one per line.

## Output
Each number doubled, one per line.
```

**3. Add example_1.txt:**
```
1
2
3
```

**4. Add test_1.txt:**
```
10
20
30
```

**5. Write solutions/solution.py:**
```python
def solve(input_text: str) -> str:
    lines = input_text.strip().split('\n')
    results = [str(int(line) * 2) for line in lines if line.strip()]
    return '\n'.join(results)
```

**6. Refresh app → Your problem is ready!**

---

## Tips

✅ Test your solution before sharing
✅ Add 2-3 examples (visible to users)
✅ Add 3-5 tests (hidden from users)
✅ Make descriptions clear
✅ Use `validate_problems.py` to check

---

## Getting Help

1. **README.md** - Complete documentation
2. **PROJECT_OVERVIEW.md** - How everything works
3. **PROBLEM_TEMPLATE.md** - Problem writing guide
4. **ARCHITECTURE.md** - Technical details

---

## You're Ready! 🎉

Start the app and begin creating challenges!

```bash
streamlit run app.py
```

Happy coding! 🚀
