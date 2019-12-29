''''''
'''
装饰器 是一个闭包，即把一个函数当做参数然后返回一个替代版函数。
装饰器：模板
def outer(func):
    AAAA
    def inner():
        func()
    return inner
    
@outer
def foo():
    pass

-----------------------
@outer相当于foo = outer(foo)
    - 所以在 被装饰函数foo 定义好后，装饰器outer函数立即执行
    - 此时foo相当于inner，仅包含inner内函数体
    - AAA部分会被执行一次，在调用foo()时，AAA将不会被执行
    - 可能涉及到执行顺序的问题，搞清楚其foo = outer（foo）即可
-----------------------

在outer中使用闭包是为了在目标函数前后都可以运行其他功能代码
而不是只能在前面运行，而后return目标函数
'''

def dec1(func):
    print('11111111111111')
    def one():
        print('2222222222222')
        func()
        print('33333333333')
    return one


def dec2(func):
    print('aaaaaaaaaaaa')
    def one():
        print('bbbbbbbbbb')
        func()
        print('ccccccccccccc')
    return one

print('-----------start----------')
@dec1
@dec2
def test():
    print('test test')
# 相当于   test = dec1(dec2(text))
# 这里实际依次执行了dec2与dec1函数，可能会产生一些输出
print('------------end------------')

if __name__ == '__main__':
    print('------------------------')
    test()
    print('------------------------')
    test()
