# 选课系统
本周作业:综合应用面向对象
角色: 学校、学员、课程、讲师
    要求:
    1. 创建北京、上海 2 所学校
    2. 创建linux , python , go 3个课程 ， 
    linux\py 在北京开， go 在上海开
    3. 课程包含，周期，价格，建通过学校创课程
    4. 通过学校创建班级， 班级关联课程
    5.1 创建学员时，选择学校，关联班级
    5.2 创建讲师角色
    6. 提供两个角色接口
    6.1 学员视图， 可以注册， 交学费， 选择班级，
    6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 
    查看班级学员列表 ， 修改所管理的学员的成绩
    6.3 管理视图，创建讲师， 创建班级，创建课程
    7. 上面的操作产生的数据都通过pickle序列化保存到文件里
        - pickle
    
    
1、需求分析
    - 管理员功能
        - 管理员注册
        - 管理员登录
        - 创建学校
        - 创建班级（先选择校区）
            - 班级名称
            - 班级绑定的校区
        - 创建课程（课程绑定给班级，先选择班级）
            - 课程周期
            - 课程价格
        - 创建老师
            - 老师名称
            - 老师密码
    - 学生的功能
        - 注册
        - 登录
        - 交学费
        - 选择校区
        - 选择课程
        - 查看分数
    - 老师的功能
        - 登录
        - 查看授课课程
        - 选择授课课程
        - 查看课程下学生
        - 修改学生分数
        
    

2、程序的架构设计
    - ATM + 购物车
        - 三层架构
            - 视图层: 
                - 与用户交互的
                - 小的逻辑判断。例如注册功能两次密码是否一致校验
                - core
                    - src.py 主视图
                    - admin.py
                        - admin_view
                    - student.py
                        - student_view
                    - teacher.py
                        - teacher_view
            - 接口层: 
                - 核心的业务逻辑
                - interface
                    - admin_interface.py
                    - student_interface.py
                    - teacher_interface.py
            - 数据层: 处理数据的，增删改查
                - db
                    - models.py
                    - db_handler.py
                        - pickle 序列化保存
                        - pickle 反序列化查看
            
    - 选课系统  
        - 三层架构
            - 视图层: 与用户交互的
            - 接口层: 核心的业务逻辑
            - 数据层: 处理数据的，增删改查
                - pickle格式的数据
                    - bytes类型数据
                
                - Python
                    - 对象: ---> object
        
        
3、分任务开发
4、测试
5、上线






















