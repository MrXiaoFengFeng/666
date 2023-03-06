# 多继承的正确打开方式：Mixins机制
# mixins机制核心：
# 1、就是在多继承背景下尽可能的提升多继承的可读性
# 2、让多继承满足人的思维习惯=》什么“是”什么

# 表达什么“是”什么的意思，放在继承的结尾
class Vehicle:  # 交通工具
    pass

# Mixin仅是单纯的表达混入功能的意思
class FlyableMixin:  # 可以飞行
    def fly(self):
        pass


class CivilAircraft(FlyableMixin, Vehicle):  # 民航飞机 表达什么“是”什么的意思，放在继承的结尾
    pass


class Helicopter(FlyableMixin, Vehicle):  # 直升飞机
    pass


class Car(Vehicle):  # 汽车并不会飞，但按照上述继承关系，汽车也能飞
    pass
