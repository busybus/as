
# RA, 2017-11-04

# Statistics for Betti numbers of the random G_{n,p} graph

import networkx as nx
import numpy    as np

import topology_localcopy as topology

## Load the topology module
#import importlib.util as iu
#spec = iu.spec_from_file_location("topology", "../topology.py")
#topology = iu.module_from_spec(spec)
#spec.loader.exec_module(topology)

# INPUT
pass

# OUTPUT
output_file_stats = "gnpbetti-out.pkl"


# The highest Betti number rank that might occur
max_expected_betti = 9

# Computes average and std dev of Betti numbers
# for the G_{n,p} random graph over (runs) runs
def betti_av(n, p, runs) :
	print("n: {}, p: {}".format(n, p))
	
	B = np.zeros( (0, 1 + max_expected_betti) )
	
	for _ in range(0, runs) :
		G = nx.fast_gnp_random_graph(n, p)
		b = topology.betti(nx.find_cliques(G))
		# Append to B, padding with zeros
		B = np.vstack([B, b + ([0] * (B.shape[1] - len(b)))])

	return (np.mean(B, 0), np.std(B, 0))


# Number of nodes in the random graph
n = 19
# Number of runs for the statistic
runs = 10000
# Percentage of edges in G_{n,p}
P = [p/100 for p in range(1, 70)]

# Compute the Betti numbers as (average, stddev) for each p
MS = [betti_av(n, p, runs) for p in P]

# Separate the average
M = [B[0] for B in MS]
# Separate the standard deviation
S = [B[1] for B in MS]

# Write output
import pickle
data = {'M' : M, 'S' : S, 'n' : n, 'P' : P, 'runs' : runs}
pickle.dump(data, open(output_file_stats, "wb"))
