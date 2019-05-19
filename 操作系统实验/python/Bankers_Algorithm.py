class Bankers_Algorithm:
    _flag = True
    _count = 0
    _processes = 4  # 进程数
    _types = 5  # 资源种类
    _allavailable = None  # 五种种资源的数量
    _allocation = None  # 分配矩阵
    _need = None  # 需求矩阵
    _max = None  # 最大需求矩阵
    _available = None  # 可利用资源向量
    _work = None
    _wordAndAllocation = None
    _finish = None

    # 初始化所有数据化
    def __init__(self):
        allavailable = [5, 6, 8, 6, 4]
        allocation = [[0, 2, 1, 1, 1], [2, 0, 1, 1, 1], [0, 1, 0, 1, 1], [0, 3, 1, 2, 0]]
        need = [[1, 0, 2, 1, 1], [0, 3, 2, 1, 0], [0, 3, 3, 2, 2], [1, 0, 1, 2, 1]]
        available = [0, 0, 0, 0, 0]
        max = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        work = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        wordAndAllocation = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        temp = [0, 0, 0, 0, 0]
        for i in range(self._processes):
            for j in range(self._types):
                temp[j] += allocation[i][j]
                max[i][j] = allocation[i][j] + need[i][j]  # 银行家之间算法的关系：Need[i, j]=Max[i, j]-Allocation[i, j]
        for i in range(self._types):
            available[i] = allavailable[i] - temp[i]
        self._allavailable = allavailable
        self._allocation = allocation
        self._need = need
        self._max = max
        self._available = available
        self._work = work
        self._wordAndAllocation = wordAndAllocation
        self._finish = [False, False, False, False]

    # 打印所有数据
    def _printAll(self):
        print('_allavailable:' + str(self._allavailable))
        print('_allocation' + str(self._allocation))
        print('_need' + str(self._need))
        print('_max' + str(self._max))
        print('_available' + str(self._available))
        print('_work' + str(self._work))
        print('_wordAndAllocation' + str(self._wordAndAllocation))
        print('_finish' + str(self._finish))

    # todo 实现银行家算法
    def _brank(self):
        return True

    # todo 实现安全性算法
    def _safe(self):
        return True

    # 外部调用
    def toWork(self):
        # self._printAll()
        if not self._brank():
            print('进制执行不符合银行家算法，系统不给予资源')
        else:
            if not self._safe():
                print('进程执行不安全，系统不能给予资源')
            else:
                print('进程可以执行，其执行顺序是：')


demo = Bankers_Algorithm()
demo.toWork()
