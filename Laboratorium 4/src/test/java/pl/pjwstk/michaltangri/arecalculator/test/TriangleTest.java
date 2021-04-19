package pl.pjwstk.michaltangri.arecalculator.test;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.Mockito;
import org.mockito.runners.MockitoJUnitRunner;
import pl.pjwstk.michaltangri.areacalculator.figures.Circle;
import pl.pjwstk.michaltangri.areacalculator.figures.Triangle;

import static org.junit.Assert.*;
import static org.junit.Assert.assertThrows;

@RunWith(MockitoJUnitRunner.class)
public class TriangleTest {
    private Triangle triangle;

    @Before
    public void setUp() {
        triangle = new Triangle();
    }

    @After
    public void tearDown() {
        triangle = null;
    }

    @Test
    public void areaShouldEqualEight() {
        triangle.setA(4.0d);
        triangle.setH(4.0d);
        assertEquals(8.00d, triangle.calculateArea(), 0.0d);
    }

    @Test
    public void  perimeterShouldEqualThree() {
        assertEquals(3.00d, triangle.calculatePerimeter(), 0.00d);
    }

    @Test
    public void figureShouldHaveAName() {
        assertNotNull(triangle.getName());
    }

    @Test
    public void triangleShouldBeEquilateral() {
        assertTrue(triangle.getName().contains("Equilateral"));
    }

    @Test
    public void testFigureShouldBeATriangle() {
        assertTrue(Triangle.isTriangle(triangle));
    }

    @Test
    public void triangleConstructorShouldThrowExceptionWhenAIsNegative() {
        assertThrows(IllegalArgumentException.class, () -> {
            new Triangle(-2.00d, 4.00d);
        });
    }

    @Test
    public void triangleConstructorShouldThrowExceptionWhenHIsNegative() {
        assertThrows(IllegalArgumentException.class, () -> {
            new Triangle(4.00d, -2.00d);
        });
    }

    @Test
    public void areaShouldEqualNineAndAHalfMock() {
        Triangle mockTriangle = Mockito.mock(Triangle.class);
        Mockito.when(mockTriangle.calculateArea()).thenReturn(9.5d);
        assertEquals(9.5d, mockTriangle.calculateArea(), 0.0d);
    }

    @Test
    public void figureShouldHaveANameMock() {
        Triangle mockTriangle = Mockito.mock(Triangle.class);
        Mockito.when(mockTriangle.getName()).thenReturn("Very cool triangle");
        assertNotNull(mockTriangle.getName());
    }

    @Test
    public void testFigureShouldBeEquilateralMock() {
        Triangle mockTriangle = Mockito.mock(Triangle.class);
        Mockito.when(mockTriangle.isEquilateral()).thenReturn(true);
        assertTrue(mockTriangle.isEquilateral());
    }
}
