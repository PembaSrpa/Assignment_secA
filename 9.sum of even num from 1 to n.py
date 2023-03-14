n=int(input('Enter a number:')) 
sum=0 
for x in range(2, n+1, 2): 
 sum =sum+x 
print ('Sum of all even numbers between 1 and ', n, ' is :', sum)