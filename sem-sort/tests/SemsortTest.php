<?php
use Src\Functions;
class semsortTest extends \PHPUnit\Framework\TestCase{
    public function testGetSortedAttendanceWithValidInput() {
        $items = ['Item1', 'Item2', 'Item3'];
        $attendances = [20, 50, 30];

        $expectedResult = [
            ['item' => 'Item2', 'attendance' => 50],
            ['item' => 'Item3', 'attendance' => 30],
            ['item' => 'Item1', 'attendance' => 20]
        ];

        $this->assertEquals($expectedResult, Functions::getSortedAttendance($items, $attendances));
    }

    public function testMismatchedArrays() {
        $this->expectException(InvalidArgumentException::class);
        $this->expectExceptionMessage('Items and attendances must have the same number of elements.');

        Functions::getSortedAttendance(['Item1'], [10, 20]);
    }

    public function testNonArrayInput() {
        $this->expectException(InvalidArgumentException::class);
        $this->expectExceptionMessage('Both items and attendances must be arrays.');

        Functions::getSortedAttendance('Item1', [10]);
    }

    public function testInvalidNumericInput() {
        $this->expectException(InvalidArgumentException::class);
        $this->expectExceptionMessage('All attendances must be numeric.');

        Functions::getSortedAttendance(['Item1', 'Item2'], [10, 'Invalid']);
    }
}