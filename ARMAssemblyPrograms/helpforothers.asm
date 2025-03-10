		AREA PROB_11, CODE, READONLY
        ENTRY
main
        ADR   r0, x        ; pointer to first element of x
        ADR   r1, y        ; pointer to first element of y
        ADR   r2, z        ; pointer to first element of z
        LDR   r3, size     ; holds size of arrays
        LDR   r4, i        ; holds loop counter
loop    CMP r4, r3   ; compute i - size
        BEQ        done         ; if i - size >= 0, done
        LDR   r6, [r0]     ; r6 = x[i]
        LDR   r7, [r1]     ; r7 = y[i]
        BL    euclid       ; call euclid function
        B     update       ; go to update

update
        STR   r7, [r2]     ; z[i] = r7
        ADD   r0, r0, #4   ; update r0 to point to next element of x
        ADD   r1, r1, #4   ; update r1 to point to next element of y
        ADD   r2, r2, #4   ; update r2 to point to next element of z
        ADD   r4, r4, #1   ; i++
        B     loop         ; loop back
done    B     done         ; end of program
size    DCD   4           ; size of arrays
i       DCD   0            ; loop counter
x       DCD   -8, -295, 280, 81
y       DCD   9, -45, 8, -243
z       SPACE 16          ; space for z array

euclid
    CMP   r6, #0
    BGE   positive_x
    ADD	  r8, r6, r6
	SUB   r6, r6, r8
positive_x
    CMP   r7, #0
    BGE   positive_y
    ADD	  r9, r7, r7
	SUB   r7, r7, r9
positive_y
euclid_loop
    CMP   r6, r7
    BEQ   return
    BLT   y_greater
    SUB   r6, r6, r7
    B     euclid_loop
y_greater
    SUB   r7, r7, r6
    B     euclid_loop
return
	BX	LR

        END