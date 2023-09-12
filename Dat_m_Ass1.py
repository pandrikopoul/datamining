import numpy as np

credit_data = np.genfromtxt('C:/Users/panos/Downloads/credit.txt', delimiter=',', skip_header=True)
array = np.array([1,0,1,1,1,0,0,1,1,0,1])

sorted = credit_data[credit_data[:,0].argsort()]
#print(sorted)

def impurity(arr):
     one = np.count_nonzero(arr==1)
     pZero = np.count_nonzero(arr==0)/len(arr)
     res = pZero*(1-pZero)

     return res

def bestsplit(attribute,clas): # mesures the quality of a numerical attribute for each of the split point

     attribute_sorted = np.sort(np.unique(attribute))

     len_of_sorted_atribute = len(attribute_sorted)
     income_splitpoints = (attribute_sorted[0:len_of_sorted_atribute-1] + attribute_sorted[1:len_of_sorted_atribute]) / 2 # find the split points

     totalIm = impurity(clas)
     # array to store all the slit points and their Quality score
     dtype = np.dtype([('SplitPoint', float), ('SplitQuality', float)])
     Split_Quality_array = np.array([], dtype=dtype)
    # print(income_splitpoints)
     for i in income_splitpoints:
         # print(i)
          imLowinput =clas[attribute < i]

          imHighinput = clas[attribute > i]

          proportion = len(imLowinput)/len(clas)
          proportion1 = len(imHighinput) / len(clas)

          impurityl=impurity(imLowinput)*proportion
          impurityh = impurity(imHighinput) *proportion1

          q= totalIm - (impurityl+impurityh)
          S_Q_A_Row = (i,q)
          Split_Quality_array= np.append(Split_Quality_array, np.array([S_Q_A_Row],dtype=dtype))
    # print(Split_Quality_array)
     max_quality= np.max(Split_Quality_array["SplitQuality"])
     bestsplitPoint = 0
   #  print(max_quality)
     for j in range(0, len(Split_Quality_array)):
          if Split_Quality_array["SplitQuality"][j] == max_quality : bestsplitPoint = Split_Quality_array["SplitPoint"][j]

    # print("This is the best Split point : " + str(bestsplitPoint))
     return  bestsplitPoint,max_quality


print("--------------------------------------------------------------")
max_fit = (0,bestsplit(credit_data[:,0],credit_data[:,5]))
for i in range(1,len(credit_data[0])-1):
     cur_fit = (i,bestsplit(credit_data[:,i],credit_data[:,5]))
     if (cur_fit[1][1] > max_fit[1][1]):
         max_fit = cur_fit
     print("Attribute in column : "+str(i)+" split point and quality :"+str(bestsplit(credit_data[:,i],credit_data[:,5])))

print("\nBEST choice Attribute in column : "+str(max_fit[0])+" split point and quality :"+str(max_fit[1]))

#x= credit_data
#y= class labels e.g. {1,1,0,0,0,1,1,1...}
#nmin = The minimum number of cases a non-leaf node should have in order to be able to be splited . if a node contains fewer cases than nmin, it becomes a leaf node.
#min leaf = The minimum number of cases a leaf node should have in order to be considered as a leaf node . If there is no split that meets the minleaf constraint, the node becomes a leaf node


#def attribute_Quality_calculator(attribute):
nmin=2
minleaf=1
#def tree_grow(x,y,nmin,minleaf,nfeat):






