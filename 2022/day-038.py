from abc import ABCMeta, abstractmethod


class Person:
    """请假申请人"""

    def __init__(self, name, dayoff, reason):
        self.__name = name
        self.__dayoff = dayoff
        self.__reason = reason
        self.__leader = None

    def get_name(self):
        return self.__name

    def get_dayoff(self):
        return self.__dayoff

    def get_reason(self):
        return self.__reason

    def set_leader(self, leader):
        self.__leader = leader

    def request(self):
        print('{} 申请请假 {} 天，原因是 {}'.format(self.__name, self.__dayoff, self.__reason))
        if self.__leader is not None:
            self.__leader.response(self)


class Manager:
    """请假申请人的上级审批"""

    def __init__(self, name, title):
        self.__name = name
        self.__title = title
        self._next_handler = None

    def get_name(self):
        return self.__name

    def get_title(self):
        return self.__title

    def set_next_handler(self, handler):
        self._next_handler = handler

    @abstractmethod
    def response(self, person):
        if person.get_dayoff() <= 2:
            print('{} 的请假申请已通过'.format(person.get_name()))
        else:
            print('{} 的请假申请已拒绝'.format(person.get_name()))


class SuperVisor(Manager):
    """主管"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def response(self, person):
        if person.get_dayoff() <= 5:
            print('{} 的请假申请已通过'.format(person.get_name()))
        if self._next_handler is not None:
            self._next_handler.response(person)


class DepartmentManager(Manager):
    """部门经理"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def response(self, person):
        if person.get_dayoff() <= 10:
            print('{} 的请假申请已通过'.format(person.get_name()))
        if self._next_handler is not None:
            self._next_handler.response(person)


class CEO(Manager):
    """CEO"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def response(self, person):
        if person.get_dayoff() <= 15:
            print('{} 的请假申请已通过'.format(person.get_name()))
        if self._next_handler is not None:
            self._next_handler.response(person)


class Administrator(Manager):
    """行政人员"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def response(self, person):
        print('{} 的请假申请已通过，情况属实！已备案处理。处理人{}({})\n'.format(person.get_name(), self.get_name(), self.get_title()))


def test_ask_for_leave():
    direct_leader = SuperVisor('张三', '客户端研发部经理')
    department_leader = DepartmentManager('李四', '技术研发中心总监')
    ceo = CEO('王五', '总经理')
    administrator = Administrator('赵六', '行政中心总监')
    direct_leader.set_next_handler(department_leader)
    department_leader.set_next_handler(ceo)
    ceo.set_next_handler(administrator)

    person = Person('张三', 2, '因为爱情原因')
    person.set_leader(direct_leader)
    person.request()

    tony = Person('Tony', 15, '家里有紧急事情！！')
    tony.set_leader(direct_leader)
    tony.request()

    pony = Person('Pony', 20, '出国深造')
    pony.set_leader(direct_leader)
    pony.request()


if __name__ == '__main__':
    test_ask_for_leave()
