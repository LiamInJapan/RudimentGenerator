# TODO
# Map to left/right drum stickings
# Get some basic rudiment patterns in
# Work out how to reverse rudiments
# Get all rudiment patterns in
# work out how to do flam roll
# work out how to do buzz roll notes
# work out how to pipe into game front end
# work out how to install dependencies  (https://pip.readthedocs.org/en/stable/user_guide/#requirements-files)
# interface with real snare pad
# get outputted sound running through timidity with drum sounds
# Design some simple markup to reduce code complexity  (e.g. LRLRLRLR -> single stroke LfRLLRfLRR -> paradiddle flam)

'''

Potential spec for rudiment markup

L - left beat
R - right beat
4 - change to 1/4s
3 - change to triplet time
Lf - Left-led flam
Rf - Right-led flam
Lr - Left roll
Rr - Right roll
O - rest
* int - number of repetitions

So for example 10 repetitions of flam paradiddle would transcribe as:

4 Rf L R R Lf R L L * 10

5 bars of single stroke 7 would be 

3 R L R L R L R O O O O O * 5

And so on

'''


import midi
import argparse

class RudimentGenerator:

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

	rudiments = {
		'single_stroke_roll' : "llllllll",
	    'single_stroke_four' : "llllllll",
	    'single_stroke_seven' : "llllllll",
	    'multiple_bounce_roll' : "llllllll",
	    'double_stroke_roll' : "llllllll",
	    'triple_stroke_roll' : "llllllll",
	    'five_stroke_roll' : "llllllll",
	    'six_stroke_roll' : "llllllll",
	    'seven_stroke_roll' : "llllllll",
	    'nine_stroke_roll' : "llllllll",
	    'ten_stroke_roll' : "llllllll",
	    'eleven_stroke_roll' : "llllllll",
	    'thirteen_stroke_roll' : "llllllll",
	    'fifteen_stroke_roll' : "llllllll",
	    'seventeen_stroke_roll' : "llllllll",
	    'single_paradiddle' : "llllllll",
	    'double_paradiddle' : "llllllll",
	    'triple_paradiddle' : "llllllll",
	    'single_paradiddle_diddle' : "llllllll",
	    'flam' : "llllllll",
	    'flam_tap' : "llllllll",
	    'flam_accent' : "llllllll",
	    'flamacue' : "llllllll",
	    'flam_paradiddle' : "llllllll",
	    'single_flammed_mill' : "llllllll",
	    'flam_paradiddle_diddle' : "llllllll",
	    'swiss_army_triplet' : "llllllll",
	    'inverted_flam_tap' : "llllllll",
	    'flam_drag' : "llllllll",
	    'pataflafla' : "llllllll",
	    'drag_ruff' : "llllllll",
	    'single_drag_tap' : "llllllll",
	    'double_drag_tap' : "llllllll",
	    'single_dragadiddle' : "llllllll",
	    'dragadiddle_1' : "llllllll",
	    'dragadiddle_2' : "llllllll",
	    'single_ratamacue' : "llllllll",
	    'double_ratamacue' : "llllllll",
	    'triple_ratamacue' : "llllllll",
	}

	

	def __init__(self, bpm):
		
		print "BPM: %d" % bpm
		self.pattern = midi.Pattern()
		self.track = midi.Track()
		self.pattern.append(self.track)
		self.rest = self.one_beat_value/self.beat_values_new["1/4"][1]
		tempo = midi.SetTempoEvent()
		tempo.set_bpm(bpm)
		self.track.append(tempo)

	def left_stick(self):
		print "left"

		on = midi.NoteOnEvent(tick = self.rest, velocity=120, pitch = self.new_sticking["l"])
		self.track.append(on)
		off = midi.NoteOffEvent(tick = self.rest+10, pitch = self.new_sticking["l"])
		self.track.append(off)
		self.rest = self.one_beat_value/self.beat_values_new["1/4"][1]

	def right_stick(self):
		print "right - Unimplemented Parser"

		on = midi.NoteOnEvent(tick = self.rest, velocity=120, pitch = self.new_sticking["r"])
		self.track.append(on)
		off = midi.NoteOffEvent(tick = self.rest+10, pitch = self.new_sticking["l"])
		self.track.append(off)
		self.rest = self.one_beat_value/self.beat_values_new["1/4"][1]

	def left_stick_accent(self):
		on = midi.NoteOnEvent(tick = self.rest, velocity=120, pitch = self.new_sticking["L"])
		self.track.append(on)
		off = midi.NoteOffEvent(tick = self.rest+10, pitch = self.new_sticking["l"])
		self.track.append(off)
		self.rest = self.one_beat_value/self.beat_values_new["1/4"][1]

	def right_stick_accent(self):
		on = midi.NoteOnEvent(tick = self.rest, velocity=120, pitch = self.new_sticking["R"])
		self.track.append(on)
		off = midi.NoteOffEvent(tick = self.rest+10, pitch = self.new_sticking["l"])
		self.track.append(off)
		self.rest = self.one_beat_value/self.beat_values_new["1/4"][1]

	def four_time(self):
		print "Swap to 3 time"
		self.timing = 4

	def three_time(self):
		print "Swap to 3 time"
		self.timing = 3

	new_sticking = {
		"l" : midi.G_3,
		"r" : midi.G_3+1,
		"L" : midi.G_3+2,
		"R" : midi.G_3+3,
	}

	rudiparse = {

		'l' : left_stick,
		'r' : right_stick,
		'L' : left_stick_accent,
		'R' : right_stick_accent,
		'4' : four_time,
		'3' : three_time,

	}

	def generateMidiFromMarkup(self, rudiment_pattern):
		print "RUDIMENT: %s" % rudiment_pattern
		self.rudiment_pattern = rudiment_pattern
		self.timing = 4

		for unit in rudiment_pattern:
			self.rudiparse[unit](self)

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
#parser.add_argument("bars", help="the number of bars of pattern to generate", type=int)
parser.add_argument("output", help="the name of the output midi file")
#parser.add_argument("rudiment", help="the name of the rudiment to generate")
parser.add_argument("rudiment_pattern", help="a rudiment markup pattern to parse")

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


rg.generateMidiFromMarkup(args.rudiment_pattern)




