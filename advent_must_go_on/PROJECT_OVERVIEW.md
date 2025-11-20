# Advent Must Go On - Project Overview

## 🎯 What You've Built

A complete coding challenge platform inspired by Advent of Code! You can:
- Create coding problems with examples and hidden tests
- Friends can solve problems and compete
- Automatic scoring and leaderboard
- Beautiful Streamlit web interface

## 📁 Project Structure

```
advent_must_go_on/
│
├── 📱 Core Application
│   ├── app.py                      # Main Streamlit app
│   └── src/
│       ├── __init__.py
│       ├── problem_loader.py       # Loads problems from folders
│       └── scoring.py              # Manages scores & leaderboard
│
├── 🎮 Problems (Auto-loaded)
│   └── problems/
│       ├── sum_of_numbers/
│       │   ├── problem_description.md
│       │   ├── example_1.txt       # Visible examples
│       │   ├── example_2.txt
│       │   ├── test_1.txt          # Hidden tests
│       │   ├── test_2.txt
│       │   ├── test_3.txt
│       │   └── solutions/
│       │       └── solution.py     # Official solution
│       │
│       └── fibonacci_finder/
│           └── [same structure]
│
├── 💾 Data (Auto-generated)
│   └── data/
│       ├── scores.json             # User best scores
│       └── submissions.json        # Full history
│
├── 🛠️ Helper Scripts
│   ├── create_problem.py           # Create new problem
│   ├── validate_problems.py        # Test problems
│   ├── start.bat                   # Windows launcher
│   └── start.sh                    # Mac/Linux launcher
│
├── 📚 Documentation
│   ├── README.md                   # Complete guide
│   ├── QUICKSTART.md              # Quick reference
│   └── DEPLOYMENT.md              # How to deploy
│
└── ⚙️ Configuration
    ├── requirements.txt           # Python dependencies
    └── .gitignore                # Git ignore rules
```

## 🚀 Quick Start (3 Easy Steps)

### 1. Install & Run
```bash
# Windows: Double-click start.bat
# Or manually:
pip install streamlit
streamlit run app.py
```

### 2. Create a Problem
```bash
python create_problem.py my_cool_problem
```

This creates:
- Problem folder with all needed files
- Templates for description, examples, tests
- Solution template

### 3. Fill in the Problem
1. Edit `problem_description.md` - Write the challenge
2. Add inputs to `example_*.txt` files
3. Add inputs to `test_*.txt` files
4. Write solution in `solutions/solution.py`

**That's it!** The app auto-loads your problem.

## 🎨 Key Features

### For Problem Creators
✅ Simple folder structure - no database setup
✅ Markdown problem descriptions
✅ Automatic test validation
✅ Your solution generates expected outputs
✅ Hidden tests keep challenge interesting

### For Problem Solvers
✅ Beautiful web interface
✅ See examples before solving
✅ Test code before submitting
✅ Instant feedback on tests
✅ Track progress and scores
✅ Compete on leaderboard

### Technical Features
✅ Auto-discovers problems from folders
✅ Validates solutions in isolated environment
✅ Persistent scoring with JSON
✅ Submission history tracking
✅ Real-time problem testing
✅ No external dependencies (except Streamlit)

## 📖 How It Works

### Problem Loading
1. App scans `problems/` directory
2. Finds all problem folders
3. Loads description, examples, tests
4. Runs official solution to get expected outputs
5. Makes available in UI

### Solving Flow
1. User selects problem
2. Reads description & studies examples
3. Writes `solve(input_text)` function
4. Tests on examples (optional)
5. Submits for full validation
6. Gets score: (passed tests / total tests) × 100

### Scoring System
- **Examples**: Visible to users, help understand problem
- **Hidden Tests**: Validate complete solution
- **Score**: Percentage of all tests passed
- **Leaderboard**: Tracks best score per problem
- **History**: All submissions saved

## 🎯 Example Problem Structure

### sum_of_numbers/

**problem_description.md:**
```markdown
# Sum of Numbers
Calculate the sum of all integers in the input.
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
    total = sum(int(line) for line in lines if line.strip())
    return str(total)
```

When user solves this:
- They see example_1.txt input and expected output (6)
- They write their solve function
- System tests on examples + hidden tests
- Score = tests passed / total tests

## 🔧 Helper Commands

```bash
# Create new problem with templates
python create_problem.py problem_name

# Validate all problems
python validate_problems.py

# Test specific problem
python validate_problems.py problem_name

# Start app (Windows)
start.bat

# Start app (Mac/Linux)
./start.sh

# Start with network access
streamlit run app.py --server.address 0.0.0.0
```

## 🌐 Deployment Options

### 1. **Local** (Easiest)
- Run on your computer
- Friends on same network can access
- `streamlit run app.py --server.address 0.0.0.0`

### 2. **Streamlit Cloud** (Free!)
- Push to GitHub
- Deploy at share.streamlit.io
- Public URL, no server needed

### 3. **Docker** (Portable)
- Create Dockerfile (see DEPLOYMENT.md)
- Deploy anywhere Docker runs

### 4. **Cloud Servers**
- Heroku, AWS, Google Cloud, Azure
- More control, custom domains

See **DEPLOYMENT.md** for detailed instructions.

## 📊 Data Storage

### JSON Files (Default)
- `data/scores.json` - Best scores per user
- `data/submissions.json` - Complete history
- Simple, no setup required
- Works for small groups (<50 users)

### Upgrade to Database (Optional)
For more users or reliability:
- SQLite: Easy, good for <100 users
- PostgreSQL: Production-ready, 100+ users
- See scoring.py for implementation hints

## 🎨 Customization Ideas

### Easy Changes
- Update emoji and styling in app.py
- Add difficulty levels to problems
- Create problem categories
- Add time limits
- Show hints after failed attempts

### Medium Changes
- Add user authentication
- Create teams/groups
- Add problem ratings
- Email notifications
- Discord integration

### Advanced Changes
- Real-time multiplayer
- Code playground/editor
- Video solution explanations
- AI hints system
- Code performance metrics

## 🐛 Troubleshooting

**Problem not showing up?**
→ Run `python validate_problems.py` to check

**Solution giving wrong answers?**
→ Test your solution manually first

**Can't access from network?**
→ Use `--server.address 0.0.0.0`
→ Check firewall settings

**Scores not saving?**
→ Check data/ folder exists
→ Verify write permissions

## 🎓 Best Practices

### Creating Problems
1. ✅ Clear, detailed descriptions
2. ✅ 2-3 examples covering edge cases
3. ✅ 3-5 hidden tests of varying difficulty
4. ✅ Test your solution thoroughly
5. ✅ Include constraints and limits

### Organizing Competition
1. 📅 Set start/end times
2. 🏆 Decide on prizes/rewards
3. 📣 Share access instructions
4. 💬 Create Discord/Slack for discussion
5. 🎉 Celebrate winners!

### Maintaining System
1. 💾 Backup data/ folder regularly
2. 📝 Keep problem solutions private
3. 🔍 Monitor for suspicious submissions
4. 📊 Review leaderboard for accuracy
5. 🐛 Test new problems before publishing

## 🔐 Security Notes

- No authentication by default (trust-based)
- Users can submit as anyone
- Consider adding login for serious competitions
- Solutions run in isolated exec() - be cautious
- Don't expose to untrusted internet without auth

## 📈 Scaling Up

**10-50 users**: Current setup works fine
**50-100 users**: Consider SQLite database
**100+ users**: PostgreSQL + proper hosting
**1000+ users**: Load balancing, caching, CDN

## 🎁 What's Included

✅ Complete working application
✅ 2 example problems (ready to solve!)
✅ Helper scripts for creating problems
✅ Validation tools
✅ Comprehensive documentation
✅ Deployment guides
✅ Startup scripts

## 🎯 Next Steps

1. **Try it out**: Run `streamlit run app.py`
2. **Solve examples**: Try the included problems
3. **Create your own**: Use `create_problem.py`
4. **Share with friends**: Deploy and invite them
5. **Customize**: Make it your own!

## 💡 Tips for Success

- Start with easy problems to build momentum
- Mix difficulty levels to keep everyone engaged
- Release problems gradually (like Advent of Code)
- Encourage discussion after solving
- Share interesting solutions
- Have fun and learn together! 🎉

## 📚 Resources

- **Streamlit Docs**: https://docs.streamlit.io
- **Python Docs**: https://docs.python.org
- **Advent of Code**: https://adventofcode.com (inspiration!)
- **LeetCode**: https://leetcode.com (more problems)

## 🤝 Contributing

This is your project! Feel free to:
- Add more features
- Create more problems
- Improve the UI
- Share with others
- Make it awesome!

---

**Built with ❤️ for coding challenges and friendly competition!**

Happy coding! 🚀
