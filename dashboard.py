import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv('Acidentes_MG_v1.csv', delimiter=';')

# Função para converter colunas de data e hora
def convert_to_datetime(df):
    df['ano_acidente'] = df['ano_acidente'].astype(str)
    df['mes_acidente'] = df['mes_acidente'].astype(str).str.zfill(2)
    df['dia_acidente'] = df['dia_semana'].astype(str).str.zfill(2)
    df['data_acidente'] = pd.to_datetime(df['ano_acidente'] + '-' + df['mes_acidente'] + '-' + df['dia_acidente'])
    return df

df = convert_to_datetime(df)

# Configurar o layout do Streamlit
st.set_page_config(layout="wide")

# Título do dashboard
st.title('Análise de Acidentes de Trânsito em MG')

# Sidebar para filtros
st.sidebar.header('Filtros')
anos = st.sidebar.multiselect('Ano do Acidente', options=df['ano_acidente'].unique(), default=df['ano_acidente'].unique())
meses = st.sidebar.multiselect('Mês do Acidente', options=df['mes_acidente'].unique(), default=df['mes_acidente'].unique())
tipos_acidente = st.sidebar.multiselect('Tipo de Acidente', options=df['tp_acidente'].unique(), default=df['tp_acidente'].unique())

# Filtrar os dados com base na seleção do usuário
df_filtered = df[(df['ano_acidente'].isin(anos)) & (df['mes_acidente'].isin(meses)) & (df['tp_acidente'].isin(tipos_acidente))]

# Análise de Categorias
st.header('Análise de Categorias')
fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(data=df_filtered, x='tp_acidente', order=df_filtered['tp_acidente'].value_counts().index, ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)

# Análise de Série Temporal
st.header('Análise de Série Temporal')
fig, ax = plt.subplots(figsize=(10, 5))
df_filtered.groupby('data_acidente').size().plot(ax=ax)
ax.set_title('Número de Acidentes por Data')
ax.set_xlabel('Data')
ax.set_ylabel('Número de Acidentes')
st.pyplot(fig)

# Tabela de Dados Filtrados
st.header('Dados Filtrados')
st.dataframe(df_filtered)
