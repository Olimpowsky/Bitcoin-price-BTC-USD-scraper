import json
import websocket
import pandas as pd

csv_file = 'output.csv'
def on_message(ws, message):
    message = json.loads(message)
    df = manipulate(message)
    df.to_csv(csv_file, mode='a', header=False, index=False)

socket = "wss://stream.binance.com:9443/stream?streams=btcusdt@kline_1m"

def manipulate(source):
    rel_data = source['data']['k']['c']
    evt_time = pd.to_datetime(source['data']['E'], unit='ms')
    df = pd.DataFrame(rel_data, columns=[source['data']['s']], index=[evt_time])
    df.index.name = 'Time'
    df = df.astype(float)
    df = df.reset_index()
    return df

ws = websocket.WebSocketApp(socket, on_message=on_message)
ws.run_forever()

