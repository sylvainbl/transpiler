#!/usr/bin/env python
# coding: utf-8


import numpy as np

from sklearn.linear_model import LinearRegression


x_train = np.random.randn(30, 2) * 1.5
y_train = np.random.randn(30) + 2 * x_train[:, 0] - 0.5 * x_train[:, 1]

x_train.shape, y_train.shape

model = LinearRegression()

model.fit(x_train, y_train)

print(model.coef_, model.n_features_in_)
print(model.coef_[1])


def generate(model):
    modelstr = "{"
    for feature in model.coef_:
        modelstr += str(feature) + ","
    modelstr = modelstr[:-1]
    modelstr += "}"

    code = '#include <stdio.h>\n\n\
float linear_regression_prediction(float* theta, float* features, int n_features ){\n\
    float res = 0;\n\
    for (int i = 0; i < n_features; i++){\n\
        res += features[i] * theta[i];\n    }\n\
    return res;\n}\n\n\
int main(int argc, char *argv[]){\n\
    float theta[] = ' + modelstr + ';\n\
    float feature[] = {0.4, 0.8};\n\
    float res = linear_regression_prediction(theta, feature, ' + str(model.n_features_in_) + '); \n\
    printf("resultat: %f", res);\n}'

    f = open("code.c", "w")
    f.write(code)


generate(model)
