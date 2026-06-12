## File with a few functions already defined for you to read and format
## the all sonar data

## module to read csv files

from csv import reader
import numpy as np
from main_HW7 import G_KPA_pred, G_KPA_train, P_KPA_pred, P_KPA_train 
# Load a CSV File
def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row: continue
            dataset.append(row)
    return dataset

# Extract the feature vectorss
def extract_features(data):
    Feature_matrix = np.zeros([len(data), len(data[0]) - 1])
    for i in range(len(data)):
        for j in range(len(data[0]) - 1):
            Feature_matrix[i][j] = float(data[i][j].strip())
    return Feature_matrix
        
# Extract the labels ("M" to be assigned with 1 and "R" to be assigned with -1)
def extract_labels(data):
    Labels = np.zeros([len(data), 1])
    for i in range(len(data)):
        Labels[i] = 1 if data[i][-1] == "M" else -1
    return Labels


# Computes the accuracy on a test dataset for the GKPA
def accuracy(alpha, Xtrain, ytrain, Xtest, ytest, sigma):
    n, m = np.shape(Xtest)
    n_mistakes = 0
    for j in range(n):
        yhat = G_KPA_pred(alpha, Xtrain, ytrain, Xtest[j,:], sigma)
        if (ytest[j] * yhat <= 0):
            n_mistakes = n_mistakes + 1.0
    return 1 - n_mistakes/n

# Computes accuracy on a test dataset for PKPA
def accuracy_p(alpha, Xtrain, ytrain, Xtest, ytest, p):
    n, m = np.shape(Xtest)
    n_mistakes = 0
    for j in range(n):
        yhat = P_KPA_pred(alpha, Xtrain, ytrain, Xtest[j,:], p)
        if (ytest[j] * yhat <= 0):
            n_mistakes = n_mistakes + 1.0
    return 1 - n_mistakes/n
