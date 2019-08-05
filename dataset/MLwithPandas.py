import csv
import numpy
import math
import pandas as pd


#########Taking imn values#########
readcsv=pd.read_csv('train.csv')
#print(readcsv.head(1))
backtolist=readcsv.values.tolist()
#print(backtolist[0][0])
# with open('train.csv') as csvfile:
# 	readCSV = csv.reader(csvfile, delimiter=',', quotechar='|')
#     #f1=[600][2]
# 	index=0
# 	#print(readCSV)
# 	# for rows in readCSV:
# 	# 	#print(row)
# 	# 	index=index+1


# 	N=577
# 	#print(index)
# 	w = 2
# 	h=N
# 	k=8
# 	A=[[[0 for x in range(w)] for y in range(577)] for z in range(k)]
# 	# f1=[[0 for x in range(w)] for y in range(h)] 
# 	# f2=[[0 for x in range(w)] for y in range(h)]
# 	# f3=[[0 for x in range(w)] for y in range(h)]
# 	# f4=[[0 for x in range(w)] for y in range(h)]
# 	# f5=[[0 for x in range(w)] for y in range(h)]
# 	# f6=[[0 for x in range(w)] for y in range(h)]
# 	# f7=[[0 for x in range(w)] for y in range(h)]
# 	# f8=[[0 for x in range(w)] for y in range(h)]
# 	out=[[0 for x in range(w)] for y in range(577)]
# 	index=0
# 	for row in readCSV:
# 		#print(row)
# 		if index>=1:

# 			A[0][index][0]=row[0]
# 			A[0][index][1]=index
# 			A[1][index][0]=row[1]
# 			A[1][index][1]=index
# 			A[2][index][0]=row[2]
# 			A[2][index][1]=index
# 			A[3][index][0]=row[3]
# 			A[3][index][1]=index
# 			A[4][index][0]=row[4]
# 			A[4][index][1]=index
# 			A[5][index][0]=row[5]
# 			A[5][index][1]=index
# 			A[6][index][0]=row[6]
# 			A[6][index][1]=index
# 			A[7][index][0]=row[7]
# 			A[7][index][1]=index
# 			out[index][0]=row[8]
# 			out[index][1]=index

		
# 		index=index+1

    


















#print(out[3][0])
##########VALUE TAKEN AS INPUT#############

q = [1,1,1,1,1,1,1,1]
#print(q[3])

t=[1 for x in range(N)] 
#print(A)


#A=[f1,f2,f3,f4,f5,f6,f7,f8]

#print(A[0][0])

##########CREATING THE FUNCTION THAT FIRSTS ARRANGE IN INCREASING ORDER, THEN FINDS ATTRIBUTE TO SPLIT,##############
 # t is for keeping track of index which are used in that split while q is for attributes that are yet to be used

def magic(q,A,t,N,Ni,out) :

	w = 2
	h=N
	k=8
	B=[[[0 for x in range(w)] for y in range(h)] for z in range(k)]
    
	#print(A)

	index_for_split_grand=0
	i_for_split=0
	mse_grand=0

	for i in range(8):
		if q[i] ==1 :
			B[i][0][0]=A[i][0][0]
			B[i][0][1]=A[i][0][1]
			#print(B[i][0][0])
			u=0
			for j in range(1,N):
				if t[A[i][j][1]]==1:
					u=u+1
					B[i][u][0]=A[i][j][0]
					B[i][u][1]=A[i][j][1]

			mse_total=0
			mse_recent_total=0
			index_for_split=0
			for d in range(1,Ni):
				#if B,[i][d][0]!=B[i][d-1][0]:
				counte=0
				sume=0
				meane=0
				for e in range(1,d):
					counte=counte+1
					#print(out[B[i][e][1]][0])
					#print(type(out[B[i][e][1]][0]))
					sume=sume+float(out[B[i][e][1]][0])
				if counte!=0:
					meane=sume/counte
				sqe=0
				msee=0
				for e in range(1,d):
						#counte=+1
					#print(out[1][0])
					#print('*')
					#print(r)	
					sqe=sqe+pow(meane-float(out[B[i][e][1]][0]),2)
				if counte!=0:
					msee=math.sqrt(sqe/counte)


				countf=0
				sumf=0
				meanf=0
				for f in range(d,Ni):
					countf=countf+1
					sumf= sumf + float(out[ B[i][f][1] ][0])
				if countf!=0:
					meanf=sumf/countf
				sqf=0
				msef=0
				for f in range(d,Ni):
						#counte=+1
					sqf=sqf+pow(meanf-float(out[B[i][f][1]][1]),2)
				if counte!=0:
					msef=math.sqrt(sqf/countf)

				mse_recent_total=counte*msee+countf*msef
				#print(mse_recent_total)
				if mse_total<mse_recent_total:
					mse_total=mse_recent_total
					index_for_split=d





			if mse_total>mse_grand:
				mse_grand=mse_total
				i_for_split=i
				index_for_split_grand=index_for_split

	u=t
	l=t
	# print('i=')
	# print(i_for_split)
	# print('value')
	# print(B[i_for_split][index_for_split_grand][0])
	for e in range(1,index_for_split_grand):
		l[B[i_for_split][e][1]]=0
	for e in range(index_for_split_grand,Ni):
		u[B[i_for_split][e][1]]=0


	q[i_for_split]=0
	w= [0,0,0,0,0,0,0,0]

	#print(q)
	if Ni<300 :
		print('leaf node found')
		return



	magic(q,B,u,N,index_for_split_grand-1,out)
	magic(q,B,l,N,Ni-index_for_split_grand ,out)




magic(q,A,t,N,N-1,out)


