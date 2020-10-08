# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%
import networkx as nx
from networkx.utils import open_file

import pandas as pd


RES = nx.read_graphml('glucoseRES_modified,noDUMMY,v2_202009.graphml')
#%%
edg = pd.DataFrame(RES.edges(data=True))
nds = pd.DataFrame(RES.nodes(data=True))

# info_edg = edg[2][144]
# info_nds = nds[1][119]

#%%
input_edg=pd.DataFrame(columns=edg.columns)
output_edg=pd.DataFrame(columns=edg.columns)
emission_edg=pd.DataFrame(columns=edg.columns)

i=0
for i in edg.index:
    info_edge=edg[2][i]
    if 'input_ratio' in info_edge:
        input_edg=input_edg.append(edg.iloc[[i]], ignore_index=True)
    if 'output_ratio' in info_edge:
        output_edg=output_edg.append(edg.iloc[[i]], ignore_index=True)    
    if 'emission_ratio' in info_edge:
        emission_edg=emission_edg.append(edg.iloc[[i]], ignore_index=True)
    i=i+1


k=0    
for k in input_edg.index:
    fuel1=input_edg[2][k]['label']
    a= input_edg[0][k]
    node=nds.loc[nds[0]==a]  
    node = node.reset_index(drop=True)
    x1=0
    for x1 in node.index:
        b=node[1][node.index[x1]]
        b['label']=fuel1
        x1=x1+1
    k=k+1

z=0    
for z in output_edg.index:
    c = output_edg[1][z]
    d = nds.loc[nds[0]==c]
    fuel2 = d[1][d.index[0]]['label']
    edge = output_edg.loc[output_edg[1]==c]
    edge = edge.reset_index(drop=True)
    x2=0
    for x2 in edge.index:
        e=edge[2][edge.index[x2]]
        e['label']=fuel2
        x2=x2+1
    edge2 = edg.loc[edg[1]==c] 
    edge2 = edge2.reset_index(drop=True)
    x3=0
    for x3 in edge2.index:
        f=edge2[2][edge2.index[x3]]
        f['label']=fuel2
        x3=x3+1
    z=z+1

y=0    
for y in emission_edg.index:
    g = emission_edg[1][y]
    h = nds.loc[nds[0]==g]
    emission = h[1][h.index[0]]['label']
    edge3 = emission_edg.loc[emission_edg[1]==g]
    edge3 = edge3.reset_index(drop=True)
    x4=0
    for x4 in edge3.index:
        m=edge3[2][edge3.index[x4]]
        m['label']=emission
        x4=x4+1
    edge4 = edg.loc[edg[1]==g]
    edge4 = edge4.reset_index(drop=True)
    x5=0
    for x5 in edge4.index:
        n=edge4[2][edge4.index[x5]]
        n['label']=emission
        x5=x5+1
    y=y+1


nds.to_dict()
edg.to_dict()

#%%
RES = nx.DiGraph()
#RES.add_edges_from(edg)

for i in edg:
    RES.add_edge(edg[0][i], edg[1][i])
for j in nds:
    RES.add_node(nds[0][j])

#%%
#RES.add_nodes_from(edg)
#RES.add_nodes_from(nds)
#RESdata = nx.path_grap()
nx.write_graphml(RES, 'glucoseRES_modified,noDUMMY,v4_202010.graphml')

# %%
