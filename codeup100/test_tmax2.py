table1 = ["XOXO", "OXXO", "XXOX", "XOXO"]
table2 = ["OXXO", "XOXO", "XXOO"]
table3 = ["OXOXO", "OOOOO", "XOXOX"]

import numpy as np


def solution(table):

    num_table = []
    for c in table:
        numerical = np.array(list(map(ord, list(c))))
        numerical -= 79
        num_table.append(numerical)

    num_table = np.abs(np.array(num_table) - 9) // 9

    num_product = len(num_table)
    num_dis = len(num_table[0])
    status = np.array([0 for _ in range(num_dis)])

    while np.sum(status) != num_dis:
        where_hyeja = np.argmax(np.sum(num_table, axis=0))

        hyeja = np.sum(num_table[where_hyeja], axis=0)

        num_hyeja = np.where(np.sum(num_table, axis=0) == hyeja)

        if num_hyeja > 1:
            


        status = status + num_table[where_hyeja]
        # miss = np.where(status == 0)[0]
        num_table = np.delete(num_table, where_hyeja, 0)[:, miss]

        print(miss)
        print(num_table[:, miss])


solution(table1)