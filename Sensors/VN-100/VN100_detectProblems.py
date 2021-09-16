#!/usr/bin/env python

"""
Simple function to determine if there are major movements with the IMU based on the yaw, pitch, and roll.
"""

import pandas as pd

def updateMean(avg):
    prev_mean = mean_list[0]
    mean_list.remove(prev_mean)
    new_mean = (prev_mean + avg) / 2
    mean_list.append(new_mean)

def detectProblems(file):
    # Read the csv
    df = pd.read_csv(file)
    # Determine if there are any major changes in yaw, pitch, or roll
    list = ["Yaw", "Pitch", "Roll"]
    for item in list:
        stats = df[item].describe() # Get summary statistics
        mean = stats[1]
        updateMean(mean)
        std = stats[2]
        out_thres_max = mean + 1.5 * std # outlier threshold --- use this for now
        out_thres_min = mean - 1.5 * std
        for val in df[item]:
            # Profit
            if val > out_thres_max or val < out_thres_min:
                return (True, mean_list) # returns true if there's a problem
    return (False, mean_list)


if __name__ == "__main__":
    path = "VNYMR.csv"
    mean_list = [0, 0, 0]
    while(True):
        output = detectProblems(path)
        problem = (output[0] == True):
        if (problem):
            # Do something
            pass
             

