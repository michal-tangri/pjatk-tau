package pl.pjwstk.michaltangri.arecalculator.test;

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mock;
import org.mockito.Mockito;
import org.mockito.runners.MockitoJUnitRunner;
import pl.pjwstk.michaltangri.areacalculator.figures.Circle;

import static org.junit.Assert.*;
import static org.junit.Assert.assertThrows;

@RunWith(MockitoJUnitRunner.class)
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

    @Test
    public void areaShouldEqualSevenMock() {
        Circle mockCircle = Mockito.mock(Circle.class);
        Mockito.when(mockCircle.calculateArea()).thenReturn(7.0d);
        assertEquals(7.0d, mockCircle.calculateArea(), 0.0d);
    }

    @Test
    public void figureShouldHaveANameMock() {
        Circle mockCircle = Mockito.mock(Circle.class);
        Mockito.when(mockCircle.getName()).thenReturn("Cool circle");
        assertNotNull(mockCircle.getName());
    }

    @Test
    public void testFigureShouldBeAnEllipseMock() {
        Circle mockCircle = Mockito.mock(Circle.class);
        Mockito.when(mockCircle.isEllipse()).thenReturn(true);
        assertTrue(mockCircle.isEllipse());
    }

}