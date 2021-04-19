package pl.pjwstk.michaltangri.areacalculator.figures;

public class Triangle implements Figure{
    private double a;
    private double h;
    private String name = "Equilateral Triangle";
    private boolean isEquilateral = true;

    public Triangle() {
        this.a = 1;
        this.h = 1;
    }

    public Triangle(final double a, final double h) throws IllegalArgumentException {
        if ( a <= 0 || h <= 0) throw new IllegalArgumentException("Side length and height cannot be 0 or less.");
        this.a = a;
        this.h = h;
    }

    @Override
    public double calculateArea() {
        return (a * h) / 2;
    }

    @Override
    public double calculatePerimeter() {
        return 3 * a;
    }

    public static boolean isTriangle(final Figure figure) {
        return figure instanceof Triangle;
    }

    public double getA() {
        return a;
    }

    public double getH() {
        return h;
    }

    public String getName() {
        return name;
    }

    public void setA(double a) {
        this.a = a;
    }

    public void setH(double h) {
        this.h = h;
    }

    public boolean isEquilateral() {
        return isEquilateral;
    }

    public void setEquilateral(boolean equilateral) {
        isEquilateral = equilateral;
    }
}
