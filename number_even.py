#A four-digit integer is given. Find the number of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.

#Print the number of even digits in the variable "var_int".
var_int=1234
number1=var_int%10
var_int//=10
number2=var_int%10
var_int//=10
number3=var_int%10
number4=var_int//10
sum_even_digits=(1-number1%2)+(1-number2%2)+(1-number3%2)+(1-number4%2)
print(sum_even_digits)