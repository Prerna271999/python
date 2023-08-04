def prime_numbers(n):
    primes = []
    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i%j == 0:
                break
        else:
            primes.append(i)
    return primes

prime_list = prime_numbers(50)
print(prime_list)

# print user table
num = int(input("Enter a number: "))

print("Multiplication Table for {num}:")
for i in range(1, 11):
    result = num * i
    print(f"{num} * {i} = {result}")


#  Print palindrome string taking input as string
def is_palindrome(s):
    return s == s[::-1]


user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
# Take input as string and reverse it

user_input = input("Enter a string: ")

reversed_string = user_input[::-1]

print("Reversed string:", reversed_string)


