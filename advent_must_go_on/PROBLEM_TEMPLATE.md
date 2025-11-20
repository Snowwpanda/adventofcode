# Problem Description Template

Copy this template when creating new problems. Save as `problem_description.md` in your problem folder.

---

# [Problem Title]

## Problem Description

[Clearly explain what needs to be solved. Be specific about the goal and what the solution should accomplish.]

## Input Format

- [Describe the input format in detail]
- [Mention any constraints: number of lines, value ranges, etc.]
- [Note any special cases: empty input, multiple test cases, etc.]

## Output Format

- [Describe the expected output]
- [Specify format: single number, multiple lines, specific formatting]
- [Mention if output should have trailing newline, specific precision, etc.]

## Example 1

**Input:**
```
[example input here]
```

**Output:**
```
[expected output here]
```

**Explanation:**
[Walk through how to get from input to output]

## Example 2 (Optional)

**Input:**
```
[another example]
```

**Output:**
```
[expected output]
```

**Explanation:**
[Explain this example, especially if it shows an edge case]

## Constraints

- [List any constraints on input size, values, etc.]
- [Example: 1 ≤ N ≤ 1000]
- [Example: All numbers are integers]
- [Example: Input will always be valid]

## Notes

- [Any additional hints or clarifications]
- [Edge cases to consider]
- [Common mistakes to avoid]

---

## Template Examples

### Example 1: Simple Math Problem

# Sum of Even Numbers

## Problem Description

Given a list of integers, calculate the sum of all even numbers.

## Input Format

- Multiple lines, each containing a single integer
- Input may have empty lines (ignore them)

## Output Format

- A single integer: the sum of all even numbers

## Example

**Input:**
```
1
2
3
4
5
6
```

**Output:**
```
12
```

**Explanation:**
Even numbers are: 2, 4, 6
Sum: 2 + 4 + 6 = 12

## Constraints

- -1000 ≤ each number ≤ 1000
- 1 ≤ number of integers ≤ 100

## Notes

- If there are no even numbers, return 0
- Remember to ignore empty lines

---

### Example 2: String Problem

# Reverse Words

## Problem Description

Given a sentence, reverse the order of words while keeping each word intact.

## Input Format

- A single line containing a sentence
- Words are separated by spaces

## Output Format

- A single line with words in reversed order

## Example

**Input:**
```
Hello World Python
```

**Output:**
```
Python World Hello
```

**Explanation:**
Words: ["Hello", "World", "Python"]
Reversed: ["Python", "World", "Hello"]
Output: "Python World Hello"

## Constraints

- 1 ≤ sentence length ≤ 1000 characters
- At least one word in the input

## Notes

- Multiple consecutive spaces should be treated as single space
- No leading or trailing spaces in output

---

### Example 3: Algorithm Problem

# Find Peak Element

## Problem Description

A peak element is an element that is strictly greater than its neighbors. Find any peak element in the array.

## Input Format

- First line: integer N (size of array)
- Second line: N space-separated integers

## Output Format

- A single integer: the value of a peak element

## Example

**Input:**
```
5
1 3 20 4 1
```

**Output:**
```
20
```

**Explanation:**
20 is greater than both neighbors (3 and 4), so it's a peak.

## Constraints

- 1 ≤ N ≤ 1000
- -10^9 ≤ array elements ≤ 10^9
- Array will always have at least one peak

## Notes

- If multiple peaks exist, return any one of them
- Corner elements are considered to have one neighbor

---

## Tips for Good Problem Descriptions

### Do:
✅ Be clear and specific
✅ Provide multiple examples
✅ Show edge cases
✅ Include constraints
✅ Explain the reasoning

### Don't:
❌ Be vague or ambiguous
❌ Assume prior knowledge
❌ Skip edge cases
❌ Forget to specify output format
❌ Make it too complex

## Problem Difficulty Guidelines

### Easy (Beginner-friendly)
- Simple input/output
- Straightforward algorithm
- 2-3 examples sufficient
- Example: sum numbers, count items, simple string manipulation

### Medium (Intermediate)
- More complex logic
- May need data structures
- 3-4 examples recommended
- Example: sorting, searching, basic algorithms

### Hard (Advanced)
- Complex algorithms
- May need dynamic programming, graphs, etc.
- 4-5 examples needed
- Example: optimization problems, complex data structures

## Testing Your Problem

Before publishing, ask yourself:

1. ✅ Is the problem statement clear?
2. ✅ Do examples cover common cases?
3. ✅ Do examples cover edge cases?
4. ✅ Are constraints clearly stated?
5. ✅ Does my solution work on all test cases?
6. ✅ Is the difficulty appropriate for my audience?
7. ✅ Would I understand this if I saw it for the first time?

## Common Problem Types

### Mathematical
- Arithmetic operations
- Number properties (prime, even/odd)
- Sequences (Fibonacci, factorial)
- Geometry calculations

### String Manipulation
- Reverse, rotate
- Pattern matching
- Substring operations
- Formatting

### Arrays/Lists
- Searching, sorting
- Finding elements
- Transformations
- Statistics (max, min, average)

### Logic Puzzles
- Conditional logic
- Game simulations
- State machines
- Decision trees

### Data Structures
- Stacks, queues
- Hash maps
- Trees, graphs
- Sets

Choose the type that matches your learning goals!
