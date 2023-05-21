def Fβ(β, precision, recall):
    result = (1 + β ** 2) * (precision * recall) / ((β ** 2 * precision) + recall)
    print(f"For β = {β}\nprecision = {precision}\nrecall = {recall}\nFβ = {result}\n")

# 1)
Fβ(2, 0.7, 0.8)
Fβ(2, 0.8, 0.7)
# 2)
Fβ(0.5, 0.7, 0.8)
Fβ(0.5, 0.8, 0.7)
