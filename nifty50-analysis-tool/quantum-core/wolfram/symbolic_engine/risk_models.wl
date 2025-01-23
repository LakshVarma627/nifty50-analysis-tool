(* Custom risk analysis scripts in Wolfram Language *)

(* Function to calculate Value at Risk (VaR) using historical simulation *)
ValueAtRisk[returns_List, confidenceLevel_Real] := Module[{sortedReturns, index},
  sortedReturns = Sort[returns];
  index = Ceiling[(1 - confidenceLevel) Length[sortedReturns]];
  sortedReturns[[index]]
]

(* Function to calculate Conditional Value at Risk (CVaR) *)
ConditionalValueAtRisk[returns_List, confidenceLevel_Real] := Module[{sortedReturns, index, var},
  sortedReturns = Sort[returns];
  index = Ceiling[(1 - confidenceLevel) Length[sortedReturns]];
  var = sortedReturns[[index]];
  Mean[Select[sortedReturns, # <= var &]]
]

(* Function to calculate the Sharpe Ratio *)
SharpeRatio[returns_List, riskFreeRate_Real] := Module[{meanReturn, stdDev},
  meanReturn = Mean[returns];
  stdDev = StandardDeviation[returns];
  (meanReturn - riskFreeRate) / stdDev
]

(* Function to calculate the Sortino Ratio *)
SortinoRatio[returns_List, riskFreeRate_Real] := Module[{meanReturn, downsideDeviation},
  meanReturn = Mean[returns];
  downsideDeviation = StandardDeviation[Select[returns, # < riskFreeRate &]];
  (meanReturn - riskFreeRate) / downsideDeviation
]

(* Function to calculate the Treynor Ratio *)
TreynorRatio[returns_List, beta_Real, riskFreeRate_Real] := Module[{meanReturn},
  meanReturn = Mean[returns];
  (meanReturn - riskFreeRate) / beta
]

(* Function to calculate the Maximum Drawdown *)
MaximumDrawdown[prices_List] := Module[{drawdowns},
  drawdowns = Table[(Max[Take[prices, i]] - prices[[i]]) / Max[Take[prices, i]], {i, 1, Length[prices]}];
  Max[drawdowns]
]
