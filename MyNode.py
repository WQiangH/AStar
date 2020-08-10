# -*- coding: utf-8 -*-

class MyNode:
	def __init__(self, row, col):
		self.parent = None
		self.row = row
		self.col = col
		self.g = -1
		self.h = -1
		self.f = -1

	# 重载 pytho heapq 的比较函数
	def __lt__(self, myNode):
		return self.f < myNode.f
