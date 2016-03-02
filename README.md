# RudimentGenerator
A command line drum MIDI Rudiment Generator for the standard 26 Drum Rudiments.

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