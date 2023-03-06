# 一、多继承带来的菱形问题

class G:
    pass

class A(G):
    def test(self):
        print('from A')

class B(G):
    def test(self):
        print('from B')

class C(A):
    def test(self):
        print('from C')


class D(C, B):
    pass

print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>,
# <class '__main__.C'>, <class '__main__.A'>,
# <class '__main__.G'>, <class 'object'>]
# 取父类中的存在的第一顺位顺序
obj = D()  # from C
obj.test()




# 总结：类相关的属性查找（类名.属性，该类的对象.属性），都是参照该类的mro