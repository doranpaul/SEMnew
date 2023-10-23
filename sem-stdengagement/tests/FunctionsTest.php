<?php
use Src\Functions;

class FunctionsTest extends \PHPUnit\Framework\TestCase {

    // happy path testing, expected results should be correct
    public function testGetStudentEngagementScore() {
        $lec = 30; 
        $lab = 20;
        $supp = 40; 
        $can = 50;
    
        $lecTotal = 33;
        $lecWeight = 0.3;
        $labTotal = 22;
        $labWeight = 0.4;
        $suppTotal = 44;
        $suppWeight = 0.15;
        $canTotal = 50;
        $canWeight = 0.15;
    
        $expectedScore = ( ( ($lec * $lecWeight) / $lecTotal )
                         + ( ($lab * $labWeight) / $labTotal )
                         + ( ($supp * $suppWeight) / $suppTotal )
                         + ( ($can * $canWeight) / $canTotal ) ) * 100;
    
        $result = Functions::getStudentEngagementScore($lec, $lab, $supp, $can);
        
        // Assert the expected result
        $this->assertEquals(round($expectedScore, 2), $result);
    }
    // testing using negative numbers, should throw an exception
    public function testGetStudentEngagementScoreWithNegativeValues(){
        $this->expectException(\Exception::class);
        Functions::getStudentEngagementScore(-1, 20, 40, 50);
    }
    
    //testing using non-numeric values, should throw an exception
    public function testGetStudentEngagementScoreWithNonNumericValues(){
        $this->expectException(\Exception::class);
        Functions::getStudentEngagementScore('a', 20, 40, 50);
    }
}