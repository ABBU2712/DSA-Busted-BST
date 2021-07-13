from math import sqrt
max_size=1000000
decompose_size=1000

arr=[0]*max_size
block=[0]*decompose_size
blk_sz=0

def update(idx,val):
    blockNumber = idx // blk_sz
    block[blockNumber] += val - arr[idx]
    arr[idx] = val

def query(l, r):
    sum = 0
    while (l < r and l % blk_sz != 0 and l != 0):
         
        # traversing first block in range
        sum += arr[l]
        l += 1
     
    while (l + blk_sz <= r):
         
        # traversing completely overlapped blocks in range
        sum += block[l//blk_sz]
        l += blk_sz
     
    while (l <= r):
         
        # traversing last block in range
        sum += arr[l]
        l += 1
     
    return sum
     
# Fills values in input[]
def preprocess(input, n):
     
    # initiating block pointer
    blk_idx = -1
 
    # calculating size of block
    global blk_sz
    blk_sz = int(sqrt(n))
 
    # building the decomposed array
    for i in range(n):
        arr[i] = input[i];
        if (i % blk_sz == 0):
             
            # entering next block
            # incrementing block pointer
            blk_idx += 1;
         
        block[blk_idx] += arr[i]
 
 input= [1, 5, 2, 4, 6, 1, 3, 5, 7, 10]
n = len(input)
 
preprocess(input, n)
 
print("query(3,8) : ",query(3, 8))
print("query(1,6) : ",query(1, 6))
update(8, 0)
print("query(8,8) : ",query(8, 8))