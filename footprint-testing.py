#!/usr/bin/python
import footgen
# using footgen to output geda footprints, and
# footgen doesn't test the footprint generating functions
#
# stand alone function defs for footprints in __init__
# qfn
# so
# soh
# twopad
# tabbed
# dip
# dih
# sip
# bga

footprintlist = [ 'qfn'] #, 'so', 'soh','twopad']

for i in footprintlist:
    f = footgen.Footgen(i+"test")
    getattr(footgen.Footgen,i)(f)
    f.finish()
    

# other function defs in __init__
# sm_pads
# via
# via_array
# themal_pad
# rowofpads
# add_pad
# ballname
# ballpos
# silkbox
# box_corner
# silk_line
# silk_crop


#and more defs in geda.py
#    def __init__(self, part): # part name
#    def mm_to_geda(self, *mm):
#    def _add_pin(self, x, y, name, flags):
#    def _add_pad(self, x, y, name, flags):
#    def add_pad(self, x, y, name):
#    def silk_line(self, x1, y1, x2, y2):
#    def _silk_arc(self, cx, cy, half_width, half_height, start, delta):
#    def silk_arc(self, x1, y1, x2, y2, angle):
#    def silk_circle(self, x, y, radius):
#    def finish(self):

