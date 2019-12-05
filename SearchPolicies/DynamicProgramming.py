class Dynamic:
	
	def __init__(self, grid, init, goal, cost):
	
		""" Dynamic Programming to calculate optimum policy.
	
		Attributes:
			grid (2D) representing the map. Ex: [[1, 1, 1, 0, 0, 0],
												[1, 1, 1, 0, 1, 0],
												[0, 0, 0, 0, 0, 0],
												[1, 1, 1, 0, 1, 1],
												[1, 1, 1, 0, 1, 1]]
												# grid format:
												#     0 = navigable space
												#     1 = unnavigable space 
			init (Point) representing the start. # given in the form [row,col,direction]
												 # direction = 0: up
												 #             1: left
												 #             2: down
												 #             3: right
			goal (Point) representing the goal. # given in the form [row,col]
			cost (1D) representing the cost. # given in the form [right,straight,left]
											# cost has 3 values, corresponding to making 
											# a right turn, no turn, and a left turn
			"""
		
		self.grid = grid
		self.goal = goal
		
		self.init = init
		self.cost = cost # the cost associated with moving from a cell to an adjacent one

		self.forward = [[-1,  0], # go up
					   [ 0, -1], # go left
					   [ 1,  0], # go down
					   [ 0,  1]] # go right
		self.forward_name = ['up', 'left', 'down', 'right']

		# action has 3 values: right turn, no turn, left turn
		self.action = [-1, 0, 1]
		self.action_name = ['R', '#', 'L']

	def optimum_policy2D(self):
		"""Function to calculate optimum policy.
				
		Args:
			None
			
		Returns:
			Policy2D
		
		"""
		value = [[[999 for row in range(len(self.grid[0]))] for col in range(len(self.grid))],
				[[999 for row in range(len(self.grid[0]))] for col in range(len(self.grid))],
				[[999 for row in range(len(self.grid[0]))] for col in range(len(self.grid))],
				[[999 for row in range(len(self.grid[0]))] for col in range(len(self.grid))]]
			
		policy = [[[' ' for row in range(len(self.grid[0]))] for col in range(len(self.grid))],
				[[' ' for row in range(len(self.grid[0]))] for col in range(len(self.grid))],
				[[' ' for row in range(len(self.grid[0]))] for col in range(len(self.grid))],
				[[' ' for row in range(len(self.grid[0]))] for col in range(len(self.grid))]]
		
		policy2D = [[' ' for row in range(len(self.grid[0]))] for col in range(len(self.grid))]
		
		change = True

		while change:
			change = False

			for x in range(len(self.grid)):
				for y in range(len(self.grid[0])):
					for orientation in range(4):
					
						if self.goal[0] == x and self.goal[1] == y:
							if value[orientation][x][y] > 0:
								value[orientation][x][y] = 0
								policy[orientation][x][y] = '*'
								change = True

						elif self.grid[x][y] == 0:
							for i in range(3):
								o2 = (orientation + self.action[i])%4
								x2 = x + self.forward[o2][0]
								y2 = y + self.forward[o2][1]

								if x2 >= 0 and x2 < len(self.grid) and y2 >= 0 and y2 < len(self.grid[0]) and self.grid[x2][y2] == 0:
									v2 = value[o2][x2][y2] + self.cost[i]

									if v2 < value[orientation][x][y]:
										change = True
										value[orientation][x][y] = v2
										policy[orientation][x][y] = self.action_name[i]
										
		x = self.init[0]
		y = self.init[1]
		orientation = self.init[2]
		
		policy2D[x][y] = policy[orientation][x][y]
		while policy[orientation][x][y] != '*':
			if policy[orientation][x][y] == '#':
				o2 = orientation
			elif policy[orientation][x][y] == 'R':
				o2 = (orientation - 1) % 4
			elif policy[orientation][x][y] == 'L':
				o2 = (orientation + 1) % 4
			x = x + self.forward[o2][0]
			y = y + self.forward[o2][1]
			orientation = o2
			policy2D[x][y] = policy[orientation][x][y]
									
		return policy2D