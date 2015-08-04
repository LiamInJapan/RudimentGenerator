# TODO
# Map to left/right drum stickings
# Get some basic rudiment patterns in
# Work out how to reverse rudiments
# Get all rudiment patterns in
# work out how to do flam roll
# work out how to do buzz roll notes
# work out how to pipe into game front end
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

	paradiddle = (1,1,2) # index into this with start_index below to get different variations

	def single_paradiddle(self, start_index):

		for beat in range(0,4):

			pass # TODO Implelement
	
	def multiple_bounce_roll(self):

		print "Unimplemented Rudiment"

	def double_stroke_roll(self):

		print "Unimplemented Rudiment"

	def triple_stroke_roll(self):

		print "Unimplemented Rudiment"

	def five_stroke_roll(self):

		print "Unimplemented Rudiment"

	def six_stroke_roll(self):

		print "Unimplemented Rudiment"

	def seven_stroke_roll(self):

		print "Unimplemented Rudiment"

	def nine_stroke_roll(self):

		print "Unimplemented Rudiment"

	def ten_stroke_roll(self):

		print "Unimplemented Rudiment"

	def eleven_stroke_roll(self):

		print "Unimplemented Rudiment"

	def thirteen_stroke_roll(self):

		print "Unimplemented Rudiment"

	def fifteen_stroke_roll(self):

		print "Unimplemented Rudiment"

	def seventeen_stroke_roll(self):

		print "Unimplemented Rudiment"

	def single_paradiddle(self):

		print "Unimplemented Rudiment"

	def double_paradiddle(self):

		print "Unimplemented Rudiment"

	def triple_paradiddle(self):

		print "Unimplemented Rudiment"

	def single_paradiddle_diddle(self):

		print "Unimplemented Rudiment"

	def flam(self):

		print "Unimplemented Rudiment"

	def flam_tap(self):

		print "Unimplemented Rudiment"

	def flam_accent(self):

		print "Unimplemented Rudiment"

	def flamacue(self):

		print "Unimplemented Rudiment"

	def flam_paradiddle(self):

		print "Unimplemented Rudiment"

	def single_flammed_mill(self):

		print "Unimplemented Rudiment"

	def flam_paradiddle_diddle(self):

		print "Unimplemented Rudiment"

	def swiss_army_triplet(self):

		print "Unimplemented Rudiment"

	def inverted_flam_tap(self):

		print "Unimplemented Rudiment"

	def flam_drag(self):

		print "Unimplemented Rudiment"

	def pataflafla(self):

		print "Unimplemented Rudiment"

	def drag_ruff(self):

		print "Unimplemented Rudiment"

	def single_drag_tap(self):

		print "Unimplemented Rudiment"

	def double_drag_tap(self):

		print "Unimplemented Rudiment"

	def single_dragadiddle(self):

		print "Unimplemented Rudiment"

	def dragadiddle_1(self):

		print "Unimplemented Rudiment"

	def dragadiddle_2(self):

		print "Unimplemented Rudiment"

	def single_ratamacue(self):

		print "Unimplemented Rudiment"

	def double_ratamacue(self):

		print "Unimplemented Rudiment"

	def triple_ratamacue(self):

		print "Unimplemented Rudiment"

	rudiments = {
		'single_stroke_roll' : single_stroke_roll,
	    'single_stroke_four' : single_stroke_four,
	    'single_stroke_seven' : single_stroke_seven,
	    'multiple_bounce_roll' : multiple_bounce_roll,
	    'double_stroke_roll' : double_stroke_roll,
	    'triple_stroke_roll' : triple_stroke_roll,
	    'five_stroke_roll' : five_stroke_roll,
	    'six_stroke_roll' : six_stroke_roll,
	    'seven_stroke_roll' : seven_stroke_roll,
	    'nine_stroke_roll' : nine_stroke_roll,
	    'ten_stroke_roll' : ten_stroke_roll,
	    'eleven_stroke_roll' : eleven_stroke_roll,
	    'thirteen_stroke_roll' : thirteen_stroke_roll,
	    'fifteen_stroke_roll' : fifteen_stroke_roll,
	    'seventeen_stroke_roll' : seventeen_stroke_roll,
	    'single_paradiddle' : single_paradiddle,
	    'double_paradiddle' : double_paradiddle,
	    'triple_paradiddle' : triple_paradiddle,
	    'single_paradiddle_diddle' : single_paradiddle_diddle,
	    'flam' : flam,
	    'flam_tap' : flam_tap,
	    'flam_accent' : flam_accent,
	    'flamacue' : flamacue,
	    'flam_paradiddle' : flam_paradiddle,
	    'single_flammed_mill' : single_flammed_mill,
	    'flam_paradiddle_diddle' : flam_paradiddle_diddle,
	    'swiss_army_triplet' : swiss_army_triplet,
	    'inverted_flam_tap' : inverted_flam_tap,
	    'flam_drag' : flam_drag,
	    'pataflafla' : pataflafla,
	    'drag_ruff' : drag_ruff,
	    'single_drag_tap' : single_drag_tap,
	    'double_drag_tap' : double_drag_tap,
	    'single_dragadiddle' : single_dragadiddle,
	    'dragadiddle_1' : dragadiddle_1,
	    'dragadiddle_2' : dragadiddle_2,
	    'single_ratamacue' : single_ratamacue,
	    'double_ratamacue' : double_ratamacue,
	    'triple_ratamacue' : triple_ratamacue,
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




