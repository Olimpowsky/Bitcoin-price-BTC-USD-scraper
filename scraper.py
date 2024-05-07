import json
import websocket
import pandas as pd

#change output file format to parquet
parquet_file = 'output.parquet'
buffer = []

def on_message(ws, message):
    message = json.loads(message)
    df = manipulate(message)
    buffer.append(df)
    if len(buffer) >= 20:
        try:
            existing_df = pd.read_parquet(parquet_file)
            df_to_write = pd.concat([existing_df] + buffer)
        except FileNotFoundError:
            df_to_write = pd.concat(buffer)
        
        df_to_write.to_parquet(parquet_file, engine='pyarrow', compression='gzip', index=False)
        buffer.clear()

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
