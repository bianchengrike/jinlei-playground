from abc import ABCMeta, abstractmethod


class Request:
    """请求内容"""

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


class Responsible(metaclass=ABCMeta):
    """责任人抽象类"""

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

    def get_next_handler(self):
        return self._next_handler

    def handle_request(self, request):
        """处理请求"""
        # 当前责任人处理请求
        self.handle_request_impl(request)
        # 如果存在下一个责任人，则将请求传递（转交）给下一个责任人
        if self._next_handler is not None:
            self._next_handler.handle_request(request)

    @abstractmethod
    def handle_request_impl(self, request):
        """处理请求的具体实现"""
        pass
