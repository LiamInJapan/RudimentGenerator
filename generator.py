# TODO
# Map to left/right drum stickings
# Get some basic rudiment patterns in
# Get all rudiment patterns in

import midi
import argparse

def single_stroke_roll():

	print "LRLR"
	pass
	#on = midi.NoteOnEvent(tick=0, velocity=120, pitch=midi.G_3+bar)
	#track.append(on)
	#off = midi.NoteOffEvent(tick=100, pitch=midi.G_3+bar)
	#track.append(off)

def single_stroke_seven():

	print "LLLLLLL"
	pass

def single_stroke_four():

	print "LLLL"
	pass
	
def getRudiment(rudiment):
    return {
        'single_stroke_roll': single_stroke_roll(),
        'single_stroke_four': single_stroke_four(),
        'single_stroke_seven': single_stroke_seven(),
    }.get(rudiment) 

parser = argparse.ArgumentParser()

parser.add_argument("bpm", help="the bpm you wish to generate at", type=int)
parser.add_argument("bars", help="the number of bars of pattern to generate", type=int)
parser.add_argument("output", help="the name of the output midi file")
parser.add_argument("rudiment", help="the name of the rudiment to generate")

args = parser.parse_args()

# Instantiate a MIDI Pattern (contains a list of tracks)
pattern = midi.Pattern()
# Instantiate a MIDI Track (contains a list of MIDI events)
track = midi.Track()
# Append the track to the pattern
pattern.append(track)
# Instantiate a MIDI note on event, append it to the track

tempo = midi.SetTempoEvent()
tempo.set_bpm(args.bpm)
track.append(tempo)

for bar in range(0,args.bars):

	getRudiment(args.rudiment)

	#on = midi.NoteOnEvent(tick=0, velocity=120, pitch=midi.G_3+bar)
	#track.append(on)
	# Instantiate a MIDI note off event, append it to the track
	#off = midi.NoteOffEvent(tick=100, pitch=midi.G_3+bar)
	#track.append(off)

# Add the end of track event, append it to the track
eot = midi.EndOfTrackEvent(tick=1)
track.append(eot)
# Print out the pattern
print pattern
# Save the pattern to disk
midi.write_midifile(args.output, pattern)

