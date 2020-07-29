package ch3;

import java.io.BufferedInputStream;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class EchoClient {
	 public static void main(String[] args){
	        try {
	            /* make connection to server socket */
	            Socket socket = new Socket("127.0.0.1", 6018);

	            /* setup reading and writing to the socket */
	            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
	            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);

	            InputStream in = socket.getInputStream();
	            BufferedInputStream buffer = new BufferedInputStream(in);

	            /* byte array to store the input from BufferedInputStream */
	            byte[] contents = new byte[1024];
	            int length;
	            String input;

	            /* keep running until null encountered */
	            while( (input = reader.readLine()) != null){
	                /* write string to socket */
	                writer.write(input);
	                writer.flush();

	                /* read string from socket */
	                String line;
	                length = buffer.read(contents);
	                if(length == -1) break;
	                line = new String(contents, 0, length);
	                System.out.println(line);

	                /* exit on 'bye' */
	                if(line.toLowerCase().contains("disconnect")) break;
	            }

	            /* close the socket connection */
	            socket.close();
	        }catch(IOException io_error){
	            System.err.println(io_error);
	        }
	    }
}
