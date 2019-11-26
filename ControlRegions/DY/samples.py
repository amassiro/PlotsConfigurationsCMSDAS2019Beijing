import os

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

#
# function to simplify the life later ...
#

def nanoGetSampleFiles(inputDir, sample):
    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

# samples

try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()


#######################
### Skims and trees ###
#######################

treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'

mcReco = 'Fall2017_102X_nAODv4_Full2017v5'
mcSteps = 'MCl1loose2017v5__MCCorr2017v5__l2loose__l2tightOR2017v5'

dataReco  = 'Run2017_102X_nAODv4_Full2017v5'
dataSteps = 'DATAl1loose2017v5__l2loose__l2tightOR2017v5'

mcDirectory = os.path.join(treeBaseDir, mcReco, mcSteps)         # --> treeBaseDir/mcReco/mcSteps
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)   # --> treeBaseDir/dataReco/dataSteps


################################################################
### Definition of common cuts (on lepton id/iso) and weights ###
################################################################

Nlep='2'

eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'

LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP



################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeight      = 'XSWeight'
SFweight      = 'SFweight'+Nlep+'l*'+LepWPweight+'*'+LepWPCut+'*PrefireWeight'
GenLepMatch   = '(Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1], 0))'



################################################
############ Data declaration ##################
################################################

DataRun = [
    ['B','Run2017B-Nano14Dec2018-v1'],
    #['C','Run2017C-Nano14Dec2018-v1'],
    #['D','Run2017D-Nano14Dec2018-v1'],
    #['E','Run2017E-Nano14Dec2018-v1'],
    #['F','Run2017F-Nano14Dec2018-v1']
]

#DataSets = ['MuonEG','SingleMuon','SingleElectron','DoubleMuon', 'DoubleEG']
DataSets = ['MuonEG','SingleMuon','SingleElectron']

#
# trigger logic:
#
DataTrig = {
    'MuonEG'         : ' Trigger_ElMu' ,
    'SingleMuon'     : '!Trigger_ElMu && Trigger_sngMu' ,
    'SingleElectron' : '!Trigger_ElMu && !Trigger_sngMu && Trigger_sngEl',
    #'DoubleMuon'     : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && Trigger_dblMu',
    #'DoubleEG'       : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && !Trigger_dblMu && Trigger_dblEl'
}

#########################################
############ MC COMMON ##################
#########################################

#
# SFweight does not include btag weights
#
# -> genmatching is not required for Vg sample
#

mcCommonWeightNoMatch = 'XSWeight*' + SFweight + '*METFilter_MC'
mcCommonWeight        = 'XSWeight*' + SFweight + '*' + GenLepMatch +'*METFilter_MC'

###########################################
#############  BACKGROUNDS  ###############
###########################################

###### DY #######

ptllDYW_NLO = '(((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))*(abs(gen_mll-90)<3) + (abs(gen_mll-90)>3))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'

files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO')
    
samples['DY'] = {
        'name': files,
        'weight': mcCommonWeight,
        'FilesPerJob': 8,
}

#                 SampleDictionary       Sample                    weight
addSampleWeight(samples,'DY',        'DYJetsToLL_M-50',           ptllDYW_NLO)
addSampleWeight(samples,'DY',        'DYJetsToLL_M-10to50-LO',    ptllDYW_LO)



###########################################
################## DATA ###################
###########################################

samples['DATA'] = {
  'name': [],
  #'weight': 'METFilter_DATA*LepWPCut',
  'weight': 'METFilter_DATA*'+LepWPCut,
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 40
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd)
    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))



