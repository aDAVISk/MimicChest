using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DrawSinc : MonoBehaviour {
	public float Xmin = -10.0f;
	public float Xmax = 10.0f;
	public float dX = 1.0f;
	public float Ymin = -10.0f;
	public float Ymax = 10.0f;
	public float dY = 1.0f;

	private Vector3[,] vertices;
	private int Xnum, Ynum;
	private GameObject[] LineObjX,LineObjY;

	// Use this for initialization
	void Start () {
		Xnum = Mathf.FloorToInt((Xmax - Xmin) / dX + 1);
		Ynum = Mathf.FloorToInt((Ymax - Ymin) / dY + 1);
		vertices = new Vector3[Xnum,Ynum];
		float x,y;
		for(int i=0; i<Xnum;i++){
			for(int j=0; j<Ynum;j++){
				x = Xmin+dX*i;
				y = Ymin+dY*j;
				vertices[i,j] = new Vector3(x,myFunc(x,y),y);
			}
		}
		LineObjX = new GameObject[Ynum];
		LineObjY = new GameObject[Xnum];
		for(int j=0; j<Ynum; j++){
			LineObjX[j] = new GameObject();
			LineObjX[j].transform.parent = transform;
			LineRenderer newLine = LineObjX[j].AddComponent<LineRenderer>();
			newLine.SetColors(Color.red,Color.red);
			newLine.SetWidth(0.25f,0.25f);
			newLine.SetVertexCount(Xnum);
			for(int i=0; i<Xnum; i++){
				newLine.SetPosition(i,vertices[i,j]);
			}
		}
		for(int i=0; i<Xnum; i++){
			LineObjY[i] = new GameObject();
			LineObjY[i].transform.parent = transform;
			LineRenderer newLine = LineObjY[i].AddComponent<LineRenderer>();
			newLine.SetColors(Color.blue,Color.blue);
			newLine.SetWidth(0.25f,0.25f);
			newLine.SetVertexCount(Xnum);
			for(int j=0; j<Ynum; j++){
				newLine.SetPosition(j,vertices[i,j]);
			}
		}
	}
	// Update is called once per frame
	void Update () {
		
	}

	float myFunc(float x, float y){
		float mag = 2.0f;
		float freq = 2.0f;
		float r = freq * Mathf.Sqrt(x*x+y*y);
		if (r == 0){
			return mag;
		}
		return mag*Mathf.Sin(r)/r;
	}
}
