package com.webapp.totalhrs;

public class TotalHoursApplication {
    private int attendance_1;
    private int attendance_2;
    private int attendance_3;
    private int attendance_4;
    private int total;
    
    public TotalHoursApplication(int attendance_1, int attendance_2, int attendance_3, int attendance_4) {
        if (attendance_1 < 0 || attendance_2 < 0 || attendance_3 < 0 || attendance_4 < 0) {
            throw new IllegalArgumentException("Attendance cannot be negative");
        }
       
        this.attendance_1 = attendance_1;
        this.attendance_2 = attendance_2;
        this.attendance_3 = attendance_3;
        this.attendance_4 = attendance_4;
    }
    // getter for attendance 1
    public int getAttendance_1() {
        return attendance_1;
    }

    // getter for attendance 2
    public int getAttendance_2() {
        return attendance_2;
    }

    // getter for attendance 3
    public int getAttendance_3() {
        return attendance_3;
    }

    // getter for attendance 4
    public int getAttendance_4() {
        return attendance_4;
    }

    // getter for total
    public int getTotal() {
        return total;
    }

    //method for adding attendances
    public void add(){
        total = attendance_1+attendance_2+attendance_3+attendance_4;
    }
}
