import numpy as np

x = np.array([0.27093981, 0.18046082, 0.36049533, 0.1971442,
              0.46258231, 0.52384941, 0.49240247, 0.12699269])

y = np.array([2.83085451, 6.18744823, 0.94532684, -2.52021475,
              3.67784773, 0.78365838, 3.15266217, 1.96372897])

x_bar = np.mean(x)
y_bar = np.mean(y)

numerator = np.sum((x - x_bar) * (y - y_bar))
denominator_base = np.sum((x - x_bar) ** 2)

print("x_bar =", x_bar)
print("y_bar =", y_bar)
print("numerator =", numerator)
print("denominator_base =", denominator_base)

for lam in [0, 1]:
    theta = numerator / (denominator_base + lam)
    theta0 = y_bar - theta * x_bar
    
    print("\nlambda =", lam)
    print("theta =", theta)
    print("theta0 =", theta0)
    

x_test = np.array([0.63446731, 0.40335105])
y_test = np.array([3.10018735, 1.42556588])


models = {
    0: {"theta": 0.46410425, "theta0": 1.97596765},
    1: {"theta": 0.06644624, "theta0": 2.10594550}
}

for lam, params in models.items():
    theta = params["theta"]
    theta0 = params["theta0"]

    y_pred = theta * x_test + theta0
    squared_errors = (y_test - y_pred) ** 2
    mse = np.mean(squared_errors)

    print("lambda =", lam)
    print("y_pred =", y_pred)
    print("squared_errors =", squared_errors)
    print("MSE =", mse)
    print()