#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Calculates total principle and compounded interest over the life of a loan.
'''

import decimal
NAME = raw_input('What is your name? ')
PRINC = decimal.Decimal(raw_input('How much will you be borrowing? '))
YEARS = decimal.Decimal(raw_input('How many years are you borrowing for? '))
PRE_QUAL = raw_input('Have you been pre-qualified for a loan? ').lower()[0]
n = decimal.Decimal('12')
INT_RATE = None


if 0 <= PRINC <= 199999:
    if 1 <= YEARS <= 15:
        if PRE_QUAL == ('y'):
            INT_RATE = decimal.Decimal(0.0363)
        else:
            INT_RATE= decimal.Decimal(0.0465)
    elif 16 <= YEARS <= 20:
        if PRE_QUAL == ('y'):
            INT_RATE = decimal.Decimal(0.0404)
        else:
            INT_RATE = decimal.Decimal(0.0498)
    else:
        21 <= YEARS <= 30
        if PRE_QUAL == ('y'):
            INT_RATE = decimal.Decimal(0.0577)
        else:
            INT_RATE = decimal.Decimal(0.0639)
elif 200000 <= PRINC <= 999999:
    if 1 <= YEARS <= 15:
        if PRE_QUAL == ('y'):
            INT_RATE = decimal.Decimal(0.0302)
        else:
            INT_RATE= decimal.Decimal(0.0398)
    elif 16 <= YEARS <= 20:
        if PRE_QUAL == ('y'):
            INT_RATE = decimal.Decimal(0.0327)
        else:
            INT_RATE = decimal.Decimal(0.0408)
    else:
        21 <= YEARS <= 30
        if PRE_QUAL == ('y'):
            INT_RATE = None
        else:
            INT_RATE = decimal.Decimal(0.0466)
else:
    PRINC >= 1000000
    if 1 <= YEARS <= 15:

        if PRE_QUAL == ('y'):
            INT_RATE = decimal.Decimal(0.0205)
        else:
            INT_RATE = None
    elif 16 <= YEARS <= 20:
        if PRE_QUAL == ('y'):
            INT_RATE = decimal.Decimal(0.0262)
        else:
            INT_RATE = None
    else:
        21 <= YEARS <= 30
        INT_RATE = None

TOTAL = 0
if INT_RATE == None:
    TOTAL = 0
else:
    TOTAL = round(PRINC * pow((1 + (INT_RATE / n)),(n * YEARS)))

REPORT = ('Loan Report for: {} \n'.format(NAME)
          + "-"*40 + '\n'
          '\t Principal: \t ${:>7,} \n'.format(PRINC)+
          '\t Duration: \t {:>9} \n'.format(YEARS)+
          '\t Pre-qualified: \t {} \n'.format(PRE_QUAL)+
          '\n'
          '\t Total: \t ${:>1,}'.format(TOTAL))
          
          

