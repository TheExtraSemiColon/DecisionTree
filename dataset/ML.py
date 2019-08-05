import csv
import numpy
import math
#import pandas as pd


#########Taking imn values#########
#readcsv=pd.read_csv('train.csv')
#print(readcsv.head(1))
#backtolist=readcsv.values.tolist()
#print(backtolist[0][0])
with open('train.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',', quotechar='|')
    #f1=[600][2]
	index=0
	#print(readCSV)
	# for rows in readCSV:
	# 	#print(row)
	# 	index=index+1


	N=577 #Number of trainig examples
	#print(index)
	w = 2 #
	h=N 
	k=8 # NUmber of attributes
	A=[[[0 for x in range(w)] for y in range(577)] for z in range(k)]
	# f1=[[0 for x in range(w)] for y in range(h)] 
	# f2=[[0 for x in range(w)] for y in range(h)]
	# f3=[[0 for x in range(w)] for y in range(h)]
	# f4=[[0 for x in range(w)] for y in range(h)]
	# f5=[[0 for x in range(w)] for y in range(h)]
	# f6=[[0 for x in range(w)] for y in range(h)]
	# f7=[[0 for x in range(w)] for y in range(h)]
	# f8=[[0 for x in range(w)] for y in range(h)]
	out=[[0 for x in range(w)] for y in range(577)]  #Output vector
	index=0 
	for row in readCSV:
		#print(row)
		if index>=1:

			A[0][index][0]=row[0]
			A[0][index][1]=index
			A[1][index][0]=row[1]
			A[1][index][1]=index
			A[2][index][0]=row[2]
			A[2][index][1]=index
			A[3][index][0]=row[3]
			A[3][index][1]=index
			A[4][index][0]=row[4]
			A[4][index][1]=index
			A[5][index][0]=row[5]
			A[5][index][1]=index
			A[6][index][0]=row[6]
			A[6][index][1]=index
			A[7][index][0]=row[7]
			A[7][index][1]=index
			out[index][0]=row[8]
			out[index][1]=index
			index=index+1

    





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

for m in range(8):
	
	for p in range(1,575):
		d=0
		for o in range(1,575):
			if A[m][o][0]>A[m][o+1][0]:
				temp=A[m][o+1][0]
				A[m][o+1][0]=A[m][o][0]
				A[m][o][0]=temp
				temp1=A[m][o+1][1]
				A[m][o+1][1]=A[m][o][1]
				A[m][o][1]=temp1
				d=d+1
		if d==0:
			break
#print(A[1])

def magic(q,A,t,N,Ni,out) : 
	#print(t)
	w = 2
	h=N
	k=8
	B=[[[0 for x in range(w)] for y in range(h)] for z in range(k)]
    
	#print(q)

	index_for_split_grand=0
	i_for_split=0
	mse_grand=1000000000000

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

			mse_total=100000000000000000
			mse_recent_total=10000000000000
			index_for_split=-1
			for d in range(1,Ni):
				#if B,[i][d][0]!=B[i][d-1][0]:
				counte=0 # counter starting from 1
				sume=0 # sum for calculating mean
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
				for f in range(d,Ni+1):
					countf=countf+1
					sumf= sumf + float(out[ B[i][f][1] ][0])
				if countf!=0:
					meanf=sumf/countf
				sqf=0
				msef=0
				for f in range(d,Ni+1):
						#counte=+1
					sqf=sqf+pow(meanf-float(out[B[i][f][1]][0]),2)
				if counte!=0:
					msef=math.sqrt(sqf/countf)

				mse_recent_total=counte*msee+countf*msef
				#print(mse_recent_total)
				if d!=1:
					
					if mse_total>mse_recent_total:
							
						mse_total=mse_recent_total
								# print(mse_total)
								# print(d)
								# print(i)
						index_for_split=d
						
								#print(d)





			# print('i=')
			# print(i)
			# print(index_for_split)
			# print('mse=')
			# print(mse_total)
			if mse_total<mse_grand:
				mse_grand=mse_total
				#print(mse_grand)
				#print(i)
				i_for_split=i
				index_for_split_grand=index_for_split


	# print(out[B[0][2][1]][0])
	# print(out[B[2][2][1]][0])
	# print(out[B[3][2][1]][0])
	# print(out[B[4][2][1]][0])

	u=t
	l=t
	#print(u)

	# print('i=')
	#print(i_for_split)
	#print(mse_grand)
	# print('value')
	# print(B[i_for_split][index_for_split_grand][0])
	for r in range(1,index_for_split_grand):
		l[B[i_for_split][r][1]]=0
	for r in range(index_for_split_grand,Ni+1):
		u[B[i_for_split][r][1]]=0


	q[i_for_split]=0
	w= [0,0,0,0,0,0,0,0]

	print(q)
	if Ni<20 or q==w:
		print('leaf node found')
		return



	magic(q,A,u,N,index_for_split_grand-1,out)
	#print('Hello')
	magic(q,A,l,N,Ni-index_for_split_grand ,out)





magic(q,A,t,N,N-1,out)













			














		 











