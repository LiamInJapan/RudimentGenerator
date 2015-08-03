# TODO
# Map to left/right drum stickings
# Get some basic rudiment patterns in
# Work out how to reverse rudiments
# Get all rudiment patterns in
# work out how to do flam
# work out how to do buzz roll
# work out how to pipe into game front end
# interface with real snare pad
# get outputted sound running through timidity with drum sounds

import midi
import argparse

class RudimentGenerator:

	sticking = {
		False : midi.G_3,
		True : midi.G_3+1,
	}

	beat_values = {
		"1"   : 128,
		"1/2" : 128/2,
		"1/4" : 128/4,
		"1/4t" : ((128/4)*4)/3,
		"1/8" : 128/8,
		"1/8t" : ((128/4)*4)/9,
		"1/16" : 128/16,
		"1/16t" : ((128/4)*4)/27,
		"1/32" : 128/32,
		"1/4t" : ((128/4)*4)/81,
		"1/64" : 128/64,
		"1/4t" : ((128/4)*4)/243,
	}

	one_beat_value = 256

	beat_values_new = {
		"1"     : (1,1),
		"1/2"   : (1,2),
		"1/3"   : (1,3),
		"1/4"   : (1,4),
		"1/6"   : (1,6),
		"1/8"   : (1,8),
		"1/12"  : (1,12),
		"1/16"  : (1,16),
		"1/24"  : (1,24),
		"1/32"  : (1,32),
		"1/48"  : (1,48),
		"1/64"  : (1,64),
		"1/96"  : (1,96),
	}

	left_stick = False

	def single_stroke_roll(self):

		for beat in range(0,4):
			on = midi.NoteOnEvent(tick=self.rest, velocity=120, pitch=self.sticking[self.left_stick])
			self.track.append(on)
			next_beat = self.one_beat_value/self.beat_values_new["1/4"][1]
			off = midi.NoteOffEvent(tick=next_beat, pitch=self.sticking[self.left_stick])
			self.track.append(off)
			self.left_stick = not self.left_stick

	def single_stroke_four(self):

		for beat in range(0,6):
			if(beat < 4):
				on = midi.NoteOnEvent(tick=self.rest, velocity=120, pitch=self.sticking[self.left_stick])
				self.track.append(on)
				self.rest = 0
				next_beat = self.one_beat_value/self.beat_values_new["1/6"][1]
				off = midi.NoteOffEvent(tick=next_beat, pitch=self.sticking[self.left_stick])
				self.track.append(off)
				self.left_stick = not self.left_stick
				self.offset = 0
			else:
				self.rest += self.one_beat_value/self.beat_values_new["1/6"][1]

		#self.offset = self.beat_values["1/4"]

	def single_stroke_seven(self):

		print "Unimplemented Rudiment"

	

	rudiments = {
		'single_stroke_roll': single_stroke_roll,
	    'single_stroke_four': single_stroke_four,
	    'single_stroke_seven': single_stroke_seven,	
	}

	def __init__(self, bpm):
		
		print "BPM: %d" % bpm
		self.pattern = midi.Pattern()
		self.track = midi.Track()
		self.pattern.append(self.track)
		self.rest = 0
		tempo = midi.SetTempoEvent()
		tempo.set_bpm(bpm)
		self.track.append(tempo)


	def generateRudiments(self, bars):
		for bar in range(0,bars):
			self.rudiments[args.rudiment](self)
		self.endOfTrack()
		self.saveTrack()

	def endOfTrack(self):
		# Add the end of track event, append it to the track
		eot = midi.EndOfTrackEvent(tick=1)
		self.track.append(eot)
		# Print out the pattern
		print self.pattern
	
	def saveTrack(self):
		# Save the pattern to disk
		midi.write_midifile(args.output, self.pattern)



parser = argparse.ArgumentParser()

parser.add_argument("bpm", help="the bpm you wish to generate at", type=int)
parser.add_argument("bars", help="the number of bars of pattern to generate", type=int)
parser.add_argument("output", help="the name of the output midi file")
parser.add_argument("rudiment", help="the name of the rudiment to generate")

parser.add_argument("--reverse_sticking", help="reverse the sticking",
                    action="store_true")
args = parser.parse_args()

rg = RudimentGenerator(args.bpm)

if args.reverse_sticking:
	print "reverse sticking"
	rg.left_stick = not rg.left_stick
else:
	print "sticking is normal"

args = parser.parse_args()


rg.generateRudiments(args.bars)




