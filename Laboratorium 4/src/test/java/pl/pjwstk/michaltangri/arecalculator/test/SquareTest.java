package pl.pjwstk.michaltangri.arecalculator.test;

import pl.pjwstk.michaltangri.areacalculator.figures.Square;
import org.junit.*;

import static org.junit.Assert.*;

public class SquareTest {
    private Square square;

    @Before
    public void setUp() {
        square = new Square();
    }

    @After
    public void tearDown() {
        square = null;
    }

    @Test
    public void areaShouldEqualSixAndAQuarter() {
        square.setA(2.5d);
        assertEquals(6.25d, square.calculateArea(), 0.0d);
    }

    /*
        This test is supposed to fail
    */
    @Test
    public void  perimeterShouldEqualThree() {
        assertEquals(3, square.calculatePerimeter(), 0.0d);
    }

    @Test
    public void figureShouldHaveAName() {
        assertNotNull(square.getName());
    }

    @Test
    public void testFigureShouldBeASquare() {
        assertTrue(Square.isSquare(square));
    }

    @Test
    public void squareConstructorShouldThrowException() {
        assertThrows(IllegalArgumentException.class, () -> {
           new Square(-2.0d);
        });
    }

}
