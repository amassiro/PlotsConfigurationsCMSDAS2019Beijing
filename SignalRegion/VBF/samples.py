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

fakeSteps = 'DATAl1loose2017v5__l2loose__fakeW'



def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcReco, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcReco, mcSteps.format(var=''))

#mcDirectory = os.path.join(treeBaseDir, mcReco, mcSteps)         # --> treeBaseDir/mcReco/mcSteps
mcDirectory = makeMCDirectory()




#/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Fall2017_102X_nAODv5_SigOnly_Full2017v5/MCl1loose2017v5__MCCorr2017v5__l2loose__l2tightOR2017v5__wwSel/
mcRecoSignal = 'Fall2017_102X_nAODv5_SigOnly_Full2017v5'

def makeMCDirectorySignal(var=''):
    if var:
        return os.path.join(treeBaseDir, mcRecoSignal, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcRecoSignal, mcSteps.format(var=''))

mcDirectorySignal = makeMCDirectorySignal()


dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)   # --> treeBaseDir/dataReco/dataSteps
fakeDirectory = os.path.join(treeBaseDir, dataReco, fakeSteps)   # --> treeBaseDir/dataReco/fakeSteps





################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
    ['B','Run2017B-Nano14Dec2018-v1'],
    ['C','Run2017C-Nano14Dec2018-v1'],
    ['D','Run2017D-Nano14Dec2018-v1'],
    ['E','Run2017E-Nano14Dec2018-v1'],
    ['F','Run2017F-Nano14Dec2018-v1']
]

DataSets = ['MuonEG','SingleMuon','SingleElectron','DoubleMuon', 'DoubleEG']

DataTrig = {
    'MuonEG'         : ' Trigger_ElMu' ,
    'SingleMuon'     : '!Trigger_ElMu && Trigger_sngMu' ,
    'SingleElectron' : '!Trigger_ElMu && !Trigger_sngMu && Trigger_sngEl',
    'DoubleMuon'     : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && Trigger_dblMu',
    'DoubleEG'       : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && !Trigger_dblMu && Trigger_dblEl'
}





#########################################
############ MC COMMON ##################
#########################################

#
# SFweight does not include btag weights
#
# -> genmatching is not required for Vg sample
#

# SFweight does not include btag weights
mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'




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



###### Top #######

files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ST_s-channel') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_top')

samples['top'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 1,
}


###### WW ########

samples['WW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu'),
    'weight': mcCommonWeight + '*nllW',
    'FilesPerJob': 1
}

samples['WWewk'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WpWmJJ_EWK_noTop'),
    'weight': mcCommonWeight + '*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)', #filter tops and Higgs
    'FilesPerJob': 2
}

files = nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENEN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENMN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENTN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNEN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNMN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNTN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNEN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNMN') + \
        nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNTN')

samples['ggWW'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.53/1.4', # updating k-factor
    'FilesPerJob': 10
}

######## Vg ########

files = nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM') + \
    nanoGetSampleFiles(mcDirectory, 'ZGToLLG')

samples['Vg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch + '*!(Gen_ZGstar_mass > 0)',
    'FilesPerJob': 10
}
addSampleWeight(samples, 'Vg', 'ZGToLLG', '(Sum$(GenPart_pdgId == 22 && TMath::Odd(GenPart_statusFlags) && GenPart_pt < 20.) == 0)')

######## VgS ########

files = nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM') + \
    nanoGetSampleFiles(mcDirectory, 'ZGToLLG') + \
    nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')

samples['VgS'] = {
    'name': files,
    #'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'weight': mcCommonWeight + ' * ((Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4) * 0.94 + (Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4) * 1.14)',
    'FilesPerJob': 15,
    'subsamples': {
      'L': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
      'H': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4'
    }
}
addSampleWeight(samples, 'VgS', 'Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'VgS', 'ZGToLLG', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_MomId == 22)*(Sum$(GenPart_pdgId == 22 && TMath::Odd(GenPart_statusFlags) && GenPart_pt < 20.) == 0)')
addSampleWeight(samples, 'VgS', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')

############ VZ ############

files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Q') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo4L') + \
    nanoGetSampleFiles(mcDirectory, 'WZTo2L2Q')

samples['VZ'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.11',
    'FilesPerJob': 2
}

########## VVV #########

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWW')

samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeight
}







###########################################
#############   SIGNALS  ##################
###########################################


#### ggH -> WW

samples['ggH_hww'] = {
    'name': nanoGetSampleFiles(mcDirectorySignal, 'GluGluHToWWTo2L2NuPowheg_M125'),
    'weight': mcCommonWeight,
    #'weight': [mcCommonWeight, {'class': 'Weight2MINLO', 'args': '%s/src/LatinoAnalysis/Gardener/python/data/powheg2minlo/NNLOPS_reweight.root' % os.getenv('CMSSW_BASE')}],
    'FilesPerJob': 4,
    #'linesToAdd': ['.L %s/Differential/weight2MINLO.cc+' % configurations]
}


############ VBF H->WW ############
samples['qqH_hww'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2NuPowheg_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 3
}


############# ZH H->WW ############

samples['ZH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'HZJ_HToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1
}


samples['ggZH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'GluGluZH_HToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 2
}


############ WH H->WW ############

samples['WH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToWW_M125') + nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToWW_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 2
}


############ ttH ############

samples['ttH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'ttHToNonbb_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1
}


############ H->TauTau ############

samples['ggH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectorySignal, 'GluGluHToTauTau_M125_ext1'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1
}


samples['qqH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 2
}


samples['ZH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'HZJ_HToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 2
}


samples['WH_htt'] = {
    'name':  nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToTauTau_M125') + nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 2
}


###########################################




###########################################
################## FAKE ###################
###########################################


samples['Fake'] = {
  'name': [],
  'weight': 'METFilter_DATA*fakeW',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 30
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(fakeDirectory, pd + '_' + sd)
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))

samples['Fake']['subsamples'] = {
  'em': 'abs(Lepton_pdgId[0]) == 11',
  'me': 'abs(Lepton_pdgId[0]) == 13'
}



###########################################
################## DATA ###################
###########################################

samples['DATA'] = {
  'name': [],
  'weight': 'METFilter_DATA*LepWPCut',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 40
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd)
    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))






