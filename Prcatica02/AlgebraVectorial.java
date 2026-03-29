public class AlgebraVectorial {
    public double x;
    public double y;
    public double z;

    public AlgebraVectorial(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public double magnitud() {
        return Math.sqrt(x * x + y * y + z * z);
    }

    public AlgebraVectorial suma(AlgebraVectorial b) {
        return new AlgebraVectorial(this.x + b.x, this.y + b.y, this.z + b.z);
    }

    public AlgebraVectorial resta(AlgebraVectorial b) {
        return new AlgebraVectorial(this.x - b.x, this.y - b.y, this.z - b.z);
    }

    public double producP(AlgebraVectorial b){
        return (x * b.x) + (y * b.y) + (z * b.z);
    }

    public AlgebraVectorial producC(AlgebraVectorial b) {
        return new AlgebraVectorial((y * b.z) - (z * b.y), (z * b.x) - (x * b.z), (x * b.y) - (y * b.x));
    }

    public AlgebraVectorial escalar(double n) {
        return new AlgebraVectorial(x * n, y * n, z * n);
    }

    @Override
    public String toString() {
        return "(" + x + ", " + y + ", " + z + ")";
    }



    public static boolean perpendicular(AlgebraVectorial a, AlgebraVectorial b) {
        AlgebraVectorial suma = a.suma(b);
        AlgebraVectorial resta = a.resta(b);
        return Math.abs(suma.magnitud() - resta.magnitud()) < 1e-6;
    }

    public static boolean perpendicular(AlgebraVectorial a, AlgebraVectorial b, boolean mutuo){
        double d1 = a.resta(b).magnitud();
        double d2 = b.resta(a).magnitud();
        return Math.abs(d1 - d2) < 1e-6;
    }

    public static boolean perpendicular(AlgebraVectorial a, AlgebraVectorial b, int c){
        if (c == 2) { 
            return Math.abs(a.producP(b)) < 1e-6;
    }
        return false;
    }

    public static boolean perpendicular(AlgebraVectorial a, AlgebraVectorial b, double d){
        double Suma = a.suma(b).magnitud(); 
        double ma = a.magnitud();
        double mb = b.magnitud();
        double hip = Suma * Suma;
        double cate = (ma * ma) + (mb * mb);
        return Math.abs(hip - cate) < 1e-6;
    }

    public static boolean paralela(AlgebraVectorial a, AlgebraVectorial b){
        double rx = a.x / b.x;
        double ry = a.y / b.y;
        double rz = a.z / b.z;
        return Math.abs(rx - ry) < 1e-6 && Math.abs(ry - rz) < 1e-6;
    }
    public static boolean paralela(AlgebraVectorial a, AlgebraVectorial b, String metodo) {
        AlgebraVectorial resultado = a.producC(b); 
        return resultado.magnitud() < 1e-6; 
    }

    public static AlgebraVectorial proyeccion(AlgebraVectorial a, AlgebraVectorial b) {
        double x = a.producP(b);
        double y = b.magnitud() * b.magnitud(); 
        double escalar = x / y;
        return b.escalar(escalar);
    }

    public static double componente(AlgebraVectorial a, AlgebraVectorial b) {
        return a.producP(b) / b.magnitud();
        }

    
    public static void main(String[] args) {
        AlgebraVectorial v1 = new AlgebraVectorial(2, 3, 1);
        AlgebraVectorial v2 = new AlgebraVectorial(4, 2, 0);

        boolean resul1 = AlgebraVectorial.perpendicular(v1, v2);
        System.out.println("a) perpendiculares? " + resul1);

        boolean resulMutuo = AlgebraVectorial.perpendicular(v1, v2, true);
        System.out.println("b) perpendicularesMut? " + resulMutuo);

        boolean resul2 = AlgebraVectorial.perpendicular(v1, v2, 2);
        System.out.println("c) perpendicularesOrt? " + resul2);

        boolean resulPita = AlgebraVectorial.perpendicular(v1, v2, 1.0);
        System.out.println("d) perpendicularesPita? " + resulPita);

        AlgebraVectorial v3 = new AlgebraVectorial(1, 2, 3);
        AlgebraVectorial v4 = new AlgebraVectorial(2, 4, 6);
        System.out.println("e) Paralelas? " + AlgebraVectorial.paralela(v3, v4));
        
        System.out.println("f) ParalelasCz? " + AlgebraVectorial.paralela(v3, v4, "cruz"));

        AlgebraVectorial proy = AlgebraVectorial.proyeccion(v1, v2);
        System.out.println("g) Proyección : " + proy);

        double comp = AlgebraVectorial.componente(v1, v2);
        System.out.println("h) Componente : " + comp);
    }
}
