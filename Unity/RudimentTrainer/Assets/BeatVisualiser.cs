using UnityEngine;
using System.Collections;


// (Vector2 center, int radius, Color color, float width, bool antiAlias, int segmentsPerQuarter)

public class BeatVisualiser : MonoBehaviour 
{
	const uint MAX_BEAT_DEPTH = 9;
	public int beatLevels = 3;
	public int []beats = new int[MAX_BEAT_DEPTH];
	public int BPM = 60;

	private float beatLineAngle = 0;

	// Use this for initialization
	void Start () 
	{
		beats [0] = 2;
		beats [1] = 3;
		beats [2] = 4;
	}
	
	// Update is called once per frame
	void Update () 
	{
		beatLineAngle += Time.deltaTime;
	}

	Vector2 getPointOnCircle(float angleRad, Vector2 center, float radius)
	{
		float x = Mathf.Sin(angleRad) * (radius);
		float y = Mathf.Cos(angleRad) * (radius);
		return new Vector2(x, y) + center;
	}

	void drawBeatLevelRings()
	{
		Vector2 center = new Vector2 (Screen.width / 2, Screen.height / 2);
		float angle = beatLineAngle * Mathf.PI * 2;

		for (int i = 0; i < beatLevels; i++) 
		{
			Drawing.DrawCircle (center, 50*(i+1), Color.black, 2.0f, true, 24);

			Vector2 beatPos = getPointOnCircle (angle, center, 50 * (i+1));
			Drawing.DrawCircle (beatPos, 5, Color.yellow, 3.0f, true, 24);
		}

		Vector2 pos = getPointOnCircle(angle, center, 50*beatLevels);

		// draw beat line
		Drawing.DrawLine (center, pos, Color.red, 2.0f, true);

	}
	void drawBeatMarkers()
	{
		Vector2 center = new Vector2 (Screen.width / 2, Screen.height / 2);

		for (int i = 0; i <= beatLevels; i++) 
		{
			for (int j = 0; j < beats [i]; j++) 
			{
				// calculate pos
				float angle = ((1.0f/beats[i])*j) * Mathf.PI * 2;
				Vector2 beatPos = getPointOnCircle (angle, center, 50 * (i+1));
				Drawing.DrawCircle (beatPos, 1, Color.red, 3.0f, true, 24);
			}
		}
	}
	void OnGUI()
	{
		drawBeatLevelRings ();
		drawBeatMarkers ();
	}
}
