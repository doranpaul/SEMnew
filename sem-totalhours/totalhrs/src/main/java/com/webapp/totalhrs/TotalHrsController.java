package com.webapp.totalhrs;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.server.ResponseStatusException;
import org.springframework.http.HttpStatus;

@RestController
@CrossOrigin(origins = "*")
public class TotalHrsController {

    @GetMapping("/")
    public int getTotalAttendance(@RequestParam ("attendance_1") int attendance_1, @RequestParam ("attendance_2") int attendance_2, @RequestParam ("attendance_3") int attendance_3, @RequestParam ("attendance_4") int attendance_4){

        
        if (attendance_1 < 0 || attendance_1 > 33 || attendance_2 < 0 || attendance_2 > 22 || attendance_3 < 0 || attendance_3 > 44 || attendance_4 < 0 || attendance_4 > 55) {
            throw new ResponseStatusException(
                HttpStatus.BAD_REQUEST, "Attendance values must be within given parameters"
            );
        }
        
        TotalHoursApplication adder = new TotalHoursApplication(attendance_1, attendance_2, attendance_3, attendance_4);
        
        try {
            adder.add();
        } catch (Exception e) {
            // If there's any exception when adding, respond with an error message
            throw new ResponseStatusException(
                HttpStatus.INTERNAL_SERVER_ERROR, "Error when adding attendances", e
            );
        }

        return adder.getTotal();
    }
}