import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

mtcars = pd.read_csv('C:\\Users\\lukal\\Desktop\\LV3\\mtcars.csv')

sns.set(style="whitegrid")

plt.figure(figsize=(8, 6))
sns.barplot(x='cyl', y='mpg', data=mtcars, ci=None, palette='pastel')
plt.title('Prosječna potrošnja po broju cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Potrošnja (mpg)')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='cyl', y='wt', data=mtcars, palette='Set2')
plt.title('Distribucija mase automobila po broju cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Težina (wt - x1000 lbs)')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.boxplot(x='am', y='mpg', data=mtcars, palette='Set1')
plt.title('Potrošnja prema vrsti mjenjača')
plt.xlabel('Mjenjač (0 = automatski, 1 = ručni)')
plt.ylabel('Potrošnja (mpg)')
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(x='hp', y='qsec', hue='am', data=mtcars, palette='coolwarm', s=100)
plt.title('Ubrzanje vs. Snaga prema vrsti mjenjača')
plt.xlabel('Snaga (hp)')
plt.ylabel('Ubrzanje (qsec)')
plt.legend(title='Mjenjač', labels=['Automatski (0)', 'Ručni (1)'])
plt.tight_layout()
plt.show()
