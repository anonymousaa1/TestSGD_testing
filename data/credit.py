import numpy as np
import sys
sys.path.append("../")

def credit_data():
    """
    Prepare the data of dataset German Credit
    :return: X, Y, input shape and number of classes
    """
    print("-->credit_data:")
    X = []
    Y = []
    i = 0

    with open("../dataset/credit_sample", "r") as ins:
        for line in ins:
            line = line.strip()
            line1 = line.split(',')
            if (i == 0):
                i += 1
                continue
            L = list(map(int, line1[:-1]))
            X.append(L)
            if int(line1[-1]) == 0:
                Y.append([1, 0])
            else:
                Y.append([0, 1])

    X = np.array(X, dtype=float)
    Y = np.array(Y, dtype=float)

    input_shape = (None, 20)
    nb_classes = 2

    print(X, Y, input_shape, nb_classes)
    return X, Y, input_shape, nb_classes