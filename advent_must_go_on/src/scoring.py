"""
Scoring and Leaderboard System
Tracks user submissions and maintains a leaderboard.
"""
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional


class ScoringSystem:
    """Manages user scores and submissions."""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        self.scores_file = self.data_dir / "scores.json"
        self.submissions_file = self.data_dir / "submissions.json"
        
        self.scores = self._load_scores()
        self.submissions = self._load_submissions()
    
    def _load_scores(self) -> Dict:
        """Load scores from JSON file."""
        if self.scores_file.exists():
            try:
                with open(self.scores_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading scores: {e}")
        return {}
    
    def _save_scores(self):
        """Save scores to JSON file."""
        try:
            with open(self.scores_file, 'w') as f:
                json.dump(self.scores, f, indent=2)
        except Exception as e:
            print(f"Error saving scores: {e}")
    
    def _load_submissions(self) -> Dict:
        """Load submission history from JSON file."""
        if self.submissions_file.exists():
            try:
                with open(self.submissions_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading submissions: {e}")
        return {}
    
    def _save_submissions(self):
        """Save submission history to JSON file."""
        try:
            with open(self.submissions_file, 'w') as f:
                json.dump(self.submissions, f, indent=2)
        except Exception as e:
            print(f"Error saving submissions: {e}")
    
    def record_submission(self, username: str, problem_id: str, results: Dict):
        """Record a user's submission for a problem."""
        if username not in self.scores:
            self.scores[username] = {}
        
        if username not in self.submissions:
            self.submissions[username] = {}
        
        if problem_id not in self.submissions[username]:
            self.submissions[username][problem_id] = []
        
        # Record submission
        submission = {
            'timestamp': datetime.now().isoformat(),
            'score': results['score'],
            'tests_passed': results['tests_passed'],
            'tests_total': results['tests_total'],
            'examples_passed': results['examples_passed'],
            'examples_total': results['examples_total']
        }
        
        self.submissions[username][problem_id].append(submission)
        
        # Update best score for this problem
        current_best = self.scores[username].get(problem_id, {}).get('score', 0)
        if results['score'] > current_best:
            self.scores[username][problem_id] = {
                'score': results['score'],
                'tests_passed': results['tests_passed'],
                'tests_total': results['tests_total'],
                'timestamp': submission['timestamp']
            }
        
        self._save_scores()
        self._save_submissions()
    
    def get_user_score(self, username: str, problem_id: str) -> Optional[Dict]:
        """Get a user's best score for a specific problem."""
        return self.scores.get(username, {}).get(problem_id)
    
    def get_user_total_score(self, username: str) -> float:
        """Calculate a user's total score across all problems."""
        if username not in self.scores:
            return 0.0
        
        total = sum(
            problem_data['score'] 
            for problem_data in self.scores[username].values()
        )
        return total
    
    def get_leaderboard(self, problem_id: Optional[str] = None) -> List[Dict]:
        """Get leaderboard for a specific problem or overall."""
        if problem_id:
            # Problem-specific leaderboard
            leaderboard = []
            for username, problems in self.scores.items():
                if problem_id in problems:
                    leaderboard.append({
                        'username': username,
                        'score': problems[problem_id]['score'],
                        'tests_passed': problems[problem_id]['tests_passed'],
                        'tests_total': problems[problem_id]['tests_total'],
                        'timestamp': problems[problem_id]['timestamp']
                    })
            
            leaderboard.sort(key=lambda x: (-x['score'], x['timestamp']))
        else:
            # Overall leaderboard
            leaderboard = []
            for username in self.scores.keys():
                total_score = self.get_user_total_score(username)
                problems_solved = len(self.scores[username])
                
                leaderboard.append({
                    'username': username,
                    'total_score': total_score,
                    'problems_solved': problems_solved
                })
            
            leaderboard.sort(key=lambda x: (-x['total_score'], -x['problems_solved']))
        
        return leaderboard
    
    def get_user_submissions(self, username: str, problem_id: str) -> List[Dict]:
        """Get all submissions for a user on a specific problem."""
        return self.submissions.get(username, {}).get(problem_id, [])
    
    def get_user_stats(self, username: str) -> Dict:
        """Get comprehensive stats for a user."""
        if username not in self.scores:
            return {
                'total_score': 0,
                'problems_attempted': 0,
                'problems_completed': 0,
                'total_submissions': 0
            }
        
        problems_completed = sum(
            1 for problem_data in self.scores[username].values()
            if problem_data['score'] == 100
        )
        
        total_submissions = sum(
            len(submissions)
            for submissions in self.submissions.get(username, {}).values()
        )
        
        return {
            'total_score': self.get_user_total_score(username),
            'problems_attempted': len(self.scores[username]),
            'problems_completed': problems_completed,
            'total_submissions': total_submissions
        }
