package org.scheduleworks.dep;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertSame;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestInstance;
import org.junit.jupiter.api.BeforeEach;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class privateInfoTest {
    privateInfo user;

    @BeforeEach
    void setup() {
        user = new privateInfo();
    }

    @AfterEach
    void tearDown() {
        user = null;
        assertNull(user);
    }

    //  Testing with default values
    @Test
    void testSetUsernameDefault() {
        assertSame("", user.getUsername());
    }
    @Test
    void testSetPasswordDefault() {
        assertSame("", user.getPassword());
    }
    @Test
    void testSetSaveCookiesToggleDefault() {
        assertTrue(user.getSaveCookiesToggle());
    }
    @Test
    void testSetSeleniumToggleDefault() {
        assertTrue(user.getSeleniumToggle());
    }

    //  Testing with custom values
    @Test
    void testSetUsername() {
        user.setUsername("Aafnan");
        assertSame("Aafnan", user.getUsername());
    }
    @Test
    void testSetPassword() {
        user.setPassword("pass");
        assertSame("pass", user.getPassword());
    }
    @Test
    void testSetSaveCookiesToggle() {
        user.setSaveCookiesToggle(false);
        assertFalse(user.getSaveCookiesToggle());
    }
    @Test
    void testSetSeleniumToggle() {
        user.setSeleniumToggle(false);
        assertFalse(user.getSeleniumToggle());
    }
}
