# Overview
This script streams real-time data from Binance for BTCUSDT pairs using WebSockets, processes the data, and appends it to output.csv.

# Requirements
Python packages: pandas, websocket-client

# Usage
Output: Data is saved in output.csv.

Run: Execute the script to start streaming:

# How It Works
on_message: Handles incoming WebSocket messages, parses JSON, and processes data.

manipulate: Extracts and formats relevant data into a DataFrame.
The WebSocket connection runs indefinitely to continuously stream data.
