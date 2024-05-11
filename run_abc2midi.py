from pathlib import Path
import music21 as m21
import subprocess
import os

def abc2midi(abcfile):
    
    if abcfile is not None:
        abc_file = Path(abcfile)
            #midiname=turn+f'{abc_file.stem}.mid'
        midiname=f'{abc_file.stem}.mid'
        print("ABC")
        print(abcfile)
        temp=m21.converter.parse(abcfile)
        temp.write('midi', fp=midiname)
        print(midiname)
        return 1
        '''try:
            abc_file = Path(abcfile)
            #midiname=turn+f'{abc_file.stem}.mid'
            midiname=f'{abc_file.stem}.mid'
            print("ABC")
            print(abcfile)
            temp=m21.converter.parse(abcfile)
            temp.write('midi', fp=midiname)
            print(midiname)
            return 1
        except:return'''
    return 0

def convert_abc_to_wav(abc_file_path, results_dir="results"):
    abc_file = Path(abc_file_path)  # abc file

    # Convert the ABC file to a MIDI file using abc2midi
    tmp_midi = Path(results_dir) / f'{abc_file.stem}.mid'
    #subprocess.run(["abc2midi", abc_file, "-o", tmp_midi])
    abc2midi(abc_file)
    #print(tmp_midi)
    # Convert MIDI to WAV using MuseScore (requires MuseScore installed)
    wav_file = Path(results_dir) / f'{abc_file.stem}.wav'
    subprocess.run(["../MuseScore-Studio-4.3.0.241231431-x86_64.AppImage", "-f", "-o", wav_file, tmp_midi])

    print(f'output wav file: {wav_file}')
    return wav_file


abc_filepath = 'outputs/test.abc'
results_dir = 'outputs'
wav_filename = convert_abc_to_wav(abc_filepath, results_dir)
if wav_filename:
    print(f"Generated WAV file: {wav_filename}")






