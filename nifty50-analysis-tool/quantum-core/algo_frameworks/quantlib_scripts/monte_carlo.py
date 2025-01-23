import numpy as np

def monte_carlo_simulation(S, K, T, r, sigma, num_simulations, num_steps, option_type='call'):
    """
    Perform Monte Carlo simulation for option pricing.

    Parameters:
    S : float : Current stock price
    K : float : Option strike price
    T : float : Time to maturity (in years)
    r : float : Risk-free interest rate
    sigma : float : Volatility of the underlying stock
    num_simulations : int : Number of Monte Carlo simulations
    num_steps : int : Number of time steps in each simulation
    option_type : str : 'call' for call option, 'put' for put option

    Returns:
    float : Option price
    """
    dt = T / num_steps
    discount_factor = np.exp(-r * T)
    option_payoffs = []

    for _ in range(num_simulations):
        stock_prices = np.zeros(num_steps + 1)
        stock_prices[0] = S

        for t in range(1, num_steps + 1):
            z = np.random.standard_normal()
            stock_prices[t] = stock_prices[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * z)

        if option_type == 'call':
            option_payoff = max(stock_prices[-1] - K, 0)
        elif option_type == 'put':
            option_payoff = max(K - stock_prices[-1], 0)
        else:
            raise ValueError("Invalid option type. Use 'call' or 'put'.")

        option_payoffs.append(option_payoff)

    option_price = discount_factor * np.mean(option_payoffs)
    return option_price
