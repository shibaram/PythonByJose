import math


def check_prime(num):
    #sqroot_of_num = math.sqrt(num)
    # print(f"Square root of num {num} is : {sqroot_of_num}")
    for n in range(2, num):
        if num % n == 0:
            # print(f"{num} is not a prime number")
            return False
            # break
    else:
        # print(f"{num} is a prime number")
        return True


maxnum = int(input("Please provide a number to check prime numbers \nfrom 1 to upto this number : "))
prime_num_list = []
for n in range(2, maxnum):
    if check_prime(n):
        prime_num_list.append(str(n))

prime_num_list_as_str = ", ".join(prime_num_list)
print(f"Prime numbers found between 1 to {maxnum} are: {prime_num_list_as_str}")
