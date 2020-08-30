from collections import deque
import heapq
class Puzzle:
  	previous = None
    state = None
    operation = None
    zero = None
    depth = 0
    cost = 0
    cost_reverse = False

    def __init__(self, state, previous = None, operation = None, depth = 0, cost_reverse = False):
        self.previous = previous
        self.state = state
        self.operation = operation
        self.zero = self.check_blank_tile()
        self.depth = depth
        self.cost_reverse = cost_reverse

        if cost_reverse == True:       
            self.cost = self.depth + self.manhattan_distance()
        else:                           
            self.cost = self.manhattan_distance()


    def __str__(self):

        return  str(self.state[:3]) + "\n" \
            +   str(self.state[3:6]) + "\n" \
            +   str(self.state[6:]) + "\n"

	def lessthan(self, another_board):
        return self.cost < another_board.cost

    def check_final_state(self):
        
        for i in range(0, len(self.state)):
            if i == self.state[i]:
                continue
            else:
                return False
        return True

    def check_blank_tile(self):
        for i in range(9):
            if self.state[i] == 0:
                return i
    
    def helper_swap(self, i, j):
        
        new_state = list(self.state)
        new_state[i], new_state[j] = new_state[j], new_state[i]
        return new_state

    def move_up(self):
        
        if self.zero > 2:
            return Puzzle(self.helper_swap(self.zero, self.zero-3), self, 'Up', self.depth+1, self.cost_reverse)
        else:
            return None
    def move_down(self):
        
        if self.zero < 6:
            return Puzzle(self.helper_swap(self.zero, self.zero+3), self, 'Down', self.depth+1, self.cost_reverse)
        else:
            return None
    
    def move_left(self):
        
        if self.zero % 3 != 0:
            return Puzzle(self.helper_swap(self.zero, self.zero-1), self, 'Left', self.depth+1, self.cost_reverse)
        else:
            return None
    
    def move_right(self):
        
        if (self.zero + 1) % 3 != 0:
            return Puzzle(self.helper_swap(self.zero, self.zero+1), self, 'Right', self.depth+1, self.cost_reverse)
        else:
            return None

    def find_next_states(self):
        next_states = []
        next_states.append(self.move_up())
        next_states.append(self.move_down())
        next_states.append(self.move_left())
        next_states.append(self.move_right())

        next_states = list(filter(None, next_states))

        return next_states

    def manhattan_distance(self):
       
	    heuristic = 0
        for i in range(len(self.state)):
            if self.state[i] == 0:      
                continue            
            heuristic += abs(self.state[i] // 3 - i // 3) + abs(self.state[i] % 3 - i % 3)

        return heuristic
    
    answer = None
    nodes_found = 0
    current_depth = 0


    def BFS(self, init_state):
        
        frontier = deque()
        explored = set()

        frontier.append(init_state)
        explored.add(tuple(init_state.state))

        while frontier:
            board = frontier.popleft()
           
            if board.checcheck_final_state():
                self.answer = board
                self.nodes_found = len(explored) - len(frontier) - 1
                return self.answer
            
            for next_state in board.find_next_states():
                if tuple(next_state.state) not in explored:
                    frontier.append(next_state)
                    explored.add(tuple(next_state.state))
                    self.current_depth = max(self.current_depth, next_state.depth)
            
        return None

    def a_star(self, init_state):
        
        frontier = []
        explored = set()

        heapq.heappush(frontier, init_state)
        explored.add(tuple(init_state.state))

        while frontier:
            board = heapq.heappop(frontier)
            
            if board.checcheck_final_state():
                self.answer = board
                self.nodes_found = len(explored) - len(frontier) - 1
                return self.answer
            
            for next_state in board.find_next_states():
                if tuple(next_state.state) not in explored:
                    heapq.heappush(frontier, next_state)
                    explored.add(tuple(next_state.state))
                    self.current_depth = max(self.current_depth, next_state.depth)
            
        return None

    def greedy_BFS(self, init_state):
        
        frontier = []
        explored = set()

        heapq.heappush(frontier, init_state)
        explored.add(tuple(init_state.state))

        while frontier:
            board = heapq.heappop(frontier)
            
            if board.checcheck_final_state():
                self.answer = board
                self.nodes_found = len(explored) - len(frontier) - 1
                return self.answer

            for next_state in board.find_next_states():
                if tuple(next_state.state) not in explored:
                    heapq.heappush(frontier, next_state)
                    explored.add(tuple(next_state.state))
                    self.current_depth = max(self.current_depth, next_state.depth)
        
        return None

    def helper_path(self):
        
        this_state = self.answer
        path = [this_state]

        while this_state.previous != None:
            path.append(this_state.previous)
            this_state = this_state.previous
        
        return path[::-1]

    def printer_details(self, algorithm):
        
        print("********************************************************************************")
        print("\nStates Visited\t:", self.nodes_found)
        print("\nDepth of {0}\t: {1}".format(algorithm, self.current_depth))
        print("\nFinal Path:\n")
    
        for state in self.helper_path():
            print("Move :", state.operation)
            print(state, "\n")
        
        print("********************************************************************************")
if __name__ == "__main__":
     
    print("\n\t\t\t Breadth-First Search: \n")
    solver = ()
    init_state = Puzzle([7, 2, 4, 5, 0, 6, 8, 3, 1])
    answer = solver.BFS(init_state)
    solver.printer_details("BF Search")

    print("\n\t\t\t A* Search: \n")
    solver = ()
    init_state = Puzzle([7, 2, 4, 5, 0, 6, 8, 3, 1], cost_reverse=True)
    answer = solver.a_star(init_state)
    solver.printer_details("A* Search")
    
    print("\n\t\t\t Greedy Best-First Search: \n")
    solver = ()
    init_state = Puzzle([7, 2, 4, 5, 0, 6, 8, 3, 1])
    answer = solver.greedy_BFS(init_state)
    solver.printer_details("Greedy BFS")        
