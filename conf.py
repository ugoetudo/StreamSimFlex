# Sensor API
HOST = 'localhost'
URL_PATH = 'fetchdata'
PORT = '9977'
DATA_TYPE = 'CSV' # 'DATABASE' or 'CSV'
DATASET = r'\\wsl.localhost\Ubuntu\home\uetudo\reviews_csv_format\part-00000-5859fdf9-3d63-477c-a3c8-7721b4a4ef51-c000.csv' # Path of the CSV dataset. Leave empty if you want to stream from database table

# Database Config
DBMS = 'postgresql'
DB_HOST = '<database_host>'
DB_PORT = 5432 # replace with <database_port>
DB_USER = '<database_user>'
DB_PASS = '<database_password>'
DB_NAME = '<database_name>'
DB_TABLE = '<database_table>'

# After each TIMEOUT (seconds), BATCH number of data entries is sent by the API
# Start time is the time recorded data stream is simulated to start from
DATE_TIME_COL = 'date'
BATCH = 1
TIMEOUT = 1
START_TIME = '2012-10-12 00:00:00' # if you aren't getting any data this may be the culprit

# Ingestion Config
OUT_DIR = "stream_sources"
