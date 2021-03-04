import board

class Floodfill:

    fontier = []
    grid = None
    board = None

    def __init__(self, game_board, start_cord):

        self.board = game_board
        self.grid = [[None for i in range(self.board.width)] for j in range(self.board.width)]

        self.frontier_add(self.create_node(start_cord["x"], start_cord["y"], False, None))

        self.solve()

        return

    def solve(self):

        while len(self.frontier) > 0:
            current = self.fontier_pop()

            for n in self.board.neighbours():
                if self.grid[n['x']][n['y']] == None:
                    unseen_node = self.create_node(n['x'], n['y'], self.board.isBlocked(n['x'], n['y']), current)
                    self.fontier_add(unseen_node)

        return

    def fontier_add(self, node):
        self.frontier.append(node)

        return

    def fontier_pop(self):

        return

    def create_node(self, x, y, blocked, prev):

        return {"x" : x, "y" : y, "blocked" : blocked, "from" : prev}
