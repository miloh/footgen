Footgen
=======

Footprint generator for Kicad and gEDA in Python

To generate footprints:
<pre><code>
tar -zxf footgen.tar.gz
cd footgen
sudo python setup.py build
sudo python setup.py install
</code></pre>

Use
===

Each script in the example dir silently generates geda/gaf or kicad (geda default) footprint files or a family of footprints in the directory that calls it.
The following commands would create as set of  bga parts in the /project directory
<pre><code>
cd ~/project
python bga.py
</code></pre>


Examples
========
<p>The following is a sample input file which generates some BGA footprints,
Notice how the part statement follows the data defining the part. When the part
statement is issued, the footprint is generated using the last defined
parameters. This allows definition of a family of parts without repeating the
portions which are the same. The script is released under the GPL, but the
footprint definition files and output are public domain. </p>

<p>
    Xilinx BGA packages
    data from XAPP157
    Entered by Darrell Harmon
    values for all 1mm pitch Xilinx BGA
        type = "bga"
        pitch = 1mm
        silkwidth = 10 mils
        silkoffset = 1mm                # used if silkbox is invalid
        dia = 0.4mm
        maskclear = 0.1mm
        polyclear = 6 mil
    Xilinx FT256 1mm pitch BGA
        silkboxwidth = 17mm
        silkboxheight = 17mm
        rows = 16
        cols = 16
    part "FT256"
        rows = 22
        cols = 22
	# some balls missing on FG456
        omitballs = "H8:R8,H8:H15,R8:R15,H15:R15"
    part "FG456"
        rows = 26
        cols = 26
        omitballs = ""
    part "FG676"
        rows = 30
        cols = 30
    part "FG900"
        rows = 34
        cols = 34
    part "FG1156"

</p>

Required parameters for all types
==================================
<pre><code>
generator.mask_clearance = X # soldermask clearance to copper feature, requires declaration of the generator since definition changes based on geda/kicad output 

generator.clearance = X # polygon clearance to copper feature, also requires generator 

type = "bga" or "qfp" or "so" or "twopad" or "tabbed" or "dip" or "sip"

silkwidth???verify this
i/code></pre> 
<pre>
    Parameters for BGA:
    rows
    cols
    pitch
    dia (ball diameter)
    omitballs
    silkboxheight and silkbox width (height and width of silkscreen box)
    or:
    silkoffset (distance from silkscreen box to outside balls
    
    Parameters for QFP:
    pins
    width
    height
    pitch
    padheight
    padwidth
    silkoffset (distance from silkscreen outline to pads)
    silkstyle = "inside" or "outside" or "none"
    
    Parameters for SO:
    pins
    pitch
    width
    padheight
    padwidth
    silkoffset
    
    Parameters for twopad:
    width (space between pads)
    padheight
    padwidth
    silkoffset
    
    Parameters for DIP:
    pins
    width (space between 2 rows of pins)
    pitch (typically 0.1 in)
    paddia (ring around hole)
    drill (hole size)
    
    Parameters for SIP:
    pins
    pitch (typically 0.1 in)
    paddia (ring around hole)
    drill (hole size)
</pre>
