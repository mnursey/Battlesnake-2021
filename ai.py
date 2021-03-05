import floodfill_pathfinding
import board
import random

class SnakeAI:

    def __init__(self):

        return

    def get_closest_safe_food(self, data, game_board, head_fill, tail_fill):

        if len(data["board"]["food"]) != 0:
            closest_apple_index = None
            best_distance = 999

            for i, f in enumerate(data["board"]["food"]):
                h_path = head_fill.path(data["board"]["food"][i])
                t_path = tail_fill.path(data["board"]["food"][i])

                if len(h_path) < best_distance and len(h_path) > 1 and len(t_path) > 1:
                    best_distance = len(h_path)
                    closest_apple_index = i

            return closest_apple_index
        else:

            return None

    def get_closest_food(self, data, game_board):

        if len(data["board"]["food"]) != 0:
            closest_apple_index = None
            best_distance = 999

            for i, f in enumerate(data["board"]["food"]):
                new_distance = game_board.distance(f, data["you"]["body"][0])
                if new_distance < best_distance:
                    best_distance = new_distance
                    closest_apple_index = i

            return closest_apple_index
        else:

            return None

    def get_available_moves(self, game_board, head_cord):

        possible_moves = []

        neighbours = game_board.neighbours(head_cord["x"], head_cord["y"])

        for n in neighbours:
            if not game_board.isBlocked(n["x"], n["y"]):
                if n["x"] < head_cord["x"]:
                    possible_moves.append("left")
                if n["x"] >head_cord["x"]:
                    possible_moves.append("right")

                if n["y"] < head_cord["y"]:
                    possible_moves.append("down")
                if n["y"] > head_cord["y"]:
                    possible_moves.append("up")

        return possible_moves

    def move(self, data):

        b = board.Board(data)
        f = floodfill_pathfinding.Floodfill(b, data["you"]["body"][0])
        f_tail = floodfill_pathfinding.Floodfill(b, data["you"]["body"][-1])
        #f.print()

        target_food_index = self.get_closest_safe_food(data, b, f, f_tail)

        if target_food_index != None:
            print("FOOD")
            path = f.path(data["board"]["food"][target_food_index])
        else:
            print("TAIL")
            path = f.path(data["you"]["body"][-1])

        # Choose a random direction to move in
        #possible_moves = ["up", "down", "left", "right"]
        possible_moves = self.get_available_moves(b, data["you"]["body"][0])

        # fail safe... encase no moves are possible
        if len(possible_moves) == 0: possible_moves = ["up"]

        move = random.choice(possible_moves)

        if len(path) > 1:

            print(path)

            if path[1]["x"] < data["you"]["body"][0]["x"]:
                move = "left"
            if path[1]["x"] > data["you"]["body"][0]["x"]:
                move = "right"

            if path[1]["y"] < data["you"]["body"][0]["y"]:
                move = "down"
            if path[1]["y"] > data["you"]["body"][0]["y"]:
                move = "up"

        return move
