#One way to check
'''
def EvenCheck(num):
    result = num % 1 == 0
    print(result)

EvenCheck(20)

#another way
def EvenCheck(num):
    return num % 2 == 0
result = EvenCheck(21)
print(result)
#Return True if any number inside the list is even
def CheckEven(num_list):
    for num in num_list:
        if num % 2 == 0:
            return True
        else:
            pass
    return False

result = CheckEven([1,3,7,9])
print(result)
'''
#This section will return a list of even number
def create_even_list(num):
    even_list = []
    for number in num:
        if number % 2 == 0:
            even_list.append(number)
        else:
            pass
    return even_list

result = create_even_list([13,34,79,56,7,9,10])
print(result)


