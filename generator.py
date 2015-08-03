# TODO
# Map to left/right drum stickings
# Get some basic rudiment patterns in
# Get all rudiment patterns in
# Have BPM and number of bars as program parameters
# Parameterise filename

import midi
# Instantiate a MIDI Pattern (contains a list of tracks)
pattern = midi.Pattern()
# Instantiate a MIDI Track (contains a list of MIDI events)
track = midi.Track()
# Append the track to the pattern
pattern.append(track)
# Instantiate a MIDI note on event, append it to the track

for bar in range(0,4):

	on = midi.NoteOnEvent(tick=0, velocity=120, pitch=midi.G_3+bar)
	track.append(on)
	# Instantiate a MIDI note off event, append it to the track
	off = midi.NoteOffEvent(tick=100, pitch=midi.G_3+bar)
	track.append(off)

# Add the end of track event, append it to the track
eot = midi.EndOfTrackEvent(tick=1)
track.append(eot)
# Print out the pattern
print pattern
# Save the pattern to disk
midi.write_midifile("example.mid", pattern)