import pandas as pd
import numpy as np

def load_data(data_path):
    data = pd.read_csv(data_path)
    return data

