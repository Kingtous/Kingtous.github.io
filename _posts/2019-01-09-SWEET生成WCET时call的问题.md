---
layout: post
title: SWEET生成WCET时call的问题
subtitle: 以Statement为单位的WCET分析
author: Kingtous
date: 2019-01-09 19:11:56
header-img: img/unsorted/callissue.png
catalog: RTCO
tags:
- WCET
typora-root-url: ../../Kingtous.github.io-master
---

# Call 结构

## 论文描述

- Call包含三个参数
  - 被 Call 的 函数
  - 函数调用的参数
  - return 返回的参数所存放的地址

![Article_Call](/img/RTCO/Article_Call.png)

## 实例1

![callissue](img/unsorted/callissue.png)



## 实例2

```bash
{ label 64 { lref 64 "fft_twiddle_gen_seq::bb13::18" } { dec_unsigned 64 0 } }
{ call
	{ label 64 { lref 64 "callfunction" } { dec_unsigned 64 0 } }
	{ add
		64 
		{ load 64
			{ addr 64 { fref 64 "%tmp14" } { dec_unsigned 64 0 } }
		}
		{ select
			128 0 63 
			{ u_mul
				64 64 
				{ s_ext
					32 64 
					{ load 32
						{ addr 64 { fref 64 "%tmp15" } { dec_unsigned 64 0 } }
					}
				}
				{ dec_unsigned 64 16 }
			}
		}
		{ dec_unsigned 1 0 }
	}
	{ add
		64 
		{ load 64
			{ addr 64 { fref 64 "%tmp18" } { dec_unsigned 64 0 } }
		}
		{ select
			128 0 63 
			{ u_mul
				64 64 
				{ s_ext
					32 64 
					{ load 32
						{ addr 64 { fref 64 "%tmp19" } { dec_unsigned 64 0 } }
					}
				}
				{ dec_unsigned 64 16 }
			}
		}
		{ dec_unsigned 1 0 }
	}
	{ load 64
		{ addr 64 { fref 64 "%tmp22" } { dec_unsigned 64 0 } }
	}
	{ load 32
		{ addr 64 { fref 64 "%tmp23" } { dec_unsigned 64 0 } }
	}
	{ load 32
		{ addr 64 { fref 64 "%tmp24" } { dec_unsigned 64 0 } }
	}
	{ load 32
		{ addr 64 { fref 64 "%tmp25" } { dec_unsigned 64 0 } }
	}
	{ select
		64 0 31 
		{ u_mul
			32 32 
			{ load 32
				{ addr 64 { fref 64 "%tmp26" } { dec_unsigned 64 0 } }
			}
			{ load 32
				{ addr 64 { fref 64 "%tmp27" } { dec_unsigned 64 0 } }
			}
		}
	}
	{ select
		64 0 31 
		{ u_mul
			32 32 
			{ load 32
				{ addr 64 { fref 64 "%tmp29" } { dec_unsigned 64 0 } }
			}
			{ load 32
				{ addr 64 { fref 64 "%tmp30" } { dec_unsigned 64 0 } }
			}
		}
	}
	result
}
```

