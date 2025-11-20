"""
Advent Must Go On - Coding Challenge Engine
A Streamlit-based platform for creating and sharing coding challenges.
"""
import streamlit as st
import sys
from pathlib import Path
import tempfile
import os

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from problem_loader import ProblemLoader
from scoring import ScoringSystem


# Page configuration
st.set_page_config(
    page_title="Advent Must Go On",
    page_icon="🎄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'selected_problem' not in st.session_state:
    st.session_state.selected_problem = None
if 'code_input' not in st.session_state:
    st.session_state.code_input = ""

# Load problems and scoring system
@st.cache_resource
def load_systems():
    """Load problem loader and scoring system."""
    base_dir = Path(__file__).parent
    loader = ProblemLoader(str(base_dir / "problems"))
    scorer = ScoringSystem(str(base_dir / "data"))
    return loader, scorer

loader, scorer = load_systems()


def main():
    """Main application logic."""
    
    # Title
    st.title("🎄 Advent Must Go On")
    st.markdown("*A coding challenge platform for friends*")
    
    # Sidebar - User login and navigation
    with st.sidebar:
        st.header("👤 User")
        username = st.text_input("Enter your name:", value=st.session_state.username)
        if username:
            st.session_state.username = username
            st.success(f"Logged in as: {username}")
            
            # User stats
            stats = scorer.get_user_stats(username)
            st.markdown("---")
            st.subheader("📊 Your Stats")
            col1, col2 = st.columns(2)
            col1.metric("Total Score", f"{stats['total_score']:.1f}")
            col2.metric("Problems Solved", f"{stats['problems_completed']}/{stats['problems_attempted']}")
        
        st.markdown("---")
        
        # Navigation
        st.header("📚 Problems")
        problems = loader.get_all_problems()
        
        if not problems:
            st.warning("No problems found. Add problems to the 'problems' folder.")
        else:
            for problem in problems:
                # Show completion status
                if username:
                    user_score = scorer.get_user_score(username, problem.problem_id)
                    if user_score and user_score['score'] == 100:
                        badge = "✅"
                    elif user_score:
                        badge = "🔶"
                    else:
                        badge = "⚪"
                else:
                    badge = "⚪"
                
                if st.button(f"{badge} {problem.title}", key=f"nav_{problem.problem_id}"):
                    st.session_state.selected_problem = problem.problem_id
                    st.rerun()
        
        st.markdown("---")
        
        # Leaderboard toggle
        if st.button("🏆 View Leaderboard"):
            st.session_state.selected_problem = "leaderboard"
            st.rerun()
    
    # Main content area
    if not st.session_state.username:
        st.info("👈 Please enter your name in the sidebar to get started!")
        show_welcome_page()
    elif st.session_state.selected_problem == "leaderboard":
        show_leaderboard_page()
    elif st.session_state.selected_problem:
        show_problem_page()
    else:
        show_welcome_page()


def show_welcome_page():
    """Display welcome page with instructions."""
    st.header("Welcome to Advent Must Go On! 🎉")
    
    st.markdown("""
    ## How it works
    
    1. **Choose a problem** from the sidebar
    2. **Read the description** and understand the requirements
    3. **Test with examples** to understand the input/output format
    4. **Write your solution** in Python
    5. **Submit** and see how many tests you pass!
    
    ## Scoring
    
    - Each problem has **example test cases** (visible) and **hidden test cases**
    - Your score is based on how many total tests you pass
    - The leaderboard tracks your best scores
    - Get 100% to fully complete a problem! ✅
    
    ## Getting Started
    
    Select a problem from the sidebar to begin your coding journey!
    """)
    
    # Show available problems
    problems = loader.get_all_problems()
    if problems:
        st.markdown("### Available Problems")
        for problem in problems:
            st.markdown(f"- **{problem.title}** ({len(problem.examples)} examples, {len(problem.tests)} tests)")


def show_problem_page():
    """Display a specific problem page."""
    problem = loader.get_problem(st.session_state.selected_problem)
    
    if not problem:
        st.error("Problem not found!")
        return
    
    # Problem header
    st.header(problem.title)
    
    # Show user's best score if available
    username = st.session_state.username
    user_score = scorer.get_user_score(username, problem.problem_id)
    
    if user_score:
        col1, col2, col3 = st.columns(3)
        col1.metric("Your Best Score", f"{user_score['score']:.1f}%")
        col2.metric("Tests Passed", f"{user_score['tests_passed']}/{user_score['tests_total']}")
        col3.metric("Status", "✅ Complete" if user_score['score'] == 100 else "🔶 In Progress")
    
    # Tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs(["📝 Problem", "💡 Examples", "🔧 Solution", "📊 Submissions"])
    
    with tab1:
        # Problem description
        if problem.description:
            st.markdown(problem.description)
        else:
            st.warning("No problem description available. Add a `problem_description.md` file.")
    
    with tab2:
        # Examples
        if problem.examples:
            for example in problem.examples:
                with st.expander(f"📋 {example['name']}", expanded=True):
                    st.markdown("**Input:**")
                    st.code(example['content'], language="text")
                    
                    if example['name'] in problem.expected_outputs:
                        st.markdown("**Expected Output:**")
                        st.code(problem.expected_outputs[example['name']], language="text")
        else:
            st.info("No examples available for this problem.")
    
    with tab3:
        # Solution submission
        st.markdown("""
        ### Write Your Solution
        
        Write a function called `solve` that takes the input as a string and returns the answer.
        
        ```python
        def solve(input_text: str) -> str:
            # Your solution here
            return result
        ```
        """)
        
        # Code editor
        default_code = '''def solve(input_text: str):
    """
    Solve the problem.
    
    Args:
        input_text: The input as a string
        
    Returns:
        The solution as a string
    """
    # Your code here
    pass
'''
        
        code = st.text_area(
            "Python Code:",
            value=default_code,
            height=400,
            key="code_editor"
        )
        
        # Submit button
        col1, col2 = st.columns([1, 4])
        with col1:
            submit_btn = st.button("🚀 Submit Solution", type="primary", use_container_width=True)
        with col2:
            test_examples_btn = st.button("🧪 Test with Examples Only", use_container_width=True)
        
        if submit_btn or test_examples_btn:
            if not code.strip():
                st.error("Please write some code first!")
            else:
                # Execute user code
                try:
                    # Create a temporary module to execute the code
                    namespace = {}
                    exec(code, namespace)
                    
                    if 'solve' not in namespace:
                        st.error("Your code must define a function called `solve`")
                    else:
                        user_func = namespace['solve']
                        
                        if test_examples_btn:
                            # Test only examples
                            st.subheader("Example Test Results")
                            all_passed = True
                            for example in problem.examples:
                                try:
                                    result = str(user_func(example['content']))
                                    expected = problem.expected_outputs.get(example['name'], '')
                                    passed = result == expected
                                    
                                    if passed:
                                        st.success(f"✅ {example['name']} - Passed")
                                    else:
                                        st.error(f"❌ {example['name']} - Failed")
                                        st.markdown(f"**Expected:** `{expected}`")
                                        st.markdown(f"**Got:** `{result}`")
                                        all_passed = False
                                except Exception as e:
                                    st.error(f"❌ {example['name']} - Error: {str(e)}")
                                    all_passed = False
                            
                            if all_passed:
                                st.success("🎉 All examples passed! Ready to submit for full testing.")
                        else:
                            # Full validation
                            with st.spinner("Running tests..."):
                                results = problem.validate_solution(user_func)
                            
                            # Record submission
                            scorer.record_submission(username, problem.problem_id, results)
                            
                            # Display results
                            st.subheader("Test Results")
                            
                            # Overall score
                            score_color = "green" if results['score'] == 100 else "orange" if results['score'] >= 50 else "red"
                            st.markdown(f"## Score: :{score_color}[{results['score']:.1f}%]")
                            
                            col1, col2 = st.columns(2)
                            col1.metric("Examples", f"{results['examples_passed']}/{results['examples_total']}")
                            col2.metric("Tests", f"{results['tests_passed']}/{results['tests_total']}")
                            
                            # Detailed results
                            st.markdown("---")
                            st.markdown("### Detailed Results")
                            
                            for detail in results['details']:
                                if detail['type'] == 'example':
                                    icon = "✅" if detail['passed'] else "❌"
                                    with st.expander(f"{icon} {detail['name']} ({'Passed' if detail['passed'] else 'Failed'})"):
                                        col1, col2 = st.columns(2)
                                        col1.markdown("**Expected:**")
                                        col1.code(detail['expected'])
                                        col2.markdown("**Your Output:**")
                                        col2.code(detail['got'])
                            
                            # Hidden test summary
                            hidden_passed = results['tests_passed']
                            hidden_total = results['tests_total']
                            st.markdown(f"**Hidden Tests:** {hidden_passed}/{hidden_total} passed 🔒")
                            
                            if results['score'] == 100:
                                st.balloons()
                                st.success("🎉 Perfect score! You've completed this problem!")
                            elif results['score'] >= 50:
                                st.info("Good progress! Keep working to pass all tests.")
                            else:
                                st.warning("Keep trying! Check the examples to understand the problem better.")
                
                except Exception as e:
                    st.error(f"Error executing your code: {str(e)}")
                    st.code(str(e))
    
    with tab4:
        # Submission history
        submissions = scorer.get_user_submissions(username, problem.problem_id)
        
        if submissions:
            st.markdown(f"### Your Submissions ({len(submissions)} total)")
            
            for i, sub in enumerate(reversed(submissions), 1):
                with st.expander(f"Submission #{len(submissions) - i + 1} - Score: {sub['score']:.1f}%"):
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Score", f"{sub['score']:.1f}%")
                    col2.metric("Tests Passed", f"{sub['tests_passed']}/{sub['tests_total']}")
                    col3.metric("Examples Passed", f"{sub['examples_passed']}/{sub['examples_total']}")
                    st.caption(f"Submitted: {sub['timestamp']}")
        else:
            st.info("No submissions yet. Submit your solution to see your history!")


def show_leaderboard_page():
    """Display the leaderboard."""
    st.header("🏆 Leaderboard")
    
    # Tabs for overall and per-problem leaderboards
    tabs = ["Overall"] + [p.title for p in loader.get_all_problems()]
    selected_tabs = st.tabs(tabs)
    
    with selected_tabs[0]:
        # Overall leaderboard
        st.subheader("Overall Rankings")
        leaderboard = scorer.get_leaderboard()
        
        if leaderboard:
            for i, entry in enumerate(leaderboard, 1):
                medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
                
                col1, col2, col3 = st.columns([1, 3, 2])
                col1.markdown(f"### {medal}")
                col2.markdown(f"**{entry['username']}**")
                col3.markdown(f"Score: **{entry['total_score']:.1f}** | Problems: **{entry['problems_solved']}**")
        else:
            st.info("No submissions yet. Be the first to solve a problem!")
    
    # Per-problem leaderboards
    for i, problem in enumerate(loader.get_all_problems(), 1):
        with selected_tabs[i]:
            st.subheader(f"{problem.title}")
            leaderboard = scorer.get_leaderboard(problem.problem_id)
            
            if leaderboard:
                for j, entry in enumerate(leaderboard, 1):
                    medal = "🥇" if j == 1 else "🥈" if j == 2 else "🥉" if j == 3 else f"{j}."
                    
                    col1, col2, col3 = st.columns([1, 3, 2])
                    col1.markdown(f"### {medal}")
                    col2.markdown(f"**{entry['username']}**")
                    col3.markdown(f"Score: **{entry['score']:.1f}%** | Tests: **{entry['tests_passed']}/{entry['tests_total']}**")
            else:
                st.info("No submissions for this problem yet.")


if __name__ == "__main__":
    main()
