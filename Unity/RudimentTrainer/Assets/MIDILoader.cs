using UnityEngine;
using System.Collections;
using SMFLite;

public class MIDILoader : MonoBehaviour 
{
	MidiTrackSequencer seq;
	public TextAsset midiFile;

	// Use this for initialization
	void Start () 
	{
		//var bytes = File.ReadAllBytes(@"single_paradiddle");

		//TextAsset ta = Resources.Load("single_paradiddle",typeof(TextAsset)) as TextAsset;
		//Object midifile = Resources.Load("single_paradiddle");
		//Debug.Log(ta);
		MidiFileContainer song = MidiFileLoader.Load (midiFile.bytes);
		seq = new MidiTrackSequencer(song.tracks[0], song.division, 120);

		foreach (MidiEvent e in seq.Start ()) 
		{
			// Do something with a MidiEvent.
			Debug.Log(e);
		}
	}
	

	void Update() 
	{
		if (seq.Playing) 
		{
			foreach (MidiEvent e in seq.Advance (Time.deltaTime)) 
			{
				Debug.Log (e);
			}
		}
	}
}
