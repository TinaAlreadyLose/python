class Bankers_Algorithm:
    _flag = True
    _count = 0
    _processes = 4  # 进程数
    _types = 5  # 资源种类
    _SecuredSequence = []  # 安全序列
    _useProcess = 0
    _allavailable = None  # 五种种资源的数量
    _allocation = None  # 分配矩阵
    _need = None  # 需求矩阵
    _max = None  # 最大需求矩阵
    _available = None  # 可利用资源向量
    _work = None
    _finish = None

    # 初始化所有数据化
    def __init__(self):
        allavailable = [5, 6, 8, 6, 4]
        allocation = [[0, 2, 1, 1, 1], [2, 0, 1, 1, 1],
                      [0, 1, 0, 1, 1], [0, 3, 1, 2, 0]]
        need = [[1, 0, 2, 1, 1], [0, 3, 2, 1, 0],
                [0, 3, 3, 2, 2], [1, 0, 1, 2, 1]]
        available = [0, 0, 0, 0, 0]
        max = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        work = [0, 0, 0, 0, 0]
        temp = [0, 0, 0, 0, 0]
        for i in range(self._processes):
            for j in range(self._types):
                temp[j] += allocation[i][j]
                # 银行家之间算法的关系：Need[i, j]=Max[i, j]-Allocation[i, j]
                max[i][j] = allocation[i][j] + need[i][j]
        for i in range(self._types):
            available[i] = allavailable[i] - temp[i]
        self._allavailable = allavailable
        self._allocation = allocation
        self._need = need
        self._max = max
        self._available = available
        self._work = work
        self._finish = [False, False, False, False]

    # 打印所有数据
    def _printAll(self):
        print('_allavailable:' + str(self._allavailable))
        print('_allocation' + str(self._allocation))
        print('_need' + str(self._need))
        print('_max' + str(self._max))
        print('_available' + str(self._available))
        # print('_work' + str(self._work))
        print('_finish' + str(self._finish))

    # 外部调用
    def toWork(self):
        # 
        # print(self._max)
        # self._printAll()
        # 是否符合银行家算法的规范
        if not self._brank():
            print('进制执行不符合银行家算法，系统不给予资源')
        else:
            # 是否符合安全行算法
            if not self._safe():
                print('进程执行不安全，系统不能给予资源')
            else:
                print('进程可以执行，其执行顺序是：' + str(self._SecuredSequence))

    # todo 实现银行家算法，符合返回true，反之false
    def _brank(self):
        request = [1, 0, 0, 0, 1]
        # request = []
        # for i in range(self._types):
        #     a = int(input("请输入request" + str(i) + "值:  "))
        #     request.append(a)
        # 1）如果Request i[j]≤Need[i, j]，转向步骤（2）；否则所需资源数已超过它所宣布的最大值。
        if not self._requestSmall(request, self._need[self._useProcess]):
            return False
        else:
            # 2）如果Requesti[j]≤Available[i, j]，转向步骤（3）；否则无足够资源，Pi需等待。
            if not self._requestSmall(request, self._available):
                return False
            else:
                # 系统试探着把资源分配给进程Pi，并修改下面数据结构中的数值：
                # Allocation[i, j]=Allocation[i, j]+Requesti[j]；
                # Need[i, j]=Need[i, j]-Requesti[j]；
                self._available = self._subtraction(self._available, request)
                self._need[self._useProcess] = self._subtraction(
                    self._need[self._useProcess], request)
                self._allocation[self._useProcess] = self._add(
                    self._allocation[self._useProcess], request)
                print('修改可利用资源向量为：' + str(self._available))
                print('修改需求矩阵为：' + str(self._need[self._useProcess]))
                print('修改分配矩阵为：' + str(self._allocation[self._useProcess]))
            return True

    # todo 实现安全性算法,安全返回true，反之false
    def _safe(self):
        count = 0
        while count < self._processes:
            flag = False  # 一次循环中找不到安全的状态，直接变为不安全，结束循环
            for i in range(self._processes):
                if not self._finish[i]:  # 只会去从没有执行过的地方执行
                    if count == 0:  # 开始的时候Work=Available
                        if self._requestSmall(self._need[i], self._available):
                            # print(self._need[i])
                            self._finish[i] = True  # 告诉程序此进程可以通过安全算法
                            self._work = self._add(self._available,
                                                   self._allocation[i])  # Work[j]=Work[j]+Allocation[i, j]；
                            count += 1
                            # print(self._work)
                            # print(i)
                            print(
                                '进程号\tWord\t\tNeed\t\tAllocation\tWork+Allocation\tFinish')
                            print(str(i)+'\t'+str(self._subtraction(self._work, self._allocation[i]))+'\t'+str(
                                self._need[i])+'\t'+str(self._allocation[i])+'\t'+str(self._work)+'\t'+str(self._finish[i]))
                            flag = True
                            self._SecuredSequence.append(i)  # 记录安全序列的值
                    else:
                        if self._requestSmall(self._need[i], self._work):
                            self._finish[i] = True  # 告诉程序此进程可以通过安全算法
                            self._work = self._add(self._work,  # debug
                                                   self._allocation[i])  # Work[j]=Work[j]+Allocation[i, j]；
                            count += 1
                            flag = True
                            # print(self._work)
                            # print(i)
                            print(str(i)+'\t'+str(self._subtraction(self._work, self._allocation[i]))+'\t'+str(
                                self._need[i])+'\t'+str(self._allocation[i])+'\t'+str(self._work)+'\t'+str(self._finish[i]))
                            self._SecuredSequence.append(i)  # 记录安全序列的值
            if not flag:
                return False
        return True

        # 比较两个列表每个的大小，第一个列表值都小于第二个列表的值返回ture，反之返回flase

    def _requestSmall(self, request, others):
        for i in range(self._types):
            if request[i] > others[i]:
                return False  # request 列表的元素有大于第二个的，直接结束
        return True

    # 返回两个列表每个元素相减的值
    def _subtraction(self, list1, list2):
        mylist = []
        for i in range(self._types):
            mylist.append(list1[i] - list2[i])
        return mylist

    # 返回两个列表每个元素相加的值
    def _add(self, list1, list2):
        mylist = []
        for i in range(self._types):
            mylist.append(list1[i] + list2[i])
        return mylist


demo = Bankers_Algorithm()
demo.toWork()
