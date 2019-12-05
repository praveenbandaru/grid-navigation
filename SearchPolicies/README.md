
# Policies
---
## DynamicProgramming

## Class Members:

### grid: 

(2D) representing the map. 

<pre>
Ex: [[1, 1, 1, 0, 0, 0],
     [1, 1, 1, 0, 1, 0],
     [0, 0, 0, 0, 0, 0],
     [1, 1, 1, 0, 1, 1],
     [1, 1, 1, 0, 1, 1]]
												
grid format:
0 = navigable space
1 = unnavigable space 
</pre>			
### init: 
<pre>
(Point) representing the start.
Given in the form [row,col,direction]
direction = 0: up
            1: left
            2: down
            3: right

Ex: [4, 3, 0]
</pre>
### goal: 
<pre>
(Point) representing the goal.
Given in the form [row,col]

Ex: [2, 0]
</pre>
### cost: 
<pre>
(1D) representing the cost associated with moving from a cell to an adjacent one
Given in the form [right,straight,left]
cost has 3 values, corresponding to making 
a right turn, no turn, and a left turn	
Ex: [2, 1, 20]
</pre>		
### forward:
<pre>
Direction of movement
[[-1,  0], # go up
 [ 0, -1], # go left
 [ 1,  0], # go down
 [ 0,  1]] # go right
</pre>		
### forward_name:
<pre>
Direction name
['up', 'left', 'down', 'right']
</pre>
		
### action:
<pre>
Action performed by robot
action has 3 values: right turn, no turn, left turn
[-1, 0, 1]
</pre>
### action_name:
<pre>
Name of the action.
['R', '#', 'L']
</pre>
### optimum_policy2D():
<pre>
Calculates 2D policy

[[' ', ' ', ' ', 'R', '#', 'R'],
 [' ', ' ', ' ', '#', ' ', '#'],
 ['*', '#', '#', '#', '#', 'R'],
 [' ', ' ', ' ', '#', ' ', ' '],
 [' ', ' ', ' ', '#', ' ', ' ']]
</pre>
