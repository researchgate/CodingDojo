; Rob had the idea of writing a simple ray tracer to render a sphere in front of a blue background
; He implemented the tracer in C and the we started with the Assembly code
; We didn't get further than filling the screen with blue.... so... there you go

; First we put the start address $0200 in $00 and $01 (LSB first: |00|02| => $0200 )
 lda #$00
 sta $00
 lda #$02
 sta $01
; We put the code for light blue into A and zero into X (needs to be zero so we can use it 
;    safely for indirect addressing)
 lda #$e
 ldx #0

; Now we loop over the entire screen
loop:
; Put #$e (in A) into the current frame buffer address (starting with $0200)
 sta ($00, x)
; Increase the LSB of the frame buffer address
 ldy $00
 iny
 sty $00
; Check if we have an overflow
 bne loop
; If we do, increase the MSB
 ldy $01
 iny
 sty $01
; Make sure that we don't run into the $0600 adress space where the code is
 cpy #$06
 beq end
 jmp loop
end: