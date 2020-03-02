import argparse
#import midi
from midiutil import MIDIFile

class RudimentGenerator:

	note_value = 0.3333333333333333

	def __init__(self):
		
		print "BPM: %d" % args.bpm
		print "Rudiment Pattern: %s" % args.rudiment_pattern
		
		self.track = 0
		self.channel = 0
		self.time = 0
		self.duration = args.note_tightness
		self.tempo = args.bpm # this libr seems to work except for one reason, everything seems to be half the speed it should be

		self.MyMIDI = MIDIFile(1)
		self.MyMIDI.addTempo(self.track, self.time, self.tempo)

		self.outputFile = args.output

	def generateMidiFromMarkup(self, rudiment_pattern):
		
		print "RUDIMENT: %s" % rudiment_pattern

		for bar in range(0, args.bars):
			self.generateBar(rudiment_pattern)

		#self.endOfTrack()
		self.saveTrack()
	
	#def endOfTrack(self):

		# Add the end of track event, append it to the track
		# eot = midi.EndOfTrackEvent(tick=1)
		# self.track.append(eot)
		# Print out the pattern
		#print self.pattern
	
	def saveTrack(self):
		# Save the pattern to disk
		with open(self.outputFile, "wb") as output_file:
			self.MyMIDI.writeFile(output_file)

	sticking = {
		"l" : 38,
		"r" : 40,
		"L" : 30,
		"R" : 31,
	}
	def left_stick(self):
		print "left"
		self.writeNote(self.sticking["l"])

	def right_stick(self):
		print "right"
		self.writeNote(self.sticking["r"])

	def left_stick_accent(self):
		print "left accent"
		self.writeNote(self.sticking["L"])

	def right_stick_accent(self):
		print "right accent"
		self.writeNote(self.sticking["R"])

	def threeTime(self):
		print "Swap to three time"

	def fourTime(self):
		print "Swap to four time"

	def rest(self):
		self.moveOn()
		print "rest"

	def flam(self):
		print "flam it up"

	rudiments = {
		'single_stroke_roll' : "4Rlrlrlrl",
	    'single_stroke_four' : "3rlrloorlrloo",
	    'liam' : "4RRLLrroo"
	}

	rudiparse = {

		'l' : left_stick,
		'r' : right_stick,
		'L' : left_stick_accent,
		'R' : right_stick_accent,
		'o' : rest,
		'3' : threeTime,
		'4' : fourTime,
		'f' : flam
	}

	def generateBar(self, rudiment_pattern):
		print "generate bar of %s" % rudiment_pattern

		for unit in self.rudiments[rudiment_pattern]:
			if unit == "f":
				print "flam" 
			else:
				self.rudiparse[unit](self)

	def writeNote(self, note):
		velocity = 60

		self.MyMIDI.addNote(self.track, self.channel, note, self.time, self.duration, velocity)
		self.time = self.time + self.note_value

	def moveOn(self):
		print(self.time)
		self.time = self.time + self.note_value

				

parser = argparse.ArgumentParser()

parser.add_argument("rudiment_pattern", help="a rudiment markup pattern to parse")
parser.add_argument("bpm", help="the bpm you wish to generate at", type=int)
parser.add_argument("output", help="the name of the output midi file")
parser.add_argument("-t", "--note_tightness", help="define the length of the midi notes (should relate to difficulty to hit in FE", type=int, default=120)
parser.add_argument("-b", "--bars", help="the number of bars of pattern to generate", type=int)
#parser.add_argument("rudiment", help="the name of the rudiment to generate")
parser.add_argument("-r", "--reverse_sticking", help="reverse the sticking",
                    action="store_true")
args = parser.parse_args()

rg = RudimentGenerator()

rg.generateMidiFromMarkup(args.rudiment_pattern)
