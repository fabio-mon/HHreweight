
float getCosThetaStar_CS(TLorentzVector h1, TLorentzVector h2)
{
  // cos theta star angle in the Collins Soper frame
  TLorentzVector hh = h1 + h2;
  h1.Boost(-hh.BoostVector());                     
  return h1.CosTheta();
}

vector<string> LoadFilelist(string filenameslist)
{
  ifstream infile(filenameslist.c_str()); 
  string line;
  vector<string> infilenames;
  if (infile.is_open()) {
    while (infile) {
      std::getline(infile,line);
      infilenames.push_back(line);
    }
  }
  return infilenames;
}

void nanoaodDumper(string filenameslist, string outputfilename, bool DEBUG=false)
{
  gROOT->SetBatch(true);

  // load inputfiles in a TChain
  vector<string> infilenames = LoadFilelist(filenameslist);
  TChain* ch = new TChain();
  for(auto infilename : infilenames) {
    cout<<"Adding file "<<infilename<<endl;
    ch->Add((infilename+"/Events").c_str());
  }
  
  // initialize branches of interest
  float Generator_weight;
  unsigned nGenPart;
  float GenPart_eta[200], GenPart_mass[200], GenPart_phi[200], GenPart_pt[200];
  int GenPart_genPartIdxMother[200], GenPart_pdgId[200], GenPart_status[200], GenPart_statusFlags[200];

  ch->SetBranchStatus("*",0);
  ch->SetBranchStatus("Generator_weight",1);
  ch->SetBranchStatus("nGenPart",1);
  ch->SetBranchStatus("GenPart_eta",1);
  ch->SetBranchStatus("GenPart_mass",1);
  ch->SetBranchStatus("GenPart_phi",1);
  ch->SetBranchStatus("GenPart_pt",1);
  ch->SetBranchStatus("GenPart_genPartIdxMother",1);
  ch->SetBranchStatus("GenPart_pdgId",1);
  ch->SetBranchStatus("GenPart_status",1);
  ch->SetBranchStatus("GenPart_statusFlags",1);

  ch->SetBranchAddress("Generator_weight",&Generator_weight);
  ch->SetBranchAddress("nGenPart",&nGenPart);
  ch->SetBranchAddress("GenPart_eta",GenPart_eta);
  ch->SetBranchAddress("GenPart_mass",GenPart_mass);
  ch->SetBranchAddress("GenPart_phi",GenPart_phi);
  ch->SetBranchAddress("GenPart_pt",GenPart_pt);
  ch->SetBranchAddress("GenPart_genPartIdxMother",GenPart_genPartIdxMother);
  ch->SetBranchAddress("GenPart_pdgId",GenPart_pdgId);
  ch->SetBranchAddress("GenPart_status",GenPart_status);
  ch->SetBranchAddress("GenPart_statusFlags",GenPart_statusFlags);

  // prepare output file
  TFile* outtreefile = new TFile(outputfilename.c_str(),"RECREATE");
  outtreefile->cd();
  TTree* outtree = new TTree("genEvents","genEvents");
  int NevMC;
  TLorentzVector h1;
  TLorentzVector h2;
  float mHH;
  float costhetaHH;
  outtree->Branch("weight",&Generator_weight);
  outtree->Branch("mHH",&mHH);
  outtree->Branch("costhetaHH",&costhetaHH);
  outtree->Branch("leadH",&h1);
  outtree->Branch("subleadH",&h2);

  //open the files and loop over entries
  long Nentries = ch->GetEntries();
  cout<<Nentries<<" entries"<<endl;
  NevMC=Nentries; 
  for(long ientry=0;ientry</*20000*/Nentries;++ientry) {
    ch->GetEntry(ientry);
    if(ientry%10000==0)
      cout<<"reading entry "<<ientry<<"\r"<<std::flush;

    //find the gen Higgs
    if(DEBUG)
      cout<<Generator_weight<<endl;
    vector<TLorentzVector> higgsvec;
    for(unsigned ipart=0; ipart<nGenPart; ++ipart) {
      if(DEBUG) {
	cout<<"----"<<endl
	    <<"pdgId "<<GenPart_pdgId[ipart]<<endl
	    <<"status "<<GenPart_status[ipart]<<endl
	    <<"statusFlags "<<GenPart_statusFlags[ipart]<<endl
	    <<"statusFlags_binary "<< std::bitset<16>(GenPart_statusFlags[ipart]).to_string()<<endl
	    <<"mother id "<<GenPart_genPartIdxMother[ipart]<<endl;
	getchar();
      }
      if(GenPart_pdgId[ipart]==25 && GenPart_genPartIdxMother[ipart]==0) {
	if(DEBUG)
	  cout<<"found higgs"<<endl;
	TLorentzVector v;
	v.SetPtEtaPhiM(GenPart_pt[ipart], GenPart_eta[ipart], GenPart_phi[ipart], GenPart_mass[ipart]);
	higgsvec.push_back(v);
      }
    }

    if(higgsvec.size()!=2) {
      cout<<"WARNING: found "<<higgsvec.size()<<" hard higgs --> skip event"<<endl;
      continue;
    }

    if(higgsvec.at(0).Pt() > higgsvec.at(1).Pt()) {
      h1 = higgsvec.at(0);
      h2 = higgsvec.at(1);
    }
    else {
      h2 = higgsvec.at(0);
      h1 = higgsvec.at(1);
    }

    mHH = (h1 + h2).M();
    costhetaHH = getCosThetaStar_CS(h1,h2); 
    outtree->Fill();
  }
  
  //save tree in the outputfile and close
  outtree->AutoSave();
  outtreefile->Close();
  delete ch;

}
