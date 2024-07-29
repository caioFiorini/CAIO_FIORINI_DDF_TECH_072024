import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("Acidentes_MG_v1.csv", sep=";")

dataset_MG = dataset.drop(columns=['hora_acidente'])
dataset_MG = dataset_MG.iloc[:300000]


dataset_MG.to_csv("Acidentes_MG.csv", index=False, sep=';')