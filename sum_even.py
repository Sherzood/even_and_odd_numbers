#A four-digit integer is given. Find the sum of even digits in it.

#Create a variable "var_int" and assign it a four-digit integer value.
var_int=1234
number1=var_int%10
var_int//=10
number2=var_int%10
var_int//=10
number3=var_int%10
number4=var_int//10
#Create a variable "sum_even" and assign it 0.
sum_even=0
#Find the sum of the even digits in the variable "var_int".
sum_even_digits=number1-(number1*(number1%2))+number2-(number2*(number2%2))+number3-(number3*(number3%2))+number4-(number4*(number4%2))
