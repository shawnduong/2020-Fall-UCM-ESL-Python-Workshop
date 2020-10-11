# 2020 Python Programming Workshops

This repository contains all of the materials needed for the 2020 Python Programming Workshops at the University of California, Merced, made possible through a partnership between Engineering Service Learning and the Solar Energy Association at UC Merced.

These workshops aim to teach the fundamentals of computer programming to beginners through a series of hands-on projects. Attendees are encouraged to focus on the **logic** behind these projects as opposed to being focused solely on the programming language itself.

## Workshop Schedule

All times are in Pacific Time.

**October 15, 2020 @ 7:30 p.m. -> 8:30 p.m.**

Topics:
- Input/Output
- Data Types and Variables
- Conditionals

Project: Rock, Paper, Scissors!

**October 22, 2020 @ 7:30 p.m. -> 8:30 p.m.**

Topics:
- Loops
- Data Types (continued)
- Functions

Project: Snake Game

**October 29, 2020 @ 7:30 p.m. -> 8:30 p.m.**

Topics:
- Object-Oriented Programming
- Libraries
- Project Structure

Project: Checkers

## Workshop 1 Reference Guide

Workshop 1 contains some functionality made specifically for the workshop that can help you make your program. Please note that these are *not* built into the actual base Python programming language. These are things that I've made specifically for this workshop for you to use so that you can focus on developing logic instead of memorizing language.

`computer_choice()` will make a random choice for the computer. It will return either `"rock"`, `"paper"`, or `"scissors"`.

```python
computerChoice = computer_choice()
print("The computer choice is", computerChoice)
```

## Workshop 2 Reference Guide

Workshop 2 contains some functionality made specifically for the workshop that can help you make your program. Please note that these are *not* built into the actual base Python programming language. These are things that I've made specifically for this workshop for you to use so that you can focus on developing logic instead of memorizing language.

Like in real-life programming, you have tools in a toolbox. You don't need to use all of the tools in your toolbox. Sometimes, you might need to make your own tools.

`UP`, `DOWN`, `LEFT`, `RIGHT`, and `ESCAPE` are all arrow keys.

`NORTH`, `EAST`, `SOUTH`, and `WEST` are all headings that are (x, y) tuples.

`cells` is a list of ordered pair tuples denoting all the coordinates that the snake resides on.

`foods` is a list of ordered pair tuples denoting all the coordinates that the foods reside on.

`add_snake_cell(x, y)` adds a cell to `cells` at the coordinate (x, y).

`remove_snake_cell(x, y)` removes a cell from `cells` at the coordinate (x, y).

`remove_all_snake_cells()` removes all cells from `cells`.

`add_food_cell(x, y)` adds a cell to `foods` at the coordinate (x, y).

`remove_food_cell(x, y)` removes a cell from `foods` at the coordinate (x, y).

`remove_all_food_cells()` removes all cells from `foods`.

`wait(n)` pauses the program for `n` seconds, which can be a float or integer.

`show_display()` shows the display to the player. This display is the window in which the game resides.

`get_keystroke()` gets the player's keystroke. It can return `UP`, `DOWN`, `LEFT`, `RIGHT`, or `ESCAPE`.

`lose_game()` loses the game.

`quit_game()` quits the game immediately.

`random_number(minimum, maximum)` generates a random integer from the minimum (inclusive) to the maximum (inclusive).
