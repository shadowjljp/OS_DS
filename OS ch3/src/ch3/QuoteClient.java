package ch3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.Socket;

public class QuoteClient {

	
	public static void main(String[] args) {
		try { /* make connection to server socket */
			Socket sock = new Socket("127.0.0.1", 6017);
			InputStream in = sock.getInputStream();
			/* InputStreamReader:It reads bytes and decodes them into characters using a specified charset*/
			/*Reads text from a character-input stream, buffering characters so as to provide for the efficient reading of characters, arrays, and lines.*/
			BufferedReader bin = new BufferedReader(new InputStreamReader(in));
			/* read the date from the socket */
			String line;
			while ((line = bin.readLine()) != null)
				System.out.println(line);
			/* close the socket connection */
			sock.close();
		} catch (IOException ioe) {
			System.err.println(ioe);
		}
	}
	
}
