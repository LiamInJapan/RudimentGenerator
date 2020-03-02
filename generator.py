# TODO
# Work out how to reverse rudiments
# Finish all easy rudiment patterns (e.g. ones without rolls)
# program accents in properly
# work out how to install dependencies  (https://pip.readthedocs.org/en/stable/user_guide/#requirements-files)
# work out how to do flam roll
# work out how to do buzz roll notes
# work out how to pipe into game front end
# interface with real snare pad
# get outputted sound running through timidity with drum sounds
# refactor interface more
# fix flam
# add difficult factor (for note length)... Should probably also calculate relative to tempo, or at least do some error checking against tempo so no overlaps



'''

Timidity potentiall useful flags:

-D n, --drum-channel=n
              Marks channel as a drum channel.  If channel is negative, channel -n is marked as an instrumental channel.  If n is 0, all channels  are  marked  as
              instrumental.


dir:directory
       directory/
              Read and play all MIDI files in the specified directory.  For example,

              % timidity some/where/

              plays all files in the directory some/where/.

-c file, --config-file=file
              Reads an extra configuration file.


'''
'''

Spec for rudiment markup

L - left beat
R - right beat
4 - change to 1/4s
3 - change to triplet time
fL - Left-led flam
fR - Right-led flam
rL - Left roll
rR - Right roll
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
import subprocess


class RudimentGenerator:

	one_beat_value = 120

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
		'single_stroke_roll' : "4rlrlrlrl",
	    'single_stroke_four' : "3rlrloorlrloo",
	    'single_stroke_seven' : "6rlrlrlroo",
	    'multiple_bounce_roll' : "llllllll",   # need to think about how to implement bounces e.t.c. with real pad
	    'double_stroke_roll' : "4rrllrrll",
	    'triple_stroke_roll' : "6rrrlllrrrlll",
	    'five_stroke_roll' : "4rrrrRooollllLooo",
	    'five_stroke_roll_triplet' : "6rrllrooollrrlooo",
	    'six_stroke_roll' : "6RoollrrLooRoollrrLoo",  # tweak, check http://vicfirth.com/six-stroke-roll/
	    'seven_stroke_roll' : "6rrllrrLoo",
	    'seven_stroke_roll_triplet' : "6rrllrrLooooo",
	    'nine_stroke_roll' : "6rrllrrllRooo",
	    'ten_stroke_roll' : "6RooolrlrlrlrLooo",  # seems very wrong...
	    'eleven_stroke_roll' : "6rrllrrllrrLooo", 
	    'thirteen_stroke_roll' : "6rrllrrllrrllRooo",
	    'fifteen_stroke_roll' : "6rrllrrllrrllrrRooo",
	    'seventeen_stroke_roll' : "6rrllrrllrrllrrLooo",
	    'single_paradiddle' : "RlrrLrll",
	    'double_paradiddle' : "RlrlrrLrlrll",
	    'triple_paradiddle' : "RlrlrlrrLrlrlrll",
	    'single_paradiddle_diddle' : "RlrrllRlrrll",
	    'flam' : "flooooooofroooooo",
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

	def __init__(self):
		
		print "BPM: %d" % args.bpm
		self.pattern = midi.Pattern()
		self.track = midi.Track()
		self.flam = False
		self.accent = False
		self.rest_beats = 1
		self.outputFile = args.output
		self.pattern.append(self.track)
		self.note_tightness = args.note_tightness
		self.rest = self.one_beat_value/self.beat_values_new["1/4"][1]
		tempo = midi.SetTempoEvent()
		tempo.set_bpm(args.bpm)
		self.track.append(tempo)

	def write_flam_note(self, note):
		on = midi.NoteOnEvent(tick = self.rest, velocity=120, pitch = note)
		self.track.append(on)
		off = midi.NoteOffEvent(tick = self.rest+self.note_tightness, pitch = note)
		self.track.append(off)

		on = midi.NoteOnEvent(tick = self.rest+1, velocity=120, pitch = note+2)
		self.track.append(on)
		off = midi.NoteOffEvent(tick = self.rest+2, pitch = note+2)
		self.track.append(off)

		self.rest = self.one_beat_value/self.beat_values_new["1/%d" % self.timing][1]
		self.rest *= self.rest_beats
		self.flam = False
		self.rest_beats = 1

	def write_note(self, note):
		print "NOTE:"
		print note
		if self.flam == True:
			self.write_flam_note(note)
		else:
			print "before - rest: %d rest_beats: %d" % (self.rest, self.rest_beats)
			self.rest *= self.rest_beats
			print "after - rest: %d rest_beats: %d" % (self.rest, self.rest_beats)
			
			velocity = 60

			if self.accent == True:
				velocity = 120

			self.accent = False

			# this is where the core of the timing stuff is going on it seems...
			on = midi.NoteOnEvent(tick = self.rest, velocity=velocity, pitch = note)
			print "midi on event generated at %d" % self.rest
			self.track.append(on)
			off = midi.NoteOffEvent(tick = self.note_tightness, pitch = note)
			self.track.append(off)
			self.rest = self.one_beat_value/self.beat_values_new["1/%d" % self.timing][1]
			print "self.rest"
			print self.rest
			self.rest_beats = 1
		

	def left_stick(self):
		print "left"
		self.write_note(self.new_sticking["l"])

	def right_stick(self):
		print "right"
		self.write_note(self.new_sticking["r"])

	def left_stick_accent(self):
		print "left accent"
		self.accent = True
		self.write_note(self.new_sticking["L"])

	def right_stick_accent(self):
		print "right accent"
		self.accent = True
		self.write_note(self.new_sticking["R"])

	def time(self, new_time):
		print "Swap to %d time" % new_time
		self.timing = new_time

	def rest(self):
		print "rest"
		self.rest_beats += 1

	new_sticking = {
		"l" : 38,
		"r" : 40,
		"L" : 38,
		"R" : 40,
	}

	rudiparse = {

		'l' : left_stick,
		'r' : right_stick,
		'L' : left_stick_accent,
		'R' : right_stick_accent,
		'o' : rest,
	}

	def generateBar(self, rudiment_pattern):

		print self.rudiments[rudiment_pattern]

		for unit in self.rudiments[rudiment_pattern]:

			print "unit: %s" % unit

			if unit == "f":
				print "prepare for flam"
				self.flam = True   # skip this unit, but note for a flam for next one
			elif unit.isdigit():
				self.time(int(unit))
			else:
				self.rudiparse[unit](self)

	def generateMidiFromMarkup(self, rudiment_pattern):
		
		print "RUDIMENT: %s" % rudiment_pattern

		if rudiment_pattern == "all":
			self.generateAllMidis()
		else:
			self.rudiment_pattern = rudiment_pattern
			self.timing = 4

			for bar in range(0,args.bars):
				self.generateBar(rudiment_pattern)

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
		midi.write_midifile(self.outputFile, self.pattern)

	def generateAllMidis(self):
		for key, value in self.rudiments.iteritems():
			self.outputFile = "./midis/%s.midi" % key
			self.generateMidiFromMarkup(value)



parser = argparse.ArgumentParser()

parser.add_argument("rudiment_pattern", help="a rudiment markup pattern to parse")
parser.add_argument("bpm", help="the bpm you wish to generate at", type=int)
parser.add_argument("output", help="the name of the output midi file")
parser.add_argument("-t", "--note_tightness", help="define the length of the midi notes (should relate to difficulty to hit in FE", type=int, default=30)
parser.add_argument("-b", "--bars", help="the number of bars of pattern to generate", type=int)
#parser.add_argument("rudiment", help="the name of the rudiment to generate")
parser.add_argument("-r", "--reverse_sticking", help="reverse the sticking",
                    action="store_true")
args = parser.parse_args()

rg = RudimentGenerator()

if args.reverse_sticking:
	print "reverse sticking"
	rg.left_stick = not rg.left_stick
else:
	print "sticking is normal"

args = parser.parse_args()
rg.generateMidiFromMarkup(args.rudiment_pattern)

#subprocess.Popen("echo __test__")


