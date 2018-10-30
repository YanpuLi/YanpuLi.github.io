# !python3
# https://www.python-course.eu/Decision_Trees.php
import pandas as pd
import numpy as np
from pprint import pprint

def entropy(target_col):
	'''
	func: calculate feature entropy
	paras: col
	return: entropy
	'''
	elements, counts = np.unique(target_col, return_counts = True)
	entropy = np.sum([(-counts[i]/np.sum(counts))*np.log2(counts[i]/np.sum(counts)) 
					   for i in range(len(elements))])
	return entropy

def InfoGain(data, split_attribute_name, target_name = 'class'):
	'''
	func: calculate the info gain for each feature
	paras: data, feature, target
	'''
	total_entropy = entropy(data[target_name])
	vals, counts = np.unique(data[split_attribute_name], return = True)

	weighted_Entropy = np.sum([(counts[i]/np.sum(counts))*entropy(data.where([split_attribute_name] == vals[i]).dropna()[target_name])
						for i in range(len(vals))])

	information_Gain = total_entropy - weighted_Entropy

	return information_Gain

def ID3(data, originaldata, features, target_attribute_name = 'class', parent_node_class = None):
	'''
	func: build ID3 tree
	paras: 
	'''
	# define stopping criteria: if one of the following is satisfied, return a leaf node
	# 1.if all target_values same, return this value
	if len(np.unique(data[target_attribute_name])) <=1:
		return np.unique(data[target_attribute_name])[0]
	# 2.if data is empty, return the mode target feature value in the original data
	elif len(data) == 0:
		return np.unique(originaldata[target_attribute_name])[np.argmax(np.unique(originaldata[target_attribute_name], return = True)[1])]
	# 3.if the feature space is empty, return the mode target feature value of the direct parent node
	#   the direct parent node is the one which has called the current run of the ID3 and hence the mode target feature value
	#   is stored in the parent_node_class variable
	elif len(feature) == 0:
		return parent_node_class
	# 4.if none the above hold true, grow the tree
	else:
		# set the default value for this node --> the mode target feature value of the current node
		parent_node_class = np.unique(data[target_attribute_name])[np.argmax(np.unique(data[target_attribute_name],
							return = True)[1])]
		# select the feature which best splits the data
		item_values = [InfoGain(data, feature, target_attribute_name) for feature in features]
		best_feature_index = np.argmax(item_values)
		best_feature = features[best_feature_index]

		# create the tree structure
		# gain in the 1st run
		tree = {best_feature:{}}

		# remove the feature with the best info gain from feature space
		features = [i for i in features if i != best_feature]

		# grow a branch under the root node for each possible value of the root node feature
		for value in np.unique(data[best_feature]):
			value = value
			sub_data = data.where(data[best_feature] == value).dropna()
			subtree = ID3(sub_data, data, features, target_attribute_name, parent_node_class)

			# add the sub tree, grown from the sub_dataset to the tree under the root node
			tree[best_feature][value] = subtree

		return tree

def predict(query, tree, default =1):
	'''
	func: predict a unseen query instance
	paras: query take the form as {'feature_name': values,...}; tree

	'''
	for key in list(query.keys()):
		if key in list(tree.keys()):
			try:
				result = tree[key][query[key]]
			except:
				return default
			result = tree[key][query[key]]
			if isinstance(result, dict):
				return predict(query, result)
			else:
				return result





































