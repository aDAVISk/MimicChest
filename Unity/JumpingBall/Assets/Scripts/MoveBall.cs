using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MoveBall : MonoBehaviour 
{
	public float speed = 10;
	public float jumpspeed = 20;
	public float ylimit = 2.0f;
	bool spacekeydown = false;
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void FixedUpdate () {
   		float x = Input.GetAxis("Horizontal");
   		float z = Input.GetAxis("Vertical");
   		Rigidbody rigidbody = GetComponent<Rigidbody>();
   		float y = 0.0f;
   		if (Input.GetKeyDown("space")){
   			if (!spacekeydown){
   				if (rigidbody.position.y <= ylimit){
   					y = 1.0f;
   					spacekeydown = true;
   				}
   			}
   		} else {
   			spacekeydown = false;
   		}
   		rigidbody.AddForce(speed * x,jumpspeed * y,speed * z);
	}
}
