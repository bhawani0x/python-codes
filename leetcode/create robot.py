def solution(moves):
    x, y = 0, 0
    visited_points = [(0, 0)]

    for move in moves:
        if move == '^':
            y += 1
        elif move == 'v':
            y -= 1
        elif move == '>':
            x += 1
        elif move == '<':
            x -= 1

        new_point = (x, y)

        if new_point in visited_points:
            print(visited_points)
            return True

        visited_points.append(new_point)

    # Check if the robot returns to the starting point (0, 0)
    return (x, y) == (0, 0)

# Test cases
print(solution("^^^<<<<vvv>>>>"))
# print(solution("<<v>>>^^^"))  # Output: True
# print(solution("^^^>v"))  # Output: False
