import pandas as pd
import numpy as np
import sklearn.model_selection
import sklearn.metrics
from sklearn import linear_model
from sklearn import neighbors
from sklearn import svm

from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score


def classification_movies(r,  C = 1.0, movie_title=None):
    """
    Compute the r_2 score of the corresponding method

    Args:
        r - A indicated of selecting the method, which should be in [1, 2].
        C - A parameter that is required to be used for SVM

    Returns: accuracy_score
    """
    # Load data
    df = pd.read_csv('./movies_clean.csv')

    classification_target = 'profitable'
    all_covariates = ['budget', 'popularity', 'runtime', 'vote_count', 'vote_average', 'Action', 'Adventure', 'Fantasy',
                      'Science Fiction', 'Crime', 'Drama', 'Thriller', 'Animation', 'Family', 'Western', 'Comedy',
                      'Romance', 'Horror', 'Mystery', 'War', 'History', 'Music', 'Documentary', 'TV Movie', 'Foreign']
    X = df[all_covariates]
    y = df[classification_target]
    # Extract here the data you will use to fit the models
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y,random_state = 0)

    # Now fit each of the models
    
    if r == 1:
        reg = linear_model.LogisticRegression(C=C,max_iter=100000)
    elif r == 2:
        reg = svm.SVC(C = C)
    else:
        print("r should be  1, or 2")
        return 0
    reg.fit(x_train,y_train)
    if movie_title is not None and r == 1:

        movie = df[df["title"] == movie_title]

        if len(movie) == 0:
            print("Movie not found.")
        else:
            movie_X = movie[all_covariates]

            prob = reg.predict_proba(movie_X)[0,1]

            print("Movie:", movie_title)
            print("Predicted probability of profitability:", prob)
            print("Actual profitable label:",
                  movie[classification_target].iloc[0])
    y_predict = reg.predict(x_test)

    return sklearn.metrics.accuracy_score(y_pred=y_predict,y_true=y_test)


def refined_classification_movies(r, n_neighbors = 0, C = 1.0):
    """
    Compute the r_2 score of the corresponding method

    Args:
        r - A indicated of selecting the method, which should be in [0, 1, 2].
        n_neighbors - A parameter that is required to be used for KNN
        C - A parameter that is required to be used for SVM

    Returns: accuracy_score
    """
    # Load data
    df = pd.read_csv('./movies_clean.csv')

    # Define here a new_df with excluding or dropping data

    # Find the new data set for fitting the models

    # Now fit each of the models
    
    if r == 1:
        reg = linear_model.LogisticRegression()
    elif r == 2:
        reg = svm.SVC(C = C)
    else:
        print("r should be  1, or 2")
        return 0

    return # the corresponding score

print("Logistic Regression C=1:", classification_movies(1, C=1.0))
print("SVM C=1:", classification_movies(2, C=1.0))

print("Logistic Regression C=0.1:", classification_movies(1, C=0.1))
print("Logistic Regression C=10:", classification_movies(1, C=10))

print("SVM C=0.1:", classification_movies(2, C=0.1))
print("SVM C=10:", classification_movies(2, C=10))
print("\nAvatar:")
classification_movies(1, C=1.0, movie_title="Avatar")

print("\nFood, Inc.:")
classification_movies(1, C=1.0, movie_title="Food, Inc.")