Z>mumu and Z>ee
====

Steps to follow ...



Create histograms
====

    mkShapeMulti.py

This step reads the post-processed latino trees (samples) and produces histograms 
for several variables and phase spaces (cuts).
It will create some preliminarily histogram (#histo=#cuts*#Variables)
and save the root file containing them in the **outpuDir**. This file
will be used by *mkPlot.py* and *mkDatacards.py*.

**Local Usage** (few samples only and good to test if the configuration is ok):

    mkShapesMulti.py --pycfg=configuration.py --batchSplit=Samples,Files

This is extremely extremely slow, but good for testing.

**Submission** (few samples only):

Produce shapes:

    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=espresso
    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=workday 

    
Check if jobs are done by doing:

    condor_q
    
Add root files:

    mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files
    mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files  --nThreads=6
    
If this is too slow try to hadd manually (TAG is the one in configuration.py)

    cd rootFileTAG
    hadd -j 5 -f plots_ggH_TAG_ALL.root plots_ggH_TAG_ALL_* 


Plots
====

Make plots:

    mkPlot.py --pycfg=configuration.py --inputFile=rootFileTAG/plots_TAG_ALL.root

For unblinding the control regions, comment out the signal regions in cuts.py and set isBlind=0 in plot.py. Then rerun mkPlot.py as above. 

**N.B**: The plots will be generated using the root file created by mkShapes, so
the samples used in plot.py **MUST** be defined in samples.py.


Datacards
====

Make datacards:

    mkDatacards.py --pycfg=configuration.py --inputFile=rootFileTAG/plots_TAG_ALL.root


**N.B**: The datacards will be generated using the root file created by mkShapes, so
the samples used in structure.py **MUST** be defined in samples.py.
    
