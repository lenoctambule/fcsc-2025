/* This file was generated by the Hex-Rays decompiler version 9.1.0.250226.
   Copyright (c) 2007-2021 Hex-Rays <info@hex-rays.com>

   Detected compiler: GNU C++
*/

#include <defs.h>


//-------------------------------------------------------------------------
// Function declarations

void __noreturn start();
int (**sub_10620())(void);
int sub_10650();
int sub_10710();
int __fastcall main(int a1, char **a2, char **a3); // idb
void fini(void); // idb
void init(void); // idb
int *sub_10AE0();
int *init_proc();
int term_proc();
// int _libc_start_main(int (*main)(int, char **, char **), int argc, char **ubp_av, void (*init)(void), void (*fini)(void), void (*rtld_fini)(void), void *stack_end);
// int _gmon_start__(void); weak
// int _cxa_finalize(void *);
// int __fastcall Jv_RegisterClasses(_DWORD); weak
// void *memset(void *s, int c, size_t n);
// int printf(const char *format, ...);
// size_t fread(void *ptr, size_t size, size_t n, FILE *stream);
// int bcmp(const void *s1, const void *s2, size_t n);
// int _strtol_internal(const char *nptr, char **endptr, int base, int group);
// int puts(const char *s);

//-------------------------------------------------------------------------
// Data declarations

_UNKNOWN unk_533; // weak
_UNKNOWN unk_554; // weak
_DWORD dword_574[8] =
{
  1178817347,
  2067100984,
  1831941983,
  929575221,
  758410852,
  2117152816,
  892550504,
  879912061
}; // weak
int dword_20C4C = -1; // weak
int dword_20C50 = 0; // weak
int dword_20C5C = 0; // weak
_UNKNOWN *off_30C60 = &off_30C60; // weak
int *off_30C64[4] = { &dword_20C58, &puts, &puts, &puts }; // weak
char byte_30D10; // weak
// extern struct _IO_FILE *stdin;


//----- (000105B0) --------------------------------------------------------
void __noreturn start()
{
  void (*rtld_fini)(void); // $v0
  int stack_end; // [sp-10h] [-20h] BYREF
  int argc; // [sp+10h] [+0h]
  char *ubp_av; // [sp+14h] [+4h] BYREF

  _libc_start_main(main, argc, &ubp_av, init, fini, rtld_fini, &stack_end);
  while ( 1 )
    ;
}
// 10604: variable 'rtld_fini' is possibly undefined

//----- (00010620) --------------------------------------------------------
int (**sub_10620())(void)
{
  int (**result)(void); // $v0

  result = &_gmon_start__;
  if ( &_gmon_start__ )
    return (int (**)(void))_gmon_start__();
  return result;
}
// 30D24: using guessed type int _gmon_start__(void);

//----- (00010650) --------------------------------------------------------
int sub_10650()
{
  int result; // $v0
  void (*v1)(void); // $t9
  int *i; // $v0

  result = (unsigned __int8)byte_30D10;
  if ( !byte_30D10 )
  {
    if ( &_cxa_finalize )
      _cxa_finalize(off_30C60);
    v1 = (void (*)(void))*off_30C64[0];
    for ( i = off_30C64[0] + 1; *off_30C64[0]; i = off_30C64[0] + 1 )
    {
      off_30C64[0] = i;
      v1();
      v1 = (void (*)(void))*off_30C64[0];
    }
    result = 1;
    byte_30D10 = 1;
  }
  return result;
}
// 30C60: using guessed type _UNKNOWN *off_30C60;
// 30C64: using guessed type int *off_30C64[4];
// 30D10: using guessed type char byte_30D10;

//----- (00010710) --------------------------------------------------------
int sub_10710()
{
  int result; // $v0

  result = dword_20C5C;
  if ( dword_20C5C )
  {
    if ( &Jv_RegisterClasses )
      return Jv_RegisterClasses(&dword_20C5C);
  }
  return result;
}
// 20C5C: using guessed type int dword_20C5C;
// 30D2C: using guessed type int __fastcall Jv_RegisterClasses(_DWORD);

//----- (00010750) --------------------------------------------------------
int __fastcall main(int a1, char **a2, char **a3)
{
  int v3; // $s1
  int v4; // $s7
  char *i; // $fp
  char v6; // $at
  char v7; // $v0
  bool v8; // dc
  int v9; // $v1
  char *v10; // $v0
  _BYTE *v11; // $at
  char *v12; // $a2
  int j; // $v1
  _DWORD *v14; // $at
  char *v15; // $a2
  int v16; // $v1
  char *endptr; // [sp+10h] [-68h] BYREF
  char v19[32]; // [sp+14h] [-64h] BYREF
  char nptr[2]; // [sp+34h] [-44h] BYREF
  char v21; // [sp+36h] [-42h] BYREF
  _BYTE s[64]; // [sp+38h] [-40h] BYREF

  memset(s, 0, sizeof(s));
  v21 = 0;
  printf("Input? ");
  v3 = 1;
  if ( fread(s, 1u, 5u, stdin) == 5 && !bcmp("FCSC{", s, 5u) )
  {
    v3 = 1;
    if ( fread(s, 1u, 64, stdin) == 64 )
    {
      v4 = 0;
      for ( i = v19; ; ++i )
      {
        v6 = s[v4 + 62];
        nptr[0] = s[v4 + 63];
        nptr[1] = v6;
        v7 = _strtol_internal(nptr, &endptr, 16, 0);
        v8 = endptr != &v21;
        *i = v7;
        if ( v8 )
          break;
        v4 -= 2;
        if ( v4 == -64 )
        {
          v3 = 1;
          if ( fread(s, 1u, 1u, stdin) == 1 && s[0] == '}' )
          {
            v9 = 0;
            v10 = v19;
            do
            {
              v11 = (char *)&unk_533 + v9;
              v12 = &v19[v9++];
              *v12 ^= *v11;
            }
            while ( v9 != 32 );
            for ( j = 0; j != 32; j += 4 )
            {
              v14 = (_DWORD *)((char *)&unk_554 + j);
              v15 = &v19[j];
              *(_DWORD *)v15 += *v14 + __CFADD__(*(_DWORD *)v15, *v14);
            }
            v16 = 0;
            while ( *(_DWORD *)v10 == dword_574[v16 ^ 7] )
            {
              ++v16;
              v10 += 4;
              if ( v16 == 8 )
              {
                puts("Success!");
                return 0;
              }
            }
            return 2;
          }
          return v3;
        }
      }
    }
  }
  return v3;
}
// 574: using guessed type _DWORD dword_574[8];

//----- (000109C0) --------------------------------------------------------
void fini(void)
{
  term_proc();
}

//----- (00010A44) --------------------------------------------------------
void init(void)
{
  init_proc();
}

//----- (00010AE0) --------------------------------------------------------
int *sub_10AE0()
{
  int *result; // $v0
  int (*v1)(void); // $t9
  int (**v2)(void); // $s0

  result = &dword_20C50;
  v1 = (int (*)(void))dword_20C4C;
  v2 = (int (**)(void))&dword_20C4C;
  if ( dword_20C4C != -1 )
  {
    do
    {
      --v2;
      result = (int *)v1();
      v1 = *v2;
    }
    while ( *v2 != (int (*)(void))-1 );
  }
  return result;
}
// 20C4C: using guessed type int dword_20C4C;
// 20C50: using guessed type int dword_20C50;

//----- (00010B50) --------------------------------------------------------
int *init_proc()
{
  sub_10620();
  sub_10710();
  return sub_10AE0();
}

//----- (00010BF4) --------------------------------------------------------
int term_proc()
{
  return sub_10650();
}

// nfuncs=20 queued=10 decompiled=10 lumina nreq=0 worse=0 better=0
// ALL OK, 10 function(s) have been successfully decompiled
