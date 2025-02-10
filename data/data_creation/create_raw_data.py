# this script is used to cast some raw data to represent some example entities we expect to create
# we will use a basic loop to represent a fleet of busses being electrified

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def create_raw_data():
    # we define some parameters to give our dataset some of the masterdata we would expect to see. this would come from data ingestion layer
    # in a production system.
    project_id = "00001"
    emission_type = "CO2"
    emittor_type = "bus"
    vehicle_numbers = list(range(1, 13))  # vehicle numbers
    start_date = datetime(2024, 1, 1) 
    end_date = datetime(2024, 12, 31)

    # generate date range per month
    months = pd.date_range(start=start_date, end=end_date, freq='MS')

    # empty df to save data from loop into
    data = []

    # vehicle types change from 1 (diesel) to 2 (electric) over time
    type_changes = {vn: 1 for vn in vehicle_numbers}

    for month_idx, month in enumerate(months):
        # each month we change one more vehicle to 2.
        if month_idx < len(vehicle_numbers):
            type_changes[vehicle_numbers[month_idx]] = 2
        
        for vn in vehicle_numbers:
            data.append({
                "project_ID": project_id,
                "emission_type": emission_type,
                "emittor_type": emittor_type,
                "vehicle_type": type_changes[vn],
                "vehicle_number": vn,
                "distance_travelled": np.random.randint(1000, 3001),
                "date": month.strftime('%Y-%m-%d')
            })

    # Create DataFrame
    df = pd.DataFrame(data)
    return df
