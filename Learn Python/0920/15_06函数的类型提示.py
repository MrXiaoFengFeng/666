
#类型提示。只是提示信息，不影响函数运行。：冒号后面接的是提示信息，=等号后面是范例。其实冒号后面写什么都行
def register(name:str='egon',age:int=16,hobbies:tuple=('eat',1))->int:
    print(name)
    print(age)
    print(hobbies)
    return 1111

register('tom',18,('play','music'))
print(register.__annotations__)