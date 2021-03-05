import board

class Floodfill:

    frontier = []
    grid = None
    board = None

    def __init__(self, game_board, start_cord):

        self.board = game_board
        self.grid = [[None for i in range(self.board.width)] for j in range(self.board.width)]

        start_node = self.create_node(start_cord["x"], start_cord["y"], False, None)
        self.frontier_add(start_node)
        self.grid[start_cord['x']][start_cord['y']] = start_node

        self.solve()

        return

    def solve(self):

        while len(self.frontier) > 0:
            current = self.frontier_pop()

            if not current["blocked"]:
                for n in self.board.neighbours(current["x"], current["y"]):
                    # Add to frontier if we haven't seen it
                    if self.grid[n['x']][n['y']] == None:
                        unseen_node = self.create_node(n['x'], n['y'], self.board.isBlocked(n['x'], n['y']), current)
                        self.grid[n['x']][n['y']] = unseen_node
                        self.frontier_add(unseen_node)

        return

    def path(self, target_cord):

        node = self.grid[target_cord['x']][target_cord['y']]

        path = []

        while node:
            path.append({"x" : node["x"], "y" : node["y"]})
            node = node["from"]

        path.reverse()
        return path

    def frontier_add(self, node):
        self.frontier.append(node)

        return

    def frontier_pop(self):

        return self.frontier.pop(0)

    def create_node(self, x, y, blocked, prev):

        return {"x" : x, "y" : y, "blocked" : blocked, "from" : prev}

    def print(self):

        output = "Grid:\n"
        for y in range(self.board.width):
            line = "\n"
            for x in range(self.board.width):
                node = self.grid[x][self.board.width - y - 1]
                value = "-"

                if node:
                    if node["from"] == None:
                        value = "s"
                    elif node["blocked"]:
                        value = "x"
                    else:
                        if node["from"]["x"] < node["x"]:
                            value = "<"
                        if node["from"]["x"] > node["x"]:
                            value = ">"

                        if node["from"]["y"] < node["y"]:
                            value = "v"
                        if node["from"]["y"] > node["y"]:
                            value = "^"

                line = line + value
            output += line

        print(output)

        return
