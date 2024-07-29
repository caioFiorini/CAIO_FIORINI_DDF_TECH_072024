import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.compose import ColumnTransformer


dataset = pd.read_csv("Acidentes_MG.csv",sep=';')

print(dataset.info())

label_encoder_uf_acidente = LabelEncoder()
label_encoder_dia_semana = LabelEncoder()
label_encoder_fase_dia = LabelEncoder()
label_encoder_tp_acidente = LabelEncoder()
label_encoder_end_acidente = LabelEncoder()
label_encoder_tp_rodovia = LabelEncoder()
label_encoder_cond_pista = LabelEncoder()
label_encoder_tp_cruzamento = LabelEncoder()
label_encoder_tp_pavimento = LabelEncoder()
label_encoder_tp_curva = LabelEncoder()
label_encoder_lim_velocidade = LabelEncoder()
label_encoder_tp_pista = LabelEncoder()

dataset.iloc[:, 0] = label_encoder_uf_acidente.fit_transform(dataset.iloc[:, 0])
dataset.iloc[:, 3] = label_encoder_dia_semana.fit_transform(dataset.iloc[:, 3])
dataset.iloc[:, 4] = label_encoder_fase_dia.fit_transform(dataset.iloc[:, 4])
dataset.iloc[:, 5] = label_encoder_tp_acidente.fit_transform(dataset.iloc[:, 5])
dataset.iloc[:, 6] = label_encoder_end_acidente.fit_transform(dataset.iloc[:, 6])
dataset.iloc[:, 8] = label_encoder_tp_rodovia.fit_transform(dataset.iloc[:, 8])
dataset.iloc[:, 9] = label_encoder_cond_pista.fit_transform(dataset.iloc[:, 9])
dataset.iloc[:, 10] = label_encoder_tp_cruzamento.fit_transform(dataset.iloc[:, 10])
dataset.iloc[:, 11] = label_encoder_tp_pavimento.fit_transform(dataset.iloc[:, 11])
dataset.iloc[:, 12] = label_encoder_tp_curva.fit_transform(dataset.iloc[:, 12])
dataset.iloc[:, 13] = label_encoder_lim_velocidade.fit_transform(dataset.iloc[:, 13])
dataset.iloc[:, 14] = label_encoder_tp_pista.fit_transform(dataset.iloc[:, 14])
OneHotEncoder_workType = ColumnTransformer(transformers = [('OneHot', OneHotEncoder(), [0])], remainder='passthrough')
OneHotEncoder_workType = ColumnTransformer(transformers = [('OneHot', OneHotEncoder(), [3,6])], remainder='passthrough')
OneHotEncoder_workType = ColumnTransformer(transformers = [('OneHot', OneHotEncoder(), [8,14])], remainder='passthrough')
dadosSemResposta = OneHotEncoder_workType.fit_transform(dataset)

dataset.to_csv("teste.csv", sep=';')