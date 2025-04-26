`timescale 1ns/1ns
module testbench;
  reg [15:0] x;
  wire [15:0] y;
  
  // Ciphertext to match (replace with your actual ciphertext lines)
  reg [15:0] ciphertext [0:18];  // 19 lines in your example
  integer i;
  
  // Initialize ciphertext (binary strings)
  initial begin
    ciphertext[0]  = 16'b0100010100000111;
    ciphertext[1]  = 16'b0110010001011000;
    ciphertext[2]  = 16'b0100010001110111;
    ciphertext[3]  = 16'b0000010001011101;
    ciphertext[4]  = 16'b0101011001010001;
    ciphertext[5]  = 16'b0100010100010000;
    ciphertext[6]  = 16'b0101011000001100;
    ciphertext[7]  = 16'b0011001101010111;
    ciphertext[8]  = 16'b0001101100111001;
    ciphertext[9]  = 16'b0001000001010010;
    ciphertext[10] = 16'b0001101001111001;
    ciphertext[11] = 16'b0111101100110100;
    ciphertext[12] = 16'b0011101001111110;
    ciphertext[13] = 16'b0101010001000111;
    ciphertext[14] = 16'b0010110101110101;
    ciphertext[15] = 16'b0101000000011110;
    ciphertext[16] = 16'b0110010100000110;
    ciphertext[17] = 16'b0101000100010101;
    ciphertext[18] = 16'b0001110101100001;
  end
  
  circuit uut (.x(x), .y(y));
  
  initial begin
    for (i = 0; i < 65536; i = i + 1) begin
      x = i;
      #1;
      for (integer j = 0; j < 19; j = j + 1) begin
        if (y == ciphertext[j]) begin
          $display("%16b %d", x, j);
        end
      end
    end
    $finish;
  end
endmodule