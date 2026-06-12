# HW8

## E4.1

The first method is that we can use weighted mean of the particles.
$$\hat{x}_t=\sum_{i=1}^{M}w_t^{[i]}x_t^{[i]}$$
The second method is that we can directly use the particle with the greatest weight to estimate.

## E4.2

### (i)

The robot should initialize particles uniformly over the hallway and assign equal initial weights to all particles.

### (ii)

$$x_{t+1}=x_{t}+u_{t}$$
The new positions of the particles are, therefore,:
$$3.0,3.3,3.5,3.9$$

### (iii)

The weights of the particles are propotional to the probability they create the measurement $z=3.0$
$$w_i\propto\exp\left(-\frac{(z-x_i)^2}{2\sigma^2}\right)$$
With $x=[3.0,3.3,3.5,3.9]$ and $z = 3.0,\ \sigma = 0.12$:
$$w =[0.958, 0.042, 0.000, 0.000]$$
The sum of them is 1.

### (iv)

```Python
rng = np.random.default_rng(42)

states = np.array(["P1", "P2", "P3", "P4"])
probabilities = np.array([0.957756, 0.042081, 0.000163, 0.000000])

samples = rng.choice(states, size=4, p=probabilities)
```

It gives result ['P1', 'P1', 'P1', 'P1'].
Therefore, after resampling, all four particles correspond to P1, whose location is 3.0.

### (v)

The particles have collapsed to a single state after resampling. This is a problem because the particle filter loses diversity and may no longer represent the full belief distribution. This can be reduced by using more particles, adding motion noise, or resampling only when the effective sample size becomes small.