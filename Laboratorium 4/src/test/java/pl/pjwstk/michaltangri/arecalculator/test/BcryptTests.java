package pl.pjwstk.michaltangri.arecalculator.test;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;
import org.mindrot.jbcrypt.BCrypt;

import static org.junit.Assert.*;

public class BcryptTests {
    private final String initialString = "TAU";
    private String hashed;

    @Before
    public void setUp() {
        hashed = BCrypt.hashpw(initialString, BCrypt.gensalt());
    }

    @After
    public void tearDown() {
        hashed = null;
    }

    @Test
    public void initialStringComparedToHashShouldReturnTrue() {
        assertTrue(BCrypt.checkpw("TAU", hashed));
    }

    @Test
    public void wrongStringComparedToHashShouldReturnFalse() {
        assertFalse(BCrypt.checkpw("AAAAAAAAAAA", hashed));
    }

    @Test
    public void twoHashedStringsShouldNotBeEqual() {
        assertNotEquals(BCrypt.hashpw(initialString, BCrypt.gensalt()), hashed);
    }

}
