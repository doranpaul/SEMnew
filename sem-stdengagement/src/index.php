<?php
header("Access-Control-Allow-Origin: *");
header("Content-type: application/json");
require('Functions.php');
use Src\Functions;

$output = array(
    "error" => false,
    "items" => "",
    "attendance" => 0,
    "student_engagement_score" => ""
);

$item_1 = $_REQUEST['item_1'];
$item_2 = $_REQUEST['item_2'];
$item_3 = $_REQUEST['item_3'];
$item_4 = $_REQUEST['item_4'];
$attendance_1 = $_REQUEST['attendance_1'];
$attendance_2 = $_REQUEST['attendance_2'];
$attendance_3 = $_REQUEST['attendance_3'];
$attendance_4 = $_REQUEST['attendance_4'];

$output['items'] = array($item_1, $item_2, $item_3, $item_4);
$output['attendance'] = array($attendance_1, $attendance_2, $attendance_3, $attendance_4);

try {
    // Call the modified function with individual attendance values
    $student_engagement_score = Functions::getStudentEngagementScore($attendance_1, $attendance_2, $attendance_3, $attendance_4);
    $output['student_engagement_score'] = $student_engagement_score;
} catch (Exception $e) {
    $output['error'] = true;
    $output['message'] = "Error calculating student engagement score: " . $e->getMessage();
}

echo json_encode($output);
exit();