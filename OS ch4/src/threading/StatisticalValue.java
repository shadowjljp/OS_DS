package threading;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;



public class StatisticalValue extends Thread {
	private Thread t;
	private String threadName;
	
	
	static boolean flag =true;
	static String input;
	 static ArrayList<Integer> intarray = new ArrayList<>();
	 
	public StatisticalValue(String name) {
		threadName = name;
//		System.out.println("Creating " + threadName);
	}

	public static void main(String args[]) {
		
		while(flag){
			try {
					forUserInput(); 
					splitConvertToInt();
				    flag=false;
			}catch(Exception e) {
				System.out.println("Please input integers and separate them with space !!");
			}
		}
		
		//create thread and start them.
		Thread R1 = new StatisticalValue("average value");

		Thread R2 = new StatisticalValue("minimum value");

		Thread R3 = new StatisticalValue("maximum value");
		R1.start();
		R2.start();
		R3.start();

		
	}
	
	//activate the user input function
	public static void forUserInput() {
		Scanner myObj = new Scanner(System.in);  // Create a Scanner object
	    System.out.println("Enter integers and separate them with space");

	     input = myObj.nextLine();  // Read user input
	    System.out.println("User input is: " + input);  // Output user input 
	    
	}
	//Transform the user input into Integer ArrayList intarray
	public static void splitConvertToInt() {
		  String[] splitStr = input.trim().split("\\s+");
		    for(int i=0;i<splitStr.length;i++) {
		    	intarray.add(Integer.parseInt(splitStr[i]));
		    }
		    
	}
		
	public void run() {


		switch (threadName) {
		case "average value":
			t.setPriority(10);
			findAverage() ;
			break;
		case "minimum value":
			t.setPriority(8);
			findMinimum();
			break;
		case "maximum value":
			t.setPriority(6);
			findMaxmium();
			break;

		}
	}

	public void start() {
		if (t == null) {
			t = new Thread(this, threadName);
			t.start();
		}
		// Setting priority and adding books to list while putting them all in a HashMap
		
	}

	public void findMinimum() {
		int mini = intarray.get(0);
		
		for(int i=0;i<intarray.size();i++) {
			
			if(intarray.get(i)<mini) {
				mini = intarray.get(i);
			}
			
		}
		System.out.println("The minimum value is "+mini);

	}

	public void findMaxmium() {
	int max = Collections.max(intarray);
	System.out.println("The maxmium value is "+max);
	}

	public void findAverage() {
		float sum=0;
		for(float element:intarray) {
			sum+=element;
		}
		float average = sum/intarray.size();
		
		System.out.println("The average value is "+ average);
	}
}
