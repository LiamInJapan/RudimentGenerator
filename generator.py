# TODO
# Map to left/right drum stickings
# Get some basic rudiment patterns in
# Work out how to reverse rudiments
# Get all rudiment patterns in
# work out how to do flam
# work out how to do buzz roll

import midi
import argparse

class RudimentGenerator:

	sticking = {
		False : midi.G_3,
		True : midi.G_3+1,
	}

	left_stick = False

	def single_stroke_roll(self):
		for beat in range(0,4):
			on = midi.NoteOnEvent(tick=0, velocity=120, pitch=self.sticking[self.left_stick])
			self.track.append(on)
			off = midi.NoteOffEvent(tick=100, pitch=self.sticking[self.left_stick])
			self.track.append(off)
			self.left_stick = not self.left_stick

	# TODO: Triplify this
	def single_stroke_four(self):

		for beat in range(0,4):
			on = midi.NoteOnEvent(tick=100+self.offset, velocity=120, pitch=self.sticking[self.left_stick])
			self.track.append(on)
			off = midi.NoteOffEvent(tick=100, pitch=self.sticking[self.left_stick])
			self.track.append(off)
			self.left_stick = not self.left_stick
			self.offset = 0

		self.offset = 100

	def single_stroke_seven(self):

		print "LLLLLLL"

	

	rudiments = {
		'single_stroke_roll': single_stroke_roll,
	    'single_stroke_four': single_stroke_four,
	    'single_stroke_seven': single_stroke_seven,	
	}

	def __init__(self, bpm):
		
		self.pattern = midi.Pattern()
		self.track = midi.Track()
		self.pattern.append(self.track)
		self.offset = 0
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

rg = RudimentGenerator(120)

if args.reverse_sticking:
	print "reverse sticking"
	rg.left_stick = not rg.left_stick
else:
	print "sticking is normal"

args = parser.parse_args()


rg.generateRudiments(args.bars)




