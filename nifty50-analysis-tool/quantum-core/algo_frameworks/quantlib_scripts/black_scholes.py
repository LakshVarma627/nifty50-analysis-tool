import math

def black_scholes(S, K, T, r, sigma, option_type='call'):
    """
    Calculate the Black-Scholes option price.

    Parameters:
    S (float): Current stock price
    K (float): Option strike price
    T (float): Time to expiration in years
    r (float): Risk-free interest rate
    sigma (float): Volatility of the stock
    option_type (str): 'call' for call option, 'put' for put option

    Returns:
    float: Option price
    """
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == 'call':
        option_price = S * norm_cdf(d1) - K * math.exp(-r * T) * norm_cdf(d2)
    elif option_type == 'put':
        option_price = K * math.exp(-r * T) * norm_cdf(-d2) - S * norm_cdf(-d1)
    else:
        raise ValueError("Invalid option type. Use 'call' or 'put'.")

    return option_price

def norm_cdf(x):
    """
    Calculate the cumulative distribution function for a standard normal distribution.

    Parameters:
    x (float): Value to evaluate

    Returns:
    float: CDF value
    """
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0
