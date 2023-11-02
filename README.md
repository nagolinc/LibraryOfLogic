The library of logic contains a set of example problems that can be 
used to train LLMs to think logically

Each example in the library is a simple problem/game that is
easy for a human or a computer algorithm to solve, but hard for
LLMs (currently) to solve

Some examples include, [Sudoku](https://manifold.markets/Mira/will-a-prompt-that-enables-gpt4-to)
and [tic tac toe](https://www.reddit.com/r/ChatGPT/comments/11v3rqw/gpt_is_really_good_at_tic_tac_toe/)



Each example in the library of logic contains 3 things:
1. A short description describing the format of the problem and the rules
2. A computer program that taking a input in the correct format can  
 * compute the "next step"
 * or produce an error if an invalid step has been taken
 * optionally an explanation of why that step was taken (or invalid)
3. some example problems, or a problem generation program

The goal of this library is ultimately to be able to produce a dataset of the following form:

```
User
Please solve this problem:
{ rules and format}
{example problem}
Assistant: 
Certainly, I will work step-by-step.  Here is first step:
{output of the first step of the computer program}
User:
Good, keep going
Assistant:
Here is the next step
{output of the next step of the computer program}
...
```


Here is a list of problems that hypothetically would fit well in the library of logic
- [ ] Playing Chess
- [x] Solving Sudoku
- [ ] Solving a Maze
- [ ] Planning a Multi-Stop Trip
- [x] Tower of Hanoi
- [ ] Eight Queens Puzzle
- [ ] N-Queens Problem
- [ ] Solving Crossword Puzzles
- [ ] Peg Solitaire
- [ ] Playing Checkers
- [ ] Tic-Tac-Toe
- [ ] Minesweeper
- [ ] Playing Connect-4
- [ ] Magic Square
- [ ] Knights Tour
- [ ] Rat in a Maze
- [ ] Word Search
- [ ] Coin Change Problem
- [ ] Sum of Subsets
- [ ] Playing Mastermind
- [ ] Travelling Salesman Problem
- [ ] Playing Reversi
- [ ] Sorting a Hand of Playing Cards
- [ ] Marble Solitaire
- [ ] Chinese Checkers
- [ ] Chutes and Ladders
- [ ] Balderdash
- [ ] Jigsaw Puzzle Solving
- [ ] Cryptarithmetic Puzzles
- [ ] Palindromes Detection
- [ ] Determining Leap Years
- [ ] Counting Number of Islands
- [ ] Coloring a Map
- [ ] Playing Cribbage
- [ ] Finding Prime Numbers
- [ ] Bingo Game
- [ ] Nim Game
- [ ] Playing Spades
- [ ] Hidden Picture Puzzle
- [ ] Counting Money Change
- [ ] Matching Brackets
- [ ] Solving Paint-by-Numbers
- [ ] Solving Kakuro
- [ ] Finding Waldo
- [ ] Playing Pinochle
- [ ] Finding Eulerian Path
- [ ] Playing Whist
- [ ] Playing Old Maid
- [ ] Solving Word Ladder Puzzles
- [ ] Playing Rummy
- [ ] Solving Futoshiki
- [ ] Playing Hearts
- [ ] Making a Rhyme
- [ ] Playing Bridge
- [ ] Playing Crazy Eights
- [ ] Identifying Palindrome Sentences
- [ ] Calculating Area of Irregular Shapes
- [ ] Identifying Anagrams
- [ ] Solving Nonograms
- [ ] Detecting Cycle in a Directed Graph
- [ ] Playing Uno
- [ ] Playing Snap
- [ ] Calculating Tips
- [x] 1D Cellular Automata
- [ ] Long multiplication
- [ ] Long Division
- [ ] Long Polynomial Division
- [x] parity (compute the parity of a a binary sequence of arbitrary length)
- [x] copy (copy a sequence, repeating each symbol k times)
- [ ] addition (arbitrary length)
- [x] balanced parenthesis


