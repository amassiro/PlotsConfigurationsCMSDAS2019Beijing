Experimental uncertainties: JES
====

Understanding experimental uncertainties.

Concentrate on file "nuisances.py"



Create histograms
====

Produce shapes:

    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=espresso
    mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=workday 
    
    
Check if jobs are done by doing:

    condor_q
    
Add root files:

    mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files
    

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
    