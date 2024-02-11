import mido
import time

def delayus(t):
    start = time.time()

mid=mido.MidiFile("test.mid")
track0 = mido.MidiTrack(mid.tracks[0])
clocks_per_click = 24
notes_per_beat = 8;
ticks_per_beat = clocks_per_click*notes_per_beat
tempo = 400000

tTgt = time.time()
tNow = time.time()


for msg in track0:
    md = msg.dict()
    if md['time']>0:
        tTgt += md['time']/ticks_per_beat*tempo/1e6
        while(time.time()<tTgt):
            pass
    if msg.is_meta:
        if md['type']=='time_signature':
            clocks_per_click = md['clocks_per_click']
            notes_per_beat = md['notated_32nd_notes_per_beat']
            ticks_per_beat = clocks_per_click*notes_per_beat
        elif md['type']=='set_tempo':
            tempo = md['tempo']
        elif md['type']=='end_of_track':
            break
        else:
            print(msg)
    else:
        print(msg)
