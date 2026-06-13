import time
import requests
import pandas as pd
from pathlib import Path
import json

from conf import *

def get_data():
    """
    Retrieves new data from the Flask server.

    Returns:
        df (pandas.DataFrame): DataFrame containing the new data from the server.
    """
    response = requests.get(SERVER_URL)
    data = response.json()
    df = pd.DataFrame(data)
    df[f'{DATE_TIME_COL}'] = pd.to_datetime(df[f'{DATE_TIME_COL}'])
    # df.set_index(f'{DATE_TIME_COL}', inplace=True)
    return df


def process_stream(new_data: pd.DataFrame) -> None:
    """
    Processes the new data received from the stream.

    Args:
        new_data (pandas.DataFrame): DataFrame containing the new data.

    Returns:
        None
    """
    # User should implement their own processing logic here
    # This is just a placeholder to print the new data for demonstration purposes
    stream_file_path = Path("stream_file.json")
    lines = []
    if stream_file_path.is_file():
        new_data['date'] = new_data['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
        with open(Path.as_posix(stream_file_path), 'a') as output_stream:
            
            for _, r in new_data.iterrows():
                lines.append(json.dumps(r.to_dict())) 
            output_stream.writelines(lines)
            output_stream.write('\n')
    else:
        new_data['date'] = new_data['date'].dt.strftime('%Y-%m-%d %H:%M:%S')
        with open(Path.as_posix(stream_file_path), 'w') as output_stream:
            
            for _, r in new_data.iterrows():
                lines.append(json.dumps(r.to_dict())) 
            output_stream.writelines(lines)
            output_stream.write('\n')
    print(lines)


if __name__ == '__main__':
    # Flask server API endpoint
    SERVER_URL = f"http://{HOST}:{PORT}"
    print(f"Collecting reviews from server: '{SERVER_URL}'...")
    try:
        while True:
            # Get new stream records
            new_data = get_data()
            # Process new stream records
            process_stream(new_data)
            # Sleep for the specified timeout
            time.sleep(TIMEOUT)
    except KeyboardInterrupt:
        print("Stopped collecting restaurant reviews")