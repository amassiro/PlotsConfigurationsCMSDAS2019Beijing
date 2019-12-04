# cuts

#
# just python ...
#

supercut_vector = [ 
                   'Lepton_pt[0]>20. && Lepton_pt[1]>13.' ,
                   '(abs(Lepton_pdgId[0])==13 || Lepton_pt[0]>25)',
                   '(abs(Lepton_pdgId[1])==13 || Lepton_pt[1]>13)', 
                   '(nLepton>=2 && Alt$(Lepton_pt[2],0)<10.)',
                   'fabs(Lepton_eta[0])<2.5 && fabs(Lepton_eta[1])<2.5',
                   'mll>12.',
                   'PuppiMET_pt > 20.',
                   'ptll > 30.',
                   'Lepton_pdgId[0]*Lepton_pdgId[1] <0',
                   'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13'
                   ]

#
# bveto = Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0
# btag = !(Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0)
#

supercut = ' && '.join(supercut_vector)

#
# Now supercut is defined
#


#
# Standard ones below ...
#

cuts['hww2l2v_13TeV'] = {
   'expr': 'sr',
    # Define the sub-categorization of sr
   'categories' : {
      'em_2j' : ' abs(Lepton_pdgId[0])==11 && multiJet',
      'me_2j' : ' abs(Lepton_pdgId[0])==13 && multiJet',
   }
}




## Top control regions
cuts['hww2l2v_13TeV_top']  = { 
   'expr' : 'topcr',
    # Define the sub-categorization of topcr
   'categories' : {
      '2j' : 'multiJet',
   }
}

## DYtt control regions
cuts['hww2l2v_13TeV_dytt']  = { 
   'expr' : 'dycr',
   # Define the sub-categorization of dycr
   'categories' : { 
      '2j' : 'multiJet',
   }
}
   
  
  
  
   