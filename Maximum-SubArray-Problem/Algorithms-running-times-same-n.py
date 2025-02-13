import random,time
def MaxCrossingSubArray(array,low,middle,high):
    sum=0
    left_sum=0
    right_sum=0;   
    global start_index
    global end_index
    for i in range(middle,high+1):
        right_sum+=array[i]
        if right_sum>sum:
            sum=right_sum
            end_index=i

    for j in range(middle,low-1,-1):
        left_sum+=array[j]
        if left_sum>sum:
            sum=left_sum
            start_index=j

    return max(left_sum,right_sum,left_sum+right_sum-array[middle])      

def MaxSubArray_nlogn(array,low,high):
    maximum_sum=0
    if low==high: return array[low]
    middle=(low+high)//2
    return max(MaxSubArray_nlogn(array,low,middle),
               MaxSubArray_nlogn(array,middle+1,high),
               MaxCrossingSubArray(array,low,middle,high))

def MaxSubArray_n(array,n):
    current_max=array[0]
    maximum_sum=0
    pointer_index=0
    global start_index,end_index
    for i in range(0,n):
        current_max=max(array[i],current_max+array[i])
        if current_max>maximum_sum:
            maximum_sum=current_max
            start_index=pointer_index
            end_index=i
        if current_max<0:    
            pointer_index+=1
    return maximum_sum   

def MaxSubArray_n2(array,n):
    maximum_sum=0
    global start_index,end_index
    for j in range(0,n):
        current_sum=0
        for k in range(j,n):
            current_sum+=array[k]
            if current_sum > maximum_sum:
                maximum_sum=current_sum
                end_index=k
                start_index=j
    return maximum_sum    
def MaxSubArray_n3(array,n):
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
randomlist =[ ]
for i in range(0,1000):
    num = random.randint(-100,101)
    randomlist.append(num)
# print('The random array is',randomlist,'\n')

n=len(randomlist)

start_n = time.time()
m_n=MaxSubArray_n(randomlist,n)
end_n=time.time()
elapsed_n=end_n-start_n
print('Time elapsed for O(n) is ',elapsed_n,'seconds')

start_n2 = time.time()
m_n2=MaxSubArray_n2(randomlist,n)
end_n2=time.time()
elapsed_n2=end_n2-start_n2
print('Time elapsed for O(n^2) is',elapsed_n2,'seconds')

start_n3 = time.time()
m_n3=MaxSubArray_n3(randomlist,n)
end_n3=time.time()
elapsed_n3=end_n3-start_n3
print('Time elapsed for O(n^3) is',elapsed_n3,'seconds')

start_nlogn = time.time()
m_nlogn=MaxSubArray_nlogn(randomlist,0,n-1)
end_nlogn=time.time()
elapsed_nlogn=end_nlogn-start_nlogn
print('Time elapsed for O(nlogn) is',elapsed_nlogn,'seconds')