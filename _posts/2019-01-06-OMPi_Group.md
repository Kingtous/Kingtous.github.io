---
layout:     post
title:      "2019-01-06 OMPi知识清单"
subtitle:   " \"ALF Format\""
date:       2019-01-06 13:23:20
author:     "Kingtous"
header-img: "img/RTCO_Omp-DAG.jpg"
catalog: true
tags:
- OMPi知识
typora-root-url: ../../Kingtous.github.io-master
---

##补充知识

- llvm-opt参数

  - ```bash
    opt -mem2reg -instcombine -instsimplify -instnamer
    
    改成
    
    opt -instnamer
    ```

opt 介绍 

[]: http://llvm.org/docs/CommandGuide/opt.html	"opt - LLVM optimizer"





```c
#include <stdio.h>
int main()
{
    int x=5; //bb::6
    int y=4; //bb::8
    int z;
    if((x>y && x>1) || y<3) //bb4  bb4_2  bb7  bb7_2  bb_10  bb_11  bb_13
    {
      z=42; //bb10
    }       //bb10::1
    else
    {
      z=41;//bb11
    }
    return 0; //bb12
}
```

CFG图：

![2019-01-06_ALFBackend](/img/RTCO/2019-01-06_ALFBackend.png)



```c
//map File
main::bb10;test_if.c;10;7
main::bb10::1;test_if.c;11;5
main::bb11;test_if.c;14;7
main::bb12;test_if.c;16;5
main::bb4;test_if.c;8;5
main::bb4::2;test_if.c;8;5
main::bb7;test_if.c;8;5
main::bb7::2;test_if.c;8;5
main::bb::10;test_if.c;8;5
main::bb::11;test_if.c;8;5
main::bb::13;test_if.c;8;5
main::bb::6;test_if.c;5;5
main::bb::8;test_if.c;6;5
```

```c
//ALF File
{ alf
 { macro_defs }
 { least_addr_unit 8 }
 little_endian
 { exports
  { frefs }
  { lrefs { lref 64 "main" } }
 }
 { imports
  { frefs
   { fref 64 "$null" }
   { fref 64 "$mem" }
  }
  { lrefs }
 }
 { decls }
 { inits }
 { funcs

  /* Definition of function main */
  { func
   { label 64 { lref 64 "main" } { dec_unsigned 64 0 } }
   { arg_decls }
   { scope
    { decls
     { alloc 64 "%tmp" 32 } /* Alloca'd memory */ 
     { alloc 64 "%x" 32 } /* Alloca'd memory */ 
     { alloc 64 "%y" 32 } /* Alloca'd memory */ 
     { alloc 64 "%z" 32 } /* Alloca'd memory */ 
     { alloc 64 "%tmp1" 32 } /* Local Variable (Non-Inlinable Instruction) */ 
     { alloc 64 "%tmp2" 32 } /* Local Variable (Non-Inlinable Instruction) */ 
     { alloc 64 "%tmp5" 32 } /* Local Variable (Non-Inlinable Instruction) */ 
     { alloc 64 "%tmp8" 32 } /* Local Variable (Non-Inlinable Instruction) */ 
    }
    { inits }
    { stmts

     /* --------- BASIC BLOCK bb ---------- */
     { label 64 { lref 64 "main::bb" } { dec_unsigned 64 0 } }

     /* STATEMENT main::bb::4
      *   %tmp = alloca i32, align 4
      *   store i32 0, i32* %tmp */
     { store { addr 64 { fref 64 "%tmp" } { dec_unsigned 64 0 } } with { dec_unsigned 32 0 } }

     /* STATEMENT main::bb::6
      *   %x = alloca i32, align 4
      *   store i32 5, i32* %x, align 4, !dbg !14 */
     { label 64 { lref 64 "main::bb::6" } { dec_unsigned 64 0 } }
     { store { addr 64 { fref 64 "%x" } { dec_unsigned 64 0 } } with { dec_unsigned 32 5 } }

     /* STATEMENT main::bb::8
      *   %y = alloca i32, align 4
      *   store i32 4, i32* %y, align 4, !dbg !17 */
     { label 64 { lref 64 "main::bb::8" } { dec_unsigned 64 0 } }
     { store { addr 64 { fref 64 "%y" } { dec_unsigned 64 0 } } with { dec_unsigned 32 4 } }

     /* STATEMENT main::bb::10
      *   %x = alloca i32, align 4
      *   %tmp1 = load i32* %x, align 4, !dbg !20 */
     { label 64 { lref 64 "main::bb::10" } { dec_unsigned 64 0 } }
     { store { addr 64 { fref 64 "%tmp1" } { dec_unsigned 64 0 } } with { load 32 { addr 64 { fref 64 "%x" } { dec_unsigned 64 0 } } } }

     /* STATEMENT main::bb::11
      *   %y = alloca i32, align 4
      *   %tmp2 = load i32* %y, align 4, !dbg !20 */
     { label 64 { lref 64 "main::bb::11" } { dec_unsigned 64 0 } }
     { store { addr 64 { fref 64 "%tmp2" } { dec_unsigned 64 0 } } with { load 32 { addr 64 { fref 64 "%y" } { dec_unsigned 64 0 } } } }

     /* STATEMENT main::bb::13
      *   %tmp3 = icmp sgt i32 %tmp1, %tmp2, !dbg !20
      *   br i1 %tmp3, label %bb4, label %bb7, !dbg !20 */
     { label 64 { lref 64 "main::bb::13" } { dec_unsigned 64 0 } }
     { switch
      { s_gt 32 { load 32 { addr 64 { fref 64 "%tmp1" } { dec_unsigned 64 0 } } } { load 32 { addr 64 { fref 64 "%tmp2" } { dec_unsigned 64 0 } } } }
      { target { dec_signed 1 { minus 1 } } { label 64 { lref 64 "main::bb4" } { dec_unsigned 64 0 } } }
      { default { label 64 { lref 64 "main::bb7" } { dec_unsigned 64 0 } } }
     }

     /* --------- BASIC BLOCK bb4 ---------- */
     { label 64 { lref 64 "main::bb4" } { dec_unsigned 64 0 } }

     /* STATEMENT main::bb4::0
      *   %x = alloca i32, align 4
      *   %tmp5 = load i32* %x, align 4, !dbg !20 */
     { store { addr 64 { fref 64 "%tmp5" } { dec_unsigned 64 0 } } with { load 32 { addr 64 { fref 64 "%x" } { dec_unsigned 64 0 } } } }

     /* STATEMENT main::bb4::2
      *   %tmp6 = icmp sgt i32 %tmp5, 1, !dbg !20
      *   br i1 %tmp6, label %bb10, label %bb7, !dbg !20 */
     { label 64 { lref 64 "main::bb4::2" } { dec_unsigned 64 0 } }
     { switch
      { s_gt 32 { load 32 { addr 64 { fref 64 "%tmp5" } { dec_unsigned 64 0 } } } { dec_unsigned 32 1 } }
      { target { dec_signed 1 { minus 1 } } { label 64 { lref 64 "main::bb10" } { dec_unsigned 64 0 } } }
      { default { label 64 { lref 64 "main::bb7" } { dec_unsigned 64 0 } } }
     }

     /* --------- BASIC BLOCK bb7 ---------- */
     { label 64 { lref 64 "main::bb7" } { dec_unsigned 64 0 } }

     /* STATEMENT main::bb7::0
      *   %y = alloca i32, align 4
      *   %tmp8 = load i32* %y, align 4, !dbg !20 */
     { store { addr 64 { fref 64 "%tmp8" } { dec_unsigned 64 0 } } with { load 32 { addr 64 { fref 64 "%y" } { dec_unsigned 64 0 } } } }

     /* STATEMENT main::bb7::2
      *   %tmp9 = icmp slt i32 %tmp8, 3, !dbg !20
      *   br i1 %tmp9, label %bb10, label %bb11, !dbg !20 */
     { label 64 { lref 64 "main::bb7::2" } { dec_unsigned 64 0 } }
     { switch
      { s_lt 32 { load 32 { addr 64 { fref 64 "%tmp8" } { dec_unsigned 64 0 } } } { dec_unsigned 32 3 } }
      { target { dec_signed 1 { minus 1 } } { label 64 { lref 64 "main::bb10" } { dec_unsigned 64 0 } } }
      { default { label 64 { lref 64 "main::bb11" } { dec_unsigned 64 0 } } }
     }

     /* --------- BASIC BLOCK bb10 ---------- */
     { label 64 { lref 64 "main::bb10" } { dec_unsigned 64 0 } }

     /* STATEMENT main::bb10::0
      *   %z = alloca i32, align 4
      *   store i32 42, i32* %z, align 4, !dbg !22 */
     { store { addr 64 { fref 64 "%z" } { dec_unsigned 64 0 } } with { dec_unsigned 32 42 } }

     /* STATEMENT main::bb10::1
      *   br label %bb12, !dbg !24 */
     { label 64 { lref 64 "main::bb10::1" } { dec_unsigned 64 0 } }
     { jump { label 64 { lref 64 "main::bb12" } { dec_unsigned 64 0 } } leaving 0 }

     /* --------- BASIC BLOCK bb11 ---------- */
     { label 64 { lref 64 "main::bb11" } { dec_unsigned 64 0 } }

     /* STATEMENT main::bb11::0
      *   %z = alloca i32, align 4
      *   store i32 41, i32* %z, align 4, !dbg !25 */
     { store { addr 64 { fref 64 "%z" } { dec_unsigned 64 0 } } with { dec_unsigned 32 41 } }

     /* STATEMENT main::bb11::1
      *   br label %bb12 */
     { label 64 { lref 64 "main::bb11::1" } { dec_unsigned 64 0 } }
     { jump { label 64 { lref 64 "main::bb12" } { dec_unsigned 64 0 } } leaving 0 }

     /* --------- BASIC BLOCK bb12 ---------- */
     { label 64 { lref 64 "main::bb12" } { dec_unsigned 64 0 } }

     /* STATEMENT main::bb12::0
      *   ret i32 0, !dbg !27 */
     { return { dec_unsigned 32 0 } }
    }
   }
  }
 }
}
```





- ALF文件构造
  - ALF 文档
    - 查看论文 《ALF-a language for wcet flow analysis》
