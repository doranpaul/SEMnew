<?php
use Src\Functions;
class FunctionsTest extends \PHPUnit\Framework\TestCase {

    public function testGetMaxMin() {
        $items = ["item1", "item2", "item3", "item4"];
        $attendances = [10, 5, 20, 15];

        $result = Functions::getMaxMin($items, $attendances);

        $this->assertEquals("item3 - 20", $result[0]);
        $this->assertEquals("item2 - 5", $result[1]);
    }

    public function testGetMaxMinWithEmptyArrays() {
        $this->assertFalse(Functions::getMaxMin([], []));
    }

    public function testGetMaxMinWithUnequalArrays() {
        $this->assertFalse(Functions::getMaxMin(["item1", "item2"], [10]));
    }
}
