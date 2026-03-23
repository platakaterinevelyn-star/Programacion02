public class Mipunto {
    private double x;
    private double y;

    public Mipunto() {
        this.x=0;
        this.y=0;
    }
    public Mipunto(double a, double b ) {
        this.x=a;
        this.y=b;
    }
    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }
    public double distancia(Mipunto p) {
        double dx = this.x - p.x;
        double dy = this.y - p.y;
        return Math.sqrt(dx * dx + dy * dy);
    }
    public double distancia(double x, double y) {
        double dx = this.x - x;
        double dy = this.y - y;
        return Math.sqrt(dx * dx + dy * dy);
    }

    
}
class mainMipunto {

    public static void main(String[] args) {

        Mipunto p1 = new Mipunto();        
        Mipunto p2 = new Mipunto(10,30.5);  

        double distancia = p1.distancia(p2);

        System.out.println("Punto 1: (" + p1.getX() + ", " + p1.getY() + ")");
        System.out.println("Punto 2: (" + p2.getX() + ", " + p2.getY() + ")");
        System.out.println("Distancia entre los puntos: " + distancia);
    }
}



