package multi_thread;

import java.util.ArrayList;
import java.util.Date;
import java.util.Timer;
import java.util.TimerTask;

public class Timer_Thread1 extends TimerTask {

	private String name;
	private int i = 0;
	ArrayList<String> list1 = new ArrayList<>();
	ArrayList<String> list2 = new ArrayList<>();
	ArrayList<String> list3 = new ArrayList<>();
	Timer t = new Timer();

	public Timer_Thread1(String n, int i) { // constructor
		this.name = n;
		this.i = i;
	}

	@Override
	public void run() {
		list1 = bookshelf1();

		if (i > 4) {

			t.cancel();
			t.purge();
			return;
		}
		System.out.println(Thread.currentThread().getName() + " " + name + " has borrow " + list1.get(i) + " successfully "
				+ new Date());

		i++;

//		if ("Task1".equalsIgnoreCase(name)) {
//			try {
//				Thread.sleep(10000);
//			} catch (InterruptedException e) {
//				// TODO Auto-generated catch block
//				e.printStackTrace();
//			}
//		}
	}

	public ArrayList<String> bookshelf1() {
		list1.add("AMA Guides to the Evaluation of Work Ability and Return to Work");
		list1.add("Heard In Data Science Interviews");
		list1.add("Make It Stick: The Science of Successful Learning");
		list1.add("Sapiens: A Brief History of Humankind");
		list1.add("Health Systems Science");
		return list1;

	}

//	public void TimerObj(Timer t) {
//		this.t =t;
//	}

}
