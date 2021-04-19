package pl.pjwstk.michaltangri.areacalculator.figures;

public class Square implements Figure{

    private double a;
    private String name = "Square";

    public Square() {
        this.a = 1;
    }

    public Square(final double a) throws IllegalArgumentException {
        if (a <= 0) throw new IllegalArgumentException("Side length cannot be 0 or less.");
        this.a = a;
    }

    @Override
    public double calculateArea() {
        return a * a;
    }

    @Override
    public double calculatePerimeter() {
        return 4 * a;
    }

    public static boolean isSquare(final Figure figure) {
        return figure instanceof Square;
    }

    public double getA() {
        return a;
    }

    public void setA(double a) {
        this.a = a;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}
