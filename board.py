
EMPTY = 0
FOOD = 1
MY_HEAD = 2
MY_BODY = 3
ENEMY_HEAD = 4
ENEMY_BODY = 5

class Board:

    blocked_values = [MY_HEAD, MY_BODY, ENEMY_HEAD, ENEMY_BODY]

    grid = None
    width = 0

    def __init__(self, data):

        self.width = data['board']['width']

        self.grid = [[EMPTY for i in range(self.width)] for j in range(self.width)]

        for f in data['board']['food']:
            self.grid[f['x']][f['y']] = FOOD

        for f in data['board']['snakes']:
            is_head = True
            head_value = ENEMY_HEAD
            body_value = ENEMY_BODY

            if f['id'] == data['you']['id']:
                head_value = MY_HEAD
                body_value = MY_BODY

            for b in f['body']:
                self.grid[b['x']][b['y']] = head_value if is_head else body_value
                is_head = False

        return

    def isBlocked(self, x, y):

        if self.grid[x][y] in self.blocked_values:
            return True

        return False

    def neighbours(self, x, y):

        output = []

        if x - 1 >= 0:
            output.append({"x": x-1,"y" : y})
        if x + 1 < self.width:
            output.append({"x": x+1,"y" : y})

        if y - 1 >= 0:
            output.append({"x": x,"y" : y-1})
        if y + 1 < self.width:
            output.append({"x": x,"y" : y+1})

        return output

    def print(self):

        output = "Grid:\n"
        for y in range(self.width):
            line = "\n"
            for x in range(self.width):
                line = line + str(self.grid[x][self.width - y - 1])
            output += line

        print(output)

        return
