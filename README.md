# Game_Of_Life
 Different implementations of Conway's Game of Life for the HMMA238 course.

# The game

In order to compute this game, one must know the rules. Let $n$ be the number of living cells in the $8$ neighborhood of a cell.
<div class="alert alert-block alert-info">
<ol type="1">
  <li>If $n=0$ or $n=1$ and the cell is alive: it dies of isolation,</li>
  <li>if $n=2$ or $n=3$ and the cell is alive: it stays alive,</li>
  <li>if $n=3$ and the cell is dead: it's born,</li>
   <li>if $n\geq 3$ and the cell is alive: it dies.</li>
</ol>
</div>

With the code created we were able to provide an example of these rules right below.

![Visualization of the rules.](https://github.com/tanglef/Game_Of_Life/blob/master/pictures/before-after.png)


# Implementations in this project

There are many ways to compute the game of life and one motivation for these versions is the computation speed. One hypothesis made for the main part is that the border of the grid will be considered dead.

This project will tackle four ways to make the game:

* with python's lists,
* with numpy arrays to vectorize some parts of the code,
* with classes.

Because the assumption of the dead border modifies the behavior of the patterns, at the end of this project we modify some functions in order to make an infinite tore-like grid.

# Remarks

A little more efficient way to make this game that wasn't computed in this project is using convolutions with scipy `signal` commands.

