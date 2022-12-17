import ROOT as r
import reweight_validation_common

variables = reweight_validation_common.variables

inputs = {}
for inputname,inputcontent in reweight_validation_common.inputs.items():
    #print inputname
    if (not "cHHH1" in inputname):
        #print "not found"
        continue
    inputs[inputname]=inputcontent

#print inputs
