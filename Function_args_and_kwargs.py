'''
#In this example we will see how to use *args and *kwargs

def sum_numbers(*custom):
    print(custom)
    return sum(custom)

result = sum_numbers(10,20,30,40,50)
print(result)

#User of **kwargs, it will return back dictionary
def func(**kwargs):
    print(kwargs)
func(Hello='Testing')

#Example - 2 for **kwargs
def kwargs_function(**kwargs):
    print(kwargs)
    if 'Fruit' in kwargs:
        print('Item {} found'.format(kwargs['Fruit']))
    else:
        print("Not found")
kwargs_function(Vegie='Maggie',Fruit='Apple',Other='Egg')
'''
#Example 3- Here we can pass *args and **kwargs
def args_with_kwargs(*args,**kwargs):
    print(args)
    print(kwargs)
    print("My name is {} and my age is {}".format(kwargs['Emp3'],args[1]))

args_with_kwargs(21,34,50,Emp1='John',Emp2='Michel',Emp3='Vivek')