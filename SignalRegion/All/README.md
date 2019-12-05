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


    
combineCards
====

    cd /afs/cern.ch/user/a/amassiro/work/Latinos/Framework/Combine/CMSSW_10_2_13/src/
    cmsenv
    cd -

    combineCards.py SR0jem=datacards/hww2l2v_13TeV_em_0j/mll/datacard.txt \
                    SR0jme=datacards/hww2l2v_13TeV_me_0j/mll/datacard.txt \
                    SR2j=datacards/hww2l2v_13TeV_2j/mll/datacard.txt \
                    TOP0j=datacards/hww2l2v_13TeV_top_0j/njet/datacard.txt \
                    TOP2j=datacards/hww2l2v_13TeV_top_2j/njet/datacard.txt \
                    DY0j=datacards/hww2l2v_13TeV_dytt_0j/njet/datacard.txt \
                    DY2j=datacards/hww2l2v_13TeV_dytt_2j/njet/datacard.txt \
                    > combined.txt

                    
Fit
====

text2workspace.py to make it faster

    text2workspace.py     combined.txt    -o combined.root
    
    combine -M FitDiagnostics   -t -1 --expectSignal=1 combined.root   &> logFit.txt
    combine -M AsymptoticLimits -t -1 --expectSignal=0 combined.root   &> logLimit.txt
    combine -M Significance     -t -1 --expectSignal=1 combined.root   &> logSignificance.txt

    
    
    
Impact plots
====

    http://cms-analysis.github.io/CombineHarvester/
    
    git clone https://github.com/cms-analysis/CombineHarvester.git CombineHarvester
                    
                    
Create impact plots:

    #do the initial fit
    combineTool.py -M Impacts -d combined.root -m 125 --doInitialFit -t -1 --expectSignal=1 -n nuis.125 
    
    # do the initial fit for rateParams separately
    rateparams = CMS_hww_WWnorm0j,CMS_hww_Topnorm0j,CMS_hww_DYttnorm0j,CMS_hww_WWnorm2j,CMS_hww_Topnorm2j,CMS_hww_DYttnorm2j
    ranges = -2,4
    rateparamsrange = ${rateparams//,/=$ranges:}
    
    combineTool.py -M Impacts -d combined.root -m 125 --doInitialFit -t -1 --expectSignal=1 \
                 --named CMS_hww_WWnorm0j,CMS_hww_Topnorm0j,CMS_hww_DYttnorm0j,CMS_hww_WWnorm2j,CMS_hww_Topnorm2j,CMS_hww_DYttnorm2j  \
                 --setParameterRanges CMS_hww_WWnorm0j=-2,4:CMS_hww_Topnorm0j=-2,4:CMS_hww_DYttnorm0j=-2,4:CMS_hww_WWnorm2j=-2,4:CMS_hww_Topnorm2j=-2,4:CMS_hww_DYttnorm2j=-2,4         \
                 -n rateParams.125
    
    # combineTool.py -M Impacts -d combined.root -m 125 --doInitialFit -t -1 --expectSignal=1 --named ${rateparams%?} --setParameterRanges ${rateparamsrange%?} -n rateParams.125
    
    
    # do the fits for each nuisance
    combineTool.py -M Impacts -d combined.root -m 125 --doFits -t -1 --expectSignal=1 --job-mode condor --task-name nuis -n nuis.125 
    
    # do the fit for each rateParam
    combineTool.py -M Impacts -d combined.root -m 125 --doFits -t -1 --expectSignal=1 --job-mode condor --task-name rateParams \
            --named CMS_hww_WWnorm0j,CMS_hww_Topnorm0j,CMS_hww_DYttnorm0j,CMS_hww_WWnorm2j,CMS_hww_Topnorm2j,CMS_hww_DYttnorm2j \
            --setParameterRanges CMS_hww_WWnorm0j=-2,4:CMS_hww_Topnorm0j=-2,4:CMS_hww_DYttnorm0j=-2,4:CMS_hww_WWnorm2j=-2,4:CMS_hww_Topnorm2j=-2,4:CMS_hww_DYttnorm2j=-2,4 \
            -n rateParams.125
    
    # combineTool.py -M Impacts -d combined.root -m 125 --doFits -t -1 --expectSignal=1 --job-mode condor --task-name rateParams --named ${rateparams%?} --setParameterRanges ${rateparamsrange%?} -n rateParams.125
    

Now plots:

    
    #collect job output
    combineTool.py -M Impacts -d combined.root -m 125 -t -1 --expectSignal=1 -o impacts.125.nuis.json -n nuis.125
    
    rateparams = CMS_hww_WWnorm0j,CMS_hww_Topnorm0j,CMS_hww_DYttnorm0j,CMS_hww_WWnorm2j,CMS_hww_Topnorm2j,CMS_hww_DYttnorm2j
    combineTool.py -M Impacts -d combined.root -m 125 -t -1 --expectSignal=1 --named CMS_hww_WWnorm0j,CMS_hww_Topnorm0j,CMS_hww_DYttnorm0j,CMS_hww_WWnorm2j,CMS_hww_Topnorm2j,CMS_hww_DYttnorm2j -o impacts.125.rateParams.json -n rateParams.125
    
    # combineTool.py -M Impacts -d combined.root -m 125 -t -1 --expectSignal=1 --named ${rateparams%?} -o impacts.125.rateParams.json -n rateParams.125
    
    
    #combine the two jsons
    echo "{\"params\":" > impacts.125.json
    jq -s ".[0].params+.[1].params" impacts.125.nuis.json impacts.125.rateParams.json >> impacts.125.json 
    echo ",\"POIs\":" >> impacts.125.json
    jq -s ".[0].POIs" impacts.125.nuis.json impacts.125.rateParams.json >> impacts.125.json
    echo "}" >> impacts.125.json
    # make plots
    plotImpacts.py -i impacts.125.json -o impacts.125 
    
    
    


Complex model 
====


    text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel \
                  --PO 'map=.*/ggH_h*:muGGH[1,0.0,2.0]' \
                  --PO 'map=.*/qqH_h*:muVBF[1,-10.0,9.0]' \
                  combined.txt -o combined.multidim.root
                    

                    
Scan:


    combine -M MultiDimFit -t -1 \
     --setParameters  muGGH=1,muVBF=1 \
     --algo=grid --points=100  \
      combined.multidim.root       >   result.combined.multidim.root.grid.txt

    
    
And via condor:

    combineTool.py -d   combined.multidim.root  -M MultiDimFit    \
               --algo=grid     --X-rtd OPTIMIZE_BOUNDS=0   \
               --setParameters  muGGH=1,muVBF=1 \
               -t -1   -n "mycondor"   \
               --points 100    --job-mode condor \
               --task-name condor-all    \
               --split-points 1 

     
     
     
               
    hadd higgs_2dScan.root   higgsCombinemycondor.POINTS.*.MultiDimFit.mH120.root

    r99t    higgs_2dScan.root     Draw2DImproved.cxx\(\"#mu_\{GGH\}\",\"#mu_\{VBF\}\",\"muGGH\",\"muVBF\",2,\"1\"\)

    
    



               
    
    
    
    