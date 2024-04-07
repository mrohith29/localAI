def isPalindrome(num):

	n = num
	rev = 0

	while (num > 0):
		k = num % 10
		rev = (rev * 10) + k
		num = num // 10

	if (n == rev):
		return True
	else:
		return False


num = 9687

num = num + 1

# Loop checks all numbers from given no.
# (num + 1) to next palindrome no.
while (True):
	if (isPalindrome(num)):
		break
	num = num + 1

# printing the next palindrome
print("Next Palindrome :")
print(num)

# This code is contributed by sidharthsingh7898.
