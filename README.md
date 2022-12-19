# PrivateMCProduction
Python scripts for running private Monte Carlo event production for the CMS experiment as the LHC.

## Installation instructions:

* setup the CMSSW_12_3_0_pre4 work area according to the L1PhaseII
  [TWiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideL1TPhase2Instructions#CMSSW_12_3_0_pre4)
 with GeneratorFragments add-ons:

```Python​
cmsrel CMSSW_12_3_0_pre4
cd CMSSW_12_3_0_pre4/src
cmsenv
git cms-init
git cms-merge-topic -u cms-l1t-offline:l1t-phase2-v3.4.44
mkdir -p Configuration/GenProduction/
git clone git@github.com:cms-sw/genproductions.git Configuration/GenProduction
mv  Configuration/GenProduction/genfragments Configuration/GenProduction/python
rm -rf  Configuration/GenProduction/python/ThirteenTeV/DisappTrksAMSB/
rm -rf  Configuration/GenProduction/python/ThirteenTeV/DelayedJets/
rm -rf  Configuration/GenProduction/python/ThirteenTeV/DMSIMP_Extensions
rm -f   Configuration/GenProduction/python/EightTeV/Exotica_HSCP_SIM_cfi.py
scram b -j 4
```

* fetch this repository:

```Python 
git clone git@github.com:akalinow/PrivateMCProduction.git
cd HSCP_Production
```

## Run instructions

The jobs are submitted with a single command:

```
./submitJobs.py
```

