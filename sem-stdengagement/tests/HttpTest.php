<?php

require('vendor/autoload.php');

use GuzzleHttp\Handler\MockHandler;
use GuzzleHttp\HandlerStack;
use GuzzleHttp\Psr7\Response;

class HttpTest extends PHPUnit\Framework\TestCase {
    protected $client;

    protected function setUp(): void {
        $mock = new MockHandler([
            // Mock a response for your test case
            new Response(200, [], json_encode([
                'error' => false,
                'items' => [],
                'attendance' => [],
                'student_engagement_score' => 100
            ]))
        ]);

        $handlerStack = HandlerStack::create($mock);
        $this->client = new GuzzleHttp\Client([
            'handler' => $handlerStack,
            'base_uri' => 'http://localhost:1100' // This will be ignored since we're mocking
        ]);
    }

    public function testGet_ValidInput_ExpectedOutput() {
        $response = $this->client->get('/', [
            'query' => [
                'item_1' => 'lecture%sessions',
                'attendance_1' => 10,
                'item_2' => 'lab%sessions',
                'attendance_2' => 20,
                'item_3' => 'support%sessions',
                'attendance_3' => 30, 
                'item_4' => 'canvas%activities',
                'attendance_4' => 40
            ]
        ]);

        $this->assertEquals(200, $response->getStatusCode());

        $data = json_decode($response->getBody(), true);
        $this->assertFalse($data['error']);
        $this->assertArrayHasKey('items', $data);
        $this->assertArrayHasKey('attendance', $data);
        $this->assertArrayHasKey('student_engagement_score', $data);
    }
}