package org.scheduleworks.dep;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertSame;
import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class CourseTest {
    Course test;

    @BeforeEach
    void setup() {
        test = new Course("password", "Aafnan", "120", "discipline", "number");
    }

    @AfterEach
    void tearDown() {
        test = null;
        assertNull(test);
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
     @Test
    void testSetCredit() {
        test.setCredit("120");
        assertSame("120", test.getCredit());
    }

    @Test
    void setDiscipline() {
        test.setDiscipline("Math");
        assertSame("Math", test.getDiscipline());
    }

    @Test
    void setNumber() {
        test.setNumber("0");
        assertSame("0", test.getNumber());

    }

    @Test
    void setBlockRequirementId() {
        test.setBlockRequirementId("12");
        assertSame("12", test.getBlockRequirementId());
    }

    @Test
    void setTerm() {
        test.setTerm("Winter");
        assertSame("Winter", test.getTerm());
    }
    
}
