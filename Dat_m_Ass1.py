import numpy as np
import binarytree as bt

# importing the data
#credit_data = np.genfromtxt('C:/Users/panos/Downloads/credit.txt', delimiter=',', skip_header=True)
credit_data = np.genfromtxt('C:/Users/panos/Downloads/credit.txt', delimiter=',', skip_header=True)
class Tree_Node:
    def __init__(self,x,current_impurity,split_point):
        self.current_data = x
        self.current_impurity = current_impurity
        self.split_point = (split_point.point, split_point.attribute_index)
        self.left = None
        self.right = None

def tree_grow(x, y, nmin, minleaf, nfeat):
    """
    Generating the "best" classification tree with the Gini-index impurity calculation
    :param x: (2-dimensional array) : Data matrix
    :param y: (1-dimensional binary array) : Class label
    :param nmin: (int) : Number of observations that a node must contain at least in order to be split
    :param minleaf: (int) : Number of observations required for a leaf node in order to become leaf
    :param nfeat: (int) : Number of features that should be considered for each split
    :return:
    (Tree type) :The generated tree
    """
    curr_class = y
    root_impurity= impurity(y)
    root = Tree_Node(x,root_impurity,)
    print(root)

    return


def tree_pred(x, tr) -> np.array(int):
    """
    Generating the class labels for the given data with the given tree
    :param x: (2-dimensional array) : Data matrix
    :param tr: (tree object) : A tree created with the function "tree_grow"
    :return:
    (1-dimensional binary array) :  predicted class labels for the cases in x
    """
    return


def impurity(curr_class) -> float:
    """
    Calculating the impurity of the current feature according to Gini-index
    :param curr_class: (1-dimensional float array) : The desire class
    :return:
    (float) : Returning the impurity of the given array
    """
    if len(curr_class) == 0:
        return 0
    zero_count = np.count_nonzero(curr_class == 0) / len(curr_class)
    current_impurity = zero_count * (1 - zero_count)
    return current_impurity


def best_split(attribute, cur_class):
    """
    Calculating the best possible split point for the current attribute with the corresponding classification
    :param attribute: (1-dimensional float array) : The candidate attribute
    :param cur_class: (1-dimensional float array) : The class distribution
    :return:
    (float) : The best split point for the candidate attribute
    (float) : The quality value of this point
    """
    sorted_attribute = np.sort(np.unique(attribute))
    len_sorted_attribute = len(sorted_attribute)
    possible_split_points = (sorted_attribute[0:len_sorted_attribute - 1] + sorted_attribute[
                                                                            1:len_sorted_attribute]) / 2
    total_impurity = impurity(cur_class)
    dtype = np.dtype([('split_point', float), ('split_quality', float)])
    split_quality_array = np.array([], dtype=dtype)
    len_cur_class = len(cur_class)

    # using the calculation for the current quality:
    # total quality = TQ, total impurity = TI,
    # impurity of before the split = IBS, proportion of before the split = PBS,
    # impurity of after the split = IAS, proportion of after the split = PAS
    # TQ = TI - ( (IBS) * (PBS) + (IAS) * (PAS) )
    # Searching for the best quality for the selection of the best split point
    for i in possible_split_points:
        impurity_arr_below_split_point = cur_class[attribute < i]
        impurity_arr_above_split_point = cur_class[attribute > i]
        proportion_below_split_point = len(impurity_arr_below_split_point) / len_cur_class
        proportion_above_split_point = len(impurity_arr_above_split_point) / len_cur_class
        impurity_below_split_point = impurity(impurity_arr_below_split_point) * proportion_below_split_point
        impurity_above_split_point = impurity(impurity_arr_above_split_point) * proportion_above_split_point
        cur_quality = total_impurity - (impurity_below_split_point + impurity_above_split_point)

        split_quality_array_row_data = (i, cur_quality)
        split_quality_array = np.append(split_quality_array, np.array([split_quality_array_row_data], dtype=dtype))
    best_quality = np.max(split_quality_array["split_quality"])
    best_split_point = 0
    # finding the corresponding split point to the best quality
    for i in range(0, len(split_quality_array)):
        if split_quality_array["split_quality"][i] == best_quality:
            best_split_point = split_quality_array["split_point"][i]
    return best_split_point, best_quality

print("--------------------------------------------------------------")
max_fit = (0,best_split(credit_data[:,0],credit_data[:,5]))
for i in range(1,len(credit_data[0])-1):
     cur_fit = (i,best_split(credit_data[:,i],credit_data[:,5]))
     if (cur_fit[1][1] > max_fit[1][1]):
         max_fit = cur_fit
     print("Attribute in column : "+str(i)+" split point and quality :"+str(best_split(credit_data[:,i],credit_data[:,5])))

print("\nBEST choice Attribute in column : "+str(max_fit[0])+" split point and quality :"+str(max_fit[1]))

#x= credit_data
#y= class labels e.g. {1,1,0,0,0,1,1,1...}
#nmin = The minimum number of cases a non-leaf node should have in order to be able to be splited . if a node contains fewer cases than nmin, it becomes a leaf node.
#min leaf = The minimum number of cases a leaf node should have in order to be considered as a leaf node . If there is no split that meets the minleaf constraint, the node becomes a leaf node


#def attribute_Quality_calculator(attribute):
nmin=2
minleaf=1
#def tree_grow(x,y,nmin,minleaf,nfeat):
hvgjvhjgk = tree_grow(credit_data,credit_data[:,5],0,0,0)
