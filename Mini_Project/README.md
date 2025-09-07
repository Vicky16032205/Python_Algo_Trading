# Mini Project: First Algo Trade

## Overview
This mini project demonstrates a simple algorithmic trading system using Python and OOP principles. It fetches live market data using Yahoo Finance (`yfinance`), applies a Simple Moving Average (SMA) strategy, and simulates trades using a mock trading API.

## Features
- Fetches real-time price data for a given stock symbol
- Implements a Simple Moving Average (SMA) trading strategy
- Simulates buy/sell trades and tracks account balance
- Modular OOP design for easy extension

## Files
- `First_Algo_Trade.ipynb`: Main notebook containing the trading system code

## How It Works
1. **TradingStrategy**: Base class for trading strategies
2. **SMA_strategy**: Implements the SMA crossover logic
3. **Trade**: Represents a trade action (buy/sell)
4. **MockTradingAPI**: Simulates order execution and balance management
5. **TradingSystem**: Orchestrates data fetching, signal generation, and trade execution

## Requirements
- Python 3.7+
- yfinance

Install dependencies:
```python
!pip install yfinance
```

## Usage
Open `First_Algo_Trade.ipynb` in Jupyter Notebook and run the cells. The system will:
- Download minute-level price data for the specified symbol (default: AAPL)
- Apply the SMA strategy
- Simulate trades and print account balance after each iteration

## Notes
- The mock API does not place real trades
- Price updates depend on market hours and data availability from Yahoo Finance
- For testing, you can modify the code to use random price data

## License
This mini project is for educational purposes only.
