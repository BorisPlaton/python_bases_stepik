import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):

    def append(self, element):
        self.log(element)
        super().append(element)
