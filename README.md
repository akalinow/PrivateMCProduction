# PrivateMCProduction
Python scripts for running private Monte Carlo event production for the CMS experiment as the LHC.

## Installation instructions:

```Shell
cd CMSSW_14_2_1_pre2/src/
cmsenv
git cms-init 
mkdir -p Configuration/GenProduction/
git clone git@github.com:cms-sw/genproductions.git Configuration/GenProduction
mv  Configuration/GenProduction/genfragments Configuration/GenProduction/python
rm -rf  Configuration/GenProduction/python/ThirteenTeV/DisappTrksAMSB/
rm -rf  Configuration/GenProduction/python/ThirteenTeV/DelayedJets/
rm -rf  Configuration/GenProduction/python/ThirteenTeV/DMSIMP_Extensions
rm -f   Configuration/GenProduction/python/EightTeV/Exotica_HSCP_SIM_cfi.py
scram b -j 4
```

* setup the CMSSW_14_2_1 work area according to the L1PhaseII
  with GeneratorFragments add-ons:

```Shell
 
#Phase-2, NN OMTF, NN for uGMT for displaced, delayed muons
scram project CMSSW CMSSW_14_2_1 -n CMSSW_14_2_1_PhaseII
cd CMSSW_14_2_1_PhaseII/src/
cmsenv
git cms-init
git fetch my-cmssw
git cms-merge-topic -u akalinow/from-CMSSW_14_2_0_pre2_AK_v1

git cms-addpkg L1Trigger/Phase2L1GMT
git cms-addpkg DataFormats/L1TMuonPhase2
git cms-addpkg L1Trigger/L1TMuon

git clone git@github.com:cms-data/L1Trigger-L1TMuon L1Trigger/L1TMuon/data1
mv L1Trigger/L1TMuon/data1/* L1Trigger/L1TMuon/data 
cd 1Trigger/L1TMuon/data/ omtf_config 
scp lxplus.cern.ch:/afs/cern.ch/work/k/kbunkow/public/CMSSW/cmssw_14_x_x/CMSSW_14_2_0_pre2/src/L1Trigger/L1TMuon/data/omtf_config ExtrapolationFactors_ExtraplMB1nadMB2_R_EtaValueP1Scale_t35.xml ./
scp lxplus.cern.ch:/afs/cern.ch/work/k/kbunkow/public/CMSSW/cmssw_14_x_x/CMSSW_14_2_0_pre2/src/L1Trigger/L1TMuon/data/omtf_config/lutNN_omtfRegression_v430_FP.xml ./
scp lxplus.cern.ch:/afs/cern.ch/work/k/kbunkow/public/CMSSW/cmssw_14_x_x/CMSSW_14_2_0_pre2/src/L1Trigger/L1TMuon/data/omtf_config/Patterns_ExtraplMB1andMB2RFixedP_ValueP1Scale_DT_2_2_2_t35__classProb17_recalib2.xml ./
scp lxplus.cern.ch:/afs/cern.ch/work/k/kbunkow/public/CMSSW/cmssw_14_x_x/CMSSW_14_2_0_pre2/src/L1Trigger/L1TMuon/data/omtf_config/muonMatcherHists_100files_smoothStdDev_withOvf.root ./
scp lxplus.cern.ch:/afs/cern.ch/work/k/kbunkow/public/CMSSW/cmssw_14_x_x/CMSSW_14_2_0_pre2/src/L1Trigger/L1TMuon/data/omtf_config/Patterns_ExtraplMB1nadMB2DTQualAndRFixedP_DT_2_2_t30__classProb17_recalib2.xml
git clone git@github.com:akalinow/usercode-OmtfAnalysis UserCode/ -b devel_AK
```

* fetch this repository:

```Shell
git clone git@github.com:akalinow/PrivateMCProduction.git -b devel_14_2_1
cd PrivateMCProduction
```

## Run instructions

* the private generator fragment templates are stored in the [GenFragments](GenFragments) directory
* the details of the generator configuration are set in functions located in [python/utilityFunctions.py
](python/utilityFunctions.py) file

The jobs are submitted with command depending on the process to generate:

* single muons with flat pt spectrum in three bins: [1,10], [10,100], [100, 1000].
```Shell
./submitJobs_SingleMuFlatPt.py
```

* single muons with flat spectrum in 1/pt in range [1,100].
```Shell
./submitJobs_SingleMuOneOverPt.py
```

* exotic scansions: HSCP and displaced:

```Shell
submitJobs_SingleStauFlatPt.py
submitJobs_SingleStopFlatPt.py
submitJobs_SingleDisplacedMuFlatPt.py
```

The eta range is set in the submission script:
```Python
etaRange = (-2.5,2.5)
```

other kinematic parameters are assumed to be fixed, and are set dedicated functions defined in [python/utilityFunctions.py](python/utilityFunctions.py).