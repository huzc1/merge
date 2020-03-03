
class School():
    def __init__(self, city, course, code):
        self.city = city
        self.course = course
        self.code = code
        self.teachers_list = []
        self.students_list = []

    def hire(self, obj):
        print('招聘到老师{}'.format(obj.name))
        self.teachers_list.append(obj.name)
        print(self.teachers_list)

    def enroll(self, name):
        print('招生到学习{}'.format(name))
        self.students_list.append(name)
        print(self.students_list)


class Teacher(School):
    def __init__(self, city, course, code, name, sex):
        super(Teacher, self).__init__(city, course, code)
        self.name = name
        self.sex = sex

    def teach(self):
        print('我叫{}在{}教{}第{}期课程'.format(self.name, self.city, self.course, self.code))


hu = Teacher('bj', 'python', 3, 'huzc', 'f')
hu1 = Teacher('cd', 'linux', 1, 'aa', 'w')
hu.teach()
hu.hire(hu1)
hu.hire(hu)