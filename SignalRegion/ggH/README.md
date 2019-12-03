ggH phase space
====

Analysis



Create histograms
====

Produce shapes:

    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=espresso
    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=workday 
    
    
Check if jobs are done by doing:

    condor_q
    
Add root files:

    mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files
    

Resubmit if needed:

    condor_submit /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__NonPrompt/mkShapes__NonPrompt__ALL__DATA.19.jds
    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__ggWW.0.sh

    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__Vg.4.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__Vg.6.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__ggWW.0.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VgS.0.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VgS.2.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VgS.4.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VgS.8.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VgS.9.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VZ.0.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VZ.1.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VZ.3.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VZ.9.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VZ.11.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VZ.22.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VZ.23.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VZ.24.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VZ.26.jds
    condor_submit  /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__ggH_hww.jds
       
       
       espresso -> workday

    sed -i 's/original/new/g' file.txt

    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__Vg.4.jds
    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__Vg.6.jds
    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__ggWW.0.jds
    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VgS.0.jds
    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VgS.2.jds
    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VgS.4.jds
    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VgS.8.jds
    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VgS.9.jds
    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VZ.0.jds
    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VZ.1.jds
    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VZ.3.jds
    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VZ.9.jds
    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VZ.11.jds
    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VZ.22.jds
    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VZ.23.jds
    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VZ.24.jds
    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__VZ.26.jds
    sed -i 's/espresso/workday/g'    /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/JobsCondor/jobs/mkShapes__ggH/mkShapes__ggH__ALL__ggH_hww.jds
    
        
        
    export _condor_SCHEDD_HOST="bigbird17.cern.ch"
    
    
    
Plots
====

Make plots:


    mkPlot.py --pycfg=configuration.py --inputFile=rootFile/plots_JetScaleNuisances.root

    

Datacard
====

Make datacard:


    mkDatacards.py --pycfg=configuration.py --inputFile=rootFile/plots_JetScaleNuisances.root

    
Check nuisances
====

    cd ../../../LatinoAnalysis/ShapeAnalysis/test/draw

    python DrawNuisancesAll.py \
     --inputFile ../../../../PlotsConfigurationsCMSDAS2019Beijing/Nuisances/JetScale/datacards/df/ptll/shapes/histos_df.root  \
     --outputDirPlots ../../../../PlotsConfigurationsCMSDAS2019Beijing/Nuisances/JetScale/df_nuisance  \
     --nuisancesFile ../../../../PlotsConfigurationsCMSDAS2019Beijing/Nuisances/JetScale/nuisances.py  \
     --samplesFile   ../../../../PlotsConfigurationsCMSDAS2019Beijing/Nuisances/JetScale/samples.py \
     --cutName df
     
    
    
    python DrawNuisancesAll.py \
     --inputFile ../../../../PlotsConfigurationsCMSDAS2019Beijing/Nuisances/JetScale/datacards/df/njet/shapes/histos_df.root  \
     --outputDirPlots ../../../../PlotsConfigurationsCMSDAS2019Beijing/Nuisances/JetScale/df_nuisance_njet  \
     --nuisancesFile ../../../../PlotsConfigurationsCMSDAS2019Beijing/Nuisances/JetScale/nuisances.py  \
     --samplesFile   ../../../../PlotsConfigurationsCMSDAS2019Beijing/Nuisances/JetScale/samples.py \
     --cutName df
    