<?php

class RomanNumberGenerator
{

    private $romanNumbers = [
        1 => 'I',
        5 => 'V',
        10 => 'X',
        50 => 'L',
        100 => 'C',
        500 => 'D',
        1000 => 'M',
    ];

    function __construct()
    {
        krsort($this->romanNumbers);
    }

    /**
     * @param int $decimal
     * @return string
     */
    public function convert($decimal)
    {
        $return = '';

        foreach ($this->romanNumbers as $arabicNumber => $romanNumber) {
            while ($decimal >= $arabicNumber) {
                $return .= $romanNumber;
                $decimal -= $arabicNumber;
            }
        }
        return $return;
    }
} 