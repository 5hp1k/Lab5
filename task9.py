# Валидационная выборка
x_val = [-0.5, 0.5]
y_val = [0.25, 0.25]

# Корни уравнения (|a-0.25|+|a-0.25|) / 2 = 0.05
a1 = 0.2
a2 = 0.3

FNN_x = [a1 for x in x_val]

MAE = sum([abs(fnn - y) for fnn, y in zip(FNN_x, y_val)]) / len(x_val)
print(MAE)
