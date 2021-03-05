#!/usr/bin/env python

"""
Module containing the IMU algorithms for detecting severe movement.
"""

def algorithm2(s, prevYaw, prevPitch, prevRoll):
    # Algorithm: Compare the previous and current YPR values to assess major movement
        # Problem:
			# Roll or pitch changes by 45 degrees or more
		    # Yaw changes by 60 degrees or more
    currYPR = s.read_yaw_pitch_roll()
    problem = abs(currYPR.z - prevRoll) >= 45 or abs(currYPR.y - prevPitch) >= 45  or abs(currYPR.x - prevYaw) >= 60
    
    return problem

def algorithm3(model, prevYaw, prevPitch, prevRoll):
    # Algorithm: Use the classifier to predict major movement
    pred = model.predict([[prevYaw, prevPitch, prevRoll, currYPR.x, currYPR.y, currYPR.z]])[0]
    modelProblem = pred == 0
    
    return modelProblem

def algorithm4(s, model, prevYaw, prevPitch, prevRoll):
    # Algorithm: Combine both of the previous algorithms
    currYPR = s.read_yaw_pitch_roll()
    problem = abs(currYPR.z - prevRoll) >= 45 or abs(currYPR.y - prevPitch) >= 45  or abs(currYPR.x - prevYaw) >= 60
    
    pred = model.predict([[prevYaw, prevPitch, prevRoll, currYPR.x, currYPR.y, currYPR.z]])[0]
    modelProblem = pred == 0

    return problem or modelProblem
