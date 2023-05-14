import math


def softmax(a, b):
    return [(math.exp(a) / (math.exp(a) + math.exp(b))), (math.exp(b) / (math.exp(a) + math.exp(b)))]


def fn(x):
    global w
    return [(x * w[0] + w[2]), (x * w[1] + w[3])]


def dldwi(x, wi_index, w_index1, w_index2):
    global w
    h = 0.01
    w_h = w.copy()
    w_h[wi_index] = w[wi_index] + h

    return (math.log(1 + math.exp(x * w_h[w_index1] + w_h[w_index2])) -
            math.log(1 + math.exp(x * w[w_index1] + w[w_index2]))) / h


def gradient(x, wi_index):
    return dldwi((x[0]), wi_index, 1, 3) + dldwi((x[1]), wi_index, 0, 2)


def stupid_classifier(m0, m1):
    return [m0 / (m0 + m1), m1 / (m0 + m1)]


x = [-1, 1]
w = [0, 0, 0, 0]
h = 0.1

epochs = int(input("Enter the number of epochs: "))

for i in range(epochs):
    w[0] = w[0] - h * gradient(x, 0)
    w[1] = w[1] - h * gradient(x, 1)
    w[2] = w[2] - h * gradient(x, 2)
    w[3] = w[3] - h * gradient(x, 3)

    print("Iteration №" + str(i + 1) + ': w1 = ' + str(w[0]) + "; w2 = " + str(w[1]) +
          "; w3 = " + str(w[2]) + "; w4 = " + str(w[3]))

print("Probability of belonging to classes: \nY=0 \t\t\t\tY=1")
print(softmax(fn(x[0])[0], fn(x[0])[1]))
print(softmax(fn(x[1])[0], fn(x[1])[1]))

print("Stupid classifier results")
print(stupid_classifier(1, 1))
