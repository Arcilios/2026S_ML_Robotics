import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

data = np.loadtxt("data_HW3_Q1.csv", delimiter=",", skiprows=1, usecols=(1, 2))

x = data[:, 0]
y = data[:, 1]

degrees = [1, 2, 3, 4, 5]
losses = []

for n in degrees:
    coeffs = np.polyfit(x, y, n)
    y_pred = np.polyval(coeffs, x)
    loss = np.mean((y - y_pred) ** 2)
    losses.append(loss)

    print(f"Degree {n}: average square loss = {loss:.4f}")

best_degree = degrees[np.argmin(losses)]
print("Best degree among tested degrees =", best_degree)

# Plot polynomial fits for visual comparison
x_plot = np.linspace(x.min(), x.max(), 300)

plt.figure(figsize=(7, 5))
plt.scatter(x, y, label="Data")

for n in degrees:
    coeffs = np.polyfit(x, y, n)
    y_plot = np.polyval(coeffs, x_plot)
    plt.plot(x_plot, y_plot, label=f"Degree {n}")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Polynomial Fits with Different Degrees")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# ============================================================
# Part (b): Define average square loss for H1(x; w) = w*x^n
# Use n = 2 based on Part (a)
# ============================================================
def avg_square_loss(w):
    n = 2
    y_pred = w * (x ** n)
    loss = np.mean((y - y_pred) ** 2)
    return loss


loss_at_minus_06 = avg_square_loss(-0.6)
print("Average square loss when w = -0.6:", loss_at_minus_06)


# ============================================================
# Part (c): Use scipy.optimize.minimize to find optimal w
# ============================================================
result = minimize(avg_square_loss, x0=-0.6)

w_opt = result.x[0]
min_loss = result.fun

print("Optimal w =", w_opt)
print("Minimum average square loss =", min_loss)

# Compute fitted values using optimal w
n = 2
y_fit = w_opt * (x ** n)

# Plot best fit and residuals
plt.figure(figsize=(7, 5))

plt.scatter(x, y, label="Data")

# Best fit curve
plt.plot(x_plot, w_opt * (x_plot ** n), label=f"Best fit: y = {w_opt:.3f}x^2")

# Residual lines
for xi, yi, yfi in zip(x, y, y_fit):
    plt.plot([xi, xi], [yi, yfi])

plt.xlabel("x")
plt.ylabel("y")
plt.title("Best Fit for H1(x; w) = wx^2 with Residuals")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

n = 2
phi_x = x ** n

plt.figure(figsize=(7, 5))
plt.scatter(phi_x, y, label="Data in feature space")

# Optional: plot the best straight line y = w * phi(x)
phi_plot = np.linspace(phi_x.min(), phi_x.max(), 300)
plt.plot(phi_plot, w_opt * phi_plot, label=f"Best fit: y = {w_opt:.3f} phi(x)")

plt.xlabel(r"$\phi(x) = x^2$")
plt.ylabel("y")
plt.title("Data in Feature Space")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
n = 2
phi_x = x ** n

# np.linalg.lstsq expects a 2D matrix for A
A = phi_x.reshape(-1, 1)

w_lstsq, residuals, rank, s = np.linalg.lstsq(A, y, rcond=None)

w = w_lstsq[0]

print("Least squares slope w =", w)