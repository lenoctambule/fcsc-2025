MOV     R2, #1
loop:
    SUB     R5, R5, R2
    JNCR    end
    POW     R6, R6
    JR      loop
end:
    STP