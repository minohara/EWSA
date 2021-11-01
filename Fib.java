
class GCD {
  static


  int gcd(int x, int y) {
    if (y == 0) {
      return x;
    }
    while ( x >= y ) {
      x = x - y;
    }
    return gcd(y, x);
  }

  public static void main(String[] args) {
    System.out.println(gcd(1900, 1080));
  }
}

/*

GCD
  STR LR, [SP, #-4]!
  CMP R1, #0
  BNE WHILE
  ADD SP, SP, #4
  MOV PC, LR
WHILE
  CMP R0, R1
  BLT DONE
  SUB R0, R0, R1
  B WHILE
DONE
  EOR R0, R0, R1
  EOR R1, R1, R0
  EOR R0, R0, R1
  BL GCD
  LDR LR, [SP], #4
  MOV PC, LR


*/
