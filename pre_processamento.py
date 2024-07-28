import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("Acidentes_DadosAbertos_20240612_Copia.csv", sep=";")

# Função para formatar a hora
def formatar_hora(hora_str):
    if pd.isnull(hora_str):
        return hora_str
    hora_str = str(hora_str).zfill(6)
    horas = hora_str[:2]
    minutos = hora_str[2:4]
    segundos = hora_str[4:6]
    return f"{horas}:{minutos}:{segundos}"

dataset_MG = dataset[dataset['uf_acidente'] == 'MG']
dataset_MG = dataset_MG.iloc[:850000]
dataset_MG['hora_acidente'] = dataset_MG['hora_acidente'].apply(formatar_hora)

dataset_MG.to_csv("Acidentes_MG.csv", index=False, sep=';')