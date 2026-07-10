#!/usr/bin/env python3

import os

from python.utilityFunctions import *
#########################################
#########################################
genFragmentsDirectory = "Configuration/GenProduction/python/GenFragments/"
generator_fragment=genFragmentsDirectory+"DoubleDisplacedMuPt1to100Eta24Dxy0to100_cfi.py"

era = "Run2029"
workAreaName = "tasks_SingleDisplacedMuFlatPt"
eventsPerJob = 5000
numberOfJobs = 100
outLFNDirBase = "/store/user/akalinow/Data/SingleMu/"
storage_element="T3_CH_CERNBOX"
outputDatasetTag = "14_2_1_10_06_2025"
withPileUp = False
withReco = False
runLocal = False
turnOffG4Secondary = False

iPtTest = None
signTest = 1
etaRange = (-3,3)
##NOTE: displacement expressed in mm
dxyRange = (0,1000)
LxyMax = 100
LzMax = 100
#########################################
#########################################
for iPt in range(0,3):
    for sign in range(-1,2,2):

        if iPtTest!=None and signTest!=None and (iPt!=iPtTest or sign!=signTest):
            continue 

        requestName = "DisplacedMu_ch"+str(sign+1)+"_iPt"+str(iPt)+"_"+era+"_"+outputDatasetTag

        process = runCMSDriver(era, withPileUp, withReco, generator_fragment)
        process = adaptGunParameters(process, iPt, sign, etaRange, turnOffG4Secondary, 
                                    dxyRange=dxyRange, LxyMax=LxyMax, LzMax=LzMax)

        dumpProcess(process, "PSet.py")

        prepareCrabCfg(workAreaName, eventsPerJob, numberOfJobs,
                    outLFNDirBase, storage_element, 
                    requestName, outputDatasetTag)

        if not runLocal:
            os.system("crab submit -c crabTmp.py")
            os.system("rm -f PSet.py* crabTmp.py*")                  
########################################################
