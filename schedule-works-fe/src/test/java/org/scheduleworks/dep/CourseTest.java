package org.scheduleworks.dep;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertSame;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class CourseTest {
    Course test;

    @BeforeEach
    void setup() {
        test = new Course("password", "Aafnan", "120", "discipline", "number");
    }

    @Test
    void testSetName() {
        test.setName("Mahmood");
        assertSame("Mahmood", test.getName());
    }

    @Test
    void testSetPass() {
        test.setPass("fakepass");
        assertSame("fakepass", test.getPass());
    }
}
