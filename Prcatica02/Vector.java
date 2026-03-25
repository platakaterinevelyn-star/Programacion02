public class Vector {
    public double x;
    public double y;
    public double z;

    public Vector(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public double magnitud() {
        return Math.sqrt(x * x + y * y + z * z);
    }

    public Vector suma(Vector b) {
        return new Vector(this.x + b.x, this.y + b.y, this.z + b.z);
    }

    public Vector resta(Vector b) {
        return new Vector(this.x - b.x, this.y - b.y, this.z - b.z);
    }

    public double producP(Vector b){
        return (x * b.x) + (y * b.y) + (z * b.z);
    }

    public Vector producC(Vector b) {
        return new Vector((y * b.z) - (z * b.y), (z * b.x) - (x * b.z), (x * b.y) - (y * b.x));
    }

    public Vector escalar(double n) {
        return new Vector(x * n, y * n, z * n);
    }

    @Override
    public String toString() {
        return "(" + x + ", " + y + ", " + z + ")";
    }
}

class AlgebraVectorial{
    public static boolean perpendicular(Vector a, Vector b) {
        Vector suma = a.suma(b);
        Vector resta = a.resta(b);
        return Math.abs(suma.magnitud() - resta.magnitud()) < 1e-6;
    }

    public static boolean perpendicular(Vector a, Vector b, boolean mutuo){
        double d1 = a.resta(b).magnitud();
        double d2 = b.resta(a).magnitud();
        return Math.abs(d1 - d2) < 1e-6;
    }

    public static boolean perpendicular(Vector a, Vector b, int c){
        if (c == 2) { 
            return Math.abs(a.producP(b)) < 1e-6;
    }
        return false;
    }

    public static boolean perpendicular(Vector a, Vector b, double d){
        double Suma = a.suma(b).magnitud(); 
        double ma = a.magnitud();
        double mb = b.magnitud();
        double hip = Suma * Suma;
        double cate = (ma * ma) + (mb * mb);
        return Math.abs(hip - cate) < 1e-6;
    }

    public static boolean paralela(Vector a, Vector b){
        double rx = a.x / b.x;
        double ry = a.y / b.y;
        double rz = a.z / b.z;
        return Math.abs(rx - ry) < 1e-6 && Math.abs(ry - rz) < 1e-6;
    }
    public static boolean paralela(Vector a, Vector b, String metodo) {
        Vector resultado = a.producC(b); 
        return resultado.magnitud() < 1e-6; 
    }

    public static Vector proyeccion(Vector a, Vector b) {
        double x = a.producP(b);
        double y = b.magnitud() * b.magnitud(); 
        double escalar = x / y;
        return b.escalar(escalar);
    }

    public static double componente(Vector a, Vector b) {
        return a.producP(b) / b.magnitud();
        }
}
    
class mainVector {
    public static void main(String[] args) {
        Vector v1 = new Vector(2, 3, 1);
        Vector v2 = new Vector(4, 2, 0);

        boolean resul1 = AlgebraVectorial.perpendicular(v1, v2);
        System.out.println("a) perpendiculares? " + resul1);

        boolean resulMutuo = AlgebraVectorial.perpendicular(v1, v2, true);
        System.out.println("b) perpendicularesMut? " + resulMutuo);

        boolean resul2 = AlgebraVectorial.perpendicular(v1, v2, 2);
        System.out.println("c) perpendicularesOrt? " + resul2);

        boolean resulPita = AlgebraVectorial.perpendicular(v1, v2, 1.0);
        System.out.println("d) perpendicularesPita? " + resulPita);

        Vector v3 = new Vector(1, 2, 3);
        Vector v4 = new Vector(2, 4, 6);
        System.out.println("e) Paralelas? " + AlgebraVectorial.paralela(v3, v4));
        
        System.out.println("f) ParalelasCz? " + AlgebraVectorial.paralela(v3, v4, "cruz"));

        Vector proy = AlgebraVectorial.proyeccion(v1, v2);
        System.out.println("g) Proyección de v1 en v2: " + proy);

        double comp = AlgebraVectorial.componente(v1, v2);
        System.out.println("h) Componente de v1 en v2: " + comp);
    }
}
