import ROOT as r


r.gROOT.ProcessLineSync(".L drawComparisonPlots/utils.C+")
r.gSystem.Load("drawComparisonPlots/utils_C.so")

variables = {
    "mHH":{
        "formula":"mHH",
        "title":"m_{HH} (GeV)",
        "xmin":250,
        "xmax":5000.,
        "ymin":1.e-07,
        "ymax":1.,
        "Nbin":300
    },

    "leadH_pT":{
        "formula":"leadH.Pt()",
        "title":"lead H p_{T} (GeV)",
        "xmin":0,
        "xmax":2000.,
        "ymin":1.e-07,
        "ymax":1.,
        "Nbin":300
    },

    "subleadH_pT":{
        "formula":"subleadH.Pt()",
        "title":"sublead H p_{T} (GeV)",
        "xmin":0,
        "xmax":2000.,
        "ymin":1.e-07,
        "ymax":1.,
        "Nbin":300
    },

    "HH_pT":{
        "formula":"HHPt(leadH.Pt(), leadH.Eta(), leadH.Phi(), leadH.M(), subleadH.Pt(), subleadH.Eta(), subleadH.Phi(), subleadH.M())", #defined in utils.C
        "title":"HH p_{T} (GeV)",
        "xmin":0,
        "xmax":1000.,
        "ymin":1.e-07,
        "ymax":1.,
        "Nbin":300
    },

    "costhetaHH":{
        "formula":"costhetaHH",
        "title":"cos(#theta*) (GeV)",
        "xmin":0.,
        "xmax":1.,
        #"ymin":0.001,
        #"ymax":1.e+04,
        "Nbin":100
    }
}

inputs = {

    "rewcHHH_to_NLOcHHH0":{
        "title":"Rew. NLO samples",
        "linecolor":r.kGreen+2,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight*BMreweight_cHHH0)",
        "stack":0,
        "filelumis":[
            ["data/reweightoutput/GluGluToHHTo4B_all_nodes_reweight.root",
             "genEvents",1.]
        ]
    },

    "NLOcHHH0":{
        "title":"NLO #kappa_{#lambda}=0",
        "linecolor":r.kBlue,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight)",
        "stack":0,
        "filelumis":[
            ["data/validation/GluGluToHHTo4B_node_cHHH0_TuneCP5_RunIIFall17NanoAODv7_realistic_v8-v1.root",
             "genEvents",1.]
        ]
    },

    "rewcHHH_to_NLOcHHH1":{
        "title":"Rew. NLO samples",
        "linecolor":r.kGreen+2,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight*BMreweight_cHHH1)",
        "stack":0,
        "filelumis":[
            ["data/reweightoutput/GluGluToHHTo4B_all_nodes_reweight.root",
             "genEvents",1.]
        ]
    },

    "NLOcHHH1":{
        "title":"NLO #kappa_{#lambda}=1",
        "linecolor":r.kBlue,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight)",
        "stack":0,
        "filelumis":[
            ["data/validation/GluGluToHHTo4B_node_cHHH1_TuneCP5_RunIIFall17NanoAODv7_realistic_v8-v1.root",
             "genEvents",1.]
        ]
    },

    "rewcHHH_to_NLOcHHH2p45":{
        "title":"Rew. NLO samples",
        "linecolor":r.kGreen+2,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight*BMreweight_cHHH2p45)",
        "stack":0,
        "filelumis":[
            ["data/reweightoutput/GluGluToHHTo4B_all_nodes_reweight.root",
             "genEvents",1.]
        ]
    },

    "NLOcHHH2p45":{
        "title":"NLO #kappa_{#lambda}=2.45",
        "linecolor":r.kBlue,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight)",
        "stack":0,
        "filelumis":[
            ["data/validation/GluGluToHHTo4B_node_cHHH2p45_TuneCP5_RunIIFall17NanoAODv7_realistic_v8-v1.root",
             "genEvents",1.]
        ]
    },

    "rewcHHH_to_NLOcHHH5":{
        "title":"Rew. NLO samples",
        "linecolor":r.kGreen+2,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight*BMreweight_cHHH5)",
        "stack":0,
        "filelumis":[
            ["data/reweightoutput/GluGluToHHTo4B_all_nodes_reweight.root",
             "genEvents",1.]
        ]
    },

    "NLOcHHH5":{
        "title":"NLO #kappa_{#lambda}=1",
        "linecolor":r.kBlue,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight)",
        "stack":0,
        "filelumis":[
            ["data/validation/GluGluToHHTo4B_node_cHHH5_TuneCP5_RunIIFall17NanoAODv7_realistic_v8-v1.root",
             "genEvents",1.]
        ]
    },

}
