import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler


def main():

    # Physical parameters
    ### Enter the correct values here
    b = 0.25
    m = 1
    g = 9.81
    L = 1
    
    # 1. Generate synthetic trajectories
    trajectories = simulate_trajectories(
        n_trajectories=100,
        t_span=(0.0, 10.0),
        n_points=101,
        b=b,
        m=m,
        g=g,
        L=L,
        theta0_range=(-np.pi, np.pi),
        omega0_range=(-10.0, 10.0),
        seed=1,
    )
    
    # 2. Select 10 random time points from each solution
    theta, omega, alpha = sample_random_time_points(
        trajectories,
        points_per_trajectory=10,
        noise_std=0.0,
        seed=2,
    )
    
    # 3. Make scatter plots similar to Fig. 2.11
    plot_dictionary_scatter(
        theta,
        omega,
        alpha,
        b=b,
        m=m,
        g=g,
        L=L,
        filename="fig_dictionary_scatter_no_noise.png",
    )
    
    # 4. Build dictionary and regress
    X = build_library(theta, omega)
    results = fit_models(X, alpha, ridge_alpha=100.0, lasso_alpha=1)
    
    # Specify the two only non-zero coefficients in the true equation
    true_coefficients = np.zeros(len(FEATURE_NAMES))
    true_coefficients[FEATURE_NAMES.index("omega")] = -b/m
    true_coefficients[FEATURE_NAMES.index("sin(theta)")] = -g/L
    
    # Generate a plot of regression coefficients similar to Fig. 2.12
    plot_coefficients(
        results,
        true_coefficients,
        filename="fig_coefficients_no_noise.png",
    )
    
    # 5. Repeat with noise
    theta_n, omega_n, alpha_n = sample_random_time_points(
        trajectories,
        points_per_trajectory=10,
        noise_std=0.1,
        seed=2,
    )
    
    
    plot_dictionary_scatter(
        theta_n,
        omega_n,
        alpha_n,
        b=b,
        m=m,
        g=g,
        L=L,
        filename="fig_dictionary_scatter_noise.png",
    )
    
    X_n = build_library(theta_n, omega_n)
    results_n = fit_models(X_n, alpha_n, ridge_alpha=10.0, lasso_alpha=0.1)
    plot_coefficients(
        results_n,
        true_coefficients,
        filename="fig_coefficients_noise.png",
    )
      
   
    plt.show()



def pendulum_rhs(t, y, b, m, L, g):
    """
    Computes the right hand sides of the two first-order ODEs that make up the 
    equations of motion of a pendulum with damping
    """
    theta, omega = y
    return [omega, -(b/m)*omega - (g/L)*np.sin(theta)]

def simulate_trajectories(
    n_trajectories,
    t_span,
    n_points,
    b,
    m,
    g,
    L,
    theta0_range,
    omega0_range,
    seed=1,
):
    """
    Simulates n_trajectories pendulum trajectories over t_span time with 
    n_points timesteps given the physical parameters b, m, g, L. Initial 
    conditions are chosen randomly from uniform distributions given 
    theta0_range and omega0_range.
    """

    # get random number generator
    rng = np.random.default_rng(seed)
    
    # compute the timesteps
    t_eval = np.linspace(t_span[0], t_span[1], n_points)
    
    #initialize a list to contain the trajectories
    trajectories = []

    # for each trajector (_ is used as a loop counter instead of i when you 
    # don't need to refer to it)
    for _ in range(n_trajectories):
        # pick random initial conditions
        y0 = [
            rng.uniform(theta0_range[0], theta0_range[1]),
            rng.uniform(omega0_range[0], omega0_range[1]),
        ]

        # solve the ODEs
        sol = solve_ivp(
            lambda t, y: pendulum_rhs(t, y, b=b, m=m, g=g, L=L),
            t_span,
            y0,
            t_eval=t_eval,
            rtol=1e-9,
            atol=1e-9,
        )

        
        theta = sol.y[0]
        omega = sol.y[1]

        trajectories.append({
            "t": sol.t,
            "theta": theta,
            "omega": omega,
        })

    return trajectories

def sample_random_time_points(
    trajectories,
    points_per_trajectory,
    noise_std,
    seed,
):
    """
    Select random time points from each trajectory.

    The dictionary is built from measured theta and omega.
    The acceleration alpha = theta_ddot is estimated from finite differences
    of measured omega
    """
    rng = np.random.default_rng(seed)

    theta_all = []
    omega_all = []
    alpha_all = []

    for traj in trajectories:
        t = traj["t"]
        theta_full = traj["theta"].copy()
        omega_full = traj["omega"].copy()

        # Add measurement noise to the full measured trajectory first.
        # This is important because acceleration is estimated from measured omega.
        if noise_std > 0:
            theta_full = theta_full + rng.normal(0.0, noise_std, size=theta_full.shape)
            omega_full = omega_full + rng.normal(0.0, noise_std, size=omega_full.shape)

        n = len(t)

        # Avoid endpoints because we use a central difference.
        idx = rng.choice(
            np.arange(1, n - 1),
            size=points_per_trajectory,
            replace=False
        )

        theta = theta_full[idx]
        omega = omega_full[idx]

        # Central difference estimate of angular acceleration
        alpha = (omega_full[idx + 1] - omega_full[idx - 1]) / (t[idx + 1] - t[idx - 1])

        theta_all.append(theta)
        omega_all.append(omega)
        alpha_all.append(alpha)

    return np.concatenate(theta_all), np.concatenate(omega_all), np.concatenate(alpha_all)


def fit_models(X, y, ridge_alpha, lasso_alpha):
    """
    Compare:
    1. No normalization: ordinary least squares on raw features
    2. Ridge normalization: standardize features, then Ridge regression
    3. Lasso normalization: standardize features, then Lasso regression

    Ridge and Lasso coefficients are converted back to the original feature scale
    so they can be compared to the physical coefficients.
    """

    results = {}
    
    
    ### Insert your code here to generate regression fits using the three
    ### approaches mentioned above
    no_model = LinearRegression()
    no_model.fit(X,y)
    results["least squares"] = no_model.coef_
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    ridge_model = Ridge(alpha=ridge_alpha)
    ridge_model.fit(X_scaled, y)
    results["ridge"] = ridge_model.coef_ / scaler.scale_
    lasso_model = Lasso(alpha=lasso_alpha)
    lasso_model.fit(X_scaled, y)
    results["lasso"] = lasso_model.coef_ / scaler.scale_
    return results


# names of each component of the dictionary of terms
FEATURE_NAMES = [
    "theta",
    "omega",
    "theta^2",
    "omega^2",
    "theta*omega",
    "sin(theta)",
    "cos(theta)",
    "sin(omega)",
    "cos(omega)",
]

# define each component of the dictionary of terms
def build_library(theta, omega):
    theta = np.asarray(theta)
    omega = np.asarray(omega)

    X = np.column_stack([
        theta,
        omega,
        theta**2,
        omega**2,
        theta * omega,
        np.sin(theta),
        np.cos(theta),
        np.sin(omega),
        np.cos(omega),
    ])

    return X

def plot_dictionary_scatter(theta, omega, alpha, b, m, g, L,
                            filename="fig_dictionary_scatter.png"):
    """
    Generates a 3x3 set of scatter plots similar to textbook Fig. 2.11:
    alpha = theta_ddot plotted versus selected dictionary terms and selected
    known combinations.
    """
    # subplot contents and captions
    ### Note: you should figure out how to plot the other quantities found in
    ### Fig. 2.11
    panels = [
    (theta, r"$\theta$"),
    (omega, r"$\omega$"),
    (theta**2, r"$\theta^2$"),
    (omega**2, r"$\omega^2$"),
    (theta * omega, r"$\theta\omega$"),
    (np.sin(theta), r"$\sin(\theta)$"),
    (np.cos(theta), r"$\cos(\theta)$"),
    (np.sin(omega), r"$\sin(\omega)$"),
    (np.cos(omega), r"$\cos(\omega)$"),
    ]

    fig, axes = plt.subplots(3, 3, figsize=(8, 8))

    # x limits of each subplot (to match Fig. 2.11)
    ### You'll need to adjust the x-limits for each subfigure
    xlims = [
        (-3, 3),
        (-3, 3),
        (-3, 3),
        (-3, 3),
        (-3, 3),
        (-3, 3),
        (-3, 3),
        (-3, 3),
        (-3, 3),
    ]
    
    # y limits of each subplot
    ylims = [(-6, 6)] * 9
    
    # assign the formatting of each subplot
    for ax, ((x, label), xlim, ylim) in zip(axes.flat, zip(panels, xlims, ylims)):
        ax.scatter(x, alpha, s=2, alpha=0.6, linewidth=0)
    
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
    
        ax.set_xlabel(label)
        ax.set_ylabel(r"$\ddot{\theta}$")
    
        #ax.grid(True, alpha=0.2)

    #overall plot specifications
    fig.suptitle("Acceleration versus selected dictionary elements", y=1.02)
    fig.tight_layout()
    fig.savefig(filename, dpi=300, bbox_inches="tight")
    return fig

def plot_coefficients(results, true_coefficients, filename="fig_coefficients.png"):
    """
    Generates a plot of the regression coefficients for each element in the 
    dictionary of terms, similar to textbook Fig. 2.11.
    """
    labels = FEATURE_NAMES
    x = np.arange(len(labels))

    fig, ax = plt.subplots(figsize=(13, 4))
    ax.plot(x, np.abs(true_coefficients), "o", label="true")

    for name, coef in results.items():
        ax.plot(x, np.abs(coef), ".", label=name)

    ax.axhline(0, linewidth=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=70, ha="right")
    ax.set_ylabel("|coefficient|")
    ax.set_title("Recovered governing-equation coefficients")
    ax.legend()
    fig.tight_layout()
    fig.savefig(filename, dpi=300, bbox_inches="tight")
    return fig


# Run the main function above (allows function definitions after where the are
# called in main() )
main()