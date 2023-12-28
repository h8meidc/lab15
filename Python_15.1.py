import pandas as pd

df = pd.DataFrame({"Team1": [100,23,56],"Team2": [20,63,54],"Team3": [76,53,36],"Team4": [40,48,56],"Team5": [70,87,88],
         "Team6": [12,23,56],"Team7": [89,99,12],"Team8": [50,55,45],"Team9": [13,78,77],"Team0": [17,56,23]})

print(df)

print(df["Team1"])

print("Середнє значення очок Team1 = ", df["Team1"].mean())

print("Сума очок Team1 = ", df["Team1"].sum())
print(df["Team5"])
print("Середнє значення очок Team4 = ", df["Team4"].mean())

print("Сума очок Team4 = ", df["Team4"].sum())

if df["Team4"].sum() > df["Team1"].sum():
    print("Кількість очок у Team4 більша ніж у Team1")
else:
    print("Кількість очок у Team1 більша ніж у Team4")
max_points = df.sum().idxmax()
print(f"Команда з найбільшою кількістю очок це: {max_points} - ",df[max_points].sum())