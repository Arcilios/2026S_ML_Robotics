import numpy as np
from scipy.spatial.distance import squareform, cdist
import scipy
from importlib import util
from pathlib import Path
from sklearn.model_selection import train_test_split

# Takes in a counting vector 'alpha', the training data Xtrain, the training
# label ytrain, a feature vector X and 'sigma' (the variance parameter in the 
# Gaussian Kernel)
# Outputs the predicted label for X.
def G_KPA_pred(alpha, Xtrain, ytrain, X, sigma):
    dist2 = np.sum((Xtrain - X)**2, axis=1)
    K = np.exp(-dist2 / (2 * sigma**2))
    score = np.sum(alpha.flatten() * ytrain.flatten() * K)
    return 1 if score >= 0 else -1

# Runs the perceptron training algorithm taking in an initial counting vector
# alpha0, matrix of covariates Xtrain, a vector of labels ytrain, and 'sigma' (the
# variance parameter in the Gaussian Kernel). 'T' is the number of passes to be
# made through the data.
# Outputs the learned counting vector a.
def G_KPA_train(alpha0, Xtrain, ytrain, T, sigma):
    alpha = alpha0.copy().flatten()
    y = ytrain.flatten()

    for _ in range(T):
        for i in range(Xtrain.shape[0]):
            yhat = G_KPA_pred(alpha, Xtrain, y, Xtrain[i], sigma)
            if y[i] * yhat <= 0:
                alpha[i] += 1

    return alpha


# Takes in a counting vector 'alpha', the training data Xtrain, the training
# label ytrain, a feature vector X and 'p' (the polynomial degree in the 
# polynomial Kernel)
# Outputs the predicted label for X.
def P_KPA_pred(alpha, Xtrain, ytrain, X, p):
    K = (1 + Xtrain @ X) ** p
    score = np.sum(alpha.flatten() * ytrain.flatten() * K)
    return 1 if score >= 0 else -1

        
# Runs the perceptron training algorithm taking in an initial counting vector
# alpha0, matrix of covariates Xtrain, a vector of labels ytrain, and 'p' (the
# polynomial degree in the polynomial Kernel). 'T' is the number of passes to be
# made through the data.
# Outputs the learned counting vector a.
def P_KPA_train(alpha0, Xtrain, ytrain, T, p):
    alpha = alpha0.copy().flatten()
    y = ytrain.flatten()

    for _ in range(T):
        for i in range(Xtrain.shape[0]):
            yhat = P_KPA_pred(alpha, Xtrain, y, Xtrain[i], p)
            if y[i] * yhat <= 0:
                alpha[i] += 1

    return alpha


def load_utils():
    utils_path = Path(__file__).with_name("utils-2.py")
    spec = util.spec_from_file_location("utils_2", utils_path)
    utils = util.module_from_spec(spec)
    spec.loader.exec_module(utils)
    return utils


if __name__ == "__main__":
    utils = load_utils()
    data = utils.load_csv("sonar.all-data.csv")
    X = utils.extract_features(data)
    y = utils.extract_labels(data).flatten()

    Xtrain, Xtest, ytrain, ytest = train_test_split(
        X, y, random_state=0
    )

    print("Gaussian Kernel Perceptron, T = 10")
    best_sigma = None
    best_test_acc = -1
    for sigma in [0.1, 1, 10]:
        alpha0 = np.zeros(Xtrain.shape[0])
        alpha = G_KPA_train(alpha0, Xtrain, ytrain, T=10, sigma=sigma)
        train_acc = utils.accuracy(alpha, Xtrain, ytrain, Xtrain, ytrain, sigma)
        test_acc = utils.accuracy(alpha, Xtrain, ytrain, Xtest, ytest, sigma)
        print(f"sigma={sigma}: train accuracy={train_acc:.4f}, test accuracy={test_acc:.4f}")

        if test_acc > best_test_acc:
            best_test_acc = test_acc
            best_sigma = sigma

    print(f"Best sigma: {best_sigma}")
    print()

    print("Polynomial Kernel Perceptron, T = 100")
    best_p = None
    best_poly_test_acc = -1
    for p in [1, 2, 10]:
        alpha0 = np.zeros(Xtrain.shape[0])
        alpha = P_KPA_train(alpha0, Xtrain, ytrain, T=100, p=p)
        train_acc = utils.accuracy_p(alpha, Xtrain, ytrain, Xtrain, ytrain, p)
        test_acc = utils.accuracy_p(alpha, Xtrain, ytrain, Xtest, ytest, p)
        print(f"p={p}: train accuracy={train_acc:.4f}, test accuracy={test_acc:.4f}")

        if test_acc > best_poly_test_acc:
            best_poly_test_acc = test_acc
            best_p = p

    print(f"Best p: {best_p}")
# For the Gaussian kernel perceptron, I tested sigma values {0.1, 1, 10} with T = 10.

# sigma = 0.1: train accuracy = 1.0000, test accuracy = 0.8077
# sigma = 1: train accuracy = 1.0000, test accuracy = 0.8269
# sigma = 10: train accuracy = 0.5449, test accuracy = 0.5000

# The best value is sigma = 1 because it gives the highest test accuracy, 0.8269. 
# Using the best sigma, the final train accuracy is 1.0000 and the final test accuracy is 0.8269.

# For the polynomial kernel perceptron, I tested p values {1, 2, 10} with T = 100.

# p = 1: train accuracy = 0.8205, test accuracy = 0.6731
# p = 2: train accuracy = 1.0000, test accuracy = 0.8269
# p = 10: train accuracy = 1.0000, test accuracy = 0.7692

# The best value is p = 2 because it gives the highest test accuracy, 0.8269.
# Using the best p, the final train accuracy is 1.0000 and the final test accuracy is 0.8269.