import json
import numpy as np

data = json.load(open("similarity.json", "r"))
file_out = open("network.txt", "w")
file_out.write(str(200) + " " + str(len(data)) + "\n")
weight_matrix = np.zeros([200, 200])
for val in data:
	weight_matrix[val["source"]][val["target"]] = val["value"]
for i in xrange(200):
	for j in xrange(i, 200):
		if weight_matrix[i][j] > 0:
			file_out.write(str(i) + " " + str(j) + " " + str(weight_matrix[i][j]) + "\n")
file_out.close()