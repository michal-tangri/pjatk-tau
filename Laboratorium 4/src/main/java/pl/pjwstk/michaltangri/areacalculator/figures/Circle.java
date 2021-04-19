package pl.pjwstk.michaltangri.areacalculator.figures;

public class Circle implements Figure {

    private double r;
    private String name = null;
    private final boolean isEllipse = true;

    public Circle() {
        this.r = 1;
    }

    public Circle(final double r) throws IllegalArgumentException{
        if (r <= 0) throw new IllegalArgumentException("Radius cannot be 0 or less.");
        this.r = r;
    }

    @Override
    public double calculateArea() {
        return Math.PI * (r * r);
    }

    @Override
    public double calculatePerimeter() {
        return 2 * Math.PI * r;
    }

    public static boolean isCircle(final Figure figure) {
        return figure instanceof Circle;
    }

    public double getR() {
        return r;
    }

    public void setR(double r) {
        this.r = r;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public boolean isEllipse() {
        return isEllipse;
    }
}
