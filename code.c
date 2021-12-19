#include <stdio.h>

float linear_regression_prediction(float* theta, float* features, int n_features ){
    float res = 0;
    for (int i = 0; i < n_features; i++){
        res += features[i] * theta[i];
    }
    return res;
}

int main(int argc, char *argv[]){
    float theta[] = {1.933556490356532,-0.35036257295529605};
    float feature[] = {0.4, 0.8};
    float res = linear_regression_prediction(theta, feature, 2); 
    printf("resultat: %f", res);
}