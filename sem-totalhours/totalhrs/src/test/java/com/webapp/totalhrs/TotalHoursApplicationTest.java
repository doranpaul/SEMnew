package com.webapp.totalhrs;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import com.webapp.totalhrs.TotalHoursApplication;

public class TotalHoursApplicationTest {

    int attendance_1;
    int attendance_2;
    int attendance_3;
    int attendance_4;
    TotalHoursApplication totalHoursApplication; 

    @BeforeEach
    void setUp() {
        attendance_1 = 10;
        attendance_2 = 20;
        attendance_3 = 30;
        attendance_4 = 40;
        
        // Instantiation of TotalHoursApplication with the right arguments.
        totalHoursApplication = new TotalHoursApplication(attendance_1, attendance_2, attendance_3, attendance_4);
    }

    @Test
    public void testAdd() {
        int expected = attendance_1 + attendance_2 + attendance_3 + attendance_4;
        totalHoursApplication.add();
        int actual = totalHoursApplication.getTotal();
        
        assertEquals(expected, actual);
    }

    @Test
	public void testGetAttendance1() {
		int actual = totalHoursApplication.getAttendance_1();
		assertEquals(10, actual);
	}

    @Test
	public void testGetAttendance2() {
		int actual = totalHoursApplication.getAttendance_2();
		assertEquals(20, actual);
	}

    @Test
	public void testGetAttendance3() {
		int actual = totalHoursApplication.getAttendance_3();
		assertEquals(30, actual);
	}

    @Test
	public void testGetAttendance4() {
		int actual = totalHoursApplication.getAttendance_4();
		assertEquals(40, actual);
	}

    @Test
	public void testGetTotal() {
        totalHoursApplication.add();
		int actual = totalHoursApplication.getTotal();
		assertEquals(100, actual);
	}
}
