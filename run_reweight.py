import os
from array import array
import  NonResonantModelNLO
import ROOT 
from optparse import OptionParser

output_nodes = {
    "cHHH0":    [0.,   1., 0., 0., 0.],
    "cHHH1":    [1.,   1., 0., 0., 0.],
    "cHHH2p45": [2.45, 1., 0., 0., 0.],
    "cHHH5":    [5.,   1., 0., 0., 0.],
}

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
parser.add_option("--denominatorfile",
                  default="/afs/cern.ch/user/f/fmonti/work/flashggFinalFit2/CMSSW_7_4_7/src/flashggFinalFit/Signal/HHreweighter/data/NevNLO_histo_2017_24JUN2021.root",
                  help="File for normalization")
parser.add_option("--denominatorname",
                  default="Nev_histo",
                  help="Name of the TH2F that provides the normalizations")
parser.add_option("--mHHname",
                  default="mhh",
                  help="Name of the branch that stores gen mHH")
parser.add_option("--costhetaHHname",
                  default="absCosThetaStar_CS",
                  help="Name of the branch that stores gen costhetaHH")
parser.add_option("--outdir",
                  default="/tmp/fmonti/",
                  help="Name of the output dir")
(options,args)=parser.parse_args()

#load reweighter
mymodel = NonResonantModelNLO.NonResonantModelNLO()
mymodel.ReadCoefficients("HHStatAnalysis/AnalyticalModels/data/pm_pw_NLO_Ais_13TeV_V2.txt") # local copy of coefficients

#open input file with events to reweight
print "Opening ",options.infilename
infile = ROOT.TFile(options.infilename,"READ")
reduced_infilename = os.path.basename(options.infilename).replace(".root","")#to be used afterwards for outfile naming

#open input file with denominator histogram
denominatorfile = ROOT.TFile(options.denominatorfile)
histo_Nev = denominatorfile.Get(options.denominatorname)# this is a TH2 histo
Nevtot = histo_Nev.Integral() 

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

# opening outfile
outfilename = "%s/%s_reweight.root"%(options.outdir,reduced_infilename)
outfile = ROOT.TFile(outfilename,"RECREATE")

#loop over trees
for i_tree in range(0,len(intreenames)):

    #loading input tree
    treename=intreenames[i_tree]
    foldername=infolders[i_tree]
    infile.ls()
    print("lala %s%s"%(foldername,treename))
    #infile.ls("genDiphotonDumper")
    #infile.ls("genDiphotonDumper/trees")
    #infile.ls(foldername)
    intree = infile.Get("%s%s"%(foldername,treename))
    mHH = array('f', [ 0 ])
    costhetaHH = array('f', [ 0 ])
    intree.SetBranchStatus("*",1)
    intree.SetBranchAddress(options.mHHname,mHH)
    intree.SetBranchAddress(options.costhetaHHname,costhetaHH)

    #prepare output tree
    outfile.cd()
    outdir=outfile.GetDirectory(foldername)
    if not outdir:
        outfile.mkdir(foldername)
    outfile.cd(foldername)
    outtree = intree.CloneTree(0)
    BMreweight = {}
    for node_label in output_nodes.keys():
        BMreweight[node_label] = array('f', [ 0 ])
        outtree.Branch("BMreweight_%s"%node_label,BMreweight[node_label],'BMreweight_%s/F'%node_label)

    print(treename)
    #loop over entries
    i=0;
    nEntries= intree.GetEntries()
    for i in range(0, nEntries):
        intree.GetEntry(i)
        if i%10000==0:
            print "reading entry ",i

        #calculate reweight
        Nev = histo_Nev.GetBinContent( histo_Nev.FindBin(mHH[0], min(0.99,costhetaHH[0])) ) #w/ protection against weird events w/ costhetaHH exactly equal to one
        for node_label,node_couplings in output_nodes.items():
            kl, kt, c2, cg, c2g = node_couplings[0], node_couplings[1], node_couplings[2], node_couplings[3], node_couplings[4]
            XStot = mymodel.getTotalXS(kl, kt, c2, cg, c2g)
            XS = mymodel.getDifferentialXS2D(mHH[0], costhetaHH[0], kl, kt, c2, cg, c2g)
            Noutputev = XS * mymodel.getmHHbinwidth(mHH[0]) * mymodel.getcosthetabinwidth(costhetaHH[0]) 
            BMreweight[node_label][0] = Noutputev/Nev * Nevtot/XStot

        #fill the output tree
        outtree.Fill()
        
    outtree.AutoSave()

outfile.Close()
infile.Close()
