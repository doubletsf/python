'''
    Data structure: queue
    Algorithm: 广度优先搜索（breadth-first search,BFS）
    deque()创建一个队列
解决:   1)从节点A出发，有前往节点B的路径吗？
        2)从节点A出发，前往节点B的哪条路径最短?
'''
# 查找目标是否是所找的
from collections import deque

def check(name):
    return name[-1] == 'm'

# 广度优先搜索


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if check(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False



graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
search("you")
