---
layout: post
title: 汇编语言-REP,RCR,ROR等指令
subtitle: 复习笔记
author: Kingtous
date: 2019-06-09 10:19:20
header-img: img/about-bg.jpg
catalog: True
tags:
- 汇编语言
---



> [Original Website](http://users.cis.fiu.edu/~downeyt/cop3402/rept.html)

*RCL* - Rotate Through Carry Left

- **Usage:** RCL dest,count

- **Modifies Flags:** CF OF

- ![img](http://www.penguin.cz/~literakl/intel/rcl.gif)

- Rotates the bits in the destination to the left "count" times with all data pushed out the left side re-entering on the right. The Carry Flag holds the last bit rotated out.



------





*RCR* - Rotate Through Carry Right

- **Usage:** RCR dest,count

- **Modifies Flags:** CF OF

- ![img](http://www.penguin.cz/~literakl/intel/rcr.gif)

- Rotates the bits in the destination to the right "count" times with all data pushed out the right side re-entering on the left. The Carry Flag holds the last bit rotated out.



------

*REP* - Repeat String Operation

- **Usage:** REP

- **Modifies Flags:** None

- Repeats execution of string instructions while CX != 0. After each string operation, CX is decremented and the Zero Flag is tested. The combination of a repeat prefix and a segment override on CPU's before the 386 may result in errors if an interrupt occurs before CX=0. The following code shows code that is susceptible to this and how to avoid it:

- ```
           again:  rep movs  byte ptr ES:[DI],ES:[SI]   ; vulnerable instr.
                       jcxz  next              ; continue if REP successful
                       loop  again             ; interrupt goofed count
           next:
  ```



------

*REPE/REPZ* - Repeat Equal / Repeat Zero

- **Usage:** REPE
  ​           REPZ

- **Modifies Flags:** None

- Repeats execution of string instructions while CX != 0 and the Zero Flag is set. CX is decremented and the Zero Flag tested after each string operation. The combination of a repeat prefix and a segment override on processors other than the 386 may result in errors if an interrupt occurs before CX=0. Look at [example](http://www.penguin.cz/~literakl/intel/r.html#code), how to avoid it.



------

*REPNE/REPNZ* - Repeat Not Equal / Repeat Not Zero

- **Usage:** REPNE
  ​           REPNZ

- **Modifies Flags:** None

- Repeats execution of string instructions while CX != 0 and the Zero Flag is clear. CX is decremented and the Zero Flag tested after each string operation. The combination of a repeat prefix and a segment override on processors other than the 386 may result in errors if an interrupt occurs before CX=0. 



------

*RET/RETF* - Return From Procedure

- **Usage:** RET nBytes
  ​           RETF nBytes
  ​           RETN nBytes

- **Modifies Flags:** None

- Transfers control from a procedure back to the instruction address saved on the stack. "n bytes" is an optional number of bytes to release. Far returns pop the IP followed by the CS, while near returns pop only the IP register.



------





*ROL* - Rotate Left

- **Usage:** ROL dest,count

- **Modifies Flags:** CF OF

- ![img](http://www.penguin.cz/~literakl/intel/rol.gif)

- Rotates the bits in the destination to the left "count" times with all data pushed out the left side re-entering on the right. The Carry Flag will contain the value of the last bit rotated out.



------





*ROR* - Rotate Right

- **Usage:** ROR dest,count

- **Modifies Flags:** CF OF

- ![img](http://www.penguin.cz/~literakl/intel/ror.gif)

- Rotates the bits in the destination to the right "count" times with all data pushed out the right side re-entering on the left. The Carry Flag will contain the value of the last bit rotated out.