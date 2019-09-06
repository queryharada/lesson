def deco2(func):
    import os
    def wrapper(*args,**kwargs):
        res = '--start--' + os.linesep
        res += func(*args,**kwargs) + '!' + os.linesep
        res += '--end--'
        return res
    return wrapper

@deco2
def test2():
    return('Hello Decorator')

print(test2())