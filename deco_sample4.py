def deco_p(func):
    def wrapper(*args, **kwargs):
        res = '<p>'
        res = res + func(args[0], **kwargs)
        res = res + '</p>'
        return res
    return wrapper

@deco_p
def test(str):
    return str

print(test('Hello Decorator!'))