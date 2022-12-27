import os
from array import array
import  NonResonantModelNLO
import ROOT 
from optparse import OptionParser

inputtrees = [
    "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_NoTag_0",
    "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_DoubleHTag_0",
    "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_DoubleHTag_1",
    "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_DoubleHTag_2",
    "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_DoubleHTag_3",
    "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_DoubleHTag_4",
    "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_DoubleHTag_5",
    "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_DoubleHTag_6",
    "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_DoubleHTag_7",
    "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_DoubleHTag_8",
    "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_DoubleHTag_9",
    "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_DoubleHTag_10",
    "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_DoubleHTag_11",
    "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_VBFDoubleHTag_0",
    "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_VBFDoubleHTag_1"
]
defaulinputtrees = (',').join(inputtrees)

parser = OptionParser()
parser.add_option("--infilename",         
                  default="/eos/user/f/fmonti/HHbbgg_run2/workspaces/24JUN2021/merged/output_hh_2017_NLO.root",
                  help="Input file to reweight")
parser.add_option("--intreenames",
                  default=defaulinputtrees,
                  help="List of input trees")
parser.add_option("--outfile",
                  default="./normalization.root",
                  help="Output file name")
parser.add_option("--genweightname",
                  default="weight",
                  help="Name of the branch that stores the gen weight")
parser.add_option("--mHHname",
                  default="mhh",
                  help="Name of the branch that stores gen mHH")
parser.add_option("--costhetaHHname",
                  default="absCosThetaStar_CS",
                  help="Name of the branch that stores gen costhetaHH")
(options,args)=parser.parse_args()

#load reweighter
mymodel = NonResonantModelNLO.NonResonantModelNLO()
mhh_edges = array('f',mymodel.binGenMHH)
ct_edges = array('f',mymodel.binGenCostS)
outfile = ROOT.TFile(options.outfile,"RECREATE")
Nev_histo = ROOT.TH2F("Nev_histo","Nev_histo",len(mhh_edges)-1,mhh_edges,len(ct_edges)-1,ct_edges)

#open input file with events to reweight
print "Opening ",options.infilename
infile = ROOT.TFile(options.infilename,"READ")
reduced_infilename = os.path.basename(options.infilename).replace(".root","")#to be used afterwards for outfile naming

#split tree name from TDirectory
intreenames = []
infolders = []
for fulltreename in options.intreenames.split(','):
    if '/' in fulltreename:
        infolders.append(fulltreename[:fulltreename.rfind('/')+1])
        intreenames.append(fulltreename[fulltreename.rfind('/')+1:])
    else:
        infolders.append("")
        intreenames.append(fulltreename)

#loop over trees
for i_tree in range(0,len(intreenames)):
    #loading input tree
    treename=intreenames[i_tree]
    foldername=infolders[i_tree]
    intree = infile.Get("%s%s"%(foldername,treename))
    weight = array('f', [ 0 ])
    mHH = array('f', [ 0 ])
    costhetaHH = array('f', [ 0 ])
    intree.SetBranchStatus("*",0)
    intree.SetBranchStatus(options.mHHname,1)
    intree.SetBranchStatus(options.genweightname,1)
    intree.SetBranchStatus(options.costhetaHHname,1)

    intree.SetBranchAddress(options.mHHname,mHH)
    intree.SetBranchAddress(options.genweightname,weight)
    intree.SetBranchAddress(options.costhetaHHname,costhetaHH)

    i=0;
    nEntries= intree.GetEntries()
    for i in range(0, nEntries):
        intree.GetEntry(i)
        if i%10000==0:
            print "reading entry ",i
        #TMP
        if(weight[0]>0.1): continue
        #
        Nev_histo.Fill(mHH[0], costhetaHH[0], weight[0]);


outfile.cd()
Nev_histo.Write();
outfile.Close();

