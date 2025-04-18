import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1, 2, 3, 4, 5, 6), delimiter=",", skiprows=1)

mpg = data[:,0:1]
hp = data[:,3:4]
wt = data[:,5:6]
cyl = data[:,1:2]

plt.scatter(hp, mpg, s=wt * 50, alpha=0.7, edgecolors="k")
plt.title("Ovisnost potrošnje (mpg) o konjskim snagama (hp)")
plt.xlabel("Konjske snage (hp)")
plt.ylabel("Potrošnja (mpg)")
plt.grid(True)
plt.show()

min_mpg = np.min(mpg)
max_mpg = np.max(mpg)
mean_mpg = np.mean(mpg)
print(f"Minimalna potrošnja: {min_mpg}")
print(f"Maksimalna potrošnja: {max_mpg}")
print(f"Srednja potrošnja: {mean_mpg}")

mpg_6_cyl = mpg[cyl == 6]
min_mpg_6_cyl = np.min(mpg_6_cyl)
max_mpg_6_cyl = np.max(mpg_6_cyl)
mean_mpg_6_cyl = np.mean(mpg_6_cyl)
print(f"Minimalna potrošnja (6 cilindara): {min_mpg_6_cyl}")
print(f"Maksimalna potrošnja (6 cilindara): {max_mpg_6_cyl}")
print(f"Srednja potrošnja (6 cilindara): {mean_mpg_6_cyl}")
