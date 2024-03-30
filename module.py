# 파일명: module.py
PI = 3.14

def dir2(obj):
    attr_list = []
    for attr in dir(obj):
        if attr[0] != '_':
            attr_list.append(attr)
    return attr_list

class FourCal:
    def setdata(self, first, second):
        self.first  = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
