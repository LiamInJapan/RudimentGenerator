# RudimentGenerator

A command line drum MIDI Rudiment Generator for the standard 26 Drum Rudiments.

I was looking to download some MIDI of drum rudiments in order to use them for a music game idea I have.
Amazingly there didn't seem to be any out there. So I wrote a generator to make them.

This remains unfinished, I can generate a few rudiments with it, but it's not very extendible. 
The next stage of development is to create a simple domain specific language to describe *any* rudiment.

Pip Install:
http://python-packaging-user-guide.readthedocs.org/en/latest/installing/

MIDI library Install:
https://github.com/vishnubob/python-midi#Installation

usage: 
python generator.py [-h] [--reverse_sticking] bpm bars output rudiment

positional arguments:
  bpm                 the bpm you wish to generate at
  bars                the number of bars of pattern to generate
  output              the name of the output midi file
  rudiment            the name of the rudiment to generate

optional arguments:
  -h, --help          show this help

For example, to create 10 bars of single stroke fours at 60 bpm:
python generator.py 60 10 example.mid single_stroke_four

You can then play the output file via timidity.

Install: 
$ brew install timidity

Test with:
timidity example.mid -D 0

(generator.py automatically outputs to channel 0 and the above -D 0 sets the drum channel to 0, hence you will hear drums if you do this)


