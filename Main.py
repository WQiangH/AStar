# -*- coding: utf-8 -*-
import Astar


if __name__ == "__main__":
	map = [ [0,0,0,1,0,0,0,0],\
			[0,0,0,1,0,0,0,0],\
			[0,0,0,1,0,0,0,0],\
			[0,0,0,1,0,0,0,0],\
			[0,0,0,1,0,0,0,0],\
			[0,0,0,0,0,0,0,0],\
			[0,0,0,1,0,0,0,0],\
			[0,0,0,1,0,0,0,0]]
	startPoint = dict()
	startPoint['row'] = 0
	startPoint['col'] = 0

	endPoint = dict()
	endPoint['row'] = 7
	endPoint['col'] = 7

	findPath, path = Astar.AStar(startPoint, endPoint, map)
	print findPath
	if findPath:
		print path
	else:
		pass
