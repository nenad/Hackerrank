#!/usr/bin/python
import math


def next_move(posr, posc, dimh, dimw, board):
    matrix = [[0 for _ in xrange(dimh)] for _ in xrange(dimw)]

    for r in range(0, dimh):
        for c in range(0, dimw):
            character = board[r][c]
            if character == '-':
                pass
            elif character == 'b':
                pass
            elif character == 'd':
                matrix[r][c] = 1

    #print all_clean(matrix)
    closest_move(matrix, posr, posc, dimh, dimw)


def closest_move(matrix, r, c, h, w):
    l = []
    for i in range(0, h):
        for j in range(0, w):
            if matrix[i][j] == 1:
                l.append((manhattan_distance(r, c, i, j), i, j))
    l = sorted(l, key=lambda point: point[0])

    closest_point = l[0]
    #print closest_point
    #print l
    v_diff = closest_point[1] - r
    h_diff = closest_point[2] - c
    #print h_diff
    #print v_diff

    if closest_point[0] == 0:
        print "CLEAN"
    elif v_diff < 0:
        print "UP"
    elif v_diff > 0:
        print "DOWN"
    elif h_diff < 0:
        print "LEFT"
    else:
        print "RIGHT"


def manhattan_distance(x1, y1, x2, y2):
    distance = abs(y2 - y1) + abs(x2 - x1)
    #print "({0}, {1}) to ({2}, {3}) is {4}".format(x1, y1, x2, y2, distance)
    return distance


def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)


def all_clean(matrix):
    #print matrix
    total_sum = 0
    for l in matrix:
        total_sum += sum(l)
    return total_sum == 0

if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    dim = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)