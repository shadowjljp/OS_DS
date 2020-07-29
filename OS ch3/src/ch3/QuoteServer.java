package ch3;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Calendar;

public class QuoteServer {

	public static void main(String[] args) {
		
		try {
			ServerSocket sock = new ServerSocket(6017);
			/* now listen for connections */
			while (true) {
				Socket client = sock.accept();
				PrintWriter writer = new PrintWriter(client.getOutputStream(), true);
				/*Judging which day of the week is it today*/
				Calendar c = Calendar.getInstance();
				c.setTime(new java.util.Date());
				int dayOfWeek = c.get(Calendar.DAY_OF_WEEK);
				String content = null;/*Prepare a String*/
				
				switch(dayOfWeek) {
				default:
				case 1:
					content="The true art of memory is the art of attention.";
					break;
				case 2:
					content="No great art has ever been made without the artist having known danger.";
					break;
				case 3:
					content="Courage is the ladder on which all the other virtues mount.";
					break;
				case 4:
					content="A good laugh is sunshine in the house.";
					break;
				case 5:
					content="Choose a job you love, and you will never have to work a day in your life.";
					break;
				case 6:
					content="Share your smile with the world. It's a symbol of friendship and peace.";
					break;
				case 7:
					content="It is not a lack of love, but a lack of friendship that makes unhappy marriages."; 
					break;
					
					
				}
				/* write the Content to the socket */
				writer.println(content);
				/* close the socket and resume */
				/* listening for connections */
				client.close();
			}
		} catch (IOException ioe) {
			System.err.println(ioe);
		}
	}

}
