import mne
import time

def save_bipolar_signal(file, channels, signal, sr):
    info=mne.create_info(channels, sfreq=sr)
    raw_bipolar_data= mne.io.RawArray(signal, info)
    mne.export.export_raw(file,raw_bipolar_data)

def save_markers(file, markers, channels, update_progress_method):
    anywave=open(file,'w')
    anywave.write('// AnyWave Marker File\n')

    n_channels=len(markers)

    for c in range(n_channels):
        for m in markers[c]:
            ch=channels[c]
            label=m[0]
            t=m[1]
            dur=m[2]
            f=m[3]
            line=label+'\t'+str(int(f))+'\t'+str(t)+'\t'+str(dur)+'\t'+ch+'\n'
            anywave.write(line)

        update_progress_method((c+1)/n_channels*100)