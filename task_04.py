#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''User is prompted for date and time. If conditions are met, initiates alarm.
'''

DAY = raw_input('What day is it? ').lower()[0:3]
TIME = raw_input('What time is it in a four digit number, no ":"? ')
SNOOZE = True

SNOOZE = True if DAY == 'sat' or DAY == 'sun' or TIME < '0600' else False
if SNOOZE != True:
    print 'Beep! Beep! Beep! Beep! Beep!'
