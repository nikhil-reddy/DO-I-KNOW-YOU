import networkx as nx
G = nx.MultiDiGraph()

G.add_edge(0, 1, s_ij=0.4,c_ij=0)
G.add_edge(1, 0, s_ij=0.4,c_ij=0)
G.add_edge(1, 2, s_ij=0.6,c_ij=0)
G.add_edge(2, 1, s_ij=0.6,c_ij=0)
G.add_edge(2, 3, s_ij=0.5,c_ij=0)
G.add_edge(3, 2, s_ij=0.5,c_ij=0)
# G.add_edge('D', 'E', weight=6)
# G.add_edge('C', 'D', weight=5)
G.add_edge(2, 4, s_ij=0.4,c_ij=0)
G.add_edge(4, 2, s_ij=0.4,c_ij=0)
G.add_edge(0, 4, s_ij=0.6,c_ij=0)
G.add_edge(4, 0, s_ij=0.6,c_ij=0)
# print G[0][1][0]['c_ij']
# print G[1][2][0]['weight'] + G[0][1][0]['weight']
sor= 0
tar=3
print "Local Trust Values s_ij:"
for x in G:
	for y in G.successors(x):
		print x,y," = ", G[x][y][0]['s_ij']


#Calculating Global Trust Values by normalising the Local Trust Values
print "Global Trust Values c_ij :"
for x in G:
	sum=0
	for y in G.successors(x):
		sum+= G[x][y][0]['s_ij']

	for y in G.successors(x):
		G[x][y][0]['c_ij']=(G[x][y][0]['s_ij'])/sum

for x in G:
	for y in G.successors(x):
		print x,y , " = ",G[x][y][0]['c_ij']


#Calculating Transitive Trust Values t_ij
t_ij=0
for path in nx.all_simple_paths(G, source=sor, target=tar):
	i=0
	t=G[path[0]][path[1]][0]['s_ij']
	
	# print path
	for i in range(0,len(path)-1):
		t=t*G[path[i]][path[i+1]][0]['c_ij']
	# print t
		
	
	t_ij+=t

print "t_ij for ",sor,tar ," = ",t_ij