import os
import pandas as pd
import torch as tc
import numpy as np

if os.path.isfile("data\\2023.csv"):
    data = pd.read_csv("data\\2023.csv")
    data["class"] = np.where(data["class"].isnull() & ~data["pattern"].isnull(), data["pattern"], data["class"])
    data = data.drop(columns = ["pattern", "rating_band", "sex_rest", "dist", "dist_f","time","prize","owner","comment"])

split_loc = "data\\set"
if not os.path.exists(split_loc):
    os.makedirs(split_loc)

print(data.isna().sum())
