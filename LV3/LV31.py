import pandas as pd
import numpy as np

mtcars = pd.read_csv('C:\\Users\\lukal\\Desktop\\LV3\\mtcars.csv')

print(mtcars.sort_values(by='mpg').head(5))
print(mtcars[mtcars.cyl == 8].sort_values(by='mpg').tail(3))

cyl6 = mtcars[mtcars.cyl == 6]
cyl6 = cyl6.iloc[:,1:2]
print(cyl6.mean())

car1 = mtcars[(mtcars.cyl == 4) & (mtcars.wt > 2.000) & (mtcars.wt <2.200 )] 
car1 = car1.iloc[:,1:2]
print(car1.mean())

manual = 0
automatik = 0
vrsta = mtcars.sort_values(by='am')
for car in vrsta.am:
    if(car == 0):
        manual += 1

    elif(car == 1):
     automatik += 1
    
print('automatika ima ' , automatik , 'manualaca ima', manual)

car6 = (mtcars[(mtcars.am == 1) & (mtcars.hp > 100)])
print('ima ih' ,len(car6))

car_kg = ([(mtcars.wt *1000 / 2.20462262)])
print(car_kg) 