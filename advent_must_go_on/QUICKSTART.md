# Advent Must Go On - Quick Reference

## Create a New Problem (5 minutes)

1. **Create folder:**
   ```
   problems/your_problem/
   ```

2. **Add these files:**
   - `problem_description.md` - Problem statement
   - `example_1.txt` - Example input (visible)
   - `example_2.txt` - Another example
   - `test_1.txt` - Hidden test
   - `test_2.txt` - Hidden test
   - `solutions/solution.py` - Your solution

3. **Write solution:**
   ```python
   def solve(input_text: str) -> str:
       # Your code
       return str(result)
   ```

4. **Done!** Reload the app to see your problem.

## Run the App

```bash
streamlit run app.py
```

## Share with Friends

```bash
streamlit run app.py --server.address 0.0.0.0
```

They visit: `http://YOUR_IP:8501`

## File Naming

- Examples: `example_1.txt`, `example_2.txt`, ...
- Tests: `test_1.txt`, `test_2.txt`, ...
- Solution: `solutions/solution.py` (exact name!)

## Tips

✅ Test your solution before adding it
✅ Use clear, descriptive problem names
✅ Add 2-3 examples, 3-5 tests
✅ Cover edge cases in tests
✅ Make problem descriptions clear

❌ Don't change solution.py after people start solving
❌ Don't make tests too easy or too hard
❌ Don't forget to return strings from solve()
