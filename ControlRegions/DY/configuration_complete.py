# example of configuration file
treeName= 'Events'

tag = 'DY2017_final_complete'


# used by mkShape to define output directory for root files
outputDir = 'rootFile'

# file with TTree aliases
# aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py' 

# file with list of samples
#samplesFile = 'samples.py' 
samplesFile = 'samples_complete.py' 

# file with list of samples
#plotFile = 'plot.py' 
plotFile = 'plot_complete.py' 



# luminosity to normalize to (in 1/fb)
lumi = 41.5
#
# run 2017 B only: 4.823
# See https://twiki.cern.ch/twiki/bin/viewauth/CMS/PdmV2017Analysis
#lumi = 4.8


# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = 'plotDY_test3'


# used by mkDatacards to define output directory for datacards
outputDirDatacard = 'datacards'


# structure file for datacard
structureFile = 'structure.py'


# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'