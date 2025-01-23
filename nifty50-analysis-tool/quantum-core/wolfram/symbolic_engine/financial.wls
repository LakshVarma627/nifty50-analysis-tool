(* Wolfram Language scripts for financial analysis *)

(* Function to calculate the moving average of a list of prices *)
MovingAverage[prices_List, n_Integer] := Module[{len = Length[prices]},
  If[len < n, 
    Message[MovingAverage::arglen, n, len]; 
    Return[$Failed]
  ];
  MovingAverage[prices, n] = Table[Mean[Take[prices, {i, i + n - 1}]], {i, 1, len - n + 1}]
]

(* Function to calculate the exponential moving average of a list of prices *)
ExponentialMovingAverage[prices_List, n_Integer] := Module[{alpha, ema},
  alpha = 2 / (n + 1);
  ema = FoldList[(1 - alpha) #1 + alpha #2 &, First[prices], Rest[prices]];
  ema
]

(* Function to calculate the relative strength index (RSI) of a list of prices *)
RelativeStrengthIndex[prices_List, n_Integer] := Module[{gains, losses, avgGain, avgLoss, rs, rsi},
  gains = Differences[prices] /. x_ /; x < 0 -> 0;
  losses = -Differences[prices] /. x_ /; x > 0 -> 0;
  avgGain = MovingAverage[gains, n];
  avgLoss = MovingAverage[losses, n];
  rs = avgGain / avgLoss;
  rsi = 100 - (100 / (1 + rs));
  rsi
]

(* Function to calculate the Bollinger Bands of a list of prices *)
BollingerBands[prices_List, n_Integer, k_Real] := Module[{sma, stddev, upperBand, lowerBand},
  sma = MovingAverage[prices, n];
  stddev = MovingStandardDeviation[prices, n];
  upperBand = sma + k stddev;
  lowerBand = sma - k stddev;
  {upperBand, sma, lowerBand}
]

(* Function to calculate the moving standard deviation of a list of prices *)
MovingStandardDeviation[prices_List, n_Integer] := Module[{len = Length[prices]},
  If[len < n, 
    Message[MovingStandardDeviation::arglen, n, len]; 
    Return[$Failed]
  ];
  MovingStandardDeviation[prices, n] = Table[StandardDeviation[Take[prices, {i, i + n - 1}]], {i, 1, len - n + 1}]
]
