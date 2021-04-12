package pl.pjwstk.michaltangri.arecalculator.test;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import pl.pjwstk.michaltangri.areacalculator.figures.Circle;

import static org.junit.Assert.*;
import static org.junit.Assert.assertThrows;

public class CircleTest {
    private Circle circle;

    @Before
    public void setUp() {
        circle = new Circle();
    }

    @After
    public void tearDown() {
        circle = null;
    }

    @Test
    public void areaShouldEqualAroundFiftyAndAQuarter() {
        circle.setR(4.0d);
        assertEquals(50.25d, circle.calculateArea(), 0.2d);
    }

    @Test
    public void  perimeterShouldEqualAroundSixAndAQuarter() {
        assertEquals(6.25, circle.calculatePerimeter(), 0.05d);
    }

    /*
        This test is supposed to fail
    */
    @Test
    public void figureShouldHaveAName() {
        assertNotNull(circle.getName());
    }

    @Test
    public void testFigureShouldBeACircle() {
        assertTrue(Circle.isCircle(circle));
    }

    @Test
    public void circleConstructorShouldThrowException() {
        assertThrows(IllegalArgumentException.class, () -> {
            new Circle(-4.20d);
        });
    }
}