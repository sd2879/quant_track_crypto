
# Crypto Portfolio Strategy & Analysis

This project delivers a robust framework for creating a quantitative trading strategy that combines technical and sentiment analysis to inform investment decisions in cryptocurrency assets. It encompasses data aggregation, feature engineering, sentiment analysis, and portfolio management. The final output is a deployable strategy that can interact with decentralized finance (DeFi) platforms and integrate insights from large language models (LLMs) for dynamic decision-making.

---

## Problem Statement

In this hackathon, a dataset containing candlestick data for various cryptocurrency assets (a mix of major and meme assets) as well as interest rate data is provided, pre-filtered over a few days. The requirements include:

1. Aggregating at least 10,000 unique data points from multiple data sources to ensure meaningful statistical analysis.
2. Collecting additional data from sources like lending markets, liquid staking tokens (LSTs), and order book data from centralized exchanges (CEXes) such as Binance.
3. Using external sources, such as LLMs and news APIs, to incorporate sentiment analysis, enabling a deeper understanding of market perceptions.

### Goal

- Provide a comprehensive notebook detailing the entire process, from data aggregation to strategy design, indicator selection, and backtesting.
- Develop pseudocode for an agent that interacts with DeFi primitives and LLMs to implement the trading strategy, with a clear formulation of each step in the agentic workflow.

---

## Table of Contents

1. [Data Aggregation and Preprocessing](#data-aggregation-and-preprocessing)
2. [Feature Processing](#feature-processing)
3. [Combine Indicators into a Strategy](#combine-indicators-into-a-strategy)
4. [Sentiment Analysis](#sentiment-analysis)
5. [Portfolio Assignment and Management](#portfolio-assignment-and-management)
6. [Agentic Workflow and Pseudocode](#agentic-workflow-and-pseudocode)
7. [Usage and Example](#usage-and-example)

---

### 1. Data Aggregation and Preprocessing

The first phase of the project involves gathering and preparing data from multiple sources to create a unified dataset for in-depth analysis.

- **Data Sources**:
  - **Candle Data**: The dataset includes historical and real-time price data for a specified set of assets. To supplement, live data is sourced from CEXes like Binance using their APIs.
  - **Sentiment Data**: Data from social media platforms (e.g., Twitter) and news sources is gathered, allowing for sentiment analysis to gauge public opinion trends.
- **Data Aggregation**:
  - **Timestamp Synchronization**: Aligns datasets by timestamp to ensure consistency across different sources, facilitating smooth time-series analysis.
  - **Standardization**: Standardizes formats, units, and naming conventions across datasets for streamlined processing and compatibility with analytical tools.
  - **Preprocessing**: Sentiment data is transformed into numerical sentiment scores or keyword vectors that quantify sentiment impacts on asset price trends. 

Through this step, a well-structured dataset is created, capturing both market metrics and sentiment indicators to support informed analysis.

### 2. Feature Processing

The next step involves engineering technical indicators that form the backbone of the trading strategy.

- **`compute_rsi()`**: 
  - **Description**: Calculates the Relative Strength Index (RSI) based on the 'Close' prices in the data.
  - **Purpose**: RSI is a widely used indicator that measures the speed and magnitude of price movements, identifying overbought or oversold conditions.
- **`calculate_dynamic_thresholds()`**:
  - **Description**: Computes dynamic buy and sell thresholds based on the mean and standard deviation of RSI over a specified rolling window.
  - **Purpose**: This enables the setting of adaptable thresholds that can respond to changing market conditions, helping establish buy and sell signals that adjust dynamically rather than remaining static.

Together, these features are essential in generating buy and sell signals based on market conditions, contributing to a responsive and flexible trading strategy.

### 3. Combine Indicators into a Strategy

This phase integrates technical indicators to design a cohesive trading strategy.

- **Moving Averages**:
  - **Fast Moving Average (5-period)**: Provides insight into short-term trends, allowing for rapid responses to recent price changes.
  - **Slow Moving Average (20-period)**: Offers a broader view of price movement, smoothing out fluctuations to identify longer-term trends.
- **Signal Generation**:
  - **Description**: Generates signals (Buy, Sell, Hold) by analyzing the relationship between fast and slow moving averages.
  - **Purpose**: These signals drive trading decisions. A buy signal is generated when the fast moving average crosses above the slow moving average, indicating positive momentum, while a sell signal is triggered when the reverse occurs.
- **Daily Scores Calculation**:
  - **Process**: For each asset, a daily score is calculated as `Daily Score = Count of 'Buy' signals - Count of 'Sell' signals`.
  - **Interpretation**: A positive score suggests a buying inclination, while a negative score indicates selling pressure. 
  - **Filtering**: The top 5 and bottom 5 assets based on daily scores are selected for deeper analysis, focusing on promising opportunities and high-risk assets.

This combined indicator approach establishes the groundwork for making data-driven trading decisions.

### 4. Sentiment Analysis

In this phase, sentiment analysis is performed to capture market sentiment, offering an additional layer of insight.

- **Date Handling**: Captures today's and yesterday's dates to retrieve relevant news articles for sentiment analysis.
- **Function**: **`analyze_sentiment(company_name)`**
  - **Purpose**: Fetches news articles for a given company to analyze the public sentiment surrounding the asset.
- **Sentiment Classification**:
  - **Methodology**: Uses the VADER sentiment analysis tool to classify news summaries as positive, neutral, or negative.
  - **Utility**: By quantifying sentiment, the strategy can better gauge the market’s stance on each asset.
- **Visualization**:
  - **Output**: Generates a pie chart summarizing sentiment distribution across positive, neutral, and negative sentiments, offering a quick visual of overall market sentiment.

This sentiment analysis process captures the public perception surrounding assets, which can be valuable in making or adjusting trading decisions.

### 5. Portfolio Assignment and Management

This step allocates funds across assets based on a combination of technical scores, sentiment, and volatility adjustments.

- **Inputs**:
  - **`daily_scores`**: List of assets with associated daily scores.
  - **`sentiment_scores`**: Dictionary mapping assets to sentiment scores, factoring in the sentiment analysis.
  - **`volatility_scores`**: Dictionary mapping assets to volatility values, allowing for risk adjustments.
  - **`initial_budget`**: The total amount available for investment.
- **Process**:
  - **Calculate Volatility-Adjusted Scores**:
    - Each asset’s score is adjusted by dividing its daily score by its volatility and multiplying it by its sentiment score. This adjustment ensures a balanced approach that considers sentiment and risk.
  - **Sort Scores and Allocate Budget**:
    - The adjusted scores are sorted in descending order. Funds are allocated proportionally, giving higher allocations to assets with stronger adjusted scores.
- **Output**:
  - **`portfolio`**: A dictionary with each asset and its allocated amount, creating a balanced and optimized investment portfolio.

### 6. Agentic Workflow and Pseudocode

The following workflow and pseudocode outline how the agent will operate, interact with DeFi primitives, and use sentiment insights from LLMs.

#### Agentic Workflow

1. **Data Acquisition**: Collect real-time data from CEXes, DeFi platforms, and sentiment APIs.
2. **Signal Analysis**: Generate signals based on combined indicators and sentiment data.
3. **Decision Making**: Use generated signals to make buy, sell, or hold decisions.
4. **Execution**: Place orders on exchanges and manage positions based on available budget and risk parameters.
5. **DeFi Interaction**: Monitor lending rates and liquidity trends to adjust positions.
6. **Feedback Loop**: Adapt the strategy as new data becomes available.

#### Pseudocode

```python
def initialize_agent():
    load_trading_strategy()
    connect_to_defi_primitives()
    initialize_llm_endpoint()
    set_risk_management_parameters()

def acquire_data():
    fetch_data_from_cex(orderbook_data)
    fetch_data_from_defi(lending_market_data)
    update_live_data_candles()

def generate_signals(data):
    indicators = calculate_indicators(data)
    entry_exit_signals = analyze_signals(indicators)
    return entry_exit_signals

def execute_trades(signals):
    for signal in signals:
        if signal == 'BUY':
            place_order("BUY", asset)
        elif signal == 'SELL':
            place_order("SELL", asset)
    manage_risk()  # Adjust position size and stop-loss

def interact_with_defi():
    check_lending_rates()
    adjust_positions_based_on_interest()

while trading_session_active:
    data = acquire_data()
    signals = generate_signals(data)
    execute_trades(signals)
    interact_with_defi()
```

---

## Usage and Example

To utilize the notebook, follow these steps:

1. **Run Data Aggregation**: Aggregate market, sentiment, and interest rate data from the specified sources.
2. **Feature Processing**: Compute RSI and dynamic thresholds using `compute_rsi()` and `calculate_dynamic_thresholds()`.
3. **Signal Generation and Scoring**: Apply moving averages to generate buy/sell signals and calculate daily scores.
4. **Sentiment Analysis**: Analyze sentiment using VADER and visualize the results to understand market trends.
