# MAE146 SP26 HW3
# Test script for hinge_loss_single function
# NOT A COMPREHENSIVE TEST: only tests against three test cases

import numpy as np
from project3 import hinge_loss_single

eps = 1e-10

def main():
    test_1()
    test_2()
    test_3()
    print('Test completed')

def test_1():
    feature_vector = np.array([1.76, 0.40])
    label = -1
    theta = np.array([0.5, 0.5])
    theta_0 = 0.5
    out = hinge_loss_single(feature_vector, label, theta, theta_0)
    expected_out = 2.58
    
    if abs(out - expected_out) > eps:
        print(f'Test case 1: Incorrect function output: expected loss: {expected_out}, yours: {out}')
    else:
        print('Test case 1: Correct function output')

def test_2():
    feature_vector = np.array([2.16,-1.34])
    label = 1
    theta = np.array([-2, 0.5])
    theta_0 = 1
    out = hinge_loss_single(feature_vector, label, theta, theta_0)
    expected_out = 4.99
    
    if abs(out - expected_out) > eps:
        print(f'Test case 2: Incorrect function output: expected loss: {expected_out}, yours: {out}')
    else:
        print('Test case 2: Correct function output')

def test_3():
    feature_vector = np.array([-1, 2])
    label = 1
    theta = np.array([-3, 2])
    theta_0 = 0.3
    out = hinge_loss_single(feature_vector, label, theta, theta_0)
    expected_out = 0
    
    if abs(out - expected_out) > eps:
        print(f'Test case 3: Incorrect function output: expected loss: {expected_out}, yours: {out}')
    else:
        print('Test case 3: Correct function output')

if __name__ == "__main__":
    main()
