# Enter your code here. Read input from STDIN. Print output to STDOUT
actual=str(input()).split(" ")
d1=int(actual[0])
m1=int(actual[1])
y1=int(actual[2])

expected=str(input()).split(" ")
d2=int(expected[0])
m2=int(expected[1])
y2=int(expected[2])

fine=0
if(y1>y2):
    fine=10000
elif(y1==y2):
    if(m1>m2):
        fine=(m1-m2)*500
    elif(m1==m2 and d1>d2):
        fine=(d1-d2)*15
print(fine)