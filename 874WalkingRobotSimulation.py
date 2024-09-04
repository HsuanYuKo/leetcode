class Solution:
    def robotSim(self, commands, obstacles):
        obstacle_set = set(map(tuple, obstacles))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # North, East, South, West
        x, y, direction = 0, 0, 0
        max_distance = 0

        for command in commands:
            if command == -1:
                if direction == 3:
                    direction = 0
                else:
                    direction = direction + 1
            elif command == -2:
                if direction == 0:
                    direction = 3
                else:
                    direction = direction - 1
            else:
                for i in range(0, command):
                    new_x, new_y = x + directions[direction][0], y + directions[direction][1]
                    if (new_x, new_y) not in obstacle_set:
                        x, y = new_x, new_y
                        max_distance = max(max_distance, x * x + y * y)
                    else:
                        break

        return max_distance
