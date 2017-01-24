Footgen
=======

Footprint generator for Kicad and gEDA in Python

 Installation
```
tar -zxf footgen.tar.gz
cd footgen
sudo python setup.py build
sudo python setup.py install --record install_files.txt
```

 Removal
```
cd footgen
sudo cat install_files.txt | xargs rm -rf
```

Use
===
Each script in the example dir silently generates geda/gaf or kicad (geda default) footprint files or a family of footprints in the directory that calls it.
The following commands would create as set of  bga parts in the /project directory
```
cd ~/project
python bga.py
```

Examples
========

Required parameters for all types
==================================

```
generator.mask_clearance = X # soldermask clearance to copper feature, requires declaration of the generator since definition changes based on geda/kicad output 

generator.clearance = X # polygon clearance to copper feature, also requires generator 

type = "bga" or "qfp" or "so" or "twopad" or "tabbed" or "dip" or "sip"

```

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
