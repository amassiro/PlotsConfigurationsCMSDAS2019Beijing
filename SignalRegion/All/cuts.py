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

cuts['hww2l2v_13TeV'] = {
   'expr': 'sr',
    # Define the sub-categorization of sr
   'categories' : {
      'em_0j' : ' abs(Lepton_pdgId[0])==11 && zeroJet',
      'me_0j' : ' abs(Lepton_pdgId[0])==13 && zeroJet',
      'em_1j' : ' abs(Lepton_pdgId[0])==11 && oneJet && Alt$(CleanJet_pt[1],0)<30',
      'me_1j' : ' abs(Lepton_pdgId[0])==13 && oneJet && Alt$(CleanJet_pt[1],0)<30',
      '2j'    : 'multiJet',
   }
}



## Top control regions
cuts['hww2l2v_13TeV_top']  = { 
   'expr' : 'topcr',
    # Define the sub-categorization of topcr
   'categories' : {
      '0j' : 'zeroJet',
      '1j' : 'oneJet && Alt$(CleanJet_pt[1],0)<30',
      '2j' : '(mjj<65 || mjj>105) && mjj<200 && multiJet',
   }
}

## DYtt control regions
cuts['hww2l2v_13TeV_dytt']  = { 
   'expr' : 'dycr',
   # Define the sub-categorization of dycr
   'categories' : { 
      '0j' : 'zeroJet',
      '1j' : 'oneJet && Alt$(CleanJet_pt[1],0)<30',
      '2j' : '(mjj<65 || mjj>105) && mjj<200 && multiJet',
   }
}
   
  
  
  
   