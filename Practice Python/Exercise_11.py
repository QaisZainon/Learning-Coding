'''
Check if the number is a prime or not
'''
def prime_num():
    ans = []
    num = int(input('Give me a number\n'))
    for i in range(2, num):
        if num % i == 0:
            ans.append(i)
    if ans != []:
        print('This isn\'t a prime number')
    else:
        print('This is a prime number')

prime_num()