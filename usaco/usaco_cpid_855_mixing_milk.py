import sys 

sys.stdin = open("mixmilk.in","r")
sys.stdout = open("mixmilk.out","w")

buckets = [list(map(int, input().split())) for i in range(3)]
f,t = 0,1

def pour(bucket_from, bucket_to):
    if buckets[bucket_from][1]+buckets[bucket_to][1] > buckets[bucket_to][0]:
        buckets[bucket_from][1] -= buckets[bucket_to][0] - buckets[bucket_to][1] 
        buckets[bucket_to][1] = buckets[bucket_to][0]
    else:
        buckets[bucket_to][1] += buckets[bucket_from][1]
        buckets[bucket_from][1] = 0
for i in range(100):  
    pour(f,t)
    f,t = (f+1)%3, (t+1)%3
print(f"{buckets[0][1]}\n{buckets[1][1]}\n{buckets[2][1]}")
