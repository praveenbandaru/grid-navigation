# grid-navigation
2D Grid Navigation for Robots

### Sample 2D Grid

![A sample grid for a robot to navigate](https://github.com/praveenbandaru/grid-navigation/blob/master/images/sample-grid.png)

<pre>
Code Input:
    [[1, 1, 1, 0, 0, 0],
     [1, 1, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 0],
     [1, 1, 1, 0, 1, 1],
     [1, 1, 1, 0, 1, 1]]
 </pre>

### Shortest Path

![Shortest Path](https://github.com/praveenbandaru/grid-navigation/blob/master/images/left-only-grid.png)

<pre>
Code Output:
    [[' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' '],
     ['*', '#', '#', 'L', ' ', ' '],
     [' ', ' ', ' ', '#', ' ', ' '],
     [' ', ' ', ' ', '#', ' ', ' ']]
</pre>

### Favoring Right Turns

![Favoring Right Turns](https://github.com/praveenbandaru/grid-navigation/blob/master/images/right-only-grid.png)

<pre>
Code Output:
    [[' ', ' ', ' ', 'R', '#', 'R'],
     [' ', ' ', ' ', '#', ' ', '#'],
     ['*', '#', '#', '#', '#', 'R'],
     [' ', ' ', ' ', '#', ' ', ' '],
     [' ', ' ', ' ', '#', ' ', ' ']]
</pre>

## Usage:

<pre>
pip install grid-navigation-policy==0.1

jupyter notebook Navigation.ipynb

or

python test.py
</pre>
