#!/usr/bin/env python
import os, re, commands
import json

cernboxPath = "gsiftp://eosuserftp.cern.ch//eos/user/a/akalinow/" 
cernboxPath = "/scratch_cmsse/akalinow/CMS/OverlapTrackFinder/Data/SingleMu/" 
cis_endpoint = "https://se.cis.gov.pl"

directories = [    
    "//dpm/cis.gov.pl/home/cms/store/user/jwiechni/HSCP/ag_12_01_2023/"
]

destinationPath = "/Data/HSCP/"

for aDir in directories:
    theSource = cis_endpoint+aDir
    theDestination = cernboxPath + destinationPath
    command = "gfal-copy --timeout 36000 -r "+theSource+ " " + theDestination
    print(command)
    os.system(command)



