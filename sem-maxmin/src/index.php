<?php
header("Access-Control-Allow-Origin: *");
header("Content-type: application/json");
require('Functions.php');
use Src\Functions;

$output = array(
    "error" => false,
    "items" => "",
    "attendance" => 0,
    "max_item" => "",
    "min_item" => ""
);

$items = array();
$attendances = array();

for ($i = 1; $i <= 4; $i++) {
    if (isset($_REQUEST['item_'.$i]) && isset($_REQUEST['attendance_'.$i])) {
        $items[] = $_REQUEST['item_'.$i];
        $attendances[] = $_REQUEST['attendance_'.$i];
    } else {
        $output['error'] = true;
        $output['message'] = "Ensure all attendances are added";
        echo json_encode($output);
        exit();
    }
}

$max_min_items = Functions::getMaxMin($items, $attendances);

if (!$max_min_items) {
    $output['error'] = true;
    $output['message'] = "Ensure all attendances are added";
    echo json_encode($output);
    exit();
}

$output['items'] = $items;
$output['attendance'] = $attendances;
$output['max_item'] = $max_min_items[0];
$output['min_item'] = $max_min_items[1];

echo json_encode($output);
exit();
