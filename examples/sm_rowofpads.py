#!/usr/bin/python

import footgen
format = "geda"

pads = 7 
pitch = 2
f = footgen.Footgen("sm_rowpart",output_format=format)
f.pitch = pitch
f.padheight = 1.1
f.padwidth = 0.6
f.generator.xsize = f.padwidth
f.generator.ysize = f.padheight
f.generator.clearance = 0.2
f.generator.mask_clearance = 0.08
#rowofpads(self,pos,whichway,startnum,numpads)
f.rowofpads([0,0],"right",1,pads)
f.box_corners(-6.5, -1 , 6.5 , 1 )
f.finish()
