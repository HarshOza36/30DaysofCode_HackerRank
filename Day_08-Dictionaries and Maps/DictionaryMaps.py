# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
d={}
for i in range (0,n):
    k,v=input().split()
    d.update({k:v})

queries=[]
while(True):
    try:
        queries.append(input())
    except EOFError:
        break
    

for i in range(0,len(queries)):
    if(queries[i] in d):
        print("{}={}".format(queries[i],d[queries[i]]))
    else:
        print("Not found")
