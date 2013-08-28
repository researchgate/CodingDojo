<?php

class RomanNumberGeneratorTest extends PHPUnit_Framework_TestCase
{
    /** @var RomanNumberGenerator */
    public $converter;

    protected function setUp()
    {
        $this->converter = new RomanNumberGenerator();
    }

    /** @dataProvider romanNumberDataProvider  */
    public function testConvertDecimalToRoman($decimal, $roman)
    {
        $this->assertEquals($roman, $this->converter->convert($decimal));
    }

    public function romanNumberDataProvider()
    {
        return [
            [10, 'X'],
            [6, 'VI'],
            [5, 'V'],
            [3, 'III'],
            [2, 'II'],
            [1, 'I'],
            [11, 'XI'],
            [50, 'L'],
            [16, 'XVI'],
            [100, 'C'],
            [500, 'D'],
            [55, 'LV'],
            [236, 'CCXXXVI'],
            [2567, 'MMDLXVII'],
            [7, 'VII'],
            [1000, 'M']
        ];
    }
}
