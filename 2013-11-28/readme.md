### Agenda ###

It's *bring-your-own-language* night! Code in any language you like or let somebody else show you the language he brought.

This time we won't do a classical coding kata but instead there'll be an open challenge involving *[HTTP]*. 
Details remain a surprise.

[HTTP]: http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol

### Speficiation###

The programs we write are to control a 4x4 LED grid over HTTP. The payload is sent with POST and contains the patterns and delay for each pattern. First the delay in milliseconds (should be >50), then a dash, and then the 16 zeros or ones for the 6 LEDs.

Example:

    500-1001100111111001
    100-0000000000000000
    500-1111100011101111
    100-0000000000000000
    500-1000100010001111
    100-0000000000000000
    500-1000100010001111
    100-0000000000000000
    500-0110100110010110
    800-0000000000000000
