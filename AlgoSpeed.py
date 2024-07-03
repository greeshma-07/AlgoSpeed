import random 
import time


# bubble sort
def bubble_sort():
    lst=numcreator()
    size=len(lst)
    for i in range(size):     
        for j in range(size-1):
            if lst[j]> lst[j+1]:
                lst[j+1], lst[j]=lst[j], lst[j+1]

#selection sort:

def selectionsort():
    lst=numcreator()
    size = len(lst)
    for i in range(size): #this loop will help us to choose min assumed values on left protion of the lst
        min_ind = i
        for j in range(i+1, size):
            if lst[min_ind]> lst[j]:
                min_ind = j
        lst[min_ind], lst[i] = lst[i], lst[min_ind]

#insertion sort:

def insertion():
    arr=numcreator()
    size= len(arr)
    for i in range(1, size): 
        j = i-1
        key = arr[i]
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j=j-1

        arr[j+1] = key


# Merge sort

def merge_sort(arr):
    if len(arr) <=1:
        return arr

    n = len(arr)
    mid = n//2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j <len(right):# this loop acutally prevents the comparison to go beyond the length of the either the left or right portion.
        if left[i]<right[j]:#checking if corresponding value at i in left is smaller or not 
            result.append(left[i])
            i+=1
        else:#checking if corresponding value at j in right is smaller or not 
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])

    return result

arr = [3,2,5,4,7,6,9,8,11,10]
print(f"The original List : {arr}")
print(f"The sorted list:  {merge_sort(arr)}")


#Quick Sort 

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[-1]
    left=[x for x in arr if x<pivot]
    mid=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]

    return quick_sort(left)+ mid+ quick_sort(right)



def numcreator():
    Numlst={}
    # for i in range(1000):
    # num= random.randint(0,1000)
    # Numlst.append(num)
    Numlst=[random.randint(0,1000) for _ in range(1000)]
    return Numlst

# Time taken by bubble sort:
BTT=0
for i in range(100):
    bubbleStime=time.time()
    bubble_sort()
    bubbleEtime=time.time()
    BTT=BTT+(bubbleEtime-bubbleStime)

#time taken by Selection Sort
Stt=0
for i in range(100):
    bubblesTime=time.time()
    selectionsort()
    bubbleeTime=time.time()
    Stt=Stt+(bubbleeTime-bubblesTime)
#time taken by Insertion Sort:
ITT=0
for _ in range(100):
    insertionStime=time.time()
    insertion()
    insertionEtime=time.time()
    ITT=ITT+(insertionEtime-insertionStime)

MST=0
for _ in range(100):
    mergeStart=time.time()
    merge_sort(numcreator())
    mergeEnd=time.time()    
    MST=MST+(mergeEnd-mergeStart)

QST=0
for _ in range(100):
    quickStime=time.time()
    quick_sort(numcreator())
    quickEtime=time.time()
    QST=QST+(quickEtime-quickStime)


# print(BTT/100)
# print(Stt/100)
# print(ITT/100)

# aBTT=BTT/100
# aStt=Stt/100
# aITT=ITT/100
# aMST=MST/100
aBTT, aStt, aITT, aMST, aQST= BTT/100, Stt/100, ITT/100, MST/100, QST/100

algorathim=[("bubble sort:", aBTT), ("Selection Sort:", aStt), ("Insertion Sort", aITT), ("Merge Sort", aMST), ("Quick SOrt", aQST)]
algorathim.sort(key =lambda x:x[1])
for i, (algo, time) in enumerate(algorathim):
    print(f"{i+1}: algorathim: {algo} : {time}")





