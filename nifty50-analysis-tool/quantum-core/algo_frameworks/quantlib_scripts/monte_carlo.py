import numpy as np

def monte_carlo_simulation(S0, T, r, sigma, num_simulations, num_steps):
    """
    Perform Monte Carlo simulation for stock price.

    Parameters:
    S0 (float): Initial stock price
    T (float): Time to maturity in years
    r (float): Risk-free interest rate
    sigma (float): Volatility of the stock
    num_simulations (int): Number of simulation paths
    num_steps (int): Number of time steps

    Returns:
    np.ndarray: Simulated stock prices
    """
    dt = T / num_steps
    prices = np.zeros((num_steps + 1, num_simulations))
    prices[0] = S0

    for t in range(1, num_steps + 1):
        z = np.random.standard_normal(num_simulations)
        prices[t] = prices[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * z)

    return prices
