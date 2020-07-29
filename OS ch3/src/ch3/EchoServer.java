package ch3;

import java.io.BufferedInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class EchoServer {
	  public static void main(String[] args){
	        try{
	            ServerSocket sock = new ServerSocket(6018);

	            /* listen for connections */
	            while(true){
	                Socket client = sock.accept();
	                InputStream in = client.getInputStream();
	                BufferedInputStream buffer = new BufferedInputStream(in);
	                PrintWriter writer = new PrintWriter(client.getOutputStream(), true);

	                byte[] contents = new byte[1024];
	                int length;

	                while(true){
	                    /* read input from socket */
	                	length = buffer.read(contents);
	                    
	                    /* echo back to client */
	                    String line = new String(contents, 0, length);
	                    writer.write("Server: " + line);
	                    writer.flush();

	                    if(line.toLowerCase().compareTo("disconnect")==0) break;
	                }

	                /* close the socket and resume listening for connections */
	                client.close();
	            }
	        }catch(IOException io_error){
	            System.err.println(io_error);
	        }
	    }
}
