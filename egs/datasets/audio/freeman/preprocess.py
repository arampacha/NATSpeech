from data_gen.tts.base_preprocess import BasePreprocessor
import pandas as pd

class FreemanPreprocess(BasePreprocessor):
    def meta_data(self):

        trainscripts = pd.read_csv(f'{self.raw_data_dir}/transcripts.tsv', sep='\t')

        for i, row in trainscripts.iterrows():
            wav_fn = f'{self.raw_data_dir}/wavs/{row.id}.wav'
            yield {'item_name': row.id, 'wav_fn': wav_fn, 'txt': row.transcript}

class FreemanAngryPreprocess(BasePreprocessor):
    def meta_data(self):

        trainscripts = pd.read_csv(f'{self.raw_data_dir}/transcripts.tsv', sep='\t')
        trainscripts = trainscripts[trainscripts.speaker == "Freeman angry"]
        for i, row in trainscripts.iterrows():
            wav_fn = f'{self.raw_data_dir}/wavs/{row.id}.wav'
            yield {'item_name': row.id, 'wav_fn': wav_fn, 'txt': row.transcript}