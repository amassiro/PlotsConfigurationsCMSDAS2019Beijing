



mc = [skey for skey in samples if skey != 'DATA' and not skey.startswith('Fake')]



##### Jet energy scale

nuisances['jes'] = {
    'name': 'CMS_scale_j_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc if 'DY' not in skey), 
    'folderUp': mcDirectory + '__JESup',
    'folderDown': mcDirectory + '__JESdo',
    #'folderUp': makeMCDirectory('JESup'),
    #'folderDown': makeMCDirectory('JESdo'),
    #'AsLnN': '1'
}
