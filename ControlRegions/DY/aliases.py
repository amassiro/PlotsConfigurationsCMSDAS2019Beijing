
# nuisances
#FIXME: TO BE UPDATED FOR 2017!

# name of samples here must match keys in samples.py 

################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity

#mc = [skey for skey in samples if skey != 'DATA' and not skey.startswith('Fake')]
#mcNotDataDriven = [skey for skey in mc if skey != 'WW' and skey != 'DY' and skey != 'DY' and skey !='WW']


nuisances['lumi']  = {
               'name'  : 'lumi_13TeV_2017',
               'type'  : 'lnN',
              }


#nuisances['lumi']  = {
               #'name'  : 'lumi_13TeV_2017',
               #'samples': dict((skey, '1.023') for skey in mc if skey not in ['WW', 'top', 'DY']), 
               #'type'  : 'lnN',
              #}
              
              
              