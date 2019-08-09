# -*- coding:utf-8 -*-

#
# スタック、キュー
#
class StackQueueData():
    def __init__(self):
        self.data = list()

    def print(self):
        resString = ""
        for item in self.data:
            resString += str(item) + ':'
        return resString


#
# スタック
#
class StackData(StackQueueData):
    def __init__(self):
        self.data = list()

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if len(self.data) == 0:
            return ""
        else:
            return self.data.pop()


#
# キュー
#
class QueueData(StackQueueData):
    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if len(self.data) == 0:
            return ''
        else:
            return self.data.pop(0)


if __name__ == '__main__':
    testStackData = StackData()
    testStackData.push(1234)
    testStackData.push(1235)
    testStackData.push(1236)
    testStackData.push(1237)
    testStackData.push(1238)
    print(testStackData.pop())
    print(testStackData.pop())
    print(testStackData.print())

    testQueueData = QueueData()
    testQueueData.enqueue(3456)
    testQueueData.enqueue(3457)
    testQueueData.enqueue(3458)
    testQueueData.enqueue(3459)
    print(testQueueData.dequeue())
    print(testQueueData.dequeue())
    print(testQueueData.dequeue())
    print(testQueueData.print())
