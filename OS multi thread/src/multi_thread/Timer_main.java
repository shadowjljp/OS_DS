package multi_thread;

import java.util.Timer;

public class Timer_main {
	
	public static void main(String[] args) {
		int i =0;
		Timer t = new Timer();
		Timer_Thread1 te1 = new Timer_Thread1("Task1", i);
		 Timer_Thread1 te2=new Timer_Thread1("Task2",i);
			
		//	te1.TimerObj(t);
			t.scheduleAtFixedRate(te1, 0,  1000);

			 t.scheduleAtFixedRate(te2, 0,500);
		
		
	}
}
