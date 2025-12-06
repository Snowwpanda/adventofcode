#!/usr/bin/env python3
"""
Script to remove specified files from Git repository history using git-filter-repo.

This script will permanently remove all specified files from the entire Git history.
Use with caution as this rewrites Git history and cannot be easily undone.

Requirements:
- git-filter-repo must be installed (pip install git-filter-repo)
- This should be run from the repository root
- Make sure you have a backup before running this script

Usage:
    python remove_input_files.py [filename]
    python remove_input_files.py input.txt
    python remove_input_files.py test.txt
    python remove_input_files.py .env
"""

import subprocess
import sys
from pathlib import Path


def check_git_filter_repo():
    """Check if git-filter-repo is available."""
    try:
        result = subprocess.run(
            ["git", "filter-repo", "--version"],
            capture_output=True,
            text=True,
            check=False
        )
        if result.returncode != 0:
            print("git-filter-repo is not installed or not in PATH")
            print("Install it with: pip install git-filter-repo")
            return False
        return True
    except FileNotFoundError:
        print("git command not found. Make sure Git is installed and in PATH.")
        return False


def check_git_repo():
    """Check if we're in a Git repository."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--git-dir"],
            capture_output=True,
            text=True,
            check=True
        )
        return True
    except subprocess.CalledProcessError:
        print("Not in a Git repository")
        return False


def get_filter_repo_commands(filename="input.txt"):
    """Get the exact git-filter-repo commands and affected files."""
    try:
        # Get git repository root directory
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            check=True
        )
        git_root = Path(result.stdout.strip())
        
        # Get all input.txt files currently in the repository
        result = subprocess.run(
            ["git", "ls-files", f"**/{filename}", filename],
            capture_output=True,
            text=True,
            check=True
        )
        current_files = [Path(f.strip()) for f in result.stdout.splitlines() if f.strip()]
        # Transform current_files to be relative to the git root
        current_files = [p.resolve().relative_to(git_root) for p in current_files]
        
        
        # Get all input.txt files that have ever existed in history
        result = subprocess.run([
            "git", "log", "--all", "--name-only", "--pretty=format:", "--", f"**/{filename}", filename
        ], capture_output=True, text=True, check=True)
        
        historical_files = set()
        for line in result.stdout.splitlines():
            line = line.strip()
            if line and line.endswith(filename):
                historical_files.add(Path(line))
        
        # Build the exact git-filter-repo commands that will be executed
        filter_commands = [
            ["git", "filter-repo", "--path", f"**/{filename}", "--invert-paths", "--force"],
            ["git", "filter-repo", "--path", filename, "--invert-paths", "--force"]
        ]
        
        return current_files, sorted(historical_files), filter_commands
    
    except subprocess.CalledProcessError as e:
        print(f"Error finding {filename} files: {e}")
        return [], [], []


def backup_warning(filename="input.txt"):
    """Warn user about the destructive nature of this operation."""
    print("WARNING: This operation will rewrite Git history!")
    print("This cannot be easily undone. Make sure you have a backup.")
    print()
    
    # Get the exact same data that will be used for removal
    current_files, historical_files, filter_commands = get_filter_repo_commands(filename)
    
    if historical_files:
        print(f"The following {filename} files will be permanently removed from ALL Git history:")
        for file in historical_files:
            status = " (currently exists)" if file in current_files else " (deleted in history)"
            print(f"  - {file}{status}")
        for file in current_files:
            if file not in historical_files:
                print(f" Warning: - {file} currently exists but was not found in history scan!")
        print(f"\nTotal files to be removed: {len(historical_files)}")
        print(f"\nCommands that will be executed:")
        for i, cmd in enumerate(filter_commands, 1):
            print(f"  {i}. {' '.join(cmd)}")
    else:
        print(f"No {filename} files found in repository history.")
        return False, [], []
    
    print()
    response = input("Do you want to continue? (yes/no): ").lower().strip()
    return response in ['yes', 'y'], historical_files, filter_commands


def remove_input_files(historical_files, filter_commands, filename="input.txt"):
    """Remove all specified files from Git history using the exact commands from backup_warning."""
    try:
        print(f"Removing all {filename} files from Git history...")
        
        if not historical_files:
            print(f"No {filename} files found to remove.")
            return True
        
        # Execute the exact same commands that were shown in backup_warning
        for i, cmd in enumerate(filter_commands, 1):
            print(f"Executing command {i}/{len(filter_commands)}: {' '.join(cmd)}")
            try:
                result = subprocess.run(cmd, check=True, capture_output=True, text=True)
                print(f"  ✓ Command {i} completed successfully")
            except subprocess.CalledProcessError as e:
                # Some commands might fail if no files match the pattern, which is OK
                if "No commits to rewrite" in str(e.stderr) or "No files to filter" in str(e.stderr):
                    print(f"  - Command {i} found no matching files (this is normal)")
                else:
                    print(f"  ✗ Command {i} failed: {e}")
                    if e.stderr:
                        print(f"    Error details: {e.stderr}")
                    return False
        
        print(f"\n✓ Successfully removed all {filename} files from Git history!")
        print(f"Removed {len(historical_files)} {filename} files from history.")
        print("\nNote: This operation has rewritten Git history.")
        print("If you have already pushed to a remote repository, you'll need to force push:")
        print("git push --force-with-lease origin main")
        
    except Exception as e:
        print(f"Error during removal process: {e}")
        return False
    
    return True


def main():
    """Main function."""
    # Get filename from command line argument or use default
    if len(sys.argv) > 2:
        print("Usage: python remove_input_files.py [filename] (atmost one argument, default is 'input.txt')")
        sys.exit(1)
    filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    
    print(f"Git Filter-Repo: Remove {filename} files")
    print("=" * 40)
    
    # Check prerequisites
    if not check_git_repo():
        sys.exit(1)
    
    if not check_git_filter_repo():
        sys.exit(1)
    
    # Show warning and get confirmation
    should_continue, historical_files, filter_commands = backup_warning(filename)
    if not should_continue:
        print("Operation cancelled.")
        sys.exit(0)
    
    # Perform the operation using the exact same data
    if remove_input_files(historical_files, filter_commands, filename):
        print("\nOperation completed successfully!")
    else:
        print("\nOperation failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()