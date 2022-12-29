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

The following commands will process the four HH(4b) samples:
```
mkdir -p data/validation/
root -l -q 'nanoaodDumper.C("configs/GluGluToHHTo4B_node_cHHH0_TuneCP5_RunIIFall17NanoAODv7_realistic_v8-v1.txt","data/validation/GluGluToHHTo4B_node_cHHH0.root", 1., true, false)'
root -l -q 'nanoaodDumper.C("configs/GluGluToHHTo4B_node_cHHH1_TuneCP5_RunIIFall17NanoAODv7_realistic_v8-v1.txt","data/validation/GluGluToHHTo4B_node_cHHH1.root", 1., true, false)'
root -l -q 'nanoaodDumper.C("configs/GluGluToHHTo4B_node_cHHH2p45_TuneCP5_RunIIFall17NanoAODv7_realistic_v8-v1.txt","data/validation/GluGluToHHTo4B_node_cHHH2p45.root", 1., true, false)'
root -l -q 'nanoaodDumper.C("configs/GluGluToHHTo4B_node_cHHH5_TuneCP5_RunIIFall17NanoAODv7_realistic_v8-v1.txt","data/validation/GluGluToHHTo4B_node_cHHH5.root", 1., true, false)'
```

### Calculate the (mHH, costhetaHH) normalization
The script `make_norm.py` can process root files containing a TTree with full HH sample to use as base for the reweight, before any analysis selection. The TTree should contain one branch for the mHH and one for the costhetaHH variables at the generator level, as well as the event weight. The command is:
```
python make_norm.py --infilename <Input file name> --intreenames <Input tree name> --outfile <Output file name> --genweightname <Event weight name> --mHHname <mHH branch name> --costhetaHHname <costhetaHH branch name> 
```
The 2D normalization will be stored in the output file as a 2D histogram (TH2F). 

The following commands will prepare the normalization to reweight the HH(4b) samples with kl = {0, 1, 2.45, 5} to the SM (kl=1).
```
mkdir data/reweightinput/

#merge all HH samples to use as input for the reweight
hadd data/reweightinput/GluGluToHHTo4B_all_nodes.root data/validation/GluGluToHHTo4B_node_cHHH0.root data/validation/GluGluToHHTo4B_node_cHHH1.root data/validation/GluGluToHHTo4B_node_cHHH2p45.root data/validation/GluGluToHHTo4B_node_cHHH5.root 

# calculate the normalization
python make_norm.py --infilename data/reweightinput/GluGluToHHTo4B_all_nodes.root --intreenames genEvents  --outfile data/reweightinput/normalization.root --mHHname mHH --costhetaHHname costhetaHH --genweightname weight
```

### Run the reweight
The script `run_reweight.py` processes the HH events in the input TTree, add a re-weight for each requested (kl,kt,c2,cg,cgg) hyphothesis as new branches, and save it in a file in the output directory. The command is:
```
python run_reweight.py --infilename <Input file name> --denominatorfile <Normalization file name> --mHHname <mHH branch name> --costhetaHHname <costhetaHH branch name> --outdir <Output directory>
```
The `--infilename` requires as second argument the files wich contains the TTree with the input events to reweight. Instead, the `--denominatorfile` options requires as second argument the 2D (mHH, costhetaHH) histogram with the normalization. 

The (kl,kt,c2,cg,cgg) points that are targeted by the reweight are defined in a dictionary <label, couplings> [at the beginning of the script](https://github.com/fabio-mon/HHreweight/blob/master/run_reweight.py#L7). Additional points can be added following the same syntax.  

The following commands will run the reweight on the HH(4b) samples which have been mentioned in the previous steps.
```
mkdir data/reweightoutput/
python run_reweight.py --infilename data/reweightinput/GluGluToHHTo4B_all_nodes.root --intreenames genEvents --denominatorfile data/reweightinput/normalization.root --mHHname mHH --costhetaHHname costhetaHH --outdir data/reweightoutput/
```

### Produce validation plots
The script `drawComparisonPlots/drawComparisonPlots.py` can be used to produce validation plots. The command is:
```
python drawComparisonPlots/drawComparisonPlots.py --settings <configuration file name> --outdir <output directory>
```
The configuration file is written in python syntax, in a style similar to CMSSW. It should be stored in the `configs` folder, and it should be provided with neither a relative or absolute path, nor the .py suffix.  

The following commands will produce plots of some relevant kinematic variables comparing the reweighted HH(4b) events to the corresponding genuine MC sample for all the available samples.
```
mkdir plots/
mkdir plots/cHHH0/
python drawComparisonPlots/drawComparisonPlots.py --settings reweight_validation_cHHH0 --outdir ./plots/cHHH0/
mkdir plots/cHHH1/
python drawComparisonPlots/drawComparisonPlots.py --settings reweight_validation_cHHH1 --outdir ./plots/cHHH1/
mkdir plots/cHHH2p45/
python drawComparisonPlots/drawComparisonPlots.py --settings reweight_validation_cHHH2p45 --outdir ./plots/cHHH2p45/
mkdir plots/cHHH5/
python drawComparisonPlots/drawComparisonPlots.py --settings reweight_validation_cHHH5 --outdir ./plots/cHHH5/
```
