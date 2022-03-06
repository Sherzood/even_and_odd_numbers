#A four-digit integer is given. Find the number of odd digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of odd digits in the variable "var_int".
var_int=1234
number1=var_int%10
var_int//=10
number2=var_int%10
var_int//=10
number3=var_int%10
number4=var_int//10
sum_odd_digits=number1%2+number2%2+number3%2+number4%2
print(sum_odd_digits)