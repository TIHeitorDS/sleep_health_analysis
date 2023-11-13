# %% [markdown]
# ### 1. Importando bibliotecas necessárias

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# ### 2. Importando o dataset

# %%
dataset = pd.read_csv('../dataset/Sleep_health_and_lifestyle_dataset.csv')
dataset['Sleep Disorder'] = dataset['Sleep Disorder'].fillna('None')

dataset

# %% [markdown]
# ### 3. Exibindo a distribuição dos ditúrbios do sono

# %%
sleep_disorder = dataset['Sleep Disorder'].value_counts()

plt.figure(figsize=(8, 8))

plt.pie(sleep_disorder,  autopct='%1.1f%%', startangle=90)
plt.title('Sleep disorder', loc='left')
plt.legend(sleep_disorder.index, title='Sleep disorder types')

plt.show()

# %% [markdown]
# ### 4. Distúrbios do sono por gênero

# %%
sleep_gender = dataset.groupby('Sleep Disorder')['Gender'].value_counts()
sleep_gender = sleep_gender.reset_index()

plt.figure(figsize=(8, 8))

sns.barplot(
    data=sleep_gender,
    x='Gender',
    y='count',
    hue='Sleep Disorder'
)

plt.title('Sleep disorder by gender')
plt.legend(title='Sleep disorder types')

plt.show()

# %% [markdown]
# No gráfico podemos perceber que:
# - Maior parte da quantidade de mulheres e homens não é afetada por algum distúrbio do sono.
# - A Apneia do sono afeta mais os homens.
# - A insônia afeta mais as mulheres.

# %% [markdown]
# ### 5. Distúrbio do sono por ocupação

# %%
sleep_occupation = dataset.groupby('Sleep Disorder')[
    'Occupation'].value_counts()
sleep_occupation = sleep_occupation.reset_index()

plt.figure(figsize=(8, 6))

sns.barplot(
    data=sleep_occupation,
    x='count',
    y='Occupation',
    hue='Sleep Disorder'
)

plt.title('Sleep disorder by on occupation')
plt.legend(title='Sleep disorder types')

plt.show()

# %% [markdown]
# - Vendedor e professor são as ocupações mais afetadas pela insônia.
# - Apneia do sono é mais presente em enfermeiros.
# - Engenheiros, médicos e advogados não sofrem de algum distúrbio do sono.
