from itertools import chain, combinations
from openpyxl import load_workbook


def loadDataSet():
    result = []
    ws = load_workbook('商品订单.xlsx').worksheets[0]
    for index, row in enumerate(ws.rows):
        if index == 0:
            continue
        set1 = set(row[2].value.split('，'))
        result.append(set1)
    return result


def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if item not in C1:
                C1.append(item)
    C2 = sorted(map(lambda i: (i,), C1))
    return C2


def scanD(dataSet, Ck, Lk, minSupport):
    total = len(dataSet)
    supportData = {}
    for candidate in Ck:
        if Lk and (not all(map(lambda item: item in Lk, combinations(candidate, len(candidate) - 1)))):
            continue
        set_candidate = set(candidate)
        frequencies = sum(map(lambda item: set_candidate <= item, dataSet))
        sup = frequencies / total
        if sup >= minSupport:
            supportData[candidate] = sup
    return supportData


def aprioriGen(Lk, k):
    result = []
    for index, item1 in enumerate(Lk):
        for item2 in Lk[index + 1:]:
            if (sorted(item1[:k - 2]) == sorted(item2[:k - 2])):
                result.append(tuple(set(item1) | set(item2)))
    return result


def apriori(dataSet, minSupport):
    C1 = createC1(dataSet)
    supportData = scanD(dataSet, C1, None, minSupport)
    K = 2
    while True:
        Lk = []
        for key in supportData:
            if len(key) == K - 1:
                Lk.append(key)
        Ck = aprioriGen(Lk, K)
        supK = scanD(dataSet, Ck, Lk, minSupport)
        if not supK:
            break
        supportData.update(supK)
        K = K + 1
    return supportData


def findRules(supportData, minConfidence):
    supportDataS = sorted(supportData.items(), key=lambda item: len(item[0]), reverse=True)
    rules = []
    for index, pre in enumerate(supportDataS):
        for aft in supportDataS[index + 1:]:
            if len(aft[0]) < len(pre) - 1:
                break
            if set(aft[0]) < set(pre[0]) and pre[1] / aft[1] >= minConfidence:
                rules.append([pre[0], aft[0]])
    return rules


dataset = loadDataSet()
supportData = apriori(dataset, 0.4)

for item in findRules(supportData, 0.6):
    pre, aft = map(set, item)
    print(aft, pre - aft, sep='==>')
