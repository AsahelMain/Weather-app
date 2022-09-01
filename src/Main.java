import java.io.BufferedReader;  
import java.io.FileReader;  
import java.io.IOException;  
import java.util.List;
import java.util.ArrayList;

public class Main{
    public static void main(String[] args){
        
        String linea = "";
        String separador = ",";
        List<Ticket> tickets = new ArrayList<>();

        try{
            BufferedReader br = new BufferedReader(new FileReader("dataset1.csv"));  
            while ((linea = br.readLine()) != null) 
            {  
                String[] ticketsArray = linea.split(separador);
                Ticket ticketNuevo = new Ticket(ticketsArray[0], ticketsArray[1], ticketsArray[2], ticketsArray[3], ticketsArray[4], ticketsArray[5]);
                tickets.add(ticketNuevo);
                //System.out.println("Origen: " + ticketsArray[0] + ", Destino: " + ticketsArray[1] + ", Origen_latitud: " + ticketsArray[2] + ", Origen longitud: " + ticketsArray[3] + ", Destino latitud: " + ticketsArray[4] + ", Destino longitud:" + ticketsArray[5]); 
            }  

        }
        catch (IOException e)   
        {  
            e.printStackTrace();  
        }  
    
        for(Ticket t: tickets){
            System.out.println(t);
        }

    }
}