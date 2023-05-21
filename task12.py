# 1 случай
precision = 0.7
recall = 0.8

F1 = 2 * (precision * recall) / (precision + recall)
print(F1)

# 2 случай
precision = 0.8
recall = 0.7

F1 = 2 * (precision * recall) / (precision + recall)
print(F1)

# Значение F1 не изменится при переставленных precision и recall.
