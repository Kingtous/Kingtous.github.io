---
layout:     post
title:      "2018-12-31 OMPi小组会议"
subtitle:   " \"解决OpenMP程序中变量未定义的问题\""
date:       2018-12-31 21:07:00
author:     "Kingtous"
header-img: "img/RTCO_Omp-DAG.jpg"
catalog: true
tags:
- OMPi小组会议
---

解决undifined问题

```
sweet -i=floorplan_ompi_trim.alf,std_hll.alf func=_taskFunc0_  -c extref=off -ae pu aac=insertsort.clt tc=st,op merge =all
```



```
-c后加
extref=<X> 		Checks if there are any unresolved external references in the
				program (like calls to external functions or accesses to external
				global variables). <X> can be one of: 
				
on             - (default) Turns on this check
off            - Turns off this check
```






```
-ae后加
pu      Process undefined functions, which means that calls to undefined
		functions will simply not be made. Further, all undefined global
		variables will initially be set to TOP, but become updated
		according to writes made during the AE analysis. Option must be
		set if AE should be run on code containing imports to functions
		that are not provided.
```
