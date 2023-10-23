<?php
namespace Src;
use Exception;

class Functions{
public static function getStudentEngagementScore($lec, $lab, $supp, $can) {
    $lecTotal = 33;
    $lecWeight = 0.3;
    $labTotal = 22;
    $labWeight = 0.4;
    $suppTotal = 44;
    $suppWeight = 0.15;
    $canTotal = 50;
    $canWeight = 0.15;

    // Validate that the inputs are numeric and within the required range
    if (!is_numeric($lec) || !is_numeric($lab) || !is_numeric($supp) || !is_numeric($can)
        || $lec < 0 || $lec > $lecTotal || $lab < 0 || $lab > $labTotal || $supp < 0 || $supp > $suppTotal || $can < 0 || $can > $canTotal) {
        throw new Exception("Invalid input. The input parameters must be numeric and within the expected range.");
    }
        $student_engagement_score = ((($lec*$lecWeight)/$lecTotal)
                                    +(($lab*$labWeight)/$labTotal)
                                    +(($supp*$suppWeight)/$suppTotal)
                                    +(($can*$canWeight)/$canTotal))*100;
                                    
                                    if ($student_engagement_score > 100) {
                                        $student_engagement_score = 100;
                                    }
    return round($student_engagement_score, 2);
}
}