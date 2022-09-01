public class Ticket {

    private String origen;
    private String destino;
    private String origenLatitud;
    private String origenLongitud;
    private String destinoLatitud;
    private String destinoLongitud;

    public Ticket(String origen, String destino, String origenLatitud, String origenLongitud, String destinoLatitud, String destinoLongitud){
        this.origen = origen;
        this.destino = destino;
        this.origenLatitud = origenLatitud;
        this.origenLongitud = origenLongitud;
        this.destinoLatitud = destinoLatitud;
        this.destinoLongitud = destinoLongitud;
    }

    @Override
    public String toString(){
        String s = "";
        s += "Origen: " + this.origen + " ";
        s += "Destino: " + this.destino + " ";
        s += "Origen_latitud: " + this.origenLatitud + " ";
        s += "Origen_longitud: " + this.origenLongitud + " ";
        s += "Destino_latitud: " + this.destinoLatitud + " ";
        s += "Destino_longitud: " + this.destinoLongitud + " ";

        return s;
    }

    @Override
    public boolean equals(Object objeto){
        if(objeto == null || getClass() != objeto.getClass()){
            return false;
        }

        Ticket ticket = (Ticket)objeto;

        if(this.origen == ticket.origen && this.destino == ticket.destino && this.origenLatitud == ticket.origenLatitud && this.origenLongitud == ticket.origenLongitud && this.destinoLatitud == ticket.destinoLatitud && this.destinoLongitud == ticket.destinoLongitud){
            return true;
        }
        else{
            return false;
        }

    }

}
