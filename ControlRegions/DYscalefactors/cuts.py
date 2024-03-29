# cuts

supercut = 'mll>60 && Lepton_pt[0]>20 && Lepton_pt[1]>10 && (nLepton>=2 && Alt$(Lepton_pt[2],0)<10) && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5'


cuts['Zee']  = '(Lepton_pdgId[0] * Lepton_pdgId[1] == -11*11)   \
                 && Lepton_pt[0]>25 && Lepton_pt[1]>13 \
                 && mll>60 && mll<120 \
               '

cuts['Zmm']  = '(Lepton_pdgId[0] * Lepton_pdgId[1] == -13*13)   \
                 && mll>60 && mll<120 \
               '
