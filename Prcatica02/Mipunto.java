/*public class Operaciones{
public float suma(float a, float b){
return a + b;
}
public float suma(float a, float b, float c){
return a + b + c;
}
public static void main(String[] args) {
float r1, r2;
Operaciones ejemplo = new Operaciones();
r1 = ejemplo.suma(5.0f, 3.0f); // Llamando al primer método
r2 = ejemplo.suma(2.0f, 3.0f, 4.0f); // Llamando al segundo
método
System.out.println("Resultado 1: " + r1);
System.out.println("Resultado 2: " + r2);
}
}*/

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
    



