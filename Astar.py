# -*- coding: utf-8 -*-
import heapq
from MyNode import MyNode

# 堆实现：可以快速找到F最小值点（O(1)）
# 问题：堆重构、多存了一份引用地址

def AStar(startPoint, endPoint, map):
	ZXDJ = 10
	XXDJ = 14
	
	maxRow = len(map)
	maxCol = len(map[0])

	# 建立open，close
	# open引用两份，heap利于快速获取 F最小值点，dict利于更新已经在open中的数据
	# 内存多消耗了一份地址（python 引用 存储的是地址）
	openHeap = list()
	openDict = dict()
	closeDict = dict()

	# 建立终点MyNode
	endNode = MyNode(endPoint['row'], endPoint['col'])
	# 建立起点MyNode
	startNode = MyNode(startPoint['row'], startPoint['col'])
	startNode.g = 0
	startNode.h = (abs(startNode.row - endNode.row) + abs(startNode.col - endNode.col)) * ZXDJ
	startNode.f = startNode.g + startNode.h

	#起点存入open 
	heapq.heappush(openHeap, startNode)
	openDict[startNode.row] = dict()
	openDict[startNode.row][startNode.col] = startNode

	#找寻路径
	findPath = False
	while len(openHeap) > 0:
		#取出open中的F最小值点，加入close
		minNode = heapq.heappop(openHeap)
		del openDict[minNode.row][minNode.col]
		closeDict[minNode.row] = dict()
		closeDict[minNode.row][minNode.col] = minNode
		
		#判定是否为终点
		if minNode.row == endNode.row and minNode.col == endNode.col:
			findPath = True
			break

		#更新minNode周边点的数据(八方向)
		dir = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
		openUpdate = False # open中是否有数据更新
		for i in range(0,8):
			newRow = minNode.row + dir[i][0]
			newCol = minNode.col + dir[i][1]
			if newCol < 0 or newCol >= maxCol or newRow < 0 or newRow >= maxRow: # 超出地图
				pass
			elif 1 == map[newRow][newCol]:  # 地图阻挡物
				pass
			elif newRow in closeDict and newCol in closeDict[newRow]: # 在close中
				pass
			elif newRow in openDict and newCol in openDict[newRow]: # 在open中
				newG = (minNode.g + ZXDJ) if 1 == abs(dir[i][0]+dir[i][1]) else (minNode.g + XXDJ)
				if newG >= openDict[newRow][newCol]:
					pass
				else:
					openDict[newRow][newCol].parent = minNode
					openDict[newRow][newCol].g = newG;
					openDict[newRow][newCol].f = openDict[newRow][newCol].g + openDict[newRow][newCol].h
					openUpdate = True
			else: # 新的节点
				newNode = MyNode(newRow, newCol)
				newNode.parent = minNode
				newNode.g = (minNode.g + ZXDJ) if 1 == abs(dir[i][0]+dir[i][1]) else (minNode.g + XXDJ)
				newNode.h = (abs(newCol - endNode.col) + abs(newRow - endNode.row)) * ZXDJ
				newNode.f = newNode.g + newNode.h
				heapq.heappush(openHeap, newNode)
				if newRow not in openDict:
					openDict[newRow] = dict()
				openDict[newRow][newCol] = newNode

		#如果open中数据更新，则重构openHeap
		#效率?
		if openUpdate:
			tempheap = list()
			for node in openHeap:
				heapq.heappush(tempheap, node)
			openHeap = tempheap
		else:
			pass
	
	# 获取路径信息
	# 起点至终点 : path[len-1] -> path[0]
	path = list()
	if findPath:
		parent = closeDict[endNode.row][endNode.col]
		while parent != None:
			path.append((parent.row, parent.col))
			parent = parent.parent
	else:
		pass

	return findPath, path