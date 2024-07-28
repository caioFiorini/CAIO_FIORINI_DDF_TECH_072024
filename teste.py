import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("Acidentes_MG_v1.csv", sep=';')

for i in dataset.columns:
    print(dataset[i].value_counts())