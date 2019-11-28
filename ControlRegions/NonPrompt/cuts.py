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
                   'mth > 60.',
                   'Lepton_pdgId[0]*Lepton_pdgId[1] >0',
                   ]


supercut = ' && '.join(supercut_vector)

#
# Now supercut is defined
#

#
# and now defines the different phase spaces
#

cuts['SS_df'] =  ' Lepton_pdgId[0]*Lepton_pdgId[1] == 11*13 \
                   && Lepton_pt[1]>20 \
                 '

cuts['SS_0j'] =  ' Lepton_pdgId[0]*Lepton_pdgId[1] == 11*13 \
                   && Lepton_pt[1]>20 \
                   && Alt$(CleanJet_pt[0],0)<30 \
                 '

cuts['SS_1j'] =  ' Lepton_pdgId[0]*Lepton_pdgId[1] == 11*13 \
                   && Lepton_pt[1]>20 \
                   && Alt$(CleanJet_pt[0],0)>30 \
                   && Alt$(CleanJet_pt[1],0)<30 \
                 '

