num = int(input("Enter any natural number : ")) 

if num >= 0 :

 summ = 0

 for i in range(0,num + 1) :

  summ = summ + i

 print("The sum is {}" .format(summ)) 

else:

 print("Kindly enter a Natural number")