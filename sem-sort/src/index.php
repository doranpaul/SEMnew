<?php
header("Access-Control-Allow-Origin: *");
header("Content-type: application/json");
require('Functions.php');
use Src\Functions;

$output = array(
	"error" => false,
  "items" => "",
	"attendance" => 0,
	"sorted_attendance" => ""
);

if(!isset($_REQUEST['item_1']) || !isset($_REQUEST['item_2']) || !isset($_REQUEST['item_3']) || !isset($_REQUEST['item_4']) 
   || !isset($_REQUEST['attendance_1']) || !isset($_REQUEST['attendance_2']) || !isset($_REQUEST['attendance_3']) || !isset($_REQUEST['attendance_4'])){
    $output['error'] = true;
    $output['message'] = "Missing parameters in the request";
    echo json_encode($output);
    exit();
}

$item_1 = $_REQUEST['item_1'];
$item_2 = $_REQUEST['item_2'];
$item_3 = $_REQUEST['item_3'];
$item_4 = $_REQUEST['item_4'];
$attendance_1 = $_REQUEST['attendance_1'];
$attendance_2 = $_REQUEST['attendance_2'];
$attendance_3 = $_REQUEST['attendance_3'];
$attendance_4 = $_REQUEST['attendance_4'];

if(!is_string($item_1) || !is_string($item_2) || !is_string($item_3) || !is_string($item_4)
    || !is_numeric($attendance_1) || !is_numeric($attendance_2) || !is_numeric($attendance_3) || !is_numeric($attendance_4)) {
    $output['error'] = true;
    $output['message'] = "Invalid parameters in the request";
    echo json_encode($output);
    exit();
}

$items = array($item_1,$item_2,$item_3,$item_4);
$attendances = array($attendance_1,$attendance_2,$attendance_3,$attendance_4);

$sorted_attendance = Functions::getSortedAttendance($items, $attendances);

$output['items']=$items;
$output['attendance']=$attendances;
$output['sorted_attendance']=$sorted_attendance;

echo json_encode($output);
exit();
?>
