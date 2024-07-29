
import great_expectations as ge
import pandas as pd
from great_expectations.dataset.pandas_dataset import PandasDataset


# Carregue os dados
df = pd.read_csv('/mnt/c/Users/caiod/OneDrive/Documents/Caio/projetos_pessoais/dadosfera/Acidentes_MG_v1.csv')

# Crie um dataset do Great Expectations
data = PandasDataset(df)

# Defina as expectativas
data.expect_column_values_to_be_of_type('uf_acidente', 'str')
data.expect_column_values_to_be_of_type('ano_acidente', 'int')
data.expect_column_values_to_be_of_type('mes_acidente', 'int')
# Adicione outras expectativas conforme necessário

# Salve o resultado
batch = ge.dataset.PandasDataset(df)
batch.save_expectation_suite('my_expectations_suite')