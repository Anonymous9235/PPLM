from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

BERT_rank = pd.read_csv("./data/BERT_ENS_euclidean_rank.csv")["rank"].values
PPLM_rank = pd.read_csv("./data/PPLM_ENS_euclidean_rank.csv")["rank"].values

plt.figure(figsize=(10, 10))
scales = [1, 3, 5, 10, 100]
idx = 0

all_y_euc_list = []

label = ["BERT", "PPLM"]
for rank_result in [BERT_rank, PPLM_rank]:
    y_euc_list = []
    total = len(rank_result)
    for s in scales:
        y_euc = len(np.where(rank_result <= s)[0])

        y_euc_list.append(y_euc/total)

    # plt.plot(scales, y_cos_list, color="blue", marker=".")
    if label[idx] == "PPLM":
        plt.plot(scales, y_euc_list, marker=".", label=label[idx], color="red")

    else:
        plt.plot(scales, y_euc_list, marker=".", label=label[idx])
             # , color = color[idx])

    all_y_euc_list.append(y_euc_list)

    idx+=1

plt.xscale('log')
plt.ylim(0,1)

plt.legend(loc=2, prop={"size":12})
plt.grid(linestyle="-.", alpha=0.6)
plt.show()
