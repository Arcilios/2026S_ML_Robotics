import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

# The following function gives a sample distributed according to N(mu,sigma^2), var = sigma^2
# and you can use it directly below
def box_muller(mu, var):
    u1 = np.random.rand(1)
    u2 = np.random.rand(1)
    x = np.cos(2*np.pi*u1)*np.sqrt(-2*np.log(u2))
    # this must give you the sample according to N(mu,sigma^2=var)
    y = mu + np.sqrt(var)*x
    return y


## Exercise E2.6
def sample_motion_model(x_t, u_t_plus_1, alpha):
    # x_t is your initial pose (position and orientation)
    # u_t_plus_1 is a vector of three components,
    #       that correspond to the sequence of commands matching the odometry reading
    # alpha are the parameters in the odometry motion model
    
    # extract data from list
    x = x_t[0]
    y = x_t[1]
    theta = x_t[2]

    delta_rot1 = u_t_plus_1[0]
    delta_rot2 = u_t_plus_1[1]
    delta_trans = u_t_plus_1[2]

    alpha1 = alpha[0]
    alpha2 = alpha[1]
    alpha3 = alpha[2]
    alpha4 = alpha[3]

    # noise variances from the formula
    var_rot1 = alpha1 * delta_rot1**2 + alpha2 * delta_trans**2
    var_trans = alpha3 * delta_trans**2 + alpha4 * delta_rot1**2 + alpha4 * delta_rot2**2
    var_rot2 = alpha1 * delta_rot2**2 + alpha2 * delta_trans**2

    # sample zero-mean Gaussian noise
    noise_rot1 = float(box_muller(0, var_rot1))
    noise_trans = float(box_muller(0, var_trans))
    noise_rot2 = float(box_muller(0, var_rot2))

    # noisy odometry
    delta_rot1_hat = delta_rot1 - noise_rot1
    delta_trans_hat = delta_trans - noise_trans
    delta_rot2_hat = delta_rot2 - noise_rot2

    # new pose
    x_new = x + delta_trans_hat * np.cos(theta + delta_rot1_hat)
    y_new = y + delta_trans_hat * np.sin(theta + delta_rot1_hat)
    theta_new = theta + delta_rot1_hat + delta_rot2_hat

    x_t_plus_1 = [x_new, y_new, theta_new]
    return x_t_plus_1


## Exercise E3.4
def landmark_sensor_model(z, x, l):
    # z is your range and bearing, x robot pose, l is the landmark
    
    ## get values
    
    pos_x = x[0]
    pos_y = x[1]
    pos_theta = x[2]

    mark_x = l[0]
    mark_y = l[1]

    # calculate true values
    
    dx = mark_x - pos_x
    dy = mark_y - pos_y

    expected_range = np.sqrt(dx**2 + dy**2)
    expected_bearing = np.atan2(dy, dx) - pos_theta
    expected_bearing = (expected_bearing + np.pi) % (2 * np.pi) - np.pi
    
    # set up model parameters
    
    sigma_r_squared = 0.25
    sigma_theta_squared = 0.01
    
    # calculate probability
    
    range_error = z[0] - expected_range
    bearing_error = (z[1] - expected_bearing+ np.pi) % (2 * np.pi) - np.pi
    p_range = scipy.stats.norm.pdf(range_error,0,sigma_r_squared)
    p_bearing = scipy.stats.norm.pdf(bearing_error,0,sigma_theta_squared)
    
    #calculate likelihood
    
    likelihood = p_range*p_bearing
    
    return likelihood


if __name__ == '__main__':
    # plot scatter plot of motion model with 5000 positions
    # from the conditions in the problem statement
    x_t = [2, 4, 0]
    u_t_plus_1 = [np.pi / 2, 0, 1]
    alpha = [0.1, 0.1, 0.01, 0.01]

    samples = []

    for _ in range(5000):
        samples.append(sample_motion_model(x_t, u_t_plus_1, alpha))

    samples = np.array(samples)

    plt.figure(figsize=(6, 6))
    plt.scatter(samples[:, 0], samples[:, 1], s=6, alpha=0.4)
    plt.xlabel("x position")
    plt.ylabel("y position")
    plt.title("5000 Samples from Odometry Motion Model")
    plt.axis("equal")
    plt.grid(True)
    plt.show()

    x = np.array([2, 3, np.pi / 4])
    l = np.array([2, 8])

    z0 = np.array([5.0, np.pi / 4])
    z1 = np.array([5.0, 0.6])
    z2 = np.array([4.5, np.pi / 4])
    z3 = np.array([5.5, 0.9])

    measurements = [z0, z1, z2, z3]

    for i, z in enumerate(measurements):
        likelihood = landmark_sensor_model(z, x, l)
        print(f"z{i} likelihood = {likelihood}")