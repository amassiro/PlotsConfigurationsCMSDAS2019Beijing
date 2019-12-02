Theory uncertainties
====

Understanding theory uncertainties.

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


    mkPlot.py --pycfg=configuration.py --inputFile=rootFile/plots_TheoryNuisances.root

    

Datacard
====

Make datacard:


    mkDatacards.py --pycfg=configuration.py --inputFile=rootFile/plots_TheoryNuisances.root

    
Check nuisances
====

    cd ../../../LatinoAnalysis/ShapeAnalysis/test/draw

    python DrawNuisancesAll.py \
     --inputFile ../../../../PlotsConfigurationsCMSDAS2019Beijing/Nuisances/TheoryScale/datacards/df/ptll/shapes/histos_df.root  \
     --outputDirPlots ../../../../PlotsConfigurationsCMSDAS2019Beijing/Nuisances/TheoryScale/df_nuisance  \
     --nuisancesFile ../../../../PlotsConfigurationsCMSDAS2019Beijing/Nuisances/TheoryScale/nuisances.py  \
     --samplesFile   ../../../../PlotsConfigurationsCMSDAS2019Beijing/Nuisances/TheoryScale/samples.py \
     --cutName df
    
     