import pandas as pd

min_conf = 0.3
K = 2


def apriori():
    data_set = load_data()
    C1 = create_C1(data_set)
    item_count = count_itemset1(data_set, C1)
    L1 = generate_L1(item_count)
    Lk_copy = L1.copy()
    L = []
    L.append(Lk_copy)
    for i in range(2, K + 1):
        Ci = create_Ck(Lk_copy, i)
        Li = generate_Lk_by_Ck(Ci, data_set)
        Lk_copy = Li.copy()
        L.append(Lk_copy)
    print('频繁项集\t支持度计数')
    support_data = {}
    for item in L:
        for i in item:
            print(list(i), '\t', item[i])
            support_data[i] = item[i]
    strong_rules_list = generate_strong_rules(L, support_data, data_set)
    strong_rules_list.sort(key=lambda result: result[2], reverse=True)
    print("\nStrong association rule\nX\t\t\tY\t\tconf")
    for item in strong_rules_list:
        print(list(item[0]), "\t", list(item[1]), "\t", item[2])


def load_data():
    df = pd.read_excel("商品订单.xlsx")
    data = df.values[:, [2]]
    data_set = []
    for i in range(len(data)):
        data_set.append(str(data[i])[2:len(str(data[i])) - 2].split('，'))
    return data_set


def create_C1(data_set):
    C1 = set()
    for t in data_set:
        for item in t:
            item_set = frozenset([item])
            C1.add(item_set)
    return C1


def count_itemset1(data_set, C1):
    item_count = {}
    for data in data_set:
        for item in C1:
            if item.issubset(data):
                if item in item_count:
                    item_count[item] += 1
                else:
                    item_count[item] = 1
    return item_count


def generate_L1(item_count):
    L1 = {}
    for i in item_count:
        if item_count[i] >= min_sup:
            L1[i] = item_count[i]
    return L1


def is_apriori(Ck_item, Lk_copy):
    for item in Ck_item:
        sub_Ck = Ck_item - frozenset([item])
        if sub_Ck not in Lk_copy:
            return False
    return True


def create_Ck(Lk_copy, k):
    Ck = set()
    len_Lk_copy = len(Lk_copy)
    list_Lk_copy = list(Lk_copy)
    for i in range(len_Lk_copy):
        for j in range(1, len_Lk_copy):
            l1 = list(list_Lk_copy[i])
            l2 = list(list_Lk_copy[j])
            l1.sort()
            l2.sort()
            if l1[0:k - 2] == l2[0:k - 2]:
                Ck_item = list_Lk_copy[i] | list_Lk_copy[j]
                if is_apriori(Ck_item, Lk_copy):
                    Ck.add(Ck_item)
    return Ck


def generate_Lk_by_Ck(Ck, data_set):
    item_count = {}
    for data in data_set:
        for item in Ck:
            if item.issubset(data):
                if item in item_count:
                    item_count[item] += 1
                else:
                    item_count[item] = 1
    Lk2 = {}
    for i in item_count:
        if item_count[i] >= min_sup:
            Lk2[i] = item_count[i]
    return Lk2


def generate_strong_rules(L, support_data, data_set):
    strong_rule_list = []
    sub_set_list = []
    for i in range(0, len(L)):
        for freq_set in L[i]:
            for sub_set in sub_set_list:
                if sub_set.issubset(freq_set):
                    sub_set_num = 0
                    for item in data_set:
                        if (freq_set - sub_set).issubset(item):
                            sub_set_num += 1
                    conf = support_data[freq_set] / sub_set_num
                    strong_rule = (freq_set - sub_set, sub_set, conf)
                    if conf >= min_conf and strong_rule not in strong_rule_list:
                        strong_rule_list.append(strong_rule)
            sub_set_list.append(freq_set)
    return strong_rule_list


# min_sup = int(len(load_data()) * min_conf)
min_sup = 1
apriori()

