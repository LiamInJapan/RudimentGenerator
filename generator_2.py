import argparse
#import midi
from midiutil import MIDIFile

class RudimentGenerator:

	note_value = 1
	double = False
	flam = False
	drag = False
	flam_gap = 0.00390625
	drag_gap = 0.0078125

	def __init__(self):
		print "INIT"

	def generateMidiFromMarkup(self, rudiment_pattern):
		
		self.initTrack()
		print "RUDIMENT: %s" % rudiment_pattern

		if rudiment_pattern == "all":
			self.generateAllMidis()
		else:
			for bar in range(0, args.bars):
				self.generateBar(rudiment_pattern)

		self.saveTrack()
	
	def generateAllMidis(self):
		for key, value in self.rudiments.iteritems():
			print "key"
			print key
			print "value"
			print value
			for bpm in range(30,240,10):
				self.outputFile = "./midis/%s@%s.midi" % (key, bpm)
				self.generateMidiFromMarkup(key)

	def generateStartBeat(self):
		self.rest()
		self.rest()
		self.rest()
		self.rest()

	def initTrack(self):
		
		print "BPM: %d" % args.bpm
		print "Rudiment Pattern: %s" % args.rudiment_pattern

		self.track = 0
		self.channel = 0
		self.time = 0
		self.duration = args.note_tightness
		self.tempo = args.bpm # this libr seems to work except for one reason, everything seems to be half the speed it should be

		self.MyMIDI = MIDIFile(1)
		self.MyMIDI.addTempo(self.track, self.time, self.tempo)

		self.generateStartBeat()

		self.outputFile = args.output

	def saveTrack(self):
		# Save the pattern to disk
		with open(self.outputFile, "wb") as output_file:
			self.MyMIDI.writeFile(output_file)

	accent_vel = {

	}
	sticking = {
		"l" : 38,
		"r" : 40,
		"L" : 38,
		"R" : 40,
	}

	def left_stick(self):
		print "left"
		self.writeNote(self.sticking["l"], 60)

	def right_stick(self):
		print "right"
		self.writeNote(self.sticking["r"], 60)

	def left_stick_accent(self):
		print "left accent"
		self.writeNote(self.sticking["L"], 100)

	def right_stick_accent(self):
		print "right accent"
		self.writeNote(self.sticking["R"], 100)

	def left_stick_double(self):
		self.note_value = self.note_value * 0.5
		self.writeNote(self.sticking["l"], 60)
		self.writeNote(self.sticking["l"], 60)
		self.note_value = self.note_value * 2.0

	def right_stick_double(self):
		self.note_value = self.note_value * 0.5
		self.writeNote(self.sticking["r"], 60)
		self.writeNote(self.sticking["r"], 60)
		self.note_value = self.note_value * 2.0

	def left_stick_accent_double(self):
		self.note_value = self.note_value * 0.5
		self.writeNote(self.sticking["L"], 100)
		self.writeNote(self.sticking["L"], 100)
		self.note_value = self.note_value * 2.0

	def right_stick_accent_double(self):
		self.note_value = self.note_value * 0.5
		self.writeNote(self.sticking["R"], 100)
		self.writeNote(self.sticking["R"], 100)
		self.note_value = self.note_value * 2.0

	def left_flam(self):
		previousNoteValue = self.note_value
		self.note_value = self.flam_gap
		self.time = self.time - self.note_value
		self.writeNote(self.sticking["r"], 32)
		self.time = self.time + self.note_value
		self.writeNote(self.sticking["l"], 60)
		self.note_value = previousNoteValue

	def left_flam_accent(self):
		previousNoteValue = self.note_value
		self.note_value = self.flam_gap
		self.time = self.time - self.note_value
		self.writeNote(self.sticking["R"], 32)
		self.time = self.time + self.note_value
		self.writeNote(self.sticking["L"], 127)
		self.note_value = previousNoteValue

	def right_flam(self):
		previousNoteValue = self.note_value
		self.note_value = self.flam_gap
		self.time = self.time - self.note_value
		self.writeNote(self.sticking["l"], 32)
		self.time = self.time + self.note_value
		self.writeNote(self.sticking["r"], 60)
		self.note_value = previousNoteValue

	def right_flam_accent(self):
		previousNoteValue = self.note_value
		self.note_value = self.flam_gap
		self.time = self.time - self.note_value
		self.writeNote(self.sticking["L"], 32)
		self.time = self.time + self.note_value
		self.writeNote(self.sticking["R"], 127)
		self.note_value = previousNoteValue

	def left_drag(self):
		previousNoteValue = self.note_value
		self.note_value = self.drag_gap * 2
		self.time = self.time - (self.note_value * 2)
		self.writeNote(self.sticking["r"], 32)
		self.time = self.time + self.note_value
		self.writeNote(self.sticking["r"], 32)
		self.time = self.time + self.note_value
		self.writeNote(self.sticking["l"], 60)
		self.note_value = previousNoteValue

	def left_drag_accent(self):
		previousNoteValue = self.note_value
		self.note_value = self.drag_gap * 2
		self.time = self.time - (self.note_value * 2)
		self.writeNote(self.sticking["r"], 32)
		self.time = self.time + self.note_value
		self.writeNote(self.sticking["r"], 32)
		self.time = self.time + self.note_value
		self.writeNote(self.sticking["L"], 127)
		self.note_value = previousNoteValue

	def right_drag(self):
		previousNoteValue = self.note_value
		self.note_value = self.drag_gap * 2
		self.time = self.time - (self.note_value * 2)
		self.writeNote(self.sticking["l"], 32)
		self.time = self.time + self.note_value
		self.writeNote(self.sticking["l"], 32)
		self.time = self.time + self.note_value
		self.writeNote(self.sticking["r"], 60)
		self.note_value = previousNoteValue

	def right_drag_accent(self):
		previousNoteValue = self.note_value
		self.note_value = self.drag_gap * 2
		self.time = self.time - (self.note_value * 2)
		self.writeNote(self.sticking["L"], 32)
		self.time = self.time + self.note_value
		self.writeNote(self.sticking["L"], 32)
		self.time = self.time + self.note_value
		self.writeNote(self.sticking["R"], 127)
		self.note_value = previousNoteValue


	def oneTime(self):
		self.note_value = 1

	def twoTime(self):
		self.note_value = 0.5

	def threeTime(self):
		self.note_value = 0.3333333333333333
		print "Swap to three time"

	def fourTime(self):
		self.note_value = 0.25
		print "Swap to four time"

	def sixTime(self):
		self.note_value = 0.16666667

	def rest(self):
		self.moveOn()
		print "rest"

	def flam(self):
		print "FLAM ON"
		self.flam = True

	def drag(self):
		self.drag = True

	def double(self):
		self.double = True


	rudiments = {
		'single_stroke_roll' : "2rlrlrlrl",
	    'single_stroke_four' : "3rlrloorlrloo",
	    'single_stroke_seven' : "6rlrlrlrooooo",
	    'multiple_bounce_roll' : "llllllll",   # need to think about how to implement bounces e.t.c. with real pad
	    'double_stroke_roll' : "2rrllrrll",
	    'triple_stroke_roll' : "3rrrlllrrrlll",
	    'five_stroke_roll_triplet' : "3RdldrLdrdl",
	    'six_stroke_roll' : "4RdldrLRdldrL", # is this correct?
	    'seven_stroke_roll' : "2dldrdlR",
	    'seven_stroke_roll_triplet' : "6rrllrrLooooo",   # https://www.youtube.com/watch?v=y-ChaSoddlA work it out...
	    'nine_stroke_roll' : "4drdldrdlRooo",
	    'ten_stroke_roll' : "3RdldrdldrLRdldrdldrL",
	    'eleven_stroke_roll' : "3RdldrdldrdlRdldrdldrdl", 
	    'thirteen_stroke_roll' : "3drdldrdldrdlRo",
	    'fifteen_stroke_roll' : "3drdldrdldrdldrL",
	    'seventeen_stroke_roll' : "3drdldrdldrdldrdlRo",  # somethings wrong with this one... Try and link up with metronome beat
	    'single_paradiddle' : "4RlrrLrll",
	    'double_paradiddle' : "4RlrlrrLrlrll",
	    'triple_paradiddle' : "4RlrlrlrrLrlrlrll",
	    'single_paradiddle_diddle' : "4RlrrllRlrrll",
	    'flam' : "4flooofrooo", 
	    'drag' : "4DloooDrooo", 
	    'flam_tap' : "2DRrDLlDRrDLl", # somethings weird here
	    'flam_accent' : "3DRlrDLrl", # somethings weird here
	    'flamacue' : "2frLrlfrooo",
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

	rudiparse = {

		'l' : left_stick,
		'r' : right_stick,
		'L' : left_stick_accent,
		'R' : right_stick_accent,
		'o' : rest,
		'1' : oneTime,
		'2' : twoTime,
		'3' : threeTime,
		'4' : fourTime,
		'6' : sixTime,
		'f' : flam,
		'D' : drag,
		'd' : double
	}

	rudiparse_flams = {
		'l' : left_flam,
		'r' : right_flam,
		'L' : left_flam_accent,
		'R' : right_flam_accent
	}

	rudiparse_drags = {
		'l' : left_drag,
		'r' : right_drag,
		'L' : right_drag_accent,
		'R' : right_drag_accent
	}

	rudiparse_doubles = {
		'l' : left_stick_double,
		'r' : right_stick_double,
		'L' : left_stick_accent_double,
		'R' : right_stick_accent_double,
	}

	def generateBar(self, rudiment_pattern):
		print "generate bar of %s" % rudiment_pattern

		for unit in self.rudiments[rudiment_pattern]:
			if self.flam == True:
				self.rudiparse_flams[unit](self) 
				self.flam = False
			elif self.drag == True:
				self.rudiparse_drags[unit](self)
				self.moveOn()
				self.drag = False
			elif self.double == True:
				self.rudiparse_doubles[unit](self)
				self.moveOn()
				self.double = False
			else:
				print "NORMAL HIT: %s" % unit
				self.rudiparse[unit](self)
				self.moveOn()
				print "NORMAL HIT OFF: %s" % unit


	def writeNote(self, note, velocity):
		print(self.time)
		self.MyMIDI.addNote(self.track, self.channel, note, self.time, self.duration, velocity)

	def moveOn(self):
		print(self.time)
		self.time = self.time + self.note_value

				

parser = argparse.ArgumentParser()

parser.add_argument("rudiment_pattern", help="a rudiment markup pattern to parse")
parser.add_argument("bpm", help="the bpm you wish to generate at", type=int)
parser.add_argument("output", help="the name of the output midi file")
parser.add_argument("-t", "--note_tightness", help="define the length of the midi notes (should relate to difficulty to hit in FE", type=int, default=120)
parser.add_argument("-b", "--bars", help="the number of bars of pattern to generate", type=int)
parser.add_argument("-r", "--reverse_sticking", help="reverse the sticking",
                    action="store_true")
args = parser.parse_args()

rg = RudimentGenerator()

rg.generateMidiFromMarkup(args.rudiment_pattern)
