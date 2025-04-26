pq_loop:
    CA generate_prime ; gen p
    MOV R6, R1
    CA generate_prime ; gen q
    MOV R7, R1
    MUL R0, R6, R7
    BTL R1, RD
    BTL R2, R0
    CMP R1, R2
    JNZA pq_loop
; check that egcd(e, p - 1) = 1
    MOV R3, RB
    MOV R1, #1
    MOV R0, R6
    SUB R0, R0, R1
    GCD R2, R0, R3
    CMP R1, R2
; check that egcd(e, q - 1) = 1
    JNZA pq_loop
    MOV R0, R7
    SUB R0, R0, R1
    GCD R2, R0, R3
    CMP R1, R2
    JNZA pq_loop

; calculate iq
    MOV RD, R6
    INV R0, R7
    MOV R8, R0

    MOV R2, R6
    CA compute_dx ; dp
    MOV R9, R1
    MOV R2, R7
    CA compute_dx ; dq
    MOV RA, R1

    CA get_phiN
    MOV RD, R0
    INV R0, RB
    MOV RC, R0

    MUL R0, R6, R7
    MOV RD, R0
    STP

; ---- functions ----

get_phiN:
    MOV R0, #1
    MOV R1, R6 ; R6 = p
    SUB R1, R1, R0
    MOV R2, R7 ; R7 = q
    SUB R2, R2, R0
    MUL R0, R1, R2
    RET

compute_dx:
    MOV R1, #1
    MOV R0, R2
    SUB R0, R0, R1
    MOV RD, R0
    INV R1, RB
    MOV R3, R1
    RET

generate_prime:
    BTL R0, RD
    MOV R2, #2
    DIV R0, R0, R2
    MOV R2, #1
    MOV R3, R0
    SUB R3, R3, R2
    SLL R2, R2, R3
loop:
    MOV R1, R0
    RND R1
    OR R1, R1, R2
    MR R1
    JNZA loop
    RET