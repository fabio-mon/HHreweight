import ROOT as r

variables = {
    "mHH":{
        "formula":"mhh",
        "title":"m_{HH} (GeV)",
        "xmin":250,
        "xmax":5000.,
        "ymin":1.e-07,
        "ymax":1.,
        "Nbin":300
    },
    "costhetaHH":{
        "formula":"absCosThetaStar_CS",
        "title":"cos(#theta*) (GeV)",
        "xmin":0.,
        "xmax":1.,
        #"ymin":0.001,
        #"ymax":1.e+04,
        "Nbin":100
    }
}

inputs = {

    "rewcHHH_to_NLOcHHHci":{
        "title":"Rew. NLO samples",
        "linecolor":r.kGreen+2,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight*BMreweight_cHHH0*0.25)",
        "stack":0,
        "filelumis":[
            ["data/output_hh_2017_NLO_reweight.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_NoTag_0",1.],
            ["data/output_hh_2017_NLO_reweight.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_DoubleHTag_0",1.],
            ["data/output_hh_2017_NLO_reweight.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_VBFDoubleHTag_0",1.]
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
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/24JUN2021/merged/output_hh_2017_cHHH0.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_NoTag_0",1.],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/24JUN2021/merged/output_hh_2017_cHHH0.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_DoubleHTag_0",1.],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/24JUN2021/merged/output_hh_2017_cHHH0.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_VBFDoubleHTag_0",1.]
        ]
    },

    "rewcHHH_to_NLOcHHH1":{
        "title":"Rew. NLO samples",
        "linecolor":r.kGreen+2,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight*BMreweight_cHHH1*0.25)",
        "stack":0,
        "filelumis":[
            ["data/output_hh_2017_NLO_reweight.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_NoTag_0",1.],
            ["data/output_hh_2017_NLO_reweight.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_DoubleHTag_0",1.],
            ["data/output_hh_2017_NLO_reweight.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_VBFDoubleHTag_0",1.]
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
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/24JUN2021/merged/output_hh_2017_cHHH1.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_NoTag_0",1.],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/24JUN2021/merged/output_hh_2017_cHHH1.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_DoubleHTag_0",1.],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/24JUN2021/merged/output_hh_2017_cHHH1.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_VBFDoubleHTag_0",1.]
        ]
    },

    "rewcHHH_to_NLOcHHH2p45":{
        "title":"Rew. NLO samples",
        "linecolor":r.kGreen+2,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight*BMreweight_cHHH2p45*0.25)",
        "stack":0,
        "filelumis":[
            ["data/output_hh_2017_NLO_reweight.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_NoTag_0",1.],
            ["data/output_hh_2017_NLO_reweight.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_DoubleHTag_0",1.],
            ["data/output_hh_2017_NLO_reweight.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_VBFDoubleHTag_0",1.]
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
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/24JUN2021/merged/output_hh_2017_cHHH2p45.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_NoTag_0",1.],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/24JUN2021/merged/output_hh_2017_cHHH2p45.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_DoubleHTag_0",1.],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/24JUN2021/merged/output_hh_2017_cHHH2p45.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_VBFDoubleHTag_0",1.]
        ]
    },

    "rewcHHH_to_NLOcHHH5":{
        "title":"Rew. NLO samples",
        "linecolor":r.kGreen+2,
        "fillcolor":0,
        "fillstyle":0,
        "drawstyle":"hist",
        "weight":"(weight*BMreweight_cHHH5*0.25)",
        "stack":0,
        "filelumis":[
            ["data/output_hh_2017_NLO_reweight.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_NoTag_0",1.],
            ["data/output_hh_2017_NLO_reweight.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_DoubleHTag_0",1.],
            ["data/output_hh_2017_NLO_reweight.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_VBFDoubleHTag_0",1.]
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
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/24JUN2021/merged/output_hh_2017_cHHH5.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_NoTag_0",1.],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/24JUN2021/merged/output_hh_2017_cHHH5.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_DoubleHTag_0",1.],
            ["/eos/user/f/fmonti/HHbbgg_run2/workspaces/24JUN2021/merged/output_hh_2017_cHHH5.root",
             "genDiphotonDumper/trees/hh2017_13TeV_125_13TeV_VBFDoubleHTag_0",1.]
        ]
    },

}
