# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#%%

import networkx as nx
from networkx.utils import open_file

#import pandas as pd
import sys

def main(filepath):

    RES = nx.read_graphml(filepath)

    edges = RES.edges(data=True)
    nodes = RES.nodes(data=True)

    input_edges = []
    output_edges = []
    emission_edges = []

    # Extract edges with input, output and emission ratios
    for edge in edges:
        info_edge = edge[2]
        if 'input_ratio' in info_edge:
            input_edges.append(edge)
        if 'output_ratio' in info_edge:
            output_edges.append(edge)    
        if 'emission_ratio' in info_edge:
            emission_edges.append(edge)

    # Update the labels of nodes 
    for edge in input_edges:
        fuel_in = edge[2]['label']
        from_node = edge[0]
        RES.nodes[from_node]['label'] = fuel_in

    for edge in output_edges:
        from_node = edge[0]
        to_node = edge[1]
        fuel_out = RES.nodes[to_node]['label']
        RES.edges[from_node,to_node]['label'] = fuel_out
    
    for edge in emission_edges:
        from_node = edge[0]
        to_node = edge[1]
        emission = RES.nodes[to_node]['label']
        RES.edges[from_node,to_node]['label'] = emission


    # k=0    
    # for k in input_edg.index:
    #     fuel1 = input_edg[2]['label']
    #     a= input_edg[0][k]
    #     node=nds.loc[nds[0]==a]  
    #     node = node.reset_index(drop=True)
    #     x1=0
    #     for x1 in node.index:
    #         b=node[1][node.index[x1]]
    #         b['label']=fuel1
    #         x1=x1+1
    #     k=k+1

    # z=0    
    # for z in output_edg.index:
    #     c = output_edg[1][z]
    #     d = nds.loc[nds[0]==c]
    #     fuel2 = d[1][d.index[0]]['label']
    #     edge = output_edg.loc[output_edg[1]==c]
    #     edge = edge.reset_index(drop=True)
    #     x2=0
    #     for x2 in edge.index:
    #         e=edge[2][edge.index[x2]]
    #         e['label']=fuel2
    #         x2=x2+1
    #     edge2 = edg.loc[edg[1]==c] 
    #     edge2 = edge2.reset_index(drop=True)
    #     x3=0
    #     for x3 in edge2.index:
    #         f=edge2[2][edge2.index[x3]]
    #         f['label']=fuel2
    #         x3=x3+1
    #     z=z+1

    # y=0    
    # for y in emission_edg.index:
    #     g = emission_edg[1][y]
    #     h = nds.loc[nds[0]==g]
    #     emission = h[1][h.index[0]]['label']
    #     edge3 = emission_edg.loc[emission_edg[1]==g]
    #     edge3 = edge3.reset_index(drop=True)
    #     x4=0
    #     for x4 in edge3.index:
    #         m=edge3[2][edge3.index[x4]]
    #         m['label']=emission
    #         x4=x4+1
    #     edge4 = edg.loc[edg[1]==g]
    #     edge4 = edge4.reset_index(drop=True)
    #     x5=0
    #     for x5 in edge4.index:
    #         n=edge4[2][edge4.index[x5]]
    #         n['label']=emission
    #         x5=x5+1
    #     y=y+1


    # nds.to_dict()
    # edg.to_dict()


    # Write out the graph to a new file
    nx.write_graphml(RES, 'glucoseRES_modified,noDUMMY,v4_202010.graphml')

# %%
if __name__ == "__main__":
    main(sys.argv[1])

