<?php
namespace Src;
use InvalidArgumentException;

class Functions{
    public static function getSortedAttendance($items, $attendances)
{
    // Check if inputs are arrays
    if (!is_array($items) || !is_array($attendances)) {
        throw new InvalidArgumentException('Both items and attendances must be arrays.');
    }

    // Check if the arrays have the same length
    if (count($items) != count($attendances)) {
        throw new InvalidArgumentException('Items and attendances must have the same number of elements.');
    }

    $item_attendances = array();
    for ($i = 0; $i < count($items); $i++) {

        // Check if attendances[$i] is numeric
        if (!is_numeric($attendances[$i])) {
            throw new InvalidArgumentException('All attendances must be numeric.');
        }
      
        $item_attendances_array = array("item"=>$items[$i], "attendance"=>$attendances[$i]);
        array_push($item_attendances,$item_attendances_array);
    }

    usort($item_attendances, function($a, $b) {
          return $b['attendance'] <=> $a['attendance'];
    });

    return $item_attendances;
    }
}
