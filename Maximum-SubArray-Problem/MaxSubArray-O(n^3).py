import random, time
#brute force algorithm
def MaxSubArray(array,n):
    maximum_sum=0
    global start_index, end_index
    for i in range(0,n):
        for j in range(i,n):
            current_sum=0
            for k in range(i,j+1):
                current_sum+=array[k]
            if current_sum>maximum_sum :
                maximum_sum=current_sum  
                start_index=i
                end_index=j
    return maximum_sum                         

randomlist =[  ]
for i in range(0,800):
    num = random.randint(-100,101)
    randomlist.append(num)
# print('The random array is',randomlist,'\n')

n=len(randomlist)
start = time.time()
m=MaxSubArray(randomlist,n)
end=time.time()
elapsed=end-start
print('The maximum sum is',m,'\n')
print('The indexes of SubArray are [{}] [{}]'.format(start_index,end_index),'\n')
print('Time elapsed is {:.6f}'.format(elapsed),'seconds')