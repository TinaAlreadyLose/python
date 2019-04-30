# coding:utf-8
# first come first server
# how to do
# 第一个进程的开始时间等于到达时间，
# 完成时间等于开始时间+完成时间，
# 周转时间等于完成时间-到达时间，
# 带圈周转时间=周转时间/服务时间
class FCFS:
    _number = int(input("请选择有几个进程\t"))
    _myList = []

    def todo(self):
        for i in range(self._number):
            templist = []
            comeTime = float(input("请输入第" + str(i) + "个作业的到达时间\t"))
            serverTime = float(input("请输入第" + str(i) + "个作业的服务时间\t"))
            templist.extend([comeTime, serverTime])
            self._myList.append(templist)
        print(self._myList)
        # first work
        comeTime = self._myList[0][0]
        serverTime = self._myList[0][1]
        beginTime = comeTime
        finishTime = beginTime + self._myList[0][1]
        turnoverTime = finishTime - beginTime
        weightedTurnoverTime = turnoverTime / serverTime
        self._myList[0].extend([beginTime, finishTime, turnoverTime, weightedTurnoverTime])
        # other word
        for i in range(1, self._number):
            lastFinishTime = self._myList[i - 1][3]
            comeTime = self._myList[i][0]
            serverTime = self._myList[i][1]
            beginTime = lastFinishTime
            finishTime = beginTime + serverTime
            turnoverTime = finishTime - comeTime
            weightedTurnoverTime = turnoverTime / serverTime
            self._myList[i].extend([beginTime, finishTime, turnoverTime, weightedTurnoverTime])
        print(self._myList)
        print('作业\t\t' + '到达时间\t' + '服务时间\t' + '开始时间 \t' + '完成时间 \t' + '周转时间\t' + '带权周转时间\t')
        for i in range(self._number):
            print(str(i + 1) + '\t\t' + str(self._myList[i][0]) + '\t\t' + str(self._myList[i][1]) + '\t\t' + str(
                self._myList[i][2]) + '\t\t' + str(self._myList[i][3]) + '\t\t' + str(
                self._myList[i][4]) + '\t\t' + str(
                self._myList[i][5]) + '\t\t')


x = FCFS()
x.todo();
