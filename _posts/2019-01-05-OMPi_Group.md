---
layout:     post
title:      "2019-01-05 OMPi知识清单"
subtitle:   " \"SWEET help\""
date:       2019-01-05 11:13:20
author:     "Kingtous"
header-img: "img/RTCO_Omp-DAG.jpg"
catalog: true
tags:
- OMPi小组会议
typora-root-url: ../../Kingtous.github.io-master
---



## SWEET Help
SWEET version 7934 (2018-09-12)
Executing command 'help'.
Options available for SWEET version 7934.

Inputs
------
-i,--input-files=<file-name(s)>  Specifies the code to be analyzed.
Meaning of <file-name(s)>: The name of the file(s) to analyze. In case of
multiple files to be linked together (only for alf), these should be separated
by , (comma).
Parameters: 
lang=<X>  The language of the code. <X> can be one of: 
auto           - (default) Makes assumptions based on the file suffix.
alf            - One or more ALF file(s).
cfg            - File containing set of control-flow graphs. Useful for
trace-based flow hypothesis generation (see -ae rtf).

func=<function-name> The start function for all analyses. By default the
root function is the start function. 
annot=<file-name> Reads a file with abstract annotations. Use the help 'help
topic=annot' option to learn more about the format of the
annotation file. 
outannot=<file-name> Reads a file with output annotations specifications.
The resulting output annotations are written to a file named: the
file base name of file-name with the suffix ".out" appended. 
merged_output=<X> Control if the values in the output annotations are merged
or not. <X> can be one of: 
yes            - The values in the output annotations are merged.
no             - The values in the output annotations are not merged, but
instead given as discrete values separated by 'OR'.

unmangle  Unmangle identifiers. Useful to make linking of several ALF files
possible. Removes the ::<number> suffix which melmac appends to
all identifiers
rde       Remove duplicate exports. When having functions that are exported
from several ALF files all but one definition of the function are
removed. Which definition to keep is unspecified, since it is
assumed that all definitions are identical. Default off.

-c,--check-statically  Check the parsed program for consistency.
Parameters: 
size=<X>  Checks if the sizes of expressions are consistent, and if there
are unsupported constructs in the program. <X> can be one of: 
on             - (default) Turns on this check
off            - Turns off this check

connected=<X> Checks if the call graph is connected, i.e. if there is an
unumbigous start point for the analysis. <X> can be one of: 
on             - (default) Turns on this check
off            - Turns off this check

extref=<X> Checks if there are any unresolved external references in the
program (like calls to external functions or accesses to external
global variables). <X> can be one of: 
on             - (default) Turns on this check
off            - Turns off this check

fcall=<X> Checks that (non-function-pointer) function calls are made with
right amount of parameters, that each function has at least one
return statement, that all return statements has the same amount
of parameters, and that calls and returns are consistent in terms
of parameters. <X> can be one of: 
on             - (default) Turns on this check
off            - Turns off this check


-m,--map-file   Loads a file mapping from statements to corresponding C-source
code.
Parameters: 
file=<file-name> Specifies the file name of the map file. If this parameter
is not given, the base name of the program file with the suffix
".map" will be used. In case more than one program file is given
to -i, the corresponding .map files are assumed to be named as the
base names of the program files, with ".map" appended. This
parameter should then not be given. Meaning of <file-name>: The
name of the map file.

rcs       Read C sources - Open C files specified in the map file and read
C-lines from them to internal mappings.
c         Check map file content. Controls that each basic block has a
corresponding c source reference in the map file.
pal=<file-name> Print .map file after linking. 


Analyses
--------
-do,--domain    Configures the domain to be used by SWEET.
Parameters: 
type=<X>  The domain to be used for integers and offsets in pointers. <X>
can be one of: 
int            - (default) Intervals
clp            - Circular Linear Progressions

floats=<X> How to handle floats. <X> can be one of: 
top            - (default) All calculations of floating point values
result in TOP (safe).
est            - A best effort analysis that tries to estimate
floating-point values rather than returning TOP, even
though the analysis may be unsound (due to different
floating point value representation on the host and on the
target).

reuse=<X> Specifies that reuse (i.e. 'copy-on-write') of internal parts of
abstract states should be used. Instead of always making deep
copies of internal objects the states are allowed to share these
objects. The actual copying takes place when a state wants to
update its particular object. Saves memory and execution time for
both VA and AE. If one or more options except 'all' or 'none' is
given other one options will be turned off. Alternatives marked
with '*' only concerns the AE. <X> can be one or more: 
all            - (default) 
none           - 
f              - Frames
c              - Frame collections
e              - Variable environments
r              - Recorders*
h              - Recorder holders*

edo       Only read/write at offsets evenly dividable by size of previously
read/written values.
noglobinitSkips the global init section. Initial values will be top or
restricted by annotations.

-ae,--abstract-execution  Run abstract execution to produce flow facts.
Parameters: 
ffg=<X>   The flow fact generators (ffgs) to use. Given using four
dimensions (as a four letter string):  1. bounds derived: upper
(u), lower and upper (l), infeasible (i).  2. entities kept track
of: headers (h), nodes (n), edges (e), call-edges (c),
loop-body-begin-edges (b).  3. combination of entities: single
(s), pairs (p), paths (n).  4. flow fact context: each iteration
(e), all iterations (a), scope (s), function (f), program (p). <X>
can be one or more: 
uhss           - (default) Upper header bounds in scope context (default
on, but must be given if ffg is used). (u)
lhss           - Lower header node bounds in scope context. (l)
uhsf           - Upper header node bounds in function context. (u)
lhsf           - Lower header node bounds in function context. (l)
uhsp           - Upper header node bounds in program context. (u)
lhsp           - Lower header node bounds in program context. (l)
uhpf           - Upper bounds for header pairs in function context. (u)
lhpf           - Lower bounds for header pairs in function context. (l)
uhpp           - Upper bounds for header pairs in program context. (u)
lhpp           - Lower bounds for header pairs in program context. (l)
unss           - Upper bounds for nodes in scope context. (u)
lnss           - Lower bounds for nodes in scope context. (l)
unsf           - Upper bounds for nodes in function context. (u)
lnsf           - Lower bounds for nodes in function context. (l)
unsp           - Upper bounds for nodes in program context. (u)
lnsp           - Lower bounds for nodes in program context. (l)
inse           - Nodes never taken for individual iterations of scope. (u)
insa           - Nodes never taken for all iterations of scope. (u)
unps           - Upper bounds for node pairs in scope-context. (u)
lnps           - Lower bounds for node pairs in scope context. (l)
unpf           - Upper bounds for node pairs in function-context. (u)
lnpf           - Lower bounds for node pairs in function context. (l)
unpp           - Upper bounds for node pairs in program-context. (u)
lnpp           - Lower bounds for node pairs in program context. (l)
inpa           - Excluding node pairs for all iterations of scope (ie.
nodes never executed together for any iteration) (u). If
no merging is used also reports on node pairs that must be
taken together (ie. each iteration either none or both
nodes must be taken).
uess           - Upper bounds for edges in scope context. (u)
less           - Lower bounds for edges in scope context. (l)
uesf           - Upper bounds for edges in function context. (u)
lesf           - Lower bounds for edges in function context. (l)
uesp           - Upper bounds for edges in program context. (u)
lesp           - Lower bounds for edges in program context. (l)
ucsf           - Upper bounds for call edges in function context. (u)
lcsf           - Lower bounds for call edges in function context. (l)
ucsp           - Upper bounds for call edges in program context. (u)
lcsp           - Lower bounds for call edges in program context. (l)
ubns           - Upper bounds for sum of loop body begin edges in scope
context (i.e. an upper bound on the number of times the
loop body can be taken for each entry of the loop). (u)
lbns           - Lower bounds for sum of loop body begin edges in scope
context (i.e. bounds on the number of times the loop body
can be taken for each entry of the loop). (l)
all            - All ffgs should be used, i.e. both (u) and (l) ffgs
allnoinse      - All ffgs except inse (since inse may give problems in
low-sweet
ub             - Upper bounds ffgs should be used. Includes ffgs marked
with (u).
lb             - Lower bounds ffgs should be used. Includes ffgs marked
with (l).

merge=<X> The merge points to be used. <X> can be one or more: 
all            - (default) All merge points (fe,fe,le,be,je).
none           - No merging should be used.
fe             - Each function entry point.
fr             - Each function return point.
le             - Each loop exit edge.
be             - Each back-edge.
je             - Each point of joining edges.

df        Execute in a depth first manner rather than breadth first manner.
usm       Use unordered state merge strategy.
op        Optimized single path execution.
debug=<X> Turns on debugging. <X> can be one of: 
inter          - Interactive debugger
trace          - Prints a trace to the file debug_msgs.txt

tc=<X>    Type counting. Reports for each type its number of occurrences
during the execution. <X> can be one or more: 
all            - Use all type countings, i.e gn,op,st,sp.
gn             - Generic nodes, i.e. i.e. nodes in ALF syntax tree.
op             - Operators, i.e. add, sub, ...
st             - Statements, i.e. store, call, ...
sp             - Statement pairs, i.e. <store,store>, <store,call>, ...
scp            - Simple count printout, prints counts as integers on a
single line (is actually no counter report, just a
printout directive)

css       Check single state, i.e., throw run-time error if more than one
state is generated during AE. Mostly for debugging purposes.
ene       Extended handling of equal and not equal condition.
ft=<X>    How to handle the fall-through state. <X> can be one of: 
c              - (default) Continue with the fall-through state if it is
not bottom (C standard, used by melmac).
n              - Do not continue with the fall-through state (new ALF
standard since late 2011).
w              - Do not continue with the fall-through state and warn if
it is not bottom - this may be due to overestimations.

vola=<X>  How to handle volatiles. If volatiles occur in the program and AE
is run this flag must be set. <X> can be one of: 
i              - Ignore volatile keyword in frame initializations. Treat
volatile declared frames as normal frames.
t              - Set all volatile frames to top values. All writes to
frame will be ignored.

isi       Ignore stores to integer addresses. Stores where the address is a
concrete integer value are skipped, and therefore have no effect
on the program state. Normally, such addresses are interpreted as
TOP addresses, which results in that the stored value is stored to
all locations in all memory frames, after first being LUBed with
the value already stored at each location. This option is useful
when analyzing code that contains stores to absolute memory
addresses, for example, when memory-mapped I/O is used. With this
option turned on, the analysis makes the unsafe assumption that
these memory locations are disjoint from the memory locations used
by regular variables in the program. Note that loads from such
addresses are not skipped and will return TOP values, but that
would happen in the normal case as well.
pu        Process undefined functions, which means that calls to undefined
functions will simply not be made. Further, all undefined global
variables will initially be set to TOP, but become updated
according to writes made during the AE analysis. Option must be
set if AE should be run on code containing imports to functions
that are not provided.
gtf=<file-name> Generate trace file, i.e., print the names's of the CFG
nodes taken during execution. Throws, similar to ccs, a run-time
error if more than one state is generated during AE. 
rtf=<file-name> Read trace from file and runs AE according to trace. A trace
file can consist of several traces. A trace is a space-separated
list of node names. Each trace ends with a semicolon. 
aac=<file-name> Generate BCET and WCET estimate using ALF AST construct
costs. The input file holds the ALF AST construct costs. Requires
tc parameter to be set. Only cost for code constructs set by tc
will be used in BCET/WCET calc. 
aacpaths  If set the aac option will also generate a BCET and WCET path
based on the ALF AST construct costs.  The paths will be printed
to screen and are lists of basic block names. Can only be used
together with aac.
oaac=<file-name> Old version of aac. Has same tc requirement. 
bbc=<file-name> Generate BCET and WCET estimate using basic block and edges
cost table. The input file holds the cost lookup table for basic
blocks and edges. Table rows should be on form BBID COST (node
with single cost) or BBID COST1 COST2 (node with lower and upper
cost) or BBID1 BBID2 COST (edge with single cost) or BBID1 BBID2
COST1 COST2 (edge with lower and upper cost). BBID is a string not
starting with a number or a minus. COST is a (potentially
negative) integer. 
bbcpaths  If set the bbc option will also generate a BCET and WCET path
based on the BB cost lookup table.  The paths will be printed to
screen and are lists of basic block names. Can only be used
together with bbc.

-td,--timing-database  Create a timing database (tdb) for basic blocks of ALF
program based on cost lookup table (clt) holding timing costs for
ALF code constructs.
Parameters: 
i=<clt-file-name> Specifies the name of the input clt file to read timing
for ALF code constructs from. If no file name is given default
timing values will be used. 
o=<tdb-file-name> Specifies the name of an output tdb file to which the
result will be written to. If no file name is given the result
will be written to stdout. 

-va,--value-analysis  Runs value analysis (on nodes in scope graph).
Parameters: 
a=<X>     The analysis processing algorithm to use. <X> can be one of: 
n              - (default) Use worklist and process in optimal node order.
l              - Use worklist but do not derive/use node ordering.
j              - Use chaotic (Jacobi) fixpoint analysis.

fp=<X>    The fixpoint passes to use. <X> can be one of: 
wn             - (default) Widening followed by narrowing.
w              - Widening only.
n              - Narrowing only.
c              - Classic fixpoint analysis (no narrowing or widening).

wnp=<X>   The widening and narrowing points to use. <X> can be one of: 
l              - (default) Do wid and nar before last stmt in loop header.
b              - Do wid and nar at back edges.
f              - Do wid and nar before first stmt in loop header.

ft=<X>    How to handle the fall-through state. <X> can be one of: 
c              - (default) Continue with the fall-through state if it is
not bottom (C standard, used by melmac).
n              - Do not continue with the fall-through state (new ALF
standard since late 2011).
w              - Do not continue with the fall-through state and warn if
it is not bottom - this may be due to overestimations.

p=<X>     Print value analysis to txt files. Generated files will be named
as _AlfValueAnalysis_<f>_<i>.txt where i is iteration and f is
fixpoint pass. <X> can be one of: 
r              - Only the final result is printed (least detailed).
f              - The result after each fixpoint pass is printed.
i              - The result of each iteration is printed (most detailed).

d=<X>     Draw value analysis to dot files. Generated files will be named as
_AlfValueAnalysis_<f>_<i>.dot where i is iteration and f is
fixpoint pass. <X> can be one of: 
r              - Only the final result is printed (least detailed).
f              - The result after each fixpoint pass is printed.
i              - The result of each iteration is printed (most detailed).


-du,--def-use-analysis  Derives defines and uses of statements.
Parameters: 
p         Print DU analysis result to txt files. Generated files will be
named _ALFDUAnalysis.txt. 

-rd,--reaching-definitions-analysis  Runs reaching definitions.
Parameters: 
a=<X>     The analysis processing algorithm to use. <X> can be one of: 
n              - (default) Use worklist and process in optimal node order.
l              - Use worklist but do not derive/use node ordering.
j              - Use chaotic (Jacobi) fixpoint analysis.

p=<X>     Print RD analysis to txt files. Generated files will be named as
_ALFRDAnalysis_<i>.txt where i is iteration.  <X> can be one of: 
r              - Only the final result is printed.
i              - The result of each iteration is printed.

d=<X>     Draw RD analysis to dot files. Generated files will be named as
_ALFRDAnalysis_<i>.dot where i is iteration.  <X> can be one of: 
r              - Only the final result is printed.
i              - The result of each iteration is printed.


-pdg,--program-dependency-graph  Derives a program dependency graph (PDG). Also
derives other intermediate graphs, such as program control-flow
graph (PCFG), program control-dependency graph (PCDG), program
data-dependency graph (PDDG), as well as a def-use analysis (DU).
See below for how to draw (-d) and print (-p) the graphs.

-sl,--slice     Derive a slice based on a program dependency graph (PDG).
Parameters: 
ent=<X>   The code entity/entities to start the slicing upon. Can not be
used together with lab or var.  <X> can be one of: 
c              - Conditions (includes loop exit conds).
l              - Loop exit conditions.
g              - Global variables.
i              - Call graph root function input variables.
r              - Call graph root function return stmts.

lab=<label(s)> Labels of code entities to start the slice upon. A comma
separated list of strings. Can be statement label(s) or function
name(s). If function name all statements in the function will be
in the start slice. Can not be used together with ent or vars. 
var=<variables(s)> Variables to start the slice upon. If several variables
have the same name (due to local and global scoping) only one of
them will be selected. If dir=f all code and data potentially
affected by var(s) are derived. This is made by first deriving all
statements which may use the var(s) and then do a forward from
these statements. If dir=b all code and data potentially affecting
var(s) are derived. This is made by first deriving all statements
where var(s) may be defined. We then do a backward slice upon
these nodes. Can not be used together with ent or vars.  
mul=<X>   How to slice upon multiple entities.  <X> can be one of: 
t              - (default) One single slice together on all entities.
i              - Individual slices on each selected entity.

dir=<X>   The slicing direction to use.  <X> can be one of: 
b              - (default) Backward, derives all statements and variables
which may affect the selected entity.
f              - Forward, derives all statements and variables which may
be affected by the selected entity.

p=<X>     Print slice result(s) to txt file(s). Generated file(s) will be
named _ALFSlicing_<ent/lab>_<dir>.txt.  <X> can be one or more: 
all            - Print all (stmts, funcs, global, local, and scoped vars).
s              - Print labels of the statements.
f              - Print names of the functions.
g              - Print the global variables.
l              - Print the local variables (using just their names).
v              - Print the local variables with scope info (using func.var
or func.scope.var naming).

inv       Invert the slice before printing it, i.e., report what parts were
removed from the slice as opposed to what parts remain in the
slice. This is the recommended setting when using source code
mappings (with --map-file), unless the provided map files are
guaranteed to include mappings for all statements in the source
code. Otherwise, if some source code statements do not have a
mapping, it will appear as though they were sliced away since they
are not included in the printed slice.
d         Draw slice result(s) to dot file(s) as PDG graph. Generated
file(s) will be named _ALFSlicing_<ent/lab/var>_<dir>.dot. 


Outputs
-------
-f,--flow-facts  Generates flow fact file(s). The generated flow facts depend on
the flow fact generation algorithms used in the AE. Requires that
the AE has been run using a fully context-sensitive scope graph.
Parameters: 
csl=<X>   Specifies the largest call string length that should be used for
generated flow information. Value should be either the keyword
'full' or a decimal integer >= 0. If csl value is not given zero
context-sensitivity will be used. 
lang=<X>  The format of the produced flow facts. <X> can be one or more: 
ff             - (default) Flow fact format, see sweet -h topic=ffg.
sg             - Scope graph - includes both flow facts and a CFG.
rapita         - The RAPITA format.
ais            - The AIS format.
tcd            - Produces a dummy tcd-file (containing only basic blocks,
no statements)

o=<file-name> Specifies the flow fact file base name. By default base name
of the input file will be used. Meaning of <file-name>: The output
file's base name.

co        The result is printed to the console rather than to a disk file.

-p,--print-textually  Print data in a textual format.
Parameters: 
g=<X>     The data structures(s) to be printed. <X> can be one or more: 
cfg            - (default) Control flow graph
cfgd           - Control flow graph with debug info
pa             - Pointer analysis
cg             - Call graph
sg             - Scope graph
sym            - Symbol table
ast            - Abstract syntax tree of the program
astl           - Abstract syntax tree of the program after linkage
expl           - Exported symbols after linkage.
impl           - Imported symbols after linkage.

o=<file-name> Specifies the graph file base name.The file name ending will
indicate the file content. If not set content will be printed to
stdout. Meaning of <file-name>: The output file's base name.

co        The result is printed to the console rather than to a disk file.

-d,--dot-print  Print program graph(s) to dot file(s).
Parameters: 
g=<X>     The graph(s) to be printed. <X> can be one or more: 
cfg            - (default) Control flow graph
cfgc           - Control flow graph, nodes annotated with C-code if
mappings are available. Depends on optional loaded C-code
mappings.
cg             - Call graph
rsg            - Reduced scope graph - cfg nodes are basic blocks
fsg            - Full scope graph - cfg nodes are statements
sgh            - Scope graph hierarchy - no cfg nodes are shown.
pdg            - Program dependency graph (requires -pdg)
pcfg           - Program control-flow graph (requires -pdg)
pcdg           - Program control dependency graph (requires -pdg)
pddg           - Program data dependency graph (requires -pdg)

file=<file-name> Specifies the base name of the file where to print the
graph(s). A string indicating the format of the file will be
appended + a '.dot' suffix. If not given, the program file base
name will be used. Meaning of <file-name>: The name of the output
file(s).

function=<function name> The name of the function where to start the
print-out. This parameter only applies to the printing of scope
graphs. Meaning of <function name>: The name of the function.

max_levels=<max_levels> The maximum number of levels that will be printed.
This parameter only applies to the printing of scope graphs. 
Meaning of<max_levels>: The maximum number of levels.

dag       Prints a scope graph generated in DAG form rather than as a
context sensitive graph. This parameter only applies to the
printing of scope graphs.
tt        The nodes in the graph will be labelled using integers, and the
node names will appear as tool tips. This will make the graph more
dense.Currently only notified by the scope hierarchy.

-at,--annotation-templates=<file-name>  Tries to generate abstract annotation
templates for each imported and referenced identifiers (i.e.,
reference to undefined entity). References not possible to make
templates for it will output error messages to the console. The
annotation value will be set to TOP in case the type is known,
else the value is left to fill in manually. Other uncertenties may
be found as comments in the file. NOTE! In case of unresolved
references, the function may in general be able to update any
existing global variable, and it's the user's responsibility to
use the annotation. Information will be provided on the source
code level if label-to-C-source mapping is provided (option -m)
Meaning of <file-name>: The name of the generated file.

-ct,--cost-lookup-table-template=<file-name>  Generate cost lookup table
template. Members of selected types are printed with zero value.
Parameters: 
types=<X> The ALF types to include in the printout. If not given all types
will be used. <X> can be one or more: 
all            - All types, i.e pr+gn+op+st+sp.
pr             - Program run, a basic cost for each program run.
gn             - Generic nodes, i.e. nodes in ALF syntax tree.
op             - Operators, i.e. add, sub, ...
st             - Statements, i.e. store, call, ...
sp             - Statement pairs, i.e. <store,store>, <store,call>, ...


-fi,--function-information=<func-name(s)>  Extract call-graphs for selected
functions and print info.
Meaning of <func-name(s)>: A comma-separated list of function names. For each
function given, its corresponding call-graph will be derived. The call-graph
includes all functions reachable from the given function. Info will then be
derived and printed to different files according to the p parameter with
appropriate names, namely: <dir><func>.alf ,<dir><func>.imports,
<dir><func>.exports, and <dir><func>.template.annot. All functions must be
reachable from the current root function in the call-graph.
Parameters: 
p=<X>     The things to be printed. If not given all printouts will be used.
<X> can be one or more: 
all            - (default) All types, i.e. alf+imp+exp+at++info.
alf            - ALF program, result is written to <dir><func>.alf
imp            - Imports, result is written to <dir><func>.imports
exp            - Exports, result is written to <dir><func>.exports
at             - Annot template, result is written to
<dir><func>.template.annots
map            - Map, result is written to <dir><func>.map. Will only
produce result when -m is used. Note: inly implemented for
melmac code.
info           - Extra info file for statistics on files content.

d=<directory> The (path and) directory to which all files produced by this
option will be written. If not given all files will be stored in
the directory in which SWEET is run. 


Other
-----
-cs,--code-statistics  Produces various information about the code structure.
Parameters: 
o=<file-name> The (path and) file to which the information will be printed.
If no file name is given the result will be printed to stdout. 

-v,--version    Shows the build version and date.

-h,--help       Shows help text.
Parameters: 
topic=<X> Help topic, i.e., what to show help text on. <X> can be one of: 
option         - (default) Shows help on SWEET's parameters and options
annot          - Shows help on SWEET's input annotation language
ffg            - Shows help on flow fact generation using AE. Also gives
an introduction to SWEET's (context-sensitive
valid-at-entry-of) flow fact format.
trace          - Shows help on flow hypotheses generation using traces.

s         Use syntax high lighting on help text.

