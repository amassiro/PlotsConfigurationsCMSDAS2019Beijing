
import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # TheoryScale
configurations = os.path.dirname(configurations) # Nuisances
configurations = os.path.dirname(configurations) # PlotsConfigurationsCMSDAS2019Beijing








# GGHUncertaintyProducer wasn't run for 2017 nAODv5 non-private
thus = [
    'ggH_mu',
    'ggH_res',
    'ggH_mig01',
    'ggH_mig12',
    'ggH_VBF2j',
    'ggH_VBF3j',
    'ggH_pT60',
    'ggH_pT120',
    'ggH_qmtop'
]

for thu in thus:
    aliases[thu] = {
        'linesToAdd': ['.L %s/Nuisances/TheoryScale/gghuncertainty.cc+' % configurations],
        #'linesToAdd': ['.L gghuncertainty.cc+'],
        'class': 'GGHUncertainty',
        'args': (thu,),
        'samples': ['ggH_hww']
    }

