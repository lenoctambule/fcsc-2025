    MOV R0, RB      ; high
    MOV R1, #0      ; low
    MOV R3, #2
    MOV R5, #1
loop:
    CMP R0, R1      ; while low >= mid
    JNCR end
    MOV R2, R0
    ADD R2, R2, R1
    DIV R2, R2, R3 ; mid =  (low + mid) // 2
    MUL R4, R2, R2 
    CMP R4, RB      
    JZR end     ; if mid ** 2 == e return
    JCA high
    MOV R1, R2
    ADD R1, R1, R5 ; low = mid + 1
    JR loop
high:
    MOV R0, R2
    SUB R0, R0, R5 ; high = mid - 1
    JR loop
end:
    STP