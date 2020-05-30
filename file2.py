program:

#fibonaccci series

n=int(input("enter the number of sequence:"))
a=0
b=1
i=0
print(a)
print(b)
while(i<n):
 c=a+b
 print(c)
 a=b
 b=c
 i=i+1
 
 output:
 
 enter the number of sequence:18
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987

program:

#to print all positive numbers in a range

list1=[12,-7,5,64,-14]
print("input:",list1) 
for num in list1: 
    if num >= 0:      
       print("output:",num, end = " ")
output:

input: [12, -7, 5, 64, -14]
output: 12 output: 5 output: 64 

program:

#to print all positive numbers in a range

list1=[12,14,-95,3]
print("input:",list1) 
for num in list1: 
    if num >= 0:      
       print("output:",num, end = " ")
       
output:

   input: [12, 14, -95, 3]
   output: 12 output: 14 output: 3
       
       
       
 
