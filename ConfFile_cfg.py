import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        '/store/data/Run2015D/MET/MINIAOD/PromptReco-v3/000/256/729/00000/527DDAFE-1460-E511-94E0-02163E014319.root'
    )
)

process.demo = cms.EDAnalyzer('MyAnalyzer'
)


process.p = cms.Path(process.demo)
