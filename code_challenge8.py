#fetch 10 numbers from the users
#get the summation of all the numbers

odd = 0
even = 0
sum = 0
for x in range (1, 11):
	num = eval(input(f"Enter #{x} :"))
	sum += num
	if num % 2 == 0:
		even += num
	else:
		odd += num

print(f"The sum of all the numbers given is {sum}.")
print(f"The sum of all the odd numbers given is {odd}.")
print(f"The sum of all the even numbers given is {even}.")






