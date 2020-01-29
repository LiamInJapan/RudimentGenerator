import argparse
import midi

class RudimentGenerator:

	one_beat_value = 1
	base_time = 4
	delta_time = 0

	def __init__(self):
		
		print "BPM: %d" % args.bpm
		print "Rudiment Pattern: %s" % args.rudiment_pattern
		self.pattern = midi.Pattern()
		self.track = midi.Track()
		self.outputFile = args.output
		self.pattern.append(self.track)
		self.note_tightness = args.note_tightness
		tempo = midi.SetTempoEvent()
		tempo.set_bpm(args.bpm)
		#tempo.set_bpm(130)
		print "mpqn: %d" % tempo.get_mpqn()
		self.one_beat_value = args.bpm
		self.track.append(tempo)


	def generateMidiFromMarkup(self, rudiment_pattern):
		
		print "RUDIMENT: %s" % rudiment_pattern

		for bar in range(0, args.bars):
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

	sticking = {
		"l" : 38,
		"r" : 40,
		"L" : 38,
		"R" : 40#31,
	}
	def left_stick(self):
		print "left"
		self.writeNote(self.sticking["l"])
		self.moveOn()

	def right_stick(self):
		print "right"
		self.writeNote(self.sticking["r"])
		self.moveOn()

	def left_stick_accent(self):
		print "left accent"
		self.writeNote(self.sticking["L"])
		self.moveOn()

	def right_stick_accent(self):
		print "right accent"
		self.writeNote(self.sticking["R"])
		self.moveOn()

	def threeTime(self):
		print "Swap to three time"
		#self.base_time = new_time

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
		print "this is where we should write a note... but where?"
		print self.delta_time
		velocity = 60
		on = midi.NoteOnEvent(tick = 0, velocity=velocity, pitch = note)
		self.track.append(on)
		off = midi.NoteOffEvent(tick = self.note_tightness, pitch = note)
		self.track.append(off)
		self.delta_time = 0

	def moveOn(self):
		print "advance time"
		self.delta_time += self.one_beat_value - self.note_tightness
		print "self.delta_time: % d" % self.delta_time 

				

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
