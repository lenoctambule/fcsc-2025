from pwn import *

REMOTE = "chall.fcsc.fr"
PORT = 2050

r = remote(REMOTE, PORT)

context.log_level = "debug"

def solve(arr):
    prev = arr[0]
    begin = 0
    end = 1
  
    for i in range(len(arr)):
        currSum = 0
        for j in range(i, len(arr)):
            currSum = currSum + arr[j]
            if currSum > prev :
                prev = currSum
                begin = i
                end = j
    return prev, begin, end

def maxSubarraySum(arr):
    if not arr:
        return 0, -1, -1  # Handle empty array case
    
    res = arr[0]
    maxEnding = arr[0]
    
    start = 0
    end = 0
    temp_start = 0  # temporary start index
    
    for i in range(1, len(arr)):
        if maxEnding + arr[i] > arr[i]:
            maxEnding = maxEnding + arr[i]
        else:
            maxEnding = arr[i]
            temp_start = i
        
        if maxEnding > res:
            res = maxEnding
            start = temp_start
            end = i
    return res, start, end

r.recvline()

for i in range(20):
    d = [int(i) for i in r.recvline().decode().split("=")[1].strip()[1:-1].split(",")]
    seed = d[0]
    n = d[1]
    N = d[2]
    random.seed(seed)
    A = [ random.randrange(-n, n) for _ in range(2 ** N) ]
    m, i, j = maxSubarraySum(A)

    r.sendlineafter(b">>> i = ", str(i).encode())
    r.sendlineafter(b">>> j = ", str(j + 1).encode())

r.recvall()