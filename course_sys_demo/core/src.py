from core import admin, student, teacher

func_dic = {
    '1': admin.admin_view,
    '2': student.student_view,
    '3': teacher.teacher_view,
}


# 主视图
def run():
    while True:
        print(
            '''
            1.管理员功能
            2.学生功能
            3.老师功能
            '''
        )

        choice = input('请选择你的编号： ').strip()

        if choice not in func_dic:
            continue

        func_dic.get(choice)()
