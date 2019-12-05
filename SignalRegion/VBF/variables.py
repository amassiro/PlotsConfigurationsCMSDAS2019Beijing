# variables

#variables = {}

variables['events']  = {   'name': '1',
                        'range' : (1,0,2),
                        'xaxis' : 'events',
                         'fold' : 3
                        }

variables['nvtx']  = {   'name': 'PV_npvsGood',      
                        'range' : (100,0,100),  
                        'xaxis' : 'nvtx', 
                         'fold' : 3
                      }

variables['ptll']  = {   'name': 'ptll',     
                        'range' : (20, 0,200),   
                        'xaxis' : 'p_{T}^{ll} [GeV]',
                        'fold' : 0
                        }

#
# Add eta lepton 1 and 2
# Add lepton 1 pt 
# Add lepton 2 pt 
#




variables['pt1']  = {   'name': 'Lepton_pt[0]',     
                        'range' : (40,0,100),   
                        'xaxis' : 'p_{T} 1st lep',
                        'fold'  : 3                         
                        }

variables['pt2']  = {   'name': 'Lepton_pt[1]',     
                        'range' : (40,0,100),   
                        'xaxis' : 'p_{T} 2nd lep',
                        'fold'  : 3                         
                        }

variables['eta1']  = {  'name': 'Lepton_eta[0]',     
                        'range' : (40,-3,3),   
                        'xaxis' : '#eta 1st lep',
                        'fold'  : 3                         
                        }

variables['eta2']  = {  'name': 'Lepton_eta[1]',     
                        'range' : (40,-3,3),   
                        'xaxis' : '#eta 2nd lep',
                        'fold'  : 3                         
                        }


#
# Number of jets
#


variables['njet']  = {
                        'name': 'Sum$(CleanJet_pt>30)',     
                        'range' : (5,0,5),   
                        'xaxis' : 'Number of jets',
                        'fold' : 2   # 0 = not fold (default), 1 = fold underflowbin, 2 = fold overflow bin, 3 = fold underflow and overflow
                        }



#
# MET
#

variables['puppimet']  = {
                        'name': 'PuppiMET_pt',
                        'range' : (40,0,200),
                        'xaxis' : 'puppimet [GeV]',
                        'fold'  : 3
                        }


#
# More
#

variables['mll'] = {
    'name': 'mll',
    'range': (31,0.,310.)
}

variables['mth'] = {
    'name': 'mth',
    'range': (30,0.,300.),
}




variables['dphill'] = {
    'name': 'abs(dphill)',     
    'range': (20,0,3.14),   
    'xaxis': ' #Delta #phi_{ll}',
}





variables['mjj'] = {
    'name': 'mjj',     
    'range': (100, 50, 1000),   
    'xaxis': ' M_{jj}',
    'fold'  : 3
    
}



variables['detajj'] = {
    'name': 'detajj',     
    'range': (30, 0.0, 6.0),   
    'xaxis': ' #Delta#eta_{jj}',
    'fold'  : 3 
}



