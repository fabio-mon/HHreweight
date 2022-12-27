# HH reweight
Scripts and macros to reweigh HH simulated events to any (kl,kt,c2,cg,cgg) hyphothesis, and to produce some validation plots. 

## Installation
This script makes use of other repositories which stores the core of the reweight and the plotting utilities.
```
git clone --recurse-submodules https://github.com/fabio-mon/HHreweight.git
cd HHreweight/
source setup.sh
```
The `source setup.sh` command is required at every startup to set the environment variables. 

## Usage with examples
Independent scripts are available to carry out different operations. The usage instructions with examples are provided below.

### Dump gen level information from CMS nanoAOD
The ROOT macro `nanoaodDumper.C` can process HH powheg MonteCarlo events in the CMS nanoAOD root format. An example command to run of 2017 HH(4b) prelegacy samples is:
```
root -l 'nanoaodDumper.C("configs/GluGluToHHTo4B_node_cHHH0_TuneCP5_RunIIFall17NanoAODv7_realistic_v8-v1.txt","/tmp/fmonti/ttt.root", 1., true, false)'
```


