def nextMove(n,r,c,grid):

    me_position = (-1, -1)
    princess_position = (-1, -1)

    m_pos = -1
    q_pos = -1

    for i in range(0, n):
        line = grid[i]
        if m_pos == -1:
            m_pos = line.find('m')
            me_position = (i, m_pos)
        if q_pos == -1:
            q_pos = line.find('p')
            princess_position = (i, q_pos)

        if m_pos != -1 and q_pos != -1:
            break

    h_diff = princess_position[1] - me_position[1]
    v_diff = princess_position[0] - me_position[0]

    if v_diff < 0:
        v_diff = abs(v_diff)
        for i in range(0, v_diff):
            print "UP"
    else:
        for i in range(0, v_diff):
            print "DOWN"

    if h_diff < 0:
        h_diff = abs(h_diff)
        for i in range(0, h_diff):
            print "LEFT"
    else:
        for i in range(0, h_diff):
            print "RIGHT"





n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

nextMove(n,r,c,grid)
