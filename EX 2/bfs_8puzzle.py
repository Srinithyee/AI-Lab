#!/usr/bin/env python
# coding: utf-8

# In[1]:


from queue import Queue 
import copy


# In[2]:


def helper_print(node):
    print(node[0],node[1],node[2])
    print(node[3],node[4],node[5])
    print(node[6],node[7],node[8])
    global nodeNumber
    print('Node:', nodeNumber)
    print('Depth:', len(node[9:]))
    print('Moves:', node[9:])
    print('------')
    nodeNumber += 1


# In[3]:


def helper_isfinal(node):
    if node[:9]==finalNode:
        heleper_print(node)
        return True
    if node[:9] not in explored:
        heleper_print(node)
        queue.put(node)
        explored.append(node[:9])
    return False


# In[5]:


if __name__ == '__main__':
    startNode = [1,5,4, 3,7,2, 6,8,0]
    finalNode = [0,1,2, 3,4,5, 6,7,8]
    
    found = False
    nodeNumber = 0
    explored = []
    queue = Queue()
    queue.put(startNode)
    explored.append(startNode)
    helper_print(startNode)
  

    while (not found and not queue.empty()):
        currentNode = queue.get()
        emptytile = currentNode.index(0)
        if emptytile!=0 and emptytile!=1 and emptytile!=2:
            up = copy.deepcopy(currentNode)
            up[emptytile] = up[emptytile-3]
            up[emptytile-3] = 0
            up.append('up')
            found = helper_isfinal(up)
        if emptytile!=0 and emptytile!=3 and emptytile!=6 and found==False:
            left = copy.deepcopy(currentNode)
            left[emptytile] = left[emptytile-1]
            left[emptytile-1] = 0
            left.append('left')
            found = helper_isfinal(left)
        if emptytile!=6 and emptytile!=7 and emptytile!=8 and found==False:
            down = copy.deepcopy(currentNode)
            down[emptytile] = down[emptytile+3]
            down[emptytile+3] = 0
            down.append('down')
            found = helper_isfinal(down)
        if emptytile!=2 and emptytile!=5 and emptytile!=8 and found==False:
            right = copy.deepcopy(currentNode)
            right[emptytile] = right[emptytile+1]
            right[emptytile+1] = 0
            right.append('right')
            found = helper_isfinal(right)


'''
1 5 4
3 7 2
6 8 0
Node: 0
Depth: 0
Moves: []
------
1 5 4
3 7 0
6 8 2
Node: 1
Depth: 1
Moves: ['up']
------
1 5 4
3 7 2
6 0 8
Node: 2
Depth: 1
Moves: ['left']
------
1 5 0
3 7 4
6 8 2
Node: 3
Depth: 2
Moves: ['up', 'up']
------
1 5 4
3 0 7
6 8 2
Node: 4
Depth: 2
Moves: ['up', 'left']
------
1 5 4
3 0 2
6 7 8
Node: 5
Depth: 2
Moves: ['left', 'up']
------
1 5 4
3 7 2
0 6 8
Node: 6
Depth: 2
Moves: ['left', 'left']
------
1 0 5
3 7 4
6 8 2
Node: 7
Depth: 3
Moves: ['up', 'up', 'left']
------
1 0 4
3 5 7
6 8 2
Node: 8
Depth: 3
Moves: ['up', 'left', 'up']
------
1 5 4
0 3 7
6 8 2
Node: 9
Depth: 3
Moves: ['up', 'left', 'left']
------
1 5 4
3 8 7
6 0 2
Node: 10
Depth: 3
Moves: ['up', 'left', 'down']
------
1 0 4
3 5 2
6 7 8
Node: 11
Depth: 3
Moves: ['left', 'up', 'up']
------
1 5 4
0 3 2
6 7 8
Node: 12
Depth: 3
Moves: ['left', 'up', 'left']
------
1 5 4
3 2 0
6 7 8
Node: 13
Depth: 3
Moves: ['left', 'up', 'right']
------
1 5 4
0 7 2
3 6 8
Node: 14
Depth: 3
Moves: ['left', 'left', 'up']
------
0 1 5
3 7 4
6 8 2
Node: 15
Depth: 4
Moves: ['up', 'up', 'left', 'left']
------
1 7 5
3 0 4
6 8 2
Node: 16
Depth: 4
Moves: ['up', 'up', 'left', 'down']
------
0 1 4
3 5 7
6 8 2
Node: 17
Depth: 4
Moves: ['up', 'left', 'up', 'left']
------
1 4 0
3 5 7
6 8 2
Node: 18
Depth: 4
Moves: ['up', 'left', 'up', 'right']
------
0 5 4
1 3 7
6 8 2
Node: 19
Depth: 4
Moves: ['up', 'left', 'left', 'up']
------
1 5 4
6 3 7
0 8 2
Node: 20
Depth: 4
Moves: ['up', 'left', 'left', 'down']
------
1 5 4
3 8 7
0 6 2
Node: 21
Depth: 4
Moves: ['up', 'left', 'down', 'left']
------
1 5 4
3 8 7
6 2 0
Node: 22
Depth: 4
Moves: ['up', 'left', 'down', 'right']
------
0 1 4
3 5 2
6 7 8
Node: 23
Depth: 4
Moves: ['left', 'up', 'up', 'left']
------
1 4 0
3 5 2
6 7 8
Node: 24
Depth: 4
Moves: ['left', 'up', 'up', 'right']
------
0 5 4
1 3 2
6 7 8
Node: 25
Depth: 4
Moves: ['left', 'up', 'left', 'up']
------
1 5 4
6 3 2
0 7 8
Node: 26
Depth: 4
Moves: ['left', 'up', 'left', 'down']
------
1 5 0
3 2 4
6 7 8
Node: 27
Depth: 4
Moves: ['left', 'up', 'right', 'up']
------
1 5 4
3 2 8
6 7 0
Node: 28
Depth: 4
Moves: ['left', 'up', 'right', 'down']
------
0 5 4
1 7 2
3 6 8
Node: 29
Depth: 4
Moves: ['left', 'left', 'up', 'up']
------
1 5 4
7 0 2
3 6 8
Node: 30
Depth: 4
Moves: ['left', 'left', 'up', 'right']
------
3 1 5
0 7 4
6 8 2
Node: 31
Depth: 5
Moves: ['up', 'up', 'left', 'left', 'down']
------
1 7 5
0 3 4
6 8 2
Node: 32
Depth: 5
Moves: ['up', 'up', 'left', 'down', 'left']
------
1 7 5
3 8 4
6 0 2
Node: 33
Depth: 5
Moves: ['up', 'up', 'left', 'down', 'down']
------
1 7 5
3 4 0
6 8 2
Node: 34
Depth: 5
Moves: ['up', 'up', 'left', 'down', 'right']
------
3 1 4
0 5 7
6 8 2
Node: 35
Depth: 5
Moves: ['up', 'left', 'up', 'left', 'down']
------
1 4 7
3 5 0
6 8 2
Node: 36
Depth: 5
Moves: ['up', 'left', 'up', 'right', 'down']
------
5 0 4
1 3 7
6 8 2
Node: 37
Depth: 5
Moves: ['up', 'left', 'left', 'up', 'right']
------
1 5 4
6 3 7
8 0 2
Node: 38
Depth: 5
Moves: ['up', 'left', 'left', 'down', 'right']
------
1 5 4
0 8 7
3 6 2
Node: 39
Depth: 5
Moves: ['up', 'left', 'down', 'left', 'up']
------
1 5 4
3 8 0
6 2 7
Node: 40
Depth: 5
Moves: ['up', 'left', 'down', 'right', 'up']
------
3 1 4
0 5 2
6 7 8
Node: 41
Depth: 5
Moves: ['left', 'up', 'up', 'left', 'down']
------
1 4 2
3 5 0
6 7 8
Node: 42
Depth: 5
Moves: ['left', 'up', 'up', 'right', 'down']
------
5 0 4
1 3 2
6 7 8
Node: 43
Depth: 5
Moves: ['left', 'up', 'left', 'up', 'right']
------
1 5 4
6 3 2
7 0 8
Node: 44
Depth: 5
Moves: ['left', 'up', 'left', 'down', 'right']
------
1 0 5
3 2 4
6 7 8
Node: 45
Depth: 5
Moves: ['left', 'up', 'right', 'up', 'left']
------
1 5 4
3 2 8
6 0 7
Node: 46
Depth: 5
Moves: ['left', 'up', 'right', 'down', 'left']
------
5 0 4
1 7 2
3 6 8
Node: 47
Depth: 5
Moves: ['left', 'left', 'up', 'up', 'right']
------
1 0 4
7 5 2
3 6 8
Node: 48
Depth: 5
Moves: ['left', 'left', 'up', 'right', 'up']
------
1 5 4
7 6 2
3 0 8
Node: 49
Depth: 5
Moves: ['left', 'left', 'up', 'right', 'down']
------
1 5 4
7 2 0
3 6 8
Node: 50
Depth: 5
Moves: ['left', 'left', 'up', 'right', 'right']
------
3 1 5
6 7 4
0 8 2
Node: 51
Depth: 6
Moves: ['up', 'up', 'left', 'left', 'down', 'down']
------
3 1 5
7 0 4
6 8 2
Node: 52
Depth: 6
Moves: ['up', 'up', 'left', 'left', 'down', 'right']
------
0 7 5
1 3 4
6 8 2
Node: 53
Depth: 6
Moves: ['up', 'up', 'left', 'down', 'left', 'up']
------
1 7 5
6 3 4
0 8 2
Node: 54
Depth: 6
Moves: ['up', 'up', 'left', 'down', 'left', 'down']
------
1 7 5
3 8 4
0 6 2
Node: 55
Depth: 6
Moves: ['up', 'up', 'left', 'down', 'down', 'left']
------
1 7 5
3 8 4
6 2 0
Node: 56
Depth: 6
Moves: ['up', 'up', 'left', 'down', 'down', 'right']
------
1 7 0
3 4 5
6 8 2
Node: 57
Depth: 6
Moves: ['up', 'up', 'left', 'down', 'right', 'up']
------
1 7 5
3 4 2
6 8 0
Node: 58
Depth: 6
Moves: ['up', 'up', 'left', 'down', 'right', 'down']
------
3 1 4
6 5 7
0 8 2
Node: 59
Depth: 6
Moves: ['up', 'left', 'up', 'left', 'down', 'down']
------
3 1 4
5 0 7
6 8 2
Node: 60
Depth: 6
Moves: ['up', 'left', 'up', 'left', 'down', 'right']
------
1 4 7
3 0 5
6 8 2
Node: 61
Depth: 6
Moves: ['up', 'left', 'up', 'right', 'down', 'left']
------
1 4 7
3 5 2
6 8 0
Node: 62
Depth: 6
Moves: ['up', 'left', 'up', 'right', 'down', 'down']
------
5 3 4
1 0 7
6 8 2
Node: 63
Depth: 6
Moves: ['up', 'left', 'left', 'up', 'right', 'down']
------
5 4 0
1 3 7
6 8 2
Node: 64
Depth: 6
Moves: ['up', 'left', 'left', 'up', 'right', 'right']
------
1 5 4
6 0 7
8 3 2
Node: 65
Depth: 6
Moves: ['up', 'left', 'left', 'down', 'right', 'up']
------
1 5 4
6 3 7
8 2 0
Node: 66
Depth: 6
Moves: ['up', 'left', 'left', 'down', 'right', 'right']
------
0 5 4
1 8 7
3 6 2
Node: 67
Depth: 6
Moves: ['up', 'left', 'down', 'left', 'up', 'up']
------
1 5 4
8 0 7
3 6 2
Node: 68
Depth: 6
Moves: ['up', 'left', 'down', 'left', 'up', 'right']
------
1 5 0
3 8 4
6 2 7
Node: 69
Depth: 6
Moves: ['up', 'left', 'down', 'right', 'up', 'up']
------
1 5 4
3 0 8
6 2 7
Node: 70
Depth: 6
Moves: ['up', 'left', 'down', 'right', 'up', 'left']
------
3 1 4
6 5 2
0 7 8
Node: 71
Depth: 6
Moves: ['left', 'up', 'up', 'left', 'down', 'down']
------
3 1 4
5 0 2
6 7 8
Node: 72
Depth: 6
Moves: ['left', 'up', 'up', 'left', 'down', 'right']
------
1 4 2
3 0 5
6 7 8
Node: 73
Depth: 6
Moves: ['left', 'up', 'up', 'right', 'down', 'left']
------
1 4 2
3 5 8
6 7 0
Node: 74
Depth: 6
Moves: ['left', 'up', 'up', 'right', 'down', 'down']
------
5 3 4
1 0 2
6 7 8
Node: 75
Depth: 6
Moves: ['left', 'up', 'left', 'up', 'right', 'down']
------
5 4 0
1 3 2
6 7 8
Node: 76
Depth: 6
Moves: ['left', 'up', 'left', 'up', 'right', 'right']
------
1 5 4
6 0 2
7 3 8
Node: 77
Depth: 6
Moves: ['left', 'up', 'left', 'down', 'right', 'up']
------
1 5 4
6 3 2
7 8 0
Node: 78
Depth: 6
Moves: ['left', 'up', 'left', 'down', 'right', 'right']
------
0 1 5
3 2 4
6 7 8
Node: 79
Depth: 6
Moves: ['left', 'up', 'right', 'up', 'left', 'left']
------
1 2 5
3 0 4
6 7 8
Node: 80
Depth: 6
Moves: ['left', 'up', 'right', 'up', 'left', 'down']
------
1 5 4
3 2 8
0 6 7
Node: 81
Depth: 6
Moves: ['left', 'up', 'right', 'down', 'left', 'left']
------
5 7 4
1 0 2
3 6 8
Node: 82
Depth: 6
Moves: ['left', 'left', 'up', 'up', 'right', 'down']
------
5 4 0
1 7 2
3 6 8
Node: 83
Depth: 6
Moves: ['left', 'left', 'up', 'up', 'right', 'right']
------
0 1 4
7 5 2
3 6 8
Node: 84
Depth: 6
Moves: ['left', 'left', 'up', 'right', 'up', 'left']
------
1 4 0
7 5 2
3 6 8
Node: 85
Depth: 6
Moves: ['left', 'left', 'up', 'right', 'up', 'right']
------
1 5 4
7 6 2
0 3 8
Node: 86
Depth: 6
Moves: ['left', 'left', 'up', 'right', 'down', 'left']
------
1 5 4
7 6 2
3 8 0
Node: 87
Depth: 6
Moves: ['left', 'left', 'up', 'right', 'down', 'right']
------
1 5 0
7 2 4
3 6 8
Node: 88
Depth: 6
Moves: ['left', 'left', 'up', 'right', 'right', 'up']
------
1 5 4
7 2 8
3 6 0
Node: 89
Depth: 6
Moves: ['left', 'left', 'up', 'right', 'right', 'down']
------
3 1 5
6 7 4
8 0 2
Node: 90
Depth: 7
Moves: ['up', 'up', 'left', 'left', 'down', 'down', 'right']
------
3 0 5
7 1 4
6 8 2
Node: 91
Depth: 7
Moves: ['up', 'up', 'left', 'left', 'down', 'right', 'up']
------
3 1 5
7 8 4
6 0 2
Node: 92
Depth: 7
Moves: ['up', 'up', 'left', 'left', 'down', 'right', 'down']
------
3 1 5
7 4 0
6 8 2
Node: 93
Depth: 7
Moves: ['up', 'up', 'left', 'left', 'down', 'right', 'right']
------
7 0 5
1 3 4
6 8 2
Node: 94
Depth: 7
Moves: ['up', 'up', 'left', 'down', 'left', 'up', 'right']
------
1 7 5
6 3 4
8 0 2
Node: 95
Depth: 7
Moves: ['up', 'up', 'left', 'down', 'left', 'down', 'right']
------
1 7 5
0 8 4
3 6 2
Node: 96
Depth: 7
Moves: ['up', 'up', 'left', 'down', 'down', 'left', 'up']
------
1 7 5
3 8 0
6 2 4
Node: 97
Depth: 7
Moves: ['up', 'up', 'left', 'down', 'down', 'right', 'up']
------
1 0 7
3 4 5
6 8 2
Node: 98
Depth: 7
Moves: ['up', 'up', 'left', 'down', 'right', 'up', 'left']
------
1 7 5
3 4 2
6 0 8
Node: 99
Depth: 7
Moves: ['up', 'up', 'left', 'down', 'right', 'down', 'left']
------
3 1 4
6 5 7
8 0 2
Node: 100
Depth: 7
Moves: ['up', 'left', 'up', 'left', 'down', 'down', 'right']
------
3 0 4
5 1 7
6 8 2
Node: 101
Depth: 7
Moves: ['up', 'left', 'up', 'left', 'down', 'right', 'up']
------
3 1 4
5 8 7
6 0 2
Node: 102
Depth: 7
Moves: ['up', 'left', 'up', 'left', 'down', 'right', 'down']
------
3 1 4
5 7 0
6 8 2
Node: 103
Depth: 7
Moves: ['up', 'left', 'up', 'left', 'down', 'right', 'right']
------
1 4 7
0 3 5
6 8 2
Node: 104
Depth: 7
Moves: ['up', 'left', 'up', 'right', 'down', 'left', 'left']
------
1 4 7
3 8 5
6 0 2
Node: 105
Depth: 7
Moves: ['up', 'left', 'up', 'right', 'down', 'left', 'down']
------
1 4 7
3 5 2
6 0 8
Node: 106
Depth: 7
Moves: ['up', 'left', 'up', 'right', 'down', 'down', 'left']
------
5 3 4
0 1 7
6 8 2
Node: 107
Depth: 7
Moves: ['up', 'left', 'left', 'up', 'right', 'down', 'left']
------
5 3 4
1 8 7
6 0 2
Node: 108
Depth: 7
Moves: ['up', 'left', 'left', 'up', 'right', 'down', 'down']
------
5 3 4
1 7 0
6 8 2
Node: 109
Depth: 7
Moves: ['up', 'left', 'left', 'up', 'right', 'down', 'right']
------
5 4 7
1 3 0
6 8 2
Node: 110
Depth: 7
Moves: ['up', 'left', 'left', 'up', 'right', 'right', 'down']
------
1 0 4
6 5 7
8 3 2
Node: 111
Depth: 7
Moves: ['up', 'left', 'left', 'down', 'right', 'up', 'up']
------
1 5 4
0 6 7
8 3 2
Node: 112
Depth: 7
Moves: ['up', 'left', 'left', 'down', 'right', 'up', 'left']
------
1 5 4
6 7 0
8 3 2
Node: 113
Depth: 7
Moves: ['up', 'left', 'left', 'down', 'right', 'up', 'right']
------
1 5 4
6 3 0
8 2 7
Node: 114
Depth: 7
Moves: ['up', 'left', 'left', 'down', 'right', 'right', 'up']
------
5 0 4
1 8 7
3 6 2
Node: 115
Depth: 7
Moves: ['up', 'left', 'down', 'left', 'up', 'up', 'right']
------
1 0 4
8 5 7
3 6 2
Node: 116
Depth: 7
Moves: ['up', 'left', 'down', 'left', 'up', 'right', 'up']
------
1 5 4
8 6 7
3 0 2
Node: 117
Depth: 7
Moves: ['up', 'left', 'down', 'left', 'up', 'right', 'down']
------
1 5 4
8 7 0
3 6 2
Node: 118
Depth: 7
Moves: ['up', 'left', 'down', 'left', 'up', 'right', 'right']
------
1 0 5
3 8 4
6 2 7
Node: 119
Depth: 7
Moves: ['up', 'left', 'down', 'right', 'up', 'up', 'left']
------
1 0 4
3 5 8
6 2 7
Node: 120
Depth: 7
Moves: ['up', 'left', 'down', 'right', 'up', 'left', 'up']
------
1 5 4
0 3 8
6 2 7
Node: 121
Depth: 7
Moves: ['up', 'left', 'down', 'right', 'up', 'left', 'left']
------
3 1 4
6 5 2
7 0 8
Node: 122
Depth: 7
Moves: ['left', 'up', 'up', 'left', 'down', 'down', 'right']
------
3 0 4
5 1 2
6 7 8
Node: 123
Depth: 7
Moves: ['left', 'up', 'up', 'left', 'down', 'right', 'up']
------
3 1 4
5 7 2
6 0 8
Node: 124
Depth: 7
Moves: ['left', 'up', 'up', 'left', 'down', 'right', 'down']
------
3 1 4
5 2 0
6 7 8
Node: 125
Depth: 7
Moves: ['left', 'up', 'up', 'left', 'down', 'right', 'right']
------
1 0 2
3 4 5
6 7 8
Node: 126
Depth: 7
Moves: ['left', 'up', 'up', 'right', 'down', 'left', 'up']
------
1 4 2
0 3 5
6 7 8
Node: 127
Depth: 7
Moves: ['left', 'up', 'up', 'right', 'down', 'left', 'left']
------
1 4 2
3 7 5
6 0 8
Node: 128
Depth: 7
Moves: ['left', 'up', 'up', 'right', 'down', 'left', 'down']
------
1 4 2
3 5 8
6 0 7
Node: 129
Depth: 7
Moves: ['left', 'up', 'up', 'right', 'down', 'down', 'left']
------
5 3 4
0 1 2
6 7 8
Node: 130
Depth: 7
Moves: ['left', 'up', 'left', 'up', 'right', 'down', 'left']
------
5 3 4
1 7 2
6 0 8
Node: 131
Depth: 7
Moves: ['left', 'up', 'left', 'up', 'right', 'down', 'down']
------
5 3 4
1 2 0
6 7 8
Node: 132
Depth: 7
Moves: ['left', 'up', 'left', 'up', 'right', 'down', 'right']
------
5 4 2
1 3 0
6 7 8
Node: 133
Depth: 7
Moves: ['left', 'up', 'left', 'up', 'right', 'right', 'down']
------
1 0 4
6 5 2
7 3 8
Node: 134
Depth: 7
Moves: ['left', 'up', 'left', 'down', 'right', 'up', 'up']
------
1 5 4
0 6 2
7 3 8
Node: 135
Depth: 7
Moves: ['left', 'up', 'left', 'down', 'right', 'up', 'left']
------
1 5 4
6 2 0
7 3 8
Node: 136
Depth: 7
Moves: ['left', 'up', 'left', 'down', 'right', 'up', 'right']
------
1 5 4
6 3 0
7 8 2
Node: 137
Depth: 7
Moves: ['left', 'up', 'left', 'down', 'right', 'right', 'up']
------
3 1 5
0 2 4
6 7 8
Node: 138
Depth: 7
Moves: ['left', 'up', 'right', 'up', 'left', 'left', 'down']
------
1 2 5
0 3 4
6 7 8
Node: 139
Depth: 7
Moves: ['left', 'up', 'right', 'up', 'left', 'down', 'left']
------
1 2 5
3 7 4
6 0 8
Node: 140
Depth: 7
Moves: ['left', 'up', 'right', 'up', 'left', 'down', 'down']
------
1 2 5
3 4 0
6 7 8
Node: 141
Depth: 7
Moves: ['left', 'up', 'right', 'up', 'left', 'down', 'right']
------
1 5 4
0 2 8
3 6 7
Node: 142
Depth: 7
Moves: ['left', 'up', 'right', 'down', 'left', 'left', 'up']
------
5 7 4
0 1 2
3 6 8
Node: 143
Depth: 7
Moves: ['left', 'left', 'up', 'up', 'right', 'down', 'left']
------
5 7 4
1 6 2
3 0 8
Node: 144
Depth: 7
Moves: ['left', 'left', 'up', 'up', 'right', 'down', 'down']
------
5 7 4
1 2 0
3 6 8
Node: 145
Depth: 7
Moves: ['left', 'left', 'up', 'up', 'right', 'down', 'right']
------
5 4 2
1 7 0
3 6 8
Node: 146
Depth: 7
Moves: ['left', 'left', 'up', 'up', 'right', 'right', 'down']
------
7 1 4
0 5 2
3 6 8
Node: 147
Depth: 7
Moves: ['left', 'left', 'up', 'right', 'up', 'left', 'down']
------
1 4 2
7 5 0
3 6 8
Node: 148
Depth: 7
Moves: ['left', 'left', 'up', 'right', 'up', 'right', 'down']
------
1 5 4
7 6 0
3 8 2
Node: 149
Depth: 7
Moves: ['left', 'left', 'up', 'right', 'down', 'right', 'up']
------
1 0 5
7 2 4
3 6 8
Node: 150
Depth: 7
Moves: ['left', 'left', 'up', 'right', 'right', 'up', 'left']
------
1 5 4
7 2 8
3 0 6
Node: 151
Depth: 7
Moves: ['left', 'left', 'up', 'right', 'right', 'down', 'left']
------
3 1 5
6 0 4
8 7 2
Node: 152
Depth: 8
Moves: ['up', 'up', 'left', 'left', 'down', 'down', 'right', 'up']
------
3 1 5
6 7 4
8 2 0
Node: 153
Depth: 8
Moves: ['up', 'up', 'left', 'left', 'down', 'down', 'right', 'right']
------
0 3 5
7 1 4
6 8 2
Node: 154
Depth: 8
Moves: ['up', 'up', 'left', 'left', 'down', 'right', 'up', 'left']
------
3 5 0
7 1 4
6 8 2
Node: 155
Depth: 8
Moves: ['up', 'up', 'left', 'left', 'down', 'right', 'up', 'right']
------
3 1 5
7 8 4
0 6 2
Node: 156
Depth: 8
Moves: ['up', 'up', 'left', 'left', 'down', 'right', 'down', 'left']
------
3 1 5
7 8 4
6 2 0
Node: 157
Depth: 8
Moves: ['up', 'up', 'left', 'left', 'down', 'right', 'down', 'right']
------
3 1 0
7 4 5
6 8 2
Node: 158
Depth: 8
Moves: ['up', 'up', 'left', 'left', 'down', 'right', 'right', 'up']
------
3 1 5
7 4 2
6 8 0
Node: 159
Depth: 8
Moves: ['up', 'up', 'left', 'left', 'down', 'right', 'right', 'down']
------
7 3 5
1 0 4
6 8 2
Node: 160
Depth: 8
Moves: ['up', 'up', 'left', 'down', 'left', 'up', 'right', 'down']
------
7 5 0
1 3 4
6 8 2
Node: 161
Depth: 8
Moves: ['up', 'up', 'left', 'down', 'left', 'up', 'right', 'right']
------
1 7 5
6 0 4
8 3 2
Node: 162
Depth: 8
Moves: ['up', 'up', 'left', 'down', 'left', 'down', 'right', 'up']
------
1 7 5
6 3 4
8 2 0
Node: 163
Depth: 8
Moves: ['up', 'up', 'left', 'down', 'left', 'down', 'right', 'right']
------
0 7 5
1 8 4
3 6 2
Node: 164
Depth: 8
Moves: ['up', 'up', 'left', 'down', 'down', 'left', 'up', 'up']
------
1 7 5
8 0 4
3 6 2
Node: 165
Depth: 8
Moves: ['up', 'up', 'left', 'down', 'down', 'left', 'up', 'right']
------
1 7 0
3 8 5
6 2 4
Node: 166
Depth: 8
Moves: ['up', 'up', 'left', 'down', 'down', 'right', 'up', 'up']
------
1 7 5
3 0 8
6 2 4
Node: 167
Depth: 8
Moves: ['up', 'up', 'left', 'down', 'down', 'right', 'up', 'left']
------
0 1 7
3 4 5
6 8 2
Node: 168
Depth: 8
Moves: ['up', 'up', 'left', 'down', 'right', 'up', 'left', 'left']
------
1 7 5
3 0 2
6 4 8
Node: 169
Depth: 8
Moves: ['up', 'up', 'left', 'down', 'right', 'down', 'left', 'up']
------
1 7 5
3 4 2
0 6 8
Node: 170
Depth: 8
Moves: ['up', 'up', 'left', 'down', 'right', 'down', 'left', 'left']
------
3 1 4
6 0 7
8 5 2
Node: 171
Depth: 8
Moves: ['up', 'left', 'up', 'left', 'down', 'down', 'right', 'up']
------
3 1 4
6 5 7
8 2 0
Node: 172
Depth: 8
Moves: ['up', 'left', 'up', 'left', 'down', 'down', 'right', 'right']
------
0 3 4
5 1 7
6 8 2
Node: 173
Depth: 8
Moves: ['up', 'left', 'up', 'left', 'down', 'right', 'up', 'left']
------
3 4 0
5 1 7
6 8 2
Node: 174
Depth: 8
Moves: ['up', 'left', 'up', 'left', 'down', 'right', 'up', 'right']
------
3 1 4
5 8 7
0 6 2
Node: 175
Depth: 8
Moves: ['up', 'left', 'up', 'left', 'down', 'right', 'down', 'left']
------
3 1 4
5 8 7
6 2 0
Node: 176
Depth: 8
Moves: ['up', 'left', 'up', 'left', 'down', 'right', 'down', 'right']
------
3 1 0
5 7 4
6 8 2
Node: 177
Depth: 8
Moves: ['up', 'left', 'up', 'left', 'down', 'right', 'right', 'up']
------
3 1 4
5 7 2
6 8 0
Node: 178
Depth: 8
Moves: ['up', 'left', 'up', 'left', 'down', 'right', 'right', 'down']
------
0 4 7
1 3 5
6 8 2
Node: 179
Depth: 8
Moves: ['up', 'left', 'up', 'right', 'down', 'left', 'left', 'up']
------
1 4 7
6 3 5
0 8 2
Node: 180
Depth: 8
Moves: ['up', 'left', 'up', 'right', 'down', 'left', 'left', 'down']
------
1 4 7
3 8 5
0 6 2
Node: 181
Depth: 8
Moves: ['up', 'left', 'up', 'right', 'down', 'left', 'down', 'left']
------
1 4 7
3 8 5
6 2 0
Node: 182
Depth: 8
Moves: ['up', 'left', 'up', 'right', 'down', 'left', 'down', 'right']
------
1 4 7
3 0 2
6 5 8
Node: 183
Depth: 8
Moves: ['up', 'left', 'up', 'right', 'down', 'down', 'left', 'up']
------
1 4 7
3 5 2
0 6 8
Node: 184
Depth: 8
Moves: ['up', 'left', 'up', 'right', 'down', 'down', 'left', 'left']
------
5 3 4
6 1 7
0 8 2
Node: 185
Depth: 8
Moves: ['up', 'left', 'left', 'up', 'right', 'down', 'left', 'down']
------
5 3 4
1 8 7
0 6 2
Node: 186
Depth: 8
Moves: ['up', 'left', 'left', 'up', 'right', 'down', 'down', 'left']
------
5 3 4
1 8 7
6 2 0
Node: 187
Depth: 8
Moves: ['up', 'left', 'left', 'up', 'right', 'down', 'down', 'right']
------
5 3 0
1 7 4
6 8 2
Node: 188
Depth: 8
Moves: ['up', 'left', 'left', 'up', 'right', 'down', 'right', 'up']
------
5 3 4
1 7 2
6 8 0
Node: 189
Depth: 8
Moves: ['up', 'left', 'left', 'up', 'right', 'down', 'right', 'down']
------
5 4 7
1 0 3
6 8 2
Node: 190
Depth: 8
Moves: ['up', 'left', 'left', 'up', 'right', 'right', 'down', 'left']
------
5 4 7
1 3 2
6 8 0
Node: 191
Depth: 8
Moves: ['up', 'left', 'left', 'up', 'right', 'right', 'down', 'down']
------
0 1 4
6 5 7
8 3 2
Node: 192
Depth: 8
Moves: ['up', 'left', 'left', 'down', 'right', 'up', 'up', 'left']
------
1 4 0
6 5 7
8 3 2
Node: 193
Depth: 8
Moves: ['up', 'left', 'left', 'down', 'right', 'up', 'up', 'right']
------
0 5 4
1 6 7
8 3 2
Node: 194
Depth: 8
Moves: ['up', 'left', 'left', 'down', 'right', 'up', 'left', 'up']
------
1 5 4
8 6 7
0 3 2
Node: 195
Depth: 8
Moves: ['up', 'left', 'left', 'down', 'right', 'up', 'left', 'down']
------
1 5 0
6 7 4
8 3 2
Node: 196
Depth: 8
Moves: ['up', 'left', 'left', 'down', 'right', 'up', 'right', 'up']
------
1 5 4
6 7 2
8 3 0
Node: 197
Depth: 8
Moves: ['up', 'left', 'left', 'down', 'right', 'up', 'right', 'down']
------
1 5 0
6 3 4
8 2 7
Node: 198
Depth: 8
Moves: ['up', 'left', 'left', 'down', 'right', 'right', 'up', 'up']
------
1 5 4
6 0 3
8 2 7
Node: 199
Depth: 8
Moves: ['up', 'left', 'left', 'down', 'right', 'right', 'up', 'left']
------
5 8 4
1 0 7
3 6 2
Node: 200
Depth: 8
Moves: ['up', 'left', 'down', 'left', 'up', 'up', 'right', 'down']
------
5 4 0
1 8 7
3 6 2
Node: 201
Depth: 8
Moves: ['up', 'left', 'down', 'left', 'up', 'up', 'right', 'right']
------
0 1 4
8 5 7
3 6 2
Node: 202
Depth: 8
Moves: ['up', 'left', 'down', 'left', 'up', 'right', 'up', 'left']
------
1 4 0
8 5 7
3 6 2
Node: 203
Depth: 8
Moves: ['up', 'left', 'down', 'left', 'up', 'right', 'up', 'right']
------
1 5 4
8 6 7
3 2 0
Node: 204
Depth: 8
Moves: ['up', 'left', 'down', 'left', 'up', 'right', 'down', 'right']
------
1 5 0
8 7 4
3 6 2
Node: 205
Depth: 8
Moves: ['up', 'left', 'down', 'left', 'up', 'right', 'right', 'up']
------
1 5 4
8 7 2
3 6 0
Node: 206
Depth: 8
Moves: ['up', 'left', 'down', 'left', 'up', 'right', 'right', 'down']
------
0 1 5
3 8 4
6 2 7
Node: 207
Depth: 8
Moves: ['up', 'left', 'down', 'right', 'up', 'up', 'left', 'left']
------
1 8 5
3 0 4
6 2 7
Node: 208
Depth: 8
Moves: ['up', 'left', 'down', 'right', 'up', 'up', 'left', 'down']
------
0 1 4
3 5 8
6 2 7
Node: 209
Depth: 8
Moves: ['up', 'left', 'down', 'right', 'up', 'left', 'up', 'left']
------
1 4 0
3 5 8
6 2 7
Node: 210
Depth: 8
Moves: ['up', 'left', 'down', 'right', 'up', 'left', 'up', 'right']
------
0 5 4
1 3 8
6 2 7
Node: 211
Depth: 8
Moves: ['up', 'left', 'down', 'right', 'up', 'left', 'left', 'up']
------
1 5 4
6 3 8
0 2 7
Node: 212
Depth: 8
Moves: ['up', 'left', 'down', 'right', 'up', 'left', 'left', 'down']
------
3 1 4
6 0 2
7 5 8
Node: 213
Depth: 8
Moves: ['left', 'up', 'up', 'left', 'down', 'down', 'right', 'up']
------
3 1 4
6 5 2
7 8 0
Node: 214
Depth: 8
Moves: ['left', 'up', 'up', 'left', 'down', 'down', 'right', 'right']
------
0 3 4
5 1 2
6 7 8
Node: 215
Depth: 8
Moves: ['left', 'up', 'up', 'left', 'down', 'right', 'up', 'left']
------
3 4 0
5 1 2
6 7 8
Node: 216
Depth: 8
Moves: ['left', 'up', 'up', 'left', 'down', 'right', 'up', 'right']
------
3 1 4
5 7 2
0 6 8
Node: 217
Depth: 8
Moves: ['left', 'up', 'up', 'left', 'down', 'right', 'down', 'left']
------
3 1 0
5 2 4
6 7 8
Node: 218
Depth: 8
Moves: ['left', 'up', 'up', 'left', 'down', 'right', 'right', 'up']
------
3 1 4
5 2 8
6 7 0
Node: 219
Depth: 8
Moves: ['left', 'up', 'up', 'left', 'down', 'right', 'right', 'down']
------
0 1 2
3 4 5
6 7 8
Node: 220
Depth: 8
Moves: ['left', 'up', 'up', 'right', 'down', 'left', 'up', 'left']
------
​'''




