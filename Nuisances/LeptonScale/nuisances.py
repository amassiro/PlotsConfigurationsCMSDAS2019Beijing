



mc = [skey for skey in samples if skey != 'DATA' and not skey.startswith('Fake')]


nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2017',
    'kind': 'tree',
    'type': 'shape',
    'samples': dict((skey, ['1', '1']) for skey in mc if 'DY' not in skey), #FIXME Add DY
    'folderUp': mcDirectory + '__ElepTup',
    'folderDown': mcDirectory + '__ElepTdo',

    #'folderUp': makeMCDirectory('ElepTup'),
    #'folderDown': makeMCDirectory('ElepTdo'),
    #'AsLnN': '1'
}


