
import math
import numpy as np


def h(x):
	if x >= 1 or x <=0:return 0
	return -x * math.log2(x)

def data_entropy(labels):
	if len(labels) < 1 : return 0
	p = sum(labels) / len(labels)
	n = 1 - p
	return h(p)+ h(n)

def split_entropy(data, property_id, property_value):
	left_index = data[:, property_id] == property_value
	right_index = data[:, property_id] != property_value

	left_data = data[left_index,:]
	right_data = data[right_index,:]

	left_entropy = data_entropy(left_data[:, -1])
	right_entropy = data_entropy(right_data[:, -1])

	split_entropy=(left_data.shape[0] * left_entropy + right_data.shape[0]*right_entropy)/data.shape[0]

	return split_entropy, left_data, right_data

weather_data = np.array([
	[0,0,0,0,0],[0,0,0,1,0],[0,1,0,0,0],
	[0,2,1,0,1],[0,1,1,1,1],[1,0,0,0,1],
	[1,2,1,1,1],[1,1,0,1,1],[1,0,1,0,1],
	[2,1,0,0,1],[2,2,1,0,1],[2,2,1,1,0],
	[2,1,1,0,1],[2,1,0,1,0]])
