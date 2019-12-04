ggH and VBF phase space
====

Analysis



Create histograms
====

Produce shapes:

    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=espresso
    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=workday 
    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=workday  --dry-run
    
    
Check if jobs are done by doing:

    condor_q
    
Add root files:

    mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files
    

Resubmit if needed:

    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__NonPrompt/mkShapes__NonPrompt__ALL__DATA.19.jds
    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__Inclusive/mkShapes__Inclusive__ALL__ggWW.0.sh

    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__Inclusive/mkShapes__Inclusive__ALL__ggH_hww.jds
       
       
       espresso -> workday

    sed -i 's/original/new/g' file.txt

    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__Inclusive/mkShapes__Inclusive__ALL__Vg.4.jds
    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__Inclusive/mkShapes__Inclusive__ALL__Vg.6.jds
        
    export _condor_SCHEDD_HOST="bigbird17.cern.ch"
    
    
    
Plots
====

Make plots:


    mkPlot.py --pycfg=configuration.py --inputFile=rootFile/plots_Inclusive.root

    

Datacard
====

Make datacard:


    mkDatacards.py --pycfg=configuration.py --inputFile=rootFile/plots_Inclusive.root


    