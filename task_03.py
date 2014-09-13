#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''Uses raw_input function and nested conditional if statemenst to choose
paint colors.
'''

BASE = raw_input('What base color, Seattle Gray or Manatee? ')

if BASE == 'Seattle Gray':
    ACCENT = raw_input('What accent color, Ceramic Glaze or Cumulus Nimbus? ')
    if ACCENT == 'Ceramic Glaze':
        HIGHLIGHT = raw_input('What highlight color, Basically White or '
                              'White? ')
    else:
        HIGHLIGHT = raw_input('What highlight color, Off-White or Paper '
                              'White? ')
else:
    ACCENT = raw_input('What accent color, Platinum Mist or Spartan Sage? ')
    if ACCENT == 'Platinum Mist':
        HIGHLIGHT = raw_input('What highlight color, Bone White or Just '
                              'White? ')
    else:
        HIGHLIGHT = raw_input('What highlight color, Fractal White or Not '
                              'White? ')

print 'The color choices are {}, {}, and {}.'.format(BASE, ACCENT, HIGHLIGHT)
