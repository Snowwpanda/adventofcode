# System Architecture

## Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         ADVENT MUST GO ON                        │
│                    Coding Challenge Platform                     │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                            │
│                      (Streamlit App)                             │
│                                                                   │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────────┐         │
│  │  Problem    │  │   Solution   │  │  Leaderboard  │         │
│  │  Browser    │  │   Editor     │  │    View       │         │
│  └─────────────┘  └──────────────┘  └────────────────┘         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      CORE SYSTEM (app.py)                        │
│                                                                   │
│  ┌──────────────────────┐         ┌──────────────────────┐     │
│  │  Problem Loader      │◄────────┤  Scoring System      │     │
│  │  - Load problems     │         │  - Track scores      │     │
│  │  - Validate tests    │         │  - Save submissions  │     │
│  │  - Run solutions     │         │  - Leaderboards      │     │
│  └──────────────────────┘         └──────────────────────┘     │
│            │                                 │                   │
└────────────┼─────────────────────────────────┼──────────────────┘
             │                                 │
             ▼                                 ▼
┌─────────────────────────┐      ┌──────────────────────────────┐
│   PROBLEMS FOLDER       │      │      DATA STORAGE            │
│                         │      │                              │
│   problems/             │      │   data/                      │
│   ├── problem_1/        │      │   ├── scores.json            │
│   │   ├── problem_      │      │   └── submissions.json       │
│   │   │   description.md│      │                              │
│   │   ├── example_*.txt │      │   Auto-saved on each         │
│   │   ├── test_*.txt    │      │   submission                 │
│   │   └── solutions/    │      │                              │
│   │       └── solution.py│     │                              │
│   └── problem_2/        │      │                              │
│       └── ...           │      │                              │
└─────────────────────────┘      └──────────────────────────────┘
```

## Component Interaction

```
USER ACTION                  SYSTEM RESPONSE
─────────────               ─────────────────

1. Select Problem
   │
   ├─► Load problem_description.md
   ├─► Load and display examples
   └─► Show expected outputs (from solution)

2. Write Solution
   │
   └─► Code editor with template

3. Test with Examples
   │
   ├─► Execute user code
   ├─► Run on example inputs
   ├─► Compare with expected outputs
   └─► Show results (pass/fail)

4. Submit Solution
   │
   ├─► Execute user code
   ├─► Run on ALL tests (examples + hidden)
   ├─► Calculate score
   ├─► Save to submissions.json
   ├─► Update best score in scores.json
   └─► Display detailed results

5. View Leaderboard
   │
   ├─► Read scores.json
   ├─► Calculate rankings
   └─► Display sorted list
```

## Data Flow

```
┌──────────────┐
│ Problem      │
│ Creator      │
└──────┬───────┘
       │ 1. Create problem folder
       │ 2. Write description
       │ 3. Add test files
       │ 4. Write solution
       ▼
┌──────────────────────┐
│ problems/my_problem/ │
│ ├── problem_desc.md  │
│ ├── example_1.txt    │
│ ├── test_1.txt       │
│ └── solutions/       │
│     └── solution.py  │
└──────┬───────────────┘
       │
       │ App starts
       ▼
┌────────────────┐
│ ProblemLoader  │
│ - Scans folder │
│ - Loads files  │
│ - Runs solution├──► Generates expected outputs
│ - Caches data  │
└────────┬───────┘
         │
         │ Problem ready
         ▼
┌──────────────────┐
│ Streamlit UI     │
│ Shows problem    │
└────────┬─────────┘
         │
         │ User submits
         ▼
┌──────────────────┐
│ Validate         │
│ - Run user code  │
│ - Check outputs  │
│ - Calculate score│
└────────┬─────────┘
         │
         │ Save results
         ▼
┌──────────────────┐
│ Scoring System   │
│ - Update scores  │
│ - Save submission│
│ - Update rankings│
└────────┬─────────┘
         │
         │ Display
         ▼
┌──────────────────┐
│ Results &        │
│ Leaderboard      │
└──────────────────┘
```

## Problem Structure

```
problem_folder/
│
├── 📝 problem_description.md
│   └─► Displayed in "Problem" tab
│
├── 💡 example_1.txt, example_2.txt, ...
│   ├─► Input shown to user
│   ├─► Output calculated from solution
│   └─► Displayed in "Examples" tab
│
├── 🔒 test_1.txt, test_2.txt, ...
│   ├─► Input hidden from user
│   ├─► Output calculated from solution
│   └─► Only show pass/fail status
│
└── 🎯 solutions/solution.py
    ├─► Contains solve(input_text) function
    ├─► Runs at startup to generate expected outputs
    └─► Used as ground truth
```

## Scoring Algorithm

```python
for each test_case in (examples + hidden_tests):
    user_output = user_solve(test_input)
    expected_output = official_solve(test_input)
    
    if user_output == expected_output:
        passed += 1
    
score = (passed / total) * 100

if score > user_best_score:
    update_best_score(user, problem, score)

save_submission(user, problem, score, details)
```

## File Loading Order

```
1. App Startup
   └─► Load ProblemLoader
       └─► Scan problems/ directory
           └─► For each problem folder:
               ├─► Load problem_description.md
               ├─► Load example_*.txt files
               ├─► Load test_*.txt files
               ├─► Import solutions/solution.py
               └─► Run solution on all tests
                   └─► Store expected outputs

2. User Interaction
   └─► Problem selected
       └─► Display from cached data (instant)

3. User Submission
   └─► Execute user code
       └─► Compare with cached expected outputs
           └─► Save results
```

## State Management

```
Session State (per user browser):
├── username
├── selected_problem
└── code_input

Cached Resources (shared across users):
├── ProblemLoader (problems data)
└── ScoringSystem (scores/submissions)

Persistent Storage:
├── data/scores.json
└── data/submissions.json
```

## Security Boundaries

```
┌────────────────────────────────┐
│ Trusted Zone                   │
│ ┌────────────────────────────┐ │
│ │ Official Solutions         │ │
│ │ - Run at startup           │ │
│ │ - Generate test outputs    │ │
│ └────────────────────────────┘ │
└────────────────────────────────┘

┌────────────────────────────────┐
│ Untrusted Zone                 │
│ ┌────────────────────────────┐ │
│ │ User Submissions           │ │
│ │ - Run in exec()            │ │
│ │ - Limited scope            │ │
│ │ - No file system access    │ │
│ └────────────────────────────┘ │
└────────────────────────────────┘
```

## Extension Points

```
Current Architecture
        │
        ├─► Add Authentication
        │   └─► Wrap app with login
        │
        ├─► Add Database
        │   └─► Replace JSON with SQLite/PostgreSQL
        │
        ├─► Add Teams
        │   └─► Extend scoring system
        │
        ├─► Add Time Limits
        │   └─► Add timeout to validation
        │
        └─► Add Code Editor
            └─► Replace textarea with Monaco/CodeMirror
```

## Performance Considerations

```
Bottlenecks:
1. Problem loading (startup)
   └─► Solution: Cache with @st.cache_resource ✓

2. User code execution (per submission)
   └─► Solution: Could add timeout
   
3. File I/O (scores/submissions)
   └─► Solution: Use database for scale

4. Multiple users
   └─► Solution: Streamlit handles this well
```

## Deployment Variants

```
Development:
streamlit run app.py
├─► localhost:8501
└─► Fast reload

Local Network:
streamlit run app.py --server.address 0.0.0.0
├─► 192.168.x.x:8501
└─► Friends on same network

Cloud:
Streamlit Cloud / Heroku / Docker
├─► https://your-app.com
└─► Public internet
```
