import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
# coo=np.loadtxt('coor.txt',dtype=str,delimiter=' ')
# print(coo)
net=sumolib.net.readNet('Base\DCC.net.xml')
# all_edge=net.getEdges() #所有的边
# for edge in all_edge:
#     edge_to_node = edge.getToNode()
#     end_ID = edge_to_node.getID()
#     edge_from_node=edge.getFromNode()
#     begin_ID=edge_from_node.getID()
#
#     with open('edge.txt','a') as f:
#         f.writelines('{begin},{end}\n'.format(begin=begin_ID,end=end_ID))

all_edge=np.loadtxt('edge.txt',dtype=str,delimiter=',')

all_node=net.getNodes() #所有节点信息
all_node_coor=[i.getCoord() for i in all_node]
all_node=[i.getID() for i in all_node]




G=nx.Graph()#创建空的无向图
'''
#先把节点加入网络中
G.add_nodes_from(all_node)
#再加坐标
G.add_edges_from(all_edge)
#绘制
nx.draw(G)
plt.show()
'''
#加入坐标
pos=dict(zip(all_node,all_node_coor))#将节点与其坐标映射关系储存到字典内
#绘制点
nx.draw_networkx_nodes(G,pos,all_node,node_size=2,node_shape='o')
#绘制边
nx.draw_networkx_edges(G,pos,all_edge)
#output
plt.show()