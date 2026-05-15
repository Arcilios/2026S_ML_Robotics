import project3 as p1
import utils
import numpy as np


def plot_toy_results(algo_name, thetas, toy_features, toy_labels):
    print('theta for', algo_name, 'is', ', '.join(map(str, list(thetas[0]))))
    print('theta_0 for', algo_name, 'is', str(thetas[1]))
    utils.plot_toy_data(algo_name, toy_features, toy_labels, thetas)

def main(file_name):
    toy_features, toy_labels = toy_data = utils.load_toy_data(file_name)

    T = 10
    L = 0.2

    thetas_perceptron = p1.perceptron(toy_features, toy_labels, T)
    thetas_avg_perceptron = p1.average_perceptron(toy_features, toy_labels, T)
    thetas_pegasos = p1.pegasos(toy_features, toy_labels, T, L)

    # Visualization part
    # You can check the figures and test the codes for your own purpose
    # This will not be graded
    plot_toy_results('Perceptron', thetas_perceptron, toy_features, toy_labels)
    plot_toy_results('Average Perceptron', thetas_avg_perceptron, toy_features, toy_labels)
    plot_toy_results('Pegasos', thetas_pegasos, toy_features, toy_labels)

if __name__ == '__main__':
    main("toy_data.tsv")
