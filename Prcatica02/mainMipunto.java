public class mainMipunto {

    public static void main(String[] args) {

        Mipunto p1 = new Mipunto();        
        Mipunto p2 = new Mipunto(10,30.5);  

        double distancia = p1.distancia(p2);

        System.out.println("Punto 1: (" + p1.getX() + ", " + p1.getY() + ")");
        System.out.println("Punto 2: (" + p2.getX() + ", " + p2.getY() + ")");
        System.out.println("Distancia entre los puntos: " + distancia);
    }
}