maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x, y: (x + 1, y),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y + 1),
    lambda x, y: (x, y - 1)
]


def maze_path(x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    while (len(stack) > 0):
        curNode = stack[-1]  # current cursor is the last element in stack

        if curNode[0] == x2 and curNode[1] == y2:  # reach the end
            for p in stack:
                print(p)
                return True

        for dirt in dirs:  # find for four directions
            nextNode = dirt(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:  # if next node is available
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]] == 2  # it is in the path
                break
        else:
            maze[curNode[0]][curNode[1]] == 2  # it is in the path
            stack.pop()

    else:
        print("No Route")
        return False

from collections import deque

def print_r(path):
    curNode = path[-1]

    realpath = []

    while curNode[2] != -1:
        realpath.append(curNode[0:2])
        curNode = path[curNode[2]]

    realpath.append(curNode[0:2])
    realpath.reverse()
    for node in realpath:
        print(node)

def maze_path_queue(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1, -1))
    path = []

    while len(queue) > 0:
        curNode = queue.popleft()
        path.append(curNode)
        print(path)

        if curNode[0] == x2 and curNode[1] == y2:
            print_r(path)
            return True

        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                # print(queue)
                queue.append((nextNode[0], nextNode[1], len(path)-1))
                maze[nextNode[0]][nextNode[1]] = 2

    else:
        print("No Route")
        return False


print(maze_path_queue(1, 1, 8, 8))