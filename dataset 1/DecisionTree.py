import csv
import numpy as np
import math
import pandas as pd
import timeit
import time
import matplotlib.pyplot as plt
#coun=1

#global tick_tock
#global coun
# class Node:
#     def __init__(self, val=0,attri='X1'):
#         self.left = Tree()
#         self.right = Tree()
#         self.value = val
#         self.attribute=attri
#         self.IsLeaf=False

#def write_output(pred):
    

class Tree:
    def __init__(self, val=0,attri='X1'):
        #self.root = None
        self.left = None
        self.right = None
        self.value = val
        self.attribute=attri
        self.IsLeaf=False


    # def getRoot(self):
    #     return self.root

    def add(self, val , attri):
        #if self.root == None:
        #self.root = Node(val, attri)
        self.value=val
        self.attribute=attri
        #else:
            #self._add(val, attri, self.root,flag)

    def predict_value(self,df):
    	if self.IsLeaf==True:
    		
    		#print (self.value)
    		x=self.value
    		#print(x)
    		return x
    	else:
    		if df[self.attribute]<self.value:
    			y=self.left.predict_value(df)
    			return y
    		else:
    			z=self.right.predict_value(df)		
    			return z





    

    def printTree(self):
        if self.IsLeaf==False:
            self.left._printTree()
            print ( str(self.value)+'  '+str(self.attribute) )
            self.right._printTree()
        else :
        	print('Leaf node  = ' + str(self.value))




def load_data(csv_file):

	df = pd.read_csv(csv_file)
	return df

def calc_var(data_framef,counterf,err_choice):
	
	#print(data_framef['output'])
	np_array=data_framef['quality'].values
	np_array1=np_array[:counterf]
	np_array2=np_array[counterf:np.size(np_array)]


	if err_choice=='mse':
		var=(counterf/np.size(np_array))*np.var(np_array1)+(np.size(np_array2)/np.size(np_array))*np.var(np_array2)


		return var
	if err_choice=='abs':
		#mean_n1=np.sum()
		var=(counterf/np.size(np_array))*np.sum(np.absolute(np.mean(np_array1)-np_array1))   +	(np.size(np_array2)/np.size(np_array))*np.sum(np.absolute(np.mean(np_array2)-np_array2)) 

		return var





def split(data_frame,tree,min_leaf_size,err_choice):


	var_min=float("inf")
	split_col='quality'
	split_index_min=0
	for col in data_frame:
		if col!='quality':
			data_frame=data_frame.sort_values(col)
			#print(data_frame)

			old=0
			counter=0
			var_col=float("inf")
			for element in data_frame[col]:
				if element!=old:
					var_elem=calc_var(data_frame,counter,err_choice)
					if var_elem<var_col:
						var_col=var_elem
						split_value=element
						split_index=counter

					
				counter=counter+1
				old=element

			#print(var_col)
			if var_col<var_min:
				var_min=var_col
				split_col=col
				split_element=split_value
				split_index_min=split_index

	#print(split_col)
	#print(data_frame.size)
	a=data_frame.shape
	if a[0]<min_leaf_size or split_col=='quality':
		#print('leaf node found')
		np_array=data_frame['quality'].values
		g=np.average(np_array)
		tree.IsLeaf=True
		tree.value=g
		#global tick_tock
		#tick_tock=tick_tock+1
		#global coun
		#coun[0]=coun[0]+1
		#coun=coun+1

		return 1
	data_frame=data_frame.sort_values(by=[split_col])
	data_frame=data_frame.drop(split_col,axis=1)

	tree.add(split_element,split_col)
	left_child=Tree()
	right_child=Tree()
	tree.left=left_child
	tree.right=right_child
	a=split(data_frame.iloc[ 0:split_index_min],left_child,min_leaf_size,err_choice)
	b=split(data_frame.iloc[split_index_min :],right_child,min_leaf_size,err_choice)
	return a+b


def main():


	df=load_data('train2.csv')



	min_leaf_para=[10,20,30,35,40,45,50,60,80,100,150,200]
	err_method='abs'
	tree=Tree()
	x_coordinate=[]
	error_plot=[]
	for elem in min_leaf_para:
		#tick_tock=0
		#coun=[0]
		cou=split(df,tree,elem,err_method)
		x_coordinate.append(cou)
		the_list=[]

		for index in range(df.shape[0]):
			y=abs(tree.predict_value(df.iloc[index])-df.iloc[index]['quality'])
		#print(y)
			the_list.append(y**2)
		#print(row)

		error_plot.append(math.sqrt(sum(the_list)/len(the_list)))

	plt.plot(x_coordinate,error_plot)
	plt.xlabel('no. of leaf nodes')
	plt.ylabel('Mean square error')
	plt.title('Error using abs on Dataset 2')
	plt.show()	


	# start=time.clock()
	# split(df,tree,min_leaf_para,err_method)
	# time_taken=time.clock()-start
	#print(time_taken)
	
	#tree.printTree()
	

	#df1=load_data('test.csv')
	#print(df1)
	# the_list=[]
	# for index in range(df.shape[0]):
	# 	y=abs(tree.predict_value(df.iloc[index])-df.iloc[index]['output'])
	# 	#print(y)
	# 	the_list.append(y**2)
	# 	#print(row)

	# error_plot=sqrt(sum(the_list)/len(the_list))


	# the_list_output=[]
	# for index in range(df1.shape[0]):
	# 	y=tree.predict_value(df1.iloc[index])
	# 	#print(y)
	# 	the_list_output.append(y)
	# #print(the_list)
	# with open('prediciton_final.csv', "w") as outfile:
	# 	outfile.write("ID")
	# 	outfile.write(",")
	# 	outfile.write('ouput')
	# 	outfile.write("\n")
	# 	index=1
	# 	for entries in the_list_output:
	# 		#print(entries)
	# 		outfile.write(str(index))
	# 		outfile.write(",")
	# 		outfile.write(str(entries))
	# 		outfile.write("\n")
	# 		index=index+1
	
	

if __name__=="__main__":
	main()






