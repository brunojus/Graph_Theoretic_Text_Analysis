import networkx as nx
import matplotlib.pyplot as plt
import heapq

def wordsByDegreeCentrality(G):
	"""
	From a generated co-occurence graph, this returns sorted the highest and lowest
	15 words ranked on the basis of Degree Centrality.
	"""

	c=nx.degree_centrality(G)

	hola=[]
	for w in c:
		hola.append((c[w],w))
	hola.sort()

	print("\n\nDEGREE CENTRALITY :")
	print("-------------------")

	print("Lowest 15 :")
	for i in range(0,15):
		print(hola[i][1],end="  ")

	print("\n\nHighest 15 :")
	for i in range(len(hola)-1,len(hola)-1-15,-1):
		print(hola[i][1],end="  ")

	print()

	# print(c["holmes"])

	# sort()
	# nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')

	# li=[]
	# for word in st:
	# 	li.append(word)
	# 	# print(word)
	# # print(li)

	# heapq.heapify(li)

	# print(heapq.nlargest(10,li))
	# # for i in range(0,10):
	# 	# print(heapq.heappop(li))
