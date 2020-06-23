# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(0, n):
    inpstr = input()
    print(inpstr[::2],inpstr[1::2])
