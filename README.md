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
Independent scripts are available to carry out different operations. The usage instructions are provided below for an example for 2017 HH(4b) prelegacy samples.  

### Dump gen level information from CMS nanoAOD
The ROOT macro `nanoaodDumper.C` can process HH powheg MonteCarlo events in the CMS nanoAOD root format. The function is
```
nanoaodDumper(string filenameslist, string outputfilename, float Normalization = 1., bool RemoveBuggedEvents = true, bool DEBUG = false)
```
The input parameters are: 
* `filenameslist` name of text file containing a list of the paths of the nanoaod files to process. 
* `outputfilename` name of the output file. The macro will dump the information of the two Higgs bosons at the generator in a TTree which will be saved in the output root file. 
* `Normalization` is the overall normalization of the output sample.
* `RemoveBuggedEvents` when true removes all theh events with a generator weight larger than 0.1
* `DEBUG` when true prints some message for the debug

The following commands will process the 4 HH(4b) samples:
```
root -l -q 'nanoaodDumper.C("configs/GluGluToHHTo4B_node_cHHH0_TuneCP5_RunIIFall17NanoAODv7_realistic_v8-v1.txt","path/to/output/directory/GluGluToHHTo4B_node_cHHH0.root", 1., true, false)'
root -l -q 'nanoaodDumper.C("configs/GluGluToHHTo4B_node_cHHH1_TuneCP5_RunIIFall17NanoAODv7_realistic_v8-v1.txt","path/to/output/directory/GluGluToHHTo4B_node_cHHH1.root", 1., true, false)'
root -l -q 'nanoaodDumper.C("configs/GluGluToHHTo4B_node_cHHH2p45_TuneCP5_RunIIFall17NanoAODv7_realistic_v8-v1.txt","path/to/output/directory/GluGluToHHTo4B_node_cHHH2p45.root", 1., true, false)'
root -l -q 'nanoaodDumper.C("configs/GluGluToHHTo4B_node_cHHH5_TuneCP5_RunIIFall17NanoAODv7_realistic_v8-v1.txt","path/to/output/directory/GluGluToHHTo4B_node_cHHH5.root", 1., true, false)'
```

### 

