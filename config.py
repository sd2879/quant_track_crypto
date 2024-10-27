# config.py

import os

DATA_SAVE_PATH_QUANT = os.path.abspath(os.path.join(os.getcwd(), '..', 'quant_data'))

# Ensure the "data" directory exists; if not, create it
if not os.path.exists(DATA_SAVE_PATH_QUANT):
    os.makedirs(DATA_SAVE_PATH_QUANT)

# Define the path to the CSV file containing symbols
SYMBOLS_CSV_PATH = os.path.join(DATA_SAVE_PATH_QUANT, 'top_100_trending_crypto.csv')

# Define the start time for fetching data
START_TIME = '2024-10-26 01:00:00'

# Define the number of days to fetch
NUM_DAYS = 7

# Define the number of symbols to fetch
NUM_SYMBOLS_TO_FETCH = 100

# Define the folder path where the CSV files will be saved
OUTPUT_FOLDER_PATH = os.path.abspath(os.path.join(os.getcwd(), '..', 'quant_data', '7_days_data'))

# Ensure the output folder exists
if not os.path.exists(OUTPUT_FOLDER_PATH):
    os.makedirs(OUTPUT_FOLDER_PATH)

print("Configuration is set up.")
