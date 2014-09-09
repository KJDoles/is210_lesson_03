#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Uses function raw_input and if statement to return BP Status.
'''

BLOOD_PRESS = int(raw_input('What is your blood pressure? '))

if BLOOD_PRESS < 90:
    BP_STATUS = "Low"
elif 90 <= BLOOD_PRESS <= 119:
    BP_STATUS = "Ideal"
elif 120 <= BLOOD_PRESS <= 139:
    BP_STATUS = "Warning"
elif 140 <= BLOOD_PRESS <= 159:
    BP_STATUS = "High"
else:
    BP_STATUS = "Emergency"

print 'Your blood pressure is at a {} level, act accordingly.'.format(BP_STATUS)

