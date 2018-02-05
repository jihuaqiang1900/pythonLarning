def yanghui(L):
    n,arr,result=1,[1],[]
    while n<L:
        for i in range(len(arr)+1):
            print(i)
            if(i==0):
                result[0]=1
                print(result)
            else:
                result.append(arr[i]+arr[i+1])
                print(result)
        n+=1
        yield result

YANGHUI=yanghui(10)
print(YANGHUI)
for j in YANGHUI:
    next(j)
