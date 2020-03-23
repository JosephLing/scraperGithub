# source: https://gist.github.com/yuriyzubarev/2355590

# import urllib
import json
from collections import defaultdict

# # f = urllib.urlopen("http://en.wikipedia.org/wiki/Categorical_list_of_programming_languages")
# f = urllib(
#     "http://en.wikipedia.org/w/api.php?format=json&action=query&titles=List%20of%20programming%20languages%20by%20type&prop=revisions&rvprop=content")
#
# s = f.read()
#
# f.close()
s = r"""{"batchcomplete":"","warnings":{"main":{"*":"Subscribe to the mediawiki-api-announce mailing list at 
<https://lists.wikimedia.org/mailman/listinfo/mediawiki-api-announce> for notice of API deprecations and breaking 
changes. Use [[Special:ApiFeatureUsage]] to see usage of deprecated features by your application."},"revisions":{
"*":"Because \"rvslots\" was not specified, a legacy format has been used for the output. This format is deprecated, 
and in the future the new format will always be used."}},"query":{"pages":{"144144":{"pageid":144144,"ns":0,
"title":"List of programming languages by type","revisions":[{"contentformat":"text/x-wiki",
"contentmodel":"wikitext","*":"{{short description|Wikimedia list article}}\n{{Programming language lists}} \nThis is 
a list of notable [[programming language]]s, grouped by type.\n\nThere is no overarching classification scheme for 
programming languages. Thus, in many cases, a language is listed under multiple headings.\n\n== Array languages ==\n{
{Main category|Array programming languages}}\n\n[[Array programming]] (also termed ''vector'' or 
''multidimensional'') languages generalize operations on scalars to apply transparently to [[Vector (
mathematics)|vector]]s, [[Matrix (mathematics)|matrices]], and [[higher-dimensional array]]s.\n\n{{div 
col|colwidth=8em}}\n* [[A+ (programming language)|A+]]\n* [[Analytica (software)|Analytica]]\n* [[APL (programming 
language)|APL]]\n* [[Chapel (programming language)|Chapel]]\n* [[Fortran 90]]\n* [[Freemat]]\n* [[GAUSS (
software)|GAUSS]]\n* [[Interactive Data Language]] (IDL)\n* [[J (programming language)|J]]\n* [[Julia (programming 
language)|Julia]]\n* [[K (programming language)|K]]\n* [[MATLAB]]\n* [[GNU Octave|Octave]]\n<!-- [[Python (
programming language)|Python]] possibly with Numpy, but not Python alone: * -->\n* [[Q (programming language from Kx 
Systems)|Q]]\n* [[R (programming language)|R]]\n* [[S (programming language)|S]]\n* [[S-Lang]]\n* [[SequenceL]]\n* [[
Speakeasy (computational environment)|Speakeasy]]\n* [[Wolfram Language]]\n* [[X10 (programming language)|X10]]\n* [[
ZPL (programming language)|ZPL]]\n{{div col end}}\n\n== Assembly languages ==\n{{main|Assembly language}}\n\n[[
Assembly language]]s directly correspond to a [[machine language]] (see below) so machine code instructions appear in 
a form understandable by humans. Assembly languages let programmers use symbolic addresses, which the [[Assembly 
language assembler|assembler]] converts to absolute addresses. Most assemblers also support [[Macro (computer 
science)|macros]] and [[Constant (computer programming)|symbolic constant]]s.\n\n== Authoring languages ==\n{{
Main|Authoring language}}\n\nAn [[authoring language]] is a programming language used to create tutorials, websites, 
and other interactive computer programs.\n\n* [[Darwin Information Typing Architecture]] (DITA)\n* [[Lasso (
programming language)|Lasso]]\n* [[PILOT]]\n* [[TUTOR (programming language)|TUTOR]]\n\n== Constraint programming 
languages ==\n{{Main|Constraint programming}}\n\nA [[constraint programming language]] is a [[declarative programming 
language]] where relationships between variables are expressed as [[Constraint (mathematics)|constraints]]. Execution 
proceeds by attempting to find values for the variables which satisfy all declared constraints. \n\n* [[
ECLiPSe]]\n\n== Command line interface languages ==\n[[Command-line interface]] (CLI) languages are also called batch 
languages or job control languages. Examples:\n{{div col|colwidth=15em}}\n* [[4DOS]] (extended command-line shell for 
[[IBM Personal Computer|IBM PC]]s)\n* [[Bash (Unix shell)|bash]] (the Bourne-Again shell from [[GNU]], 
[[Free Software Foundation]] (FSF))\n* [[CLIST]] ([[MVS]] Command List)\n* [[CMS EXEC]]\n* [[C shell|csh]] and [[
tcsh]] (C-like shell from [[Bill Joy]] at UC [[BSD|Berkeley]])\n* [[DIGITAL Command Language]] (DCL) \u2013 standard 
CLI language for [[OpenVMS|VMS]] ([[Digital Equipment Corporation|DEC]], [[Compaq]], [[Hewlett-Packard|HP]])\n* [[
Batch file|DOS batch language]] (standard CLI/batch language for the [[IBM Personal Computer|IBM PC]] running [[DOS]] 
operating systems, popular before [[Microsoft Windows|Windows]])\n* [[EXEC 2]]\n* [[Expect]] (a [[Unix]] automation 
and test tool)\n* [[Friendly interactive shell|fish]] (a [[Unix]] shell)\n* [[Hamilton C shell]] (a C shell for 
Windows)\n* [[Job Control Language|JCL]] ([[punched card|punch card]]-oriented batch control language for [[IBM 
System/360]] family mainframes)\n* [[Korn shell|ksh]] (a standard [[Unix]] shell, written by [[David Korn (computer 
scientist)|David Korn]])\n* [[Rc]] (command-line shell for [[Plan 9 from Bell Labs|Plan 9]])\n* [[Rexx]]\n* [[Bourne 
shell|sh]] (the standard [[Unix]] shell, written by [[Stephen R. Bourne]])\n* [[TACL]] (Tandem Advanced Command 
Language)\n* [[Batch file|Windows batch language]] (Windows batch file language as understood by [[COMMAND.COM]] and 
[[CMD.EXE]])\n* [[Windows PowerShell]] ([[.NET Framework|.NET]]-based CLI)\n* [[z shell|zsh]] (a [[Unix]] shell)\n{{
div col end}}\n\n== Compiled languages ==\nThese are languages typically processed by [[compiler]]s, 
though theoretically any language can be compiled or interpreted{{citation needed|date=April 2017}}. See also [[
compiled language]].\n\n{{div col|colwidth=15em}}\n* [[ActionScript]]\n* [[Ada (programming language)|Ada]] (
multi-purpose language)\n* [[ALGOL]] (very influential language design; the second high level language compiler)\n** 
[[SMALL]] Machine ALGOL Like Language\n* [[Ballerina (programming language)|Ballerina]] (compiled to [[bytecode]] 
specific to the Ballerina Runtime (BVM))\n* [[BASIC]] (some dialects, including the first version of Dartmouth 
BASIC)\n* [[BCPL]]\n* [[C (programming language)|C]] (one of the most widely used procedural languages)\n* [[C++]] (
widely used multiparadigm language derived from C)\n* [[C Sharp (programming language)|C#]] (compiled into [[Common 
Intermediate Language|CIL]], generates a native image at runtime)\n* [[Ceylon (programming language)|Ceylon]] (
compiled into [[Java virtual machine|JVM]] [[bytecode]])\n* [[CHILL]]\n* [[Clipper (programming language)|CLIPPER 
5.3]] (programming Language for DOS-based software)\n* [[LEO (computer)|CLEO]] (Clear Language for Expressing Orders) 
on the British [[LEO (computer)|Leo computers]]\n* [[COBOL]]\n* [[Cobra (programming language)|Cobra]]\n* [[Common 
Lisp]]\n* [[Crystal (programming language)|Crystal]]\n* [[Curl (programming language)|Curl]]\n* [[D (programming 
language)|D]] (from a reengineering of C++)\n* [[Distributed Application Specification Language|DASL]] compiles into 
Java, JavaScript, JSP, Flex, etc. as .war file\n* [[Delphi (software)|Delphi]] ([[Borland]]'s [[Object Pascal]] 
development system)\n* [[DIBOL]] (Digital Interactive Business Oriented Language)\n* [[Dylan (programming 
language)|Dylan]]\n* [[eC (programming language)|eC]]\n* [[Eiffel (programming language)|Eiffel]] (object-oriented 
language developed by [[Bertrand Meyer]])\n** [[Sather]]\n** [[Ubercode]]\n* [[Elm (programming language)|Elm]]\n* [[
Emacs Lisp]]\n* [[Emerald (programming language)|Emerald]]\n* [[Erlang (programming language)|Erlang]]\n* [[F Sharp (
programming language)|F#]] (compiled into [[Common Intermediate Language|CIL]], to generate runtime image\n* [[Factor 
(programming language)|Factor]]\n* [[Forth (programming language)|Forth]] (professional systems, like VFX and 
SwiftForth)\n* [[Fortran]] (the first high-level, compiled language, from [[IBM]]'s [[John Backus]])\n* [[GAUSS (
software)|GAUSS]]\n* [[Go (programming language)|Go]]\n* [[Gosu (programming language)|Gosu]] (compiled into [[Java 
virtual machine|JVM]] [[bytecode]])\n* [[Groovy (programming language)|Groovy]] (compiled into [[Java virtual 
machine|JVM]] [[bytecode]])\n* [[Haskell (programming language)|Haskell]]\n* [[Harbour (software)|Harbour]]\n* [[Java 
(programming language)|Java]] (usually compiled into [[Java virtual machine|JVM]] [[bytecode]] although ahead-of-time 
(AOT) compilers exist that compile to [[machine code]])\n* [[JOVIAL]]\n* [[Julia (programming language)|Julia]] (
Compiled on the fly to machine code)\n* [[LabVIEW]]\n* [[Mercury (programming language)|Mercury]]\n* [[Mesa (
programming language)|Mesa]]\n* [[Nemerle]] (compiled into intermediate language bytecode)\n* [[Nim (programming 
language)|Nim]]\n* [[Objective-C]]\n* [[P (programming language)|P]]\n* [[Pascal (programming language)|Pascal]] (
most implementations)\n* [[PL/I]] (general purpose language, originally for IBM mainframes)\n* [[Plus (programming 
language)|Plus]]\n* [[Python (programming language)|Python]] (compiles to intermediate [[Virtual machine|VM]] [[
bytecode]])\n* [[IBM RPG|RPG]] (Report Program Generator)\n* [[Rust (programming language)|Rust]]\n* [[Scala (
programming language)|Scala]] (compiled into [[Java virtual machine|JVM]] [[bytecode]])\n* [[Scheme (programming 
language)|Scheme]] (some implementations, e.g. Gambit)\n* [[SequenceL]] \u2013 purely functional, automatically 
parallelizing and race-free\n* [[Simula]] (first object-oriented language, a superset of [[ALGOL 60]])\n* [[
Smalltalk]] compiles to platform independent [[bytecode]] for a Virtual Machine\n* [[Swift (programming 
language)|Swift]]\n* [[ML (programming language)|ML]]\n** [[Standard ML]] (SML)\n*** [[Alice (programming 
language)|Alice]]\n** [[OCaml]]\n* [[Turing (programming language)|Turing]]\n* [[Vala (programming language)|Vala]] (
compiler for the GObject type system)\n* [[Visual Basic]] (use [[Common Intermediate Language]] (CIL) that is JIT 
compiled into a native runtime)\n* [[Visual FoxPro]]\n* [[Visual Prolog]]\n* [[Xojo]]\n{{div col end}}\n\n== 
Concurrent languages ==\n{{Main category|Concurrent programming languages}}\n{{Main list|List of concurrent and 
parallel programming languages}}\n\n[[Message passing]] languages provide language constructs for [[concurrency (
computer science)|concurrency]]. The predominant paradigm for concurrency in mainstream languages such as [[Java (
programming language)|Java]] is [[shared memory]] concurrency. Concurrent languages that make use of message passing 
have generally been inspired by process calculi such as [[communicating sequential processes]] (CSP) or the [[
\u03c0-calculus]].\n{{div col|colwidth=15em}}\n* [[Ada (programming language)|Ada]] \u2013 multi-purpose language\n* 
[[Alef (programming language)|Alef]] \u2013 concurrent language with threads and message passing, used for systems 
programming in early versions of [[Plan 9 from Bell Labs]]\n* [[Ateji PX]] an extension of the Java language for 
parallelism\n* [[Ballerina (programming language)|Ballerina]] - a language designed for implementing and 
orchestrating micro-services. Provides a message based parallel-first concurrency model.\n* [[ChucK]] \u2013 domain 
specific programming language for audio, precise control over concurrency and timing\n* [[Cilk]] \u2013 a concurrent 
[[C (programming language)|C]]\n* [[C\u03c9]] \u2013 C Omega, a research language extending C#, uses asynchronous 
communication\n* [[Clojure]] \u2013 a dialect of [[Lisp (programming language)|Lisp]] for the [[Java virtual 
machine]]\n* [[Chapel (programming language)|Chapel]]\n* [[Co-array Fortran]]\n* [[Concurrent Pascal]] (by 
Brinch-Hansen)\n* [[Curry (programming language)|Curry]]\n* [[E (programming language)|E]] \u2013 uses promises, 
ensures deadlocks cannot occur\n* [[Eiffel (programming language)|Eiffel]] (through the [[SCOOP (software)|SCOOP]] 
mechanism, Simple Concurrent Object-Oriented Computation)\n* [[Elixir (programming language)|Elixir]] (runs on the 
Erlang VM)\n* [[Emerald (programming language)|Emerald]] - uses threads and monitors\n* [[Erlang (programming 
language)|Erlang]] \u2013 uses asynchronous message passing with nothing shared\n* [[Gambit (scheme 
implementation)|Gambit Scheme]] - using the Termite library\n* [[Go (programming language)|Go]]\n* [[Java (
programming language)|Java]]\n** [[Join Java]] \u2013 concurrent language based on Java\n** [[X10 (programming 
language)|X10]]\n* [[Julia (programming language)|Julia]]\n* [[Joule (programming language)|Joule]] \u2013 dataflow 
language, communicates by message passing\n* [[Limbo (programming language)|Limbo]] \u2013 relative of [[Alef (
programming language)|Alef]], used for systems programming in [[Inferno (operating system)]]\n* [[MultiLisp]] \u2013 
[[Scheme (programming language)|Scheme]] variant extended to support parallelism\n* [[occam (programming 
language)|occam]] \u2013 influenced heavily by [[Communicating sequential processes|Communicating Sequential 
Processes]] (CSP)\n** [[occam-\u03c0]] \u2013 a modern variant of [[occam (programming language)|occam]], 
which incorporates ideas from Milner's [[\u03c0-calculus]]\n* [[Orc (programming language)|Orc]]\n* [[Oz (programming 
language)|Oz]] \u2013 multiparadigm language, supports shared-state and message-passing concurrency, and futures, 
and Mozart Programming System [[cross-platform]] Oz\n* [[P (programming language)|P]]\n* [[Pict (programming 
language)|Pict]] \u2013 essentially an executable implementation of Milner's [[\u03c0-calculus]]\n* [[Rust (
programming language)|Rust]]\n* [[Scala (programming language)|Scala]] \u2013 implements Erlang-style [[Actor 
model|actors]] on the JVM\n* [[SequenceL]] \u2013 purely functional, automatically parallelizing and race-free\n* [[
SR (programming language)|SR]] \u2013 research language\n* [[Unified Parallel C]]\n* [[XProc]] \u2013 XML processing 
language, enabling concurrency\n{{div col end}}\n\n==  ==\n'''''' or 
'''curly-brace programming languages''' have a syntax that defines statement blocks using the [[Braces (
punctuation)| or brace characters <code>{</code> and <code>}</code>]]. This syntax originated with [[
BCPL]] (1966), and was popularized by [[C (programming language)|C]]. Many  descend from or 
are strongly influenced by C. Examples of  include:\n\n{{div col|colwidth=15em}}\n* [[
Actor-Based Concurrent Language|ABCL/c+]]\n* [[Alef (programming language)|Alef]]\n** [[Limbo (programming 
language)|Limbo]]\n*** [[Go (programming language)|Go]]\n* [[AWK]]\n* [[B (programming language)|B]]\n* [[bc (
programming language)|bc]]\n* [[BCPL]]\n* [[Ballerina (programming language)|Ballerina]]\n* [[C (programming 
language)|C]] \u2013 developed circa 1970 at [[Bell Labs]]\n* [[C++]]\n* [[C Sharp (programming language)|C#]]\n* [[
Ceylon (programming language)|Ceylon]]\n* [[ChucK]] \u2013 audio programming language\n* [[Cilk]] \u2013 concurrent C 
for multithreaded parallel programming\n* [[Cyclone (programming language)|Cyclone]] \u2013 a safer C variant\n* [[D 
(programming language)|D]]\n* [[Dart (programming language)|Dart]]\n* [[Distributed Application Specification 
Language|DASL]] \u2013 based on Java\n* [[E (programming language)|E]]\n* [[eC (programming language)|eC]]\n* [[
ECMAScript]]\n** [[ActionScript]]\n** [[ECMAScript for XML]]\n** [[JavaScript]]\n** [[JScript]]\n** [[TypeScript]]\n* 
[[OpenGL Shading Language|GLSL]]\n* [[High-Level Shading Language|HLSL]]\n* [[ICI (programming language)|ICI]]\n* [[
Java (programming language)|Java]]\n** [[Processing (programming language)|Processing]]\n** [[Groovy (programming 
language)|Groovy]]\n** [[Join Java]]\n** [[Kotlin (programming language)|Kotlin]]\n** [[Tea (programming 
language)|Tea]]\n** [[X10 (programming language)|X10]]\n* [[LPC (programming language)|LPC]]\n* [[Maya Embedded 
Language|MEL]]\n* [[Nemerle]] \u2013 combines C# and ML features, provides syntax extension abilities\n* [[
PCASTL]]\n* [[Perl]]\n* [[PHP]]\n* [[Pico (programming language)|Pico]]\n* [[Pike (programming language)|Pike]]\n* [[
PowerShell]]\n* [[R (programming language)|R]]\n* [[Rust (programming language)|Rust]]\n* [[S-Lang]]\n* [[Scala (
programming language)|Scala]]\n* [[sed]]\n* [[SuperCollider]]\n* [[Swift (programming language)|Swift]]\n* [[
UnrealScript]]\n* [[Yorick (programming language)|Yorick]]\n{{div col end}}\n<!-- It was possible, indeed trivial, 
to use automated methods for recognizing BEGIN blocks in, e.g., Alogol 60. well before BCPL and C -->\n\n== Dataflow 
languages ==\n[[Dataflow programming]] languages rely on a (usually visual) representation of the flow of data to 
specify the program.  Frequently used for reacting to discrete events or for processing streams of data.  Examples of 
dataflow languages include:\n\n{{div col}}\n* [[Analytica (software)|Analytica]]\n* [[BMDFM]]\n* [[Hartmann 
pipeline]]s\n* G (used in [[LabVIEW]])\n* [[Lucid (programming language)|Lucid]]\n* [[Max (software)|Max]]\n* [[Oz (
programming language)|Oz]]\n* [[Prograph]]\n* [[Pure Data]]\n* [[Reaktor]]\n* [[StreamBase Systems#StreamSQL 
EventFlow Language|StreamBase StreamSQL EventFlow]]\n* [[Agilent VEE|VEE]]\n* [[VHDL]]\n* [[VisSim]]\n* [[Vvvv]]\n* [
[WebMethods Flow]]\n* [[Ballerina (programming language)|Ballerina]]\n* [[Swift (parallel scripting language)]]\n{{
div col end}}\n\n== Data-oriented languages ==\nData-oriented languages provide powerful ways of searching and 
manipulating the relations that have been described as entity relationship tables which map one set of things into 
other sets.{{citation needed|date=January 2018}} Examples of data-oriented languages include:\n\n{{div col}}\n* [[
Clarion (programming language)|Clarion]]\n* [[Clipper (programming language)|Clipper]]\n* [[dBase]] a relational 
database access language\n* [[Gremlin_(programming_language)|Gremlin]]\n* [[MUMPS]] (an ANSI standard general purpose 
language with specializations for database work)\n* [[Cach\u00e9 (software)|Cach\u00e9]] (similar to MUMPS)\n* [[
RDQL]]\n* [[SPARQL]]\n* [[SQL]]\n* [[D (data language specification)|Tutorial D]] \u2013 see also [[The Third 
Manifesto]]\n* [[Visual FoxPro]] \u2013 a native RDBMS engine, object-oriented, RAD\n* [[WebDNA]]\n* [[Wolfram 
Language]]\n{{div col end}}\n\n== Decision table languages ==\n[[Decision table]]s can be used as an aid to 
clarifying the logic before writing a program in any language, but in the 1960s a number of languages were developed 
where the main logic is expressed directly in the form of a decision table, including:\n\n* [[Filetab]]\n\n== 
Declarative languages ==\n{{Main category|Declarative programming languages}}\n\n[[Declarative 
programming|Declarative languages]] express the logic of a computation without describing its control flow in detail. 
[[Declarative programming]] stands in contrast to [[imperative programming]] via imperative programming languages, 
where control flow is specified by serial orders (imperatives). (Pure) [[#Functional languages|functional]] and [[
#Logic-based languages|logic-based]] programming languages are also declarative, and constitute the major 
subcategories of the declarative category. This section lists additional examples not in those subcategories.\n\n* [[
Analytica (software)|Analytica]]\n* [[Apache Ant|Ant]] (combine [[declarative programming]] and [[imperative 
programming]])\n* [[Cypher (query language)|Cypher]]\n* [[Distributed Application Specification Language]] (DASL) (
combine [[declarative programming]] and [[imperative programming]])\n* [[ECL (data-centric programming 
language)|ECL]]\n* [[Gremlin (programming language)|Gremlin]]\n* [[Lustre (programming language)|Lustre]]\n* [[
Mercury (programming language)|Mercury]]\n* [[MetaPost]]\n* [[Modelica]]\n* [[Prolog]]\n* [[QML]]\n* [[Oz (
programming language)|Oz]]\n* [[RDQL]]\n* [[SequenceL]] \u2013 purely functional, automatically parallelizing and 
race-free\n* [[SPARQL]]\n* [[SQL]]\n* [[Wolfram Language]]\n* [[xBase]]\n* [[XSL Transformations]]\n\n== Embeddable 
languages ==\n\n=== In source code ===\nSource embeddable languages embed small pieces of executable code inside a 
piece of free-form text, often a web page.\n\nClient-side embedded languages are limited by the abilities of the 
browser or intended client. They aim to provide dynamism to web pages without the need to recontact the 
server.\n\nServer-side embedded languages are much more flexible, since almost any language can be built into a 
server. The aim of having fragments of server-side code embedded in a web page is to generate additional markup 
dynamically; the code itself disappears when the page is served, to be replaced by its output.\n\n==== Server side 
====\n* [[PHP]]\n* [[VBScript]]\n* [[SMX (computer language)|SMX]] \u2013 dedicated to web pages\n* [[Tcl]] \u2013 
server-side in [[NaviServer]] and an essential component in electronics industry systems\n* [[WebDNA]] \u2013 
dedicated to database-driven websites\n\nThe above examples are particularly dedicated to this purpose. A large 
number of other languages, such as [[Erlang (programming language)|Erlang]], [[Scala (programming language)|Scala]], 
[[Perl]] and [[Ruby (programming language)|Ruby]] can be adapted (for instance, by being made into [[Apache HTTP 
Server|Apache]] modules).\n\n==== Client side ====\n* [[ActionScript]]\n* [[JavaScript|JavaScript (aka ECMAScript or 
JScript)]]\n* [[VBScript]] (Windows only)\n\n=== In object code ===\nA wide variety of dynamic or scripting languages 
can be embedded in compiled executable code. Basically, object code for the language's [[interpreter (
computing)|interpreter]] needs to be linked into the executable. Source code fragments for the embedded language can 
then be passed to an evaluation function as strings. Application control languages can be implemented this way, 
if the source code is input by the user. Languages with small interpreters are preferred.\n\n{{div col}}\n* [[
AngelScript]]\n* [[Ch (computer programming)|Ch]]\n* [[Extensible Embeddable Language|EEL]]\n* [[Io (programming 
language)|Io]]\n* [[Julia (programming language)|Julia]]\n* [[Lua (programming language)|Lua]]\n* [[MiniD]]\n* [[
Python (programming language)|Python]]\n* [[Ruby (programming language)|Ruby]] (via [[mruby]])\n* [[Squirrel (
programming language)|Squirrel]]\n* [[Tcl]]\n{{div col end}}\n\n== Educational languages ==\n{{Main list|List of 
educational programming languages}}\n\nLanguages developed primarily for the purpose of teaching and learning of 
programming.\n\n{{div col}}\n* [[Alice (software)|Alice]]\n* [[Blockly]] \n* [[COMAL (programming 
language)|COMAL]]\n* [[ELAN (programming language)|Elan]]\n* [[Emerald (programming language)|Emerald]]\n* [[Logo (
programming language)|Logo]]\n* [[KTurtle]]\n* [[Modula-2]]\n* [[Pascal (programming language)|Pascal]]\n* [[Python (
programming language)|Python]]\n* [[Racket (programming language)|Racket]]\n* [[Scheme (programming 
language)|Scheme]]\n* [[Scratch (programming language)|Scratch]]\n* [[Snap! (programming language)|Snap!]] \n* [[
Turing (programming language)|Turing]]\n* [[Wolfram Language]]\n{{div col end}}\n\n== Esoteric languages ==\n{{Main 
category|Esoteric programming languages}}\n\nAn [[esoteric programming language]] is a programming language designed 
as a test of the boundaries of computer programming language design, as a proof of concept, or as a joke.\n\n{{div 
col}}\n* [[Beatnik (programming language)|Beatnik]]\n* [[Befunge]]\n* [[Brainfuck]]\n* [[Chef (programming 
language)|Chef]]\n* [[INTERCAL]]\n* [[LOLCODE]]\n* [[Malbolge]]\n* [[Piet (programming language)|Piet]]\n* [[
Shakespeare (programming language)|Shakespeare]]\n* [[Whitespace (programming language)|Whitespace]]\n{{div col 
end}}\n\n== Extension languages ==\n[[Extension programming language]]s are languages embedded into another program 
and used to harness its features in extension scripts.\n{{div col}}\n* [[AutoLISP]] (specific to [[AutoCAD]])\n* [[
BeanShell]]\n* [[Cakewalk (sequencer)#Features|CAL]]\n* [[C/AL]] (C/SIDE)\n* [[GNU Guile|Guile]]\n* [[Emacs Lisp]]\n* 
[[JavaScript]] and some dialects, e.g., [[JScript]]\n* [[Lua (programming language)|Lua]] (embedded in many games)\n* 
[[OpenCL]] (extension of C and C++ to use the GPU and parallel extensions of the CPU)\n* [[OptimJ]] (extension of 
Java with language support for writing optimization models and powerful abstractions for bulk data processing)\n* [[
Perl]]\n* [[Pike (programming language)|Pike]]\n* [[Python (programming language)|Python]] (embedded in Maya, 
Blender, and other 3-D animation packages)\n* [[Rexx]]\n* [[Ruby (programming language)|Ruby]] (Google SketchUp)\n* [
[S-Lang]]\n* [[SQL]]\n* [[Squirrel (programming language)|Squirrel]]\n* [[Tcl]]\n* [[Vim script]]\n* [[Visual Basic 
for Applications]] (VBA)\n* [[Windows PowerShell]]\n{{div col end}}\n\n== Fourth-generation languages ==\n{{Main 
category|4GL}}\n\n[[Fourth-generation programming language]]s are high-level languages built around database systems. 
They are generally used in commercial environments.\n\n{{div col}}\n* [[1C:Enterprise programming language]]\n* [[
ABAP]]\n* [[CorVision]]\n* [[Computer Sciences Corporation|CSC]]'s GraphTalk\n* [[DATACOM/DB|CA-IDEAL]] (Interactive 
Development Environment for an Application Life) for use with [[DATACOM/DB|CA-DATACOM/DB]]\n* [[Easytrieve]] report 
generator (now CA-Easytrieve Plus)\n* [[FOCUS]]\n* [[IBM Informix-4GL]]\n* [[LINC 4GL]]\n* [[MAPPER]] ([[
Unisys|Unisys/Sperry]]) \u2013 now part of BIS\n* [[MARK IV (software)|MARK-IV]] ([[Sterling 
Software|Sterling/Informatics]]) now VISION:BUILDER of CA\n* [[NATURAL]]\n* [[Progress 4GL]]\n* [[PV-Wave]]\n* [[
LiveCode]] (not based on a database; still, the goal is to work at a higher level of abstraction than 3GLs)\n* [[SAS 
System|SAS]]\n* [[SQL]]\n* [[Ubercode]] (VHLL, or Very High Level Language)\n* [[Uniface (programming 
language)|Uniface]]\n* [[Visual DataFlex]]\n* [[Visual FoxPro]]\n* [[xBase]]\n{{div col end}}\n\n== Functional 
languages ==\n{{Main category|Functional languages}}\n\n[[Functional programming]] languages define programs and 
subroutines as mathematical functions and treat them as first-class. Many so-called functional languages are 
\"impure\", containing imperative features. Many functional languages are tied to mathematical calculation tools. 
Functional languages include:\n\n=== Pure ===\n{{div col|colwidth=10em}}\n* [[Agda (programming language)|Agda]]\n* [
[Clean (programming language)|Clean]]\n* [[Coq]] (Gallina)\n* [[Cuneiform (programming language)|Cuneiform]]\n* [[
Curry (programming language)|Curry]]\n* [[Elm (programming language)|Elm]]\n* [[Futhark (programming 
language)|Futhark]]\n* [[Haskell (programming language)|Haskell]]\n* [[Hope (programming language)|Hope]]\n* [[Idris 
(programming language)|Idris]]\n* [[Joy (programming language)|Joy]]\n* [[Mercury (programming language)|Mercury]]\n* 
[[Miranda (programming language)|Miranda]]\n* [[PureScript]]\n* [[Ur (programming language)|Ur]]\n* [[Kent Recursive 
Calculator|KRC]]\n* [[SAC programming language|SAC]]\n* [[SASL (programming language)|SASL]]\n* [[SequenceL]]\n{{div 
col end}}\n\n=== Impure ===\n{{div col|colwidth=15em}}\n* [[APL (programming language)|APL]]\n* [[ATS (programming 
language)|ATS]]\n* [[CAL (programming language)|CAL]]\n* [[C++]] (since [[C++11]])\n* [[C Sharp (programming 
language)|C#]]\n* [[Ceylon (programming language)|Ceylon]]\n* [[D (programming language)|D]]\n* [[Dart (programming 
language)|Dart]]\n* [[Curl (programming language)|Curl]]\n* [[ECMAScript]]\n** [[ActionScript]]\n** [[ECMAScript for 
XML]]\n** [[JavaScript]]\n** [[JScript]]\n** [[Source (programming language)|Source]]\n* [[Erlang (programming 
language)|Erlang]]\n** [[Elixir (programming language)|Elixir]]\n** [[LFE (programming language)|LFE]]\n* [[F Sharp (
programming language)|F#]]\n* [[Groovy (programming language)|Groovy]]\n* [[Hop (software)|Hop]]\n* [[J (programming 
language)|J]]\n* [[Java (programming language)|Java (since version 8)]]\n* [[Julia (programming language)|Julia]]\n* 
[[Kotlin (programming language)|Kotlin]]\n* [[Lisp (programming language)|Lisp]]\n** [[Clojure]]\n** [[Common 
Lisp]]\n** [[Dylan (programming language)|Dylan]]\n** [[Emacs Lisp]]\n** [[LFE (programming language)|LFE]]\n** [[
Little b (programming language)|Little b]]\n** [[Logo (programming language)|Logo]]\n** [[Scheme (programming 
language)|Scheme]]\n*** [[Racket (programming language)|Racket]] (formerly PLT Scheme)\n** [[Tea (programming 
language)|Tea]]\n* [[Mathematica]] \n* [[ML (programming language)|ML]]\n** [[Standard ML]] (SML)\n*** [[Alice (
programming language)|Alice]]\n** [[OCaml]]\n* [[Nemerle]]\n* [[Nim (programming language)|Nim]]\n* [[Opal (
programming language)|Opal]]\n* [[OPS5]]\n* [[Perl]]\n* [[PHP]]\n* [[Python (programming language)|Python]]\n* [[Q (
equational programming language)]]\n* [[Q (programming language from Kx Systems)]]\n* [[R (programming 
language)|R]]\n* [[Raku (programming language)|Raku]]\n* [[REBOL]]\n* [[Red (programming language)|Red]]\n* [[Ruby (
programming language)|Ruby]]\n* [[REFAL]]\n* [[Rust (programming language)|Rust]]\n* [[Scala (programming 
language)|Scala]]\n* [[Spreadsheet]]s\n* [[Tcl]]\n* [[Wolfram Language]]\n{{div col end}}\n\n== Hardware description 
languages ==\n{{Main list|List of hardware description languages}}\n\nIn electronics, a [[hardware description 
language]] (HDL) is a specialized computer language used to describe the structure, design, and operation of 
electronic circuits, and most commonly, digital logic circuits. The two most widely used and well-supported HDL 
varieties used in industry are [[Verilog]] and [[VHDL]]. Hardware description languages include:\n\n=== HDLs for 
analog circuit design ===\n* [[Verilog-AMS]] (Verilog for Analog and Mixed-Signal)\n* [[VHDL-AMS]] (VHDL with 
Analog/Mixed-Signal extension)\n\n=== HDLs for digital circuit design ===\n{{div col}}\n* [[Advanced Boolean 
Expression Language]](ABEL)\n* [[Altera Hardware Description Language]](AHDL)\n* [[Bluespec]]\n* [[Confluence]]\n* [[
ELLA (programming language)|ELLA]]\n* [[ESys.net]]\n* [[Handel-C]]\n* [[Impulse C]]\n* [[JHDL]]\n* [[Lava (
programming language)|Lava]]\n* [[Lola (computing)|Lola]]\n* [[M]]\n* [[MyHDL]]\n* [[PALASM]]\n* [[Ruby (hardware 
description language)]]\n* [[SystemC]]\n* [[SystemVerilog]]\n* [[Verilog]]\n* [[VHDL]] (VHSIC HDL)\n{{div col 
end}}\n\n== Imperative languages ==\nImperative programming languages may be multi-paradigm and appear in other 
classifications. Here is a list of programming languages that follow the [[imperative paradigm]]:\n\n{{div 
col|colwidth=10em}}\n* [[Ada (programming language)|Ada]]\n* [[ALGOL]]\n* [[BASIC]]\n* [[C (programming 
language)|C]]\n* [[C++]]\n* [[C Sharp (programming language)|C#]]\n* [[Ceylon (programming language)|Ceylon]]\n* [[
CHILL]]\n* [[COBOL]]\n* [[D (programming language)|D]]\n* [[ECMAScript]]\n** [[ActionScript]]\n** [[ECMAScript for 
XML]]\n** [[JavaScript]]\n** [[JScript]]\n** [[Source (programming language)|Source]]\n* [[FORTRAN]]\n* [[GAUSS (
software)|GAUSS]]\n* [[Go (programming language)|Go]]\n* [[Groovy (programming language)|Groovy]]\n* [[Java (
programming language)|Java]]\n* [[Julia (programming language)|Julia]]\n* [[Lua (programming language)|Lua]]\n* [[
MATLAB]]\n* [[Machine code|Machine language]]\n* [[Modula-2]], [[Modula-3]]\n* [[MUMPS]]\n* [[Nim (programming 
language)|Nim]]\n* [[OCaml]]\n* [[Oberon (programming language)|Oberon]]\n* [[Object Pascal]]\n* [[Pascal (
programming language)|Pascal]]\n* [[Perl]]\n* [[PHP]]\n* [[PL/I]]\n* [[PowerShell]]\n* [[PROSE modeling 
language|PROSE]]\n* [[Python (programming language)|Python]]\n* [[Ruby (programming language)|Ruby]]\n* [[Rust (
programming language)|Rust]]\n* [[Speakeasy (computational environment)|Speakeasy]]\n* [[Swift (programming 
language)|Swift]]\n* [[Tcl]]\n* [[Wolfram Language]]\n{{div col end}}\n\n== Interactive mode languages 
==\nInteractive mode languages act as a kind of shell: expressions or statements can be entered one at a time, 
and the result of their evaluation is seen immediately. The interactive mode is also termed a [[
read\u2013eval\u2013print loop]] (REPL).\n\n{{div col|colwidth=15em}}\n* [[APL (programming language)|APL]]\n* [[
BASIC]] (some dialects)\n* [[Clojure]]\n* [[Common Lisp]]\n* [[Dart (programming language)|Dart]] (with Observatory 
or Dartium's developer tools)\n* [[ECMAScript]]\n** [[ActionScript]]\n** [[ECMAScript for XML]]\n** [[
JavaScript]]\n** [[JScript]]\n** [[Source (programming language)|Source]]\n* [[Erlang (programming 
language)|Erlang]]\n* [[Elixir (programming language)|Elixir]] (with iex)\n* [[F Sharp (programming language)|F#]]\n* 
[[Forth (programming language)|Forth]]\n* [[Fril]]\n* [[GAUSS (software)|GAUSS]]\n* [[Groovy (programming 
language)|Groovy]]\n* [[Haskell (programming language)|Haskell]] (with the GHCi or Hugs interpreter)\n* [[IDL (
programming language)|IDL]]\n* [[J (programming language)|J]]\n* [[Java (programming language)|Java]] (since version 
9)\n* [[Julia (programming language)|Julia]]\n* [[Lua (programming language)|Lua]]\n* [[MUMPS]] (an ANSI standard 
general purpose language)\n* [[Maple (software)|Maple]]\n* [[Mathematica]] ([[Wolfram language]])\n* [[MATLAB]]\n* [[
ML (programming language)|ML]]\n* [[OCaml]]\n* [[Perl]]\n* [[PHP]]\n* [[Pike (programming language)|Pike]]\n* [[
PostScript]]\n* [[Prolog (programming language)|Prolog]]\n* [[Python (programming language)|Python]]\n* [[PROSE 
modeling language|PROSE]]\n* [[R (programming language)|R]]\n* [[REBOL]]\n* [[Rexx]]\n* [[Ruby (programming 
language)|Ruby]] (with [[Interactive Ruby Shell|IRB]])\n* [[Scala (programming language)|Scala]]\n* [[Scheme (
programming language)|Scheme]]\n* [[Smalltalk]] (anywhere in a Smalltalk environment)\n* [[S-Lang]] (with the S-Lang 
shell, slsh)\n* [[Speakeasy (computational environment)|Speakeasy]]\n* [[Swift (programming language)|Swift]]\n* [[
Tcl]] (with the Tcl shell, tclsh)\n* [[Unix shell]]\n* [[Windows PowerShell]] ([[.NET Framework|.NET]]-based CLI)\n* 
[[Visual FoxPro]]\n{{div col end}}\n\n== Interpreted languages ==\n[[Interpreted language]]s are programming 
languages in which programs may be executed from source code form, by an interpreter. Theoretically, any language can 
be compiled or interpreted, so the term ''interpreted language'' generally refers to languages that are usually 
interpreted rather than compiled.\n\n{{div col|colwidth=15em}}\n* [[Apache Ant|Ant]]\n* [[APL (programming 
language)|APL]]\n* [[AutoHotkey]] scripting language\n* [[AutoIt]] scripting language\n* [[BASIC]] (some dialects)\n* 
[[Programming Language for Business]] (PL/B, formerly DATABUS, later versions added optional compiling)\n* [[DM (
computing)|DM]]\n* [[Eiffel (programming language)|Eiffel]] (via ''Melting Ice Technology'' in [[EiffelStudio]])\n* [
[Emacs Lisp]]\n* [[Forth (programming language)|Forth]] (interactive shell only, otherwise compiled to native or [[
threaded code]])\n* [[GameMaker Studio|GameMaker Language]]\n* [[Groovy (programming language)|Groovy]]\n* [[J (
programming language)|J]]\n* [[Julia (programming language)|Julia]] (compiled on the fly to [[machine code]], 
but a transpiler [[Julia (programming language)#Julia2C|Julia2C]] exists)\n* [[JavaScript]]\n* [[Lisp (programming 
language)|Lisp]] (early versions, pre-1962, and some experimental ones; production Lisp systems are compilers, 
but many of them still provide an interpreter if needed)\n* [[LPC (programming language)|LPC]]\n* [[Lua (programming 
language)|Lua]]\n* [[MUMPS]] (an ANSI standard general purpose language)\n* [[Maple (software)|Maple]]\n* [[
Mathematica]]\n* [[MATLAB]]\n* [[OCaml]]\n* [[Pascal (programming language)|Pascal]] (early implementations)\n* [[
PCASTL]]\n* [[Perl]]\n* [[PHP]]\n* [[PostScript]]\n* [[PowerShell]]\n* [[PROSE modeling language|PROSE]]\n* [[Python 
(programming language)|Python]]\n* [[Rexx]]\n* [[R (programming language)|R]]\n* [[REBOL]]\n* [[Ruby (programming 
language)|Ruby]]\n* [[S-Lang]]\n* [[Speakeasy (computational environment)|Speakeasy]]\n* [[Standard ML]] (SML)\n* [[
Parallax Propeller|Spin]]\n* [[Tcl]]\n* [[Tea (programming language)|Tea]]\n* [[TorqueScript]]\n* [[thinBasic]] 
scripting language\n* [[VBScript]]\n* [[Windows PowerShell]] \u2013 [[.NET Framework|.NET]]-based CLI\n* [[Wolfram 
Language]]\n* Some scripting languages \u2013 [[#Scripting languages|below]]\n{{div col end}}\n\n== Iterative 
languages ==\nIterative languages are built around or offering [[generator (computer science)|generator]]s.\n\n{{div 
col|colwidth=20em}}\n* [[Aldor]]\n* [[Alphard (programming language)|Alphard]]\n* [[Generator (computer 
science)#C#|C#]]\n* [[CLU (programming language)|CLU]]\n* [[Cobra (programming language)|Cobra]]\n* [[Eiffel (
programming language)|Eiffel]], through \"agents\"\n* [[Icon (programming language)|Icon]]\n* [[Information 
Processing Language|IPL-v]]\n* [[Julia (programming language)|Julia]]<!-- from memory, has iterators and I if I 
recall generators..-->\n* [[Lua (programming language)|Lua]]\n* [[Nim (programming language)|Nim]]\n* [[PHP]]\n* [[
Python (programming language)|Python]]\n* [[Sather]]\n{{div col end}}\n\n== Languages by memory management type 
==\n\n=== Garbage collected languages ===\n{{Expand section|date=November 2016}}\n{{div col|colwidth=15em}}\n* [[C 
Sharp (programming language)|C#]]\n* [[ECMAScript]]\n** [[ActionScript]]\n** [[ECMAScript for XML]]\n** [[
JavaScript]]\n** [[JScript]]\n** [[Source (programming language)|Source]]\n* [[Emerald (programming 
language)|Emerald]]\n* [[Erlang (programming language)|Erlang]]\n* [[Go (programming language)|Go]]\n* [[Apache 
Groovy|Groovy]]\n* [[Java (programming language)|Java]]\n* [[Kotlin (programming language)|Kotlin]]\n* [[Lisp (
programming language)|Lisp]] (originator)\n** [[Arc (programming language)|Arc]]\n** [[Clojure]]\n** [[Common 
Lisp]]\n** [[Dylan (programming language)|Dylan]]\n** [[Emacs Lisp]]\n** [[Racket (programming language)|Racket]]\n** 
[[Scheme (programming language)|Scheme]]\n** [[Logo (programming language)|Logo]]\n* [[Haskell (programming 
language)|Haskell]]\n* [[Lua (programming language)|Lua]]\n* [[ML (programming language)|ML]]\n** [[Standard ML]] (
SML)\n*** [[Alice (programming language)|Alice]]\n** [[OCaml]]\n* [[Perl]]\n* [[PHP]]\n* [[PowerShell]]\n* [[Python (
programming language)|Python]]\n* [[Ruby (programming language)|Ruby]]\n* [[Smalltalk]]\n{{div col end}}\n\n=== 
Languages with manual memory management ===\n{{Expand section|date=November 2016}}\n* [[Ada (programming 
language)|Ada]]\n* [[C (programming language)|C]]\n* [[C++]]\n* [[Fortran]]\n* [[Pascal (programming 
language)|Pascal]]\n* [[Rust (programming language)|Rust]]\n* [[Objective-C]]\n\n=== Languages with deterministic 
memory management ===\n{{Expand section|date=April 2018}}\n*[[Ada (programming language)|Ada]]\n* [[C (programming 
language)|C]]\n* [[C++]]\n* [[Fortran]]\n* [[Pascal (programming language)|Pascal]]\n* [[Rust (programming 
language)|Rust]]<ref>{{cite web|url=https://doc.rust-lang.org/nightly/book/ch04-00-understanding-ownership.html|title
=Understanding Ownership - The Rust Programming Language|website=doc.rust-lang.org}}</ref><ref>{{cite 
web|url=https://doc.rust-lang.org/nightly/book/second-edition/ch15-00-smart-pointers.html|title=Smart Pointers - The 
Rust Programming Language|website=doc.rust-lang.org}}</ref>\n* [[Objective-C]]\n\n=== Languages with automatic 
reference counting (ARC) ===\n{{Expand section|date=September 2018}}\n* [[Objective-C]]\n* [[Swift (programming 
language)|Swift]]\n* [[Visual Basic]]\n* [[Xojo]]\n\n== List-based languages \u2013 LISPs ==\nList-based languages 
are a type of [[data-structured language]] that are based on the [[List (abstract data type)|list]] data 
structure.\n{{div col}}\n{{no col break|\n* [[Lisp (programming language)|Lisp]]\n** [[Arc (programming 
language)|Arc]]\n** [[Clojure]]\n** [[Common Lisp]]\n** [[Dylan (programming language)|Dylan]]\n** [[Emacs Lisp]]\n** 
[[Racket (programming language)|Racket]]\n** [[Scheme (programming language)|Scheme]]\n** [[Logo (programming 
language)|Logo]]\n}}\n* [[Joy (programming language)|Joy]]\n* [[R (programming language)|R]]\n* [[Source (programming 
language)|Source]]\n* [[Tcl]]\n** [[Tea (programming language)|Tea]]\n* [[TRAC (programming language)|TRAC]]\n{{div 
col end}}\n\n== Little languages ==\n[[Domain-specific language|Little languages]]<ref> Jon Bentley (AT&T) August 
1986 ''CACM'' '''29''' (8) \"Little Languages\", pp 711-721 from his [
http://www.cs.toronto.edu/~chechik/courses18/csc2125/paper13.pdf Programming Pearls column]</ref> serve a specialized 
problem domain.\n\n* [[AWK|awk]] \u2013 can serve as a prototyping language for [[C (programming language)|C]] (
shares similar syntax)\n* [[Comet (programming language)|Comet]] \u2013 used to solve complex combinatorial [[Program 
optimization|optimization]] problems in areas such as [[resource allocation]] and [[Scheduling (
computing)|scheduling]]\n* [[sed]] \u2013 parses and transforms text\n* [[SQL]] \u2013 has only a few keywords, 
and not all the constructs needed for a full programming language{{efn|The objects of SQL are collections of [[
database record]]s, called tables. A full [[programming language]] can specify [[algorithm]]s, irrespective of [[
software execution|runtime]]. Thus an algorithm can be considered to generate usable results. In contrast, 
SQL can only select records which are limited to the current collection, the data at hand in the system, rather than 
produce a statement of the correctness of the result.}} \u2013 many database management systems extend SQL with 
additional constructs as a [[stored procedure]] language\n\n== Logic-based languages ==\n{{Main category|Logic 
programming languages}}\n\n[[Logic programming|Logic-based]] languages specify a set of attributes that a solution 
must have, rather than a set of steps to obtain a solution.\n\nExamples:\n* [[Algebraic Logic Functional (programming 
language)|ALF]]\n* [[Alma-0]]\n* [[CLACL (programming language)|CLACL (CLAC-Language)]]\n* [[Curry (programming 
language)|Curry]]\n* [[Fril]]\n* [[Janus (concurrent constraint programming language)|Janus]]\n* [[\u03bbProlog]] (a 
logic programming language featuring polymorphic typing, modular programming, and higher-order programming)\n* [[Oz (
programming language)|Oz]], and Mozart Programming System [[cross-platform]] Oz\n* [[Prolog]] (formulates data and 
the program evaluation mechanism as a special form of mathematical logic called [[Horn clause|Horn logic]] and a 
general proving mechanism called [[Resolution (logic)|logical resolution]])\n** [[Mercury (programming 
language)|Mercury]] (based on Prolog)\n** [[Visual Prolog]] (object-oriented Prolog extension)\n* [[ROOP (programming 
language)|ROOP]]\n\n== Machine languages ==\n[[Machine code|Machine language]]s are directly executable by a 
computer's CPU. They are typically formulated as bit patterns, usually represented in [[octal]] or [[hexadecimal]]. 
Each bit pattern causes the circuits in the CPU to execute one of the fundamental operations of the hardware. The 
activation of specific electrical inputs (e.g., CPU package pins for microprocessors), and logical settings for CPU 
state values, control the processor's computation. Individual machine languages are specific to a family of 
processors; machine-language code for one family of processors cannot run directly on processors in another family 
unless the processors in question have additional hardware to support it (for example, DEC VAX processors included a 
PDP-11 compatibility mode). They are (essentially) always defined by the CPU developer, not by 3rd parties. The 
symbolic version, the processor's [[assembly language]], is also defined by the developer, in most cases. Some 
commonly used machine code [[instruction set]]s are:\n\n{{div col}}\n* [[ARM architecture|ARM]]\n** Original 
32-bit\n** 16-bit Thumb instructions (subset or registers used)\n** 64-bit (major architecture change, 
more registers)\n* [[Digital Equipment Corporation|DEC]]:\n** 18-bit: [[PDP-1]], [[PDP-4]], [[PDP-7]], [[PDP-9]], 
[[PDP-15]]\n** 12-bit: [[PDP-5]], [[PDP-8]], [[LINC-8]], [[PDP-12]]\n** 36-bit: [[PDP-6]], [[PDP-10]], 
[[DECSYSTEM-20]]\n** 16-bit: [[PDP-11]] (influenced VAX and M68000)\n** 32-bit: [[VAX]]\n** 64-bit: [[DEC 
Alpha|Alpha]]\n* [[Intel Corporation|Intel]] [[Intel 8008|8008]], [[Intel 8080|8080]] and [[Intel 8085|8085]]\n** [[
Zilog Z80]]\n* [[x86]]:\n** [[x86#16-bit|16-bit x86]], first used in the Intel 8086\n*** [[Intel 8086]] and [[Intel 
8088|8088]] (the latter was used in the first and early [[IBM PC]])\n*** [[Intel 80186]]\n*** [[Intel 80286]] (the 
first x86 processor with [[protected mode]], used in the [[IBM AT]])\n** [[IA-32]], introduced in the [[80386]]\n** [
[x86-64]] The original specification was created by [[Advanced Micro Devices|AMD]]. There are vendor variants, 
but they're essentially the same:\n*** [[Advanced Micro Devices|AMD's]] [[x86-64#AMD64|AMD64]]\n*** [[Intel 
Corporation|Intel's]] [[Intel 64]]\n* [[IBM System/360]] and successors, including [[z/Architecture]]\n* [[MIPS 
architecture|MIPS]]\n* [[Motorola 6800]]\n* [[Motorola 68000 family]] (CPUs used in early [[Apple Macintosh]] and 
early [[Sun Microsystems|Sun]] computers)\n* [[MOS Technology]] [[MOS Technology 65xx|65xx]]\n** [[MOS Technology 
6502|6502]] (CPU for [[Commodore VIC-20|VIC-20]], [[Apple II family|Apple II]], and [[Atari 8-bit family|Atari 
800]])\n** [[MOS Technology 6510|6510]] (CPU for [[Commodore 64]])\n** [[Western Design Center]] [[WDC 
65816/65802|65816/65802]] (CPU for [[Apple IIGS]] and (variant) [[Super Nintendo Entertainment System]])\n* National 
[[NS320xx]]\n* [[IBM POWER Instruction Set Architecture|POWER]], first used in the [[IBM RS/6000]]\n** [[PowerPC]] 
\u2013 used in [[Power Macintosh]] and in many [[PowerPC#Gaming consoles|game consoles]], particularly of the [[
Seventh generation of video game consoles|seventh generation]].\n** [[Power ISA]]\n* Sun, [[Oracle 
Corporation|Oracle]] [[SPARC]]\n* [[Moscow Center of SPARC Technologies|MCST]] [[Elbrus 2000]]\n{{div col end}}\n\n== 
Macro languages ==\n{{Main category|Macro programming languages}}\n\n=== Textual substitution macro languages ===\n[[
Macro (computer science)|Macro]] languages transform one source code file into another. A \"macro\" is essentially a 
short piece of text that expands into a longer one (not to be confused with [[hygienic macro]]s), possibly with 
parameter substitution. They are often used to [[preprocess]] source code. Preprocessors can also supply facilities 
like [[Include directive|file inclusion]].\n\nMacro languages may be restricted to acting on specially labeled code 
regions (pre-fixed with a <code>#</code> in the case of the C preprocessor). Alternatively, they may not, but in this 
case it is still often undesirable to (for instance) expand a macro embedded in a [[string literal]], so they still 
need a rudimentary awareness of syntax. That being the case, they are often still applicable to more than one 
language. Contrast with source-embeddable languages like [[PHP]], which are fully featured.\n\n* [[C 
preprocessor|cpp]] (the C preprocessor)\n* [[M4 (computer language)|m4]] (originally from AT&T, bundled with Unix)\n* 
[[ML/I]] (general purpose macro processor)\n\n=== Application macro languages ===\n[[Scripting language]]s such as [[
Tcl]] and [[ECMAScript]] ([[ActionScript]], [[ECMAScript for XML]], [[JavaScript]], [[JScript]]) have been embedded 
into applications. These are sometimes called \"macro languages\", although in a somewhat different sense to 
textual-substitution macros like [[M4 (computer language)|m4]].\n\n== Metaprogramming languages ==\n[[
Metaprogramming]] is the writing of programs that write or manipulate other programs, including themselves, 
as their data or that do part of the work that is otherwise done at [[Run time (program lifecycle phase)|run time]] 
during [[compile time]]. In many cases, this allows programmers to get more done in the same amount of time as they 
would take to write all the code manually.\n\n{{div col|colwidth=15em}}\n* [[C++]]\n* [[Compiler 
compiler#CWIC|CWIC]]\n* [[Curl (programming language)|Curl]]\n* [[D (programming language)|D]]\n* [[eC (programming 
language)|eC]]\n* [[Emacs Lisp]]\n* [[Elixir (programming language)|Elixir]]\n* [[Forth (programming 
language)|Forth]]\n* [[F Sharp (programming language)|F#]]\n* [[Groovy (programming language)|Groovy]]\n* [[Haskell (
programming language)|Haskell]]\n* [[Julia (programming language)|Julia]]\n* [[Lisp (programming language)|Lisp]]\n* 
[[Lua (programming language)|Lua]]\n* [[Maude system]]\n* [[Mathematica]]\n* [[META II]] (and META I, a subset)\n* [[
MetaOCaml]]\n* [[Nemerle]]\n* [[Nim (programming language)|Nim]]\n* [[Perl]]\n* [[Python (programming 
language)|Python]]\n* [[Ruby (programming language)|Ruby]]\n* [[Rust (programming language)|Rust]]<ref>{{cite 
web|url=https://doc.rust-lang.org/nightly/book/ch19-06-macros.html#procedural-macros-for-generating-code-from
-attributes|title=Procedural Macros for Generating Code from Attributes|website=doc.rust-lang.org}}</ref>\n* [[Scheme 
(programming language)|Scheme]]\n* [[SequenceL]]\n* [[Smalltalk]]\n* [[Source (programming language)|Source]]\n* [[
TREE-META|TREEMETA]]\n* [[Wolfram Language]]\n{{div col end}}\n\n== Multiparadigm languages ==\n{{main|Comparison of 
multi-paradigm programming languages}}\n[[Multi-paradigm programming language|Multiparadigm language]]s support more 
than one [[programming paradigm]]. They allow a [[Computer program|program]] to use more than one [[Computer 
program|programming]] style. The goal is to allow programmers to use the best tool for a job, admitting that no one 
paradigm solves all problems in the easiest or most efficient way.\n\n*[[1C:Enterprise programming language]] (
generic, imperative, object-oriented, prototype-based, functional)\n*[[Ada (programming language)|Ada]] ([[Parallel 
computing|concurrent]], [[distributed computing|distributed]], [[Generic programming|generic]] ([[template 
metaprogramming]]), [[Imperative programming|imperative]], [[Object-oriented programming|object-oriented]] ([[Class (
computer science)|class-based]]))\n* [[Algebraic Logic Functional (programming language)|ALF]] ([[Functional 
programming|functional]], [[logic programming|logic]])\n* [[Alma-0]] (constraint, imperative, logic)\n* [[APL (
programming language)|APL]] (functional, imperative, object-oriented (class-based))\n* [[BETA (programming 
language)|BETA]] (functional, imperative, object-oriented (class-based))\n* [[C++]] (generic, imperative, 
object-oriented (class-based), functional, metaprogramming for large-scale, complex, high-performance)\n* [[C Sharp (
programming language)|C#]] (generic, imperative, object-oriented (class-based), functional, declarative)\n* [[Ceylon 
(programming language)|Ceylon]] (generic, imperative, object-oriented (class-based), functional, declarative)\n* [[
ChucK]] (imperative, object-oriented, time-based, concurrent, on-the-fly)\n* [[Cobra (programming language)|Cobra]] (
generic, imperative, object-oriented (class-based), functional, contractual)\n* [[Common Lisp]] (functional, 
imperative, object-oriented (class-based), [[Aspect-oriented programming|aspect-oriented]] (user may add further 
paradigms, e.g., logic))\n* [[Curl (programming language)|Curl]] (functional, imperative, object-oriented (
class-based), metaprogramming)\n* [[Curry (programming language)|Curry]] (concurrent, functional, logic)\n* [[D (
programming language)|D]] (generic, imperative, functional, object-oriented (class-based), metaprogramming)\n* [[
Delphi (software)|Delphi]] [[Object Pascal]] (generic, imperative, object-oriented (class-based), metaprogramming)\n* 
[[Dylan (programming language)|Dylan]] (functional, object-oriented (class-based))\n* [[eC (programming 
language)|eC]] (generic, imperative, object-oriented (class-based))\n* [[ECMAScript]] (functional, imperative, 
object-oriented (prototype-based))\n** [[ActionScript]]\n** [[ECMAScript for XML]]\n** [[JavaScript]]\n** [[
JScript]]\n* [[Eiffel (programming language)|Eiffel]] (imperative, object-oriented (class-based), generic, 
functional (agents), concurrent (SCOOP))\n* [[F Sharp (programming language)|F#]] (functional, generic, 
object-oriented (class-based), language-oriented)\n* [[Fantom (programming language)|Fantom]] (functional, 
object-oriented (class-based))\n* [[Go (programming language)|Go]] (imperative, procedural),\n* [[Groovy (programming 
language)|Groovy]] (functional, object-oriented (class-based),imperative,procedural)\n* [[Harbour (
software)|Harbour]]\n* [[Hop (software)|Hop]]\n* [[J (programming language)|J]] (functional, imperative, 
object-oriented (class-based))\n* [[Julia (programming language)|Julia]] (imperative, [[multiple dispatch]] (
\"object-oriented\"), functional, metaprogramming)\n* [[LabVIEW]] ([[Dataflow programming|dataflow]], 
[[Visual programming language|visual]])\n* [[Lava (programming language)|Lava]] (object-oriented (class-based), 
visual)\n* [[Lua (programming language)|Lua]] (functional, imperative, object-oriented ([[Prototype-based 
programming|prototype-based]]))\n* [[Mercury (programming language)|Mercury]] (functional, logical, 
object-oriented)\n* [[Metaobject|Metaobject protocols]] (object-oriented (class-based, prototype-based))\n* [[
Nemerle]] (functional, object-oriented (class-based), imperative, metaprogramming)\n* [[Objective-C]] (imperative, 
object-oriented (class-based), reflective)\n* [[OCaml]] (functional, imperative, object-oriented (class-based), 
modular)\n* [[Oz (programming language)|Oz]] (functional (evaluation: [[eager evaluation|eager]], 
[[lazy evaluation|lazy]]), logic, [[Constraint programming|constraint]], imperative, object-oriented (class-based), 
concurrent, distributed), and Mozart Programming System [[cross-platform]] Oz\n* [[Object Pascal]] (imperative, 
object-oriented (class-based))\n* [[Perl]] (imperative, functional (can't be purely functional), object-oriented, 
class-oriented, aspect-oriented (through modules))\n* [[PHP]] (imperative, object-oriented)\n* [[Pike (programming 
language)|Pike]]\n* [[Prograph]] (dataflow, object-oriented (class-based), visual)\n* [[Python (programming 
language)|Python]] (functional, compiled, interpreted, object-oriented (class-based), imperative, metaprogramming, 
extension, impure, interactive mode, iterative, reflective, scripting)\n* [[R (programming language)|R]] (array, 
interpreted, impure, interactive mode, list-based, object-oriented prototype-based, scripting)\n* [[Racket (
programming language)|Racket]] (functional, imperative, object-oriented (class-based) and can be extended by the 
user)\n* [[REBOL]] (functional, imperative, object-oriented (prototype-based), metaprogramming (dialected))\n* [[Red 
(programming language)|Red]] (functional, imperative, object-oriented (prototype-based), metaprogramming (
dialected))\n* [[ROOP (programming language)|ROOP]] (imperative, logic, object-oriented (class-based), rule-based)\n* 
[[Ruby (programming language)|Ruby]] (imperative, functional, object-oriented (class-based), metaprogramming)\n* [[
Rust (programming language)|Rust]] (concurrent, functional, imperative, object-oriented, generic, metaprogramming, 
compiled)\n* [[Scala (programming language)|Scala]] (functional, object-oriented)\n* [[Seed7]] (imperative, 
object-oriented, generic)\n* [[SISAL]] (concurrent, dataflow, functional)\n* [[Spreadsheet]]s (functional, 
visual)\n* [[Swift (programming language)|Swift]] (protocol-oriented, object-oriented, functional, imperative, 
block-structured)\n* [[Tcl]] (functional, imperative, object-oriented (class-based))\n** [[Tea (programming 
language)|Tea]] (functional, imperative, object-oriented (class-based))\n* [[Windows PowerShell]] (functional, 
imperative, pipeline, object-oriented (class-based))\n* [[Wolfram Language]]\n\n== Numerical analysis ==\n{{div 
col}}\n* [[AIMMS]]\n* [[AMPL (programming language)|AMPL]]\n* [[Analytica (software)|Analytica]]\n* [[GAUSS (
software)|GAUSS]]\n* [[General Algebraic Modeling System|GAMS]]\n* [[Julia (programming language)|Julia]]\n* [[
Klerer-May System]]\n* [[Mathematica]]\n* [[MATLAB]]\n* [[PROSE modeling language|PROSE]]\n* [[R (programming 
language)|R]]\n* [[Oberon (programming language)|Seneca]] \u2013 an [[Oberon (programming language)|Oberon]] 
variant\n* [[Wolfram Language]]\n{{div col end}}\n\n== Non-English-based languages ==\n{{Main|Non-English-based 
programming languages}}\n\n* [[Chinese BASIC]] \u2013 [[Chinese language|Chinese]]\n* [[Fj\u00f6lnir (programming 
language)|Fj\u00f6lnir]] \u2013 [[Icelandic language|Icelandic]]\n* [[LSE (programming language)|Language Symbolique 
d'Enseignement]] \u2013 [[French language|French]]\n* [[Lexico programming language|Lexico]] \u2013 [[Spanish 
language|Spanish]]\n* [[Rapira]] \u2013 [[Russian language|Russian]]\n* [[ezhil (programming language)|ezhil]]-[[
Tamil language|Tamil]]\n\n== Object-oriented class-based languages ==\nClass-based [[Object-oriented programming 
language]]s support objects defined by their class. Class definitions include member data. [[Message passing]] is a 
key concept (if not ''the'' key concept)  in Object-oriented languages.\n\nPolymorphic functions parameterized by the 
class of some of their arguments are typically called methods. In languages with [[single dispatch]], 
classes typically also include method definitions. In languages with [[multiple dispatch]], methods are defined by [[
generic function]]s. There are exceptions where [[single dispatch]] methods are [[generic function]]s (e.g. [[
Bigloo]]'s object system).\n\n=== [[Multiple dispatch]] ===\n{{div col|colwidth=10em}}\n* [[Common Lisp]]\n* [[Cecil 
(programming language)|Cecil]]\n* [[Dylan (programming language)|Dylan]]\n* [[Julia (programming 
language)|Julia]]\n\n{{div col end}}\n\n=== Single dispatch ===\n{{div col|colwidth=20em}}\n* [[
ActionScript|ActionScript 3.0]]\n* [[Actor (programming language)|Actor]]\n* [[Ada (programming language)|Ada 95]] 
and [[Ada (programming language)|Ada 2005]] (multi-purpose language)\n* [[APL (programming language)|APL]]\n* [[BETA 
(programming language)|BETA]]\n* [[C++]]\n* [[C Sharp (programming language)|C#]]\n* [[Ceylon (programming 
language)|Ceylon]]\n* [[Oxygene (programming language)|Oxygene]] (formerly named Chrome)\n* [[ChucK]]\n* [[Cobra (
programming language)|Cobra]]\n* [[ColdFusion]]\n* [[Curl (programming language)|Curl]]\n* [[D (programming 
language)|D]]\n* [[Distributed Application Specification Language]] (DASL)\n* [[Delphi]] [[Object Pascal]]\n* [[E (
programming language)|E]]\n* [[GNU E]]\n* [[eC (programming language)|eC]]\n* [[Eiffel (programming 
language)|Eiffel]]\n** [[Sather]]\n** [[Ubercode]]\n* [[F-Script (programming language)|F-Script]]\n* [[Fortran 
2003]]\n* [[Fortress (programming language)|Fortress]]\n* [[Gambas]]\n* [[GameMaker: Studio|Game Maker Language]]\n* 
[[Harbour (software)|Harbour]]\n* [[J (programming language)|J]]\n* [[Java (programming language)|Java]]\n** [[
Processing (programming language)|Processing]]\n** [[Groovy (programming language)|Groovy]]\n** [[Join Java]]\n** [[
Tea (programming language)|Tea]]\n** [[X10 (programming language)|X10]]\n* [[LabVIEW]]\n* [[Lava (programming 
language)|Lava]]\n* [[Lua (programming language)|Lua]]\n* [[Modula-2]] (data abstraction, information hiding, 
strong typing, full modularity)\n** [[Modula-3]] (added more object-oriented features to Modula-2)\n* [[Nemerle]]\n* 
[[NetRexx]]\n* [[Oberon-2 (programming language)|Oberon-2]] (full object-orientation equivalence in an original, 
strongly typed, Wirthian manner)\n* [[Object Pascal]]\n* [[Object REXX]]\n* [[Objective-C]] (a superset of C adding a 
[[Smalltalk]] derived object model and message passing syntax)\n* [[OCaml]]\n* [[Oz (programming language)|Oz, 
Mozart Programming System]]\n* [[Perl]] 5\n* [[PHP]]\n* [[Pike (programming language)|Pike]]\n* [[Prograph]]\n* [[
Python (programming language)|Python]] (interpretive language, optionally object-oriented)\n* [[Revolution (
programming language)|Revolution]] (programmer does not get to pick the objects)\n* [[Ruby (programming 
language)|Ruby]]\n* [[Scala (programming language)|Scala]]\n* [[Speakeasy (computational environment)|Speakeasy]]\n* 
[[Simula]] (first object-oriented language, developed by [[Ole-Johan Dahl]] and [[Kristen Nygaard]])\n* [[Smalltalk]] 
(pure object-orientation, developed at [[PARC (company)|Xerox PARC]])\n** [[F-Script (programming 
language)|F-Script]]\n** [[Little Smalltalk]]\n** [[Pharo]]\n** [[Squeak]]\n*** [[Scratch (programming 
language)|Scratch]]\n** [[IBM VisualAge]]\n** [[VisualWorks]]\n* [[Parallax Propeller|SPIN]]\n* [[SuperCollider]]\n* 
[[VBScript]] (Microsoft Office 'macro scripting' language)\n* [[Visual DataFlex]]\n* [[Visual FoxPro]]\n* [[Visual 
Prolog]]\n* [[Microsoft Dynamics AX|X++]]\n* [[Xojo]]\n* [[XOTcl]]\n{{div col end}}\n\n== Object-oriented 
prototype-based languages ==\n[[Prototype-based programming|Prototype-based languages]] are object-oriented languages 
where the distinction between classes and instances has been removed:\n\n{{div col|colwidth=20em}}\n* [[1C:Enterprise 
programming language]]\n* [[Actor-Based Concurrent Language]] (ABCL, ABCL/1, ABCL/R, ABCL/R2, ABCL/c+)\n* [[Agora (
programming language)|Agora]]\n* [[Cecil (programming language)|Cecil]]\n* [[ECMAScript]]\n** [[ActionScript]]\n** [[
ECMAScript for XML]]\n** [[JavaScript]] (first named Mocha, then LiveScript)\n** [[JScript]]\n* [[Etoys (programming 
language)|Etoys]] in [[Squeak]]\n* [[Io (programming language)|Io]]\n* [[Lua (programming language)|Lua]]\n* [[MOO (
programming language)|MOO]]\n* [[NewtonScript]]\n* [[Obliq]]\n* [[R (programming language)|R]]\n* [[REBOL]]\n* [[Red 
(programming language)|Red]]\n* [[Self (programming language)|Self]] (first prototype-based language, derived from [[
Smalltalk]])\n* [[TADS]]\n{{div col end}}\n\n== Off-side rule languages ==\n{{Main|Off-side rule#Off-side rule 
languages}}\n\n[[Off-side rule]] languages denote blocks of code by their [[indentation style|indentation]].\n\n{{div 
col|colwidth=20em}}\n* [[ISWIM]], the abstract language that introduced the rule\n* [[ABC (programming 
language)|ABC]], Python's parent\n** [[Python (programming language)|Python]]\n*** [[Cobra (programming 
language)|Cobra]]\n*** [[Boo (programming language)|Boo]]\n*** [[Genie (programming language)|Genie]]\n* [[Miranda (
programming language)|Miranda]], Haskell's parent\n** [[Orwell (programming language)|Orwell]]\n** [[Haskell (
programming language)|Haskell]]\n*** [[Curry (programming language)|Curry]]\n* [[Elixir (programming 
language)|Elixir]] (, do: blocks)\n* [[F Sharp (programming language)|F#]]\n* [[Nim (programming language)|Nim]]\n* [
[Occam (programming language)|Occam]]\n* [[Parallax Propeller|SPIN]]\n{{div col end}}\n\n== Procedural languages 
==\n[[Procedural programming]] languages are based on the concept of the unit and scope (the data viewing range) of 
an executable code statement. A procedural program is composed of one or more units or modules, either user coded or 
provided in a code library; each module is composed of one or more procedures, also called a function, routine, 
subroutine, or method, depending on the language. Examples of procedural languages include:\n\n{{div 
col|colwidth=15em}}\n* [[Ada (programming language)|Ada]] (multi-purpose language)\n* [[ALGOL]] (very influential 
language design; the second high level language compiler)\n** [[SMALL]] Machine ALGOL Like Language\n* [[Alma-0]]\n* 
[[BASIC]] (these lack most modularity in (especially) versions before about 1990)\n* [[BCPL]]\n* [[BLISS]]\n* [[C (
programming language)|C]]\n* [[C++]] (C with objects plus much else, such as, generics through STL)\n* [[C Sharp (
programming language)|C#]] (similar to Java/C++)\n* [[Ceylon (programming language)|Ceylon]]\n* [[CHILL]]\n* [[
ChucK]] (C/Java-like syntax, with new syntax elements for time and parallelism)\n* [[COBOL]]\n* [[Cobra (programming 
language)|Cobra]]\n* [[ColdFusion]]\n* [[Combined Programming Language]] (CPL)\n* [[Curl (programming 
language)|Curl]]\n* [[D (programming language)|D]]\n* [[Distributed Application Specification Language]] (DASL) (
combine [[declarative programming]] and [[imperative programming]])\n* [[eC (programming language)|eC]]\n* [[
ECMAScript]]\n** [[ActionScript]]\n** [[ECMAScript for XML]]\n** [[JavaScript]] (first named Mocha, 
then LiveScript)\n** [[JScript]]\n** [[Source (programming language)|Source]]\n* [[Eiffel (programming 
language)|Eiffel]]\n* [[Fortran]] (better modularity in later Standards)\n** [[F (programming language)|F]]\n* [[
GAUSS (software)|GAUSS]]\n* [[Go (programming language)|Go]]\n* [[Harbour (software)|Harbour]]\n* [[HyperTalk]]\n* [[
Java (programming language)|Java]]\n** [[Groovy (programming language)|Groovy]]\n** [[Join Java]]\n** [[Tea (
programming language)|Tea]]\n* [[JOVIAL]]\n* [[Julia (programming language)|Julia]]\n* [[Lasso (programming 
language)|Lasso]]\n* [[Modula-2]] (fundamentally based on modules)\n* [[Mathematica]]\n* [[MATLAB]]\n* [[Mesa]]\n* [[
MUMPS]] (first release was more modular than other languages of the time; the standard has become even more modular 
since then)\n* [[Nemerle]]\n* [[Nim (programming language)|Nim]]\n* [[Oberon (programming language)|Oberon]], 
[[Oberon-2]] (improved, smaller, faster, safer follow-ons for Modula-2)\n** [[Component Pascal]]\n** [[Oberon-2 (
programming language)|Seneca]]\n* [[OCaml]]\n* [[Occam (programming language)|Occam]]\n* [[Oriel (scripting 
language)|Oriel]]\n* [[Pascal (programming language)|Pascal]] (successor to ALGOL 60, predecessor of Modula-2)\n** [[
Free Pascal]] (FPC)\n** [[Object Pascal]], [[Delphi (software)|Delphi]]\n* [[PCASTL]]\n* [[Perl]]\n* [[Pike (
programming language)|Pike]]\n* [[PL/C]]\n* [[PL/I]] (large general purpose language, originally for IBM 
mainframes)\n* [[Plus (programming language)|Plus]]\n* [[PowerShell]]\n* [[PROSE modeling language|PROSE]]\n* [[
Python (programming language)|Python]]\n* [[R (programming language)|R]]\n* [[Rapira]]\n* [[IBM RPG|RPG]] (available 
only in [[IBM]]'s [[IBM System i|System i]] midrange computers)\n* [[Rust (programming language)|Rust]]\n* [[
S-Lang]]\n* [[VBScript]]\n* [[Visual Basic]]\n* [[Visual FoxPro]]\n* [[Wolfram Language]]\n* [[Microsoft Dynamics 
AX]] (X++)\n{{div col end}}\n\n== Query languages ==\n{{Main|Query language}}\n\n== Reflective Language ==\n[[
Reflection (computer science)|Reflective]] languages let programs examine and possibly modify their high level 
structure at runtime or compile-time. This is most common in high-level virtual machine programming languages like [[
Smalltalk]], and less common in lower-level programming languages like [[C (programming language)|C]]. Languages and 
platforms supporting reflection:\n\n{{See also|Aspect-oriented programming}}\n\n{{div col|colwidth=20em}}\n* [[
Befunge]]\n* [[Ceylon (programming language)|Ceylon]]\n* [[Charm (language)|Charm]]\n* [[ChucK]]\n* [[List of CLI 
languages|CLI]]\n** [[C Sharp (programming language)|C#]]\n* [[Cobra (programming language)|Cobra]]\n* [[Component 
Pascal]] [[BlackBox Component Builder]]\n* [[Curl (programming language)|Curl]]\n* [[Cypher (query 
language)|Cypher]]\n* [[Delphi (software)|Delphi]] [[Object Pascal]]\n* [[eC (programming language)|eC]]\n* [[
ECMAScript]]\n** [[ActionScript]]\n** [[ECMAScript for XML]]\n** [[JavaScript]]\n** [[JScript]]\n* [[Emacs Lisp]]\n* 
[[Eiffel (programming language)|Eiffel]]\n* [[Forth (programming language)|Forth]]\n* [[Harbour (
software)|Harbour]]\n* [[Julia (programming language)|Julia]]\n* [[List of JVM languages|JVM]]\n** [[Java (
programming language)|Java]]\n** [[Groovy (programming language)|Groovy]]\n** [[Join Java]]\n** [[X10 (programming 
language)|X10]]\n* [[Lisp (programming language)|Lisp]]\n** [[Clojure]]\n** [[Common Lisp]]\n** [[Dylan (programming 
language)|Dylan]]\n** [[Logo (programming language)|Logo]]\n** [[Scheme (programming language)|Scheme]]\n* [[Lua (
programming language)|Lua]]\n* [[Maude system]]\n* [[Oberon-2 (programming language)|Oberon-2]] \u2013 ETH Oberon 
System\n* [[Objective-C]]\n* [[PCASTL]]\n* [[Perl]]\n* [[PHP]]\n* [[Pico (programming language)|Pico]]\n* [[
Poplog]]\n** [[POP-11]]\n* [[PowerShell]]\n* [[Prolog]]\n* [[Python (programming language)|Python]]\n* [[REBOL]]\n* [
[Red (programming language)|Red]]\n* [[Ruby (programming language)|Ruby]]\n* [[Smalltalk]] (pure object-orientation, 
originally from [[PARC (company)|Xerox PARC]])\n** [[F-Script (programming language)|F-Script]]\n** [[Little 
Smalltalk]]\n** [[Self (programming language)|Self]]\n** [[Squeak]]\n** [[IBM VisualAge]]\n** [[VisualWorks]]\n* [[
SNOBOL|Snobol]]\n* [[Tcl]]\n* [[Wolfram Language]]\n* [[XOTcl]]\n* [[Microsoft Dynamics AX|X++]]\n* [[Xojo]]\n{{div 
col end}}\n\n== Rule-based languages ==\nRule-based languages instantiate rules when activated by conditions in a set 
of data. Of all possible activations, some set is selected and the statements belonging to those rules execute. 
Rule-based languages include:{{citation needed|date=March 2015}}\n\n{{div col|colwidth=20em}}\n* [[awk]]\n* [[
CLIPS]]\n* [[Constraint Handling Rules]]\n* [[Drools]]\n* [[GOAL agent programming language]]\n* [[Jess (programming 
language)|Jess]]\n* [[OPS5]]\n* [[Prolog]]\n* [[ToonTalk]] \u2013 robots are rules\n* [[Mathematica]]\n* {{citation 
span|text=[[XSLT]]|date=August 2015}}\n* [[Wolfram Language]]\n{{div col end}}\n\n== Scripting languages ==\n\"[[
Scripting language]]\" has two apparently different, but in fact similar, meanings. In a traditional sense, 
scripting languages are designed to automate frequently used tasks that usually involve calling or passing commands 
to external programs. Many complex application programs provide built-in languages that let users automate tasks. 
Those that are [[interpreter (computing)|interpretive]] are often called scripting languages.\n\nRecently, 
many applications have built-in traditional scripting languages, such as [[Perl]] or [[Visual Basic]], but there are 
quite a few ''native'' scripting languages still in use. Many scripting languages are compiled to bytecode and then 
this (usually) platform-independent bytecode is run through a virtual machine (compare to [[Java virtual 
machine]]).\n\n{{div col|colwidth=20em}}\n* [[AppleScript]]\n* [[AutoHotKey]]\n* [[AutoIt]]\n* [[AWK]]\n* [[bc (
programming language)|bc]]\n* [[BeanShell]]\n* [[Bash (Unix shell)|Bash]]\n* [[Ch (computer programming)|Ch]] (
Embeddable C/C++ interpreter)\n* [[List of CLI languages|CLI]]\n** [[C Sharp (programming language)|C#]] (compiled to 
bytecode, and running [[Just-in-time compilation|JIT]] inside VM)\n* [[CLIST]]\n* [[ColdFusion]]\n* [[
ECMAScript]]\n** [[ActionScript]]\n** [[ECMAScript for XML]]\n** [[JavaScript]] (first named Mocha, 
then LiveScript)\n** [[JScript]]\n** [[Source (programming language)|Source]]\n* [[Emacs Lisp]]\n* [[CMS EXEC]]\n* [[
EXEC 2]]\n* [[F-Script (programming language)|F-Script]]\n* [[GameMaker: Studio|Game Maker Language]] (GML)\n* [[ICI 
(programming language)|ICI]]\n* [[Io (programming language)|Io]]\n* [[JASS]]\n* [[Julia (programming 
language)|Julia]] (still, compiled on the fly to [[machine code]])\n* [[List of JVM languages|JVM]]\n** [[Groovy (
programming language)|Groovy]]\n** [[Join Java]]\n* [[KornShell|Ksh]]\n* [[Lasso (programming language)|Lasso]]\n* [[
Lua (programming language)|Lua]]\n* [[MAXScript]]\n* [[Maya Embedded Language|MEL]]\n* [[Object REXX]] (OREXX, 
OOREXX)\n* [[Oriel (scripting language)|Oriel]]\n* [[Pascal Script]]\n* [[Perl]]\n* [[PHP]] (intended for Web 
servers)\n* [[PowerShell]]\n* [[Python (programming language)|Python]]\n* [[R (programming language)|R]]\n* [[
REBOL]]\n* [[Red (programming language)|Red]]\n* [[Rexx]]\n* [[Revolution (programming language)|Revolution]]\n* [[
Ruby (programming language)|Ruby]]\n* [[Bourne shell|Sh]]\n* [[Smalltalk]]\n* [[S-Lang]]\n* [[sed]]\n* [[Tea (
programming language)|Tea]]\n* [[Tcl]]\n* [[TorqueScript (programming language)|TorqueScript]]\n* [[VBScript]]\n* [[
WebDNA]], dedicated to database-driven websites\n* [[Windows PowerShell]] ([[.NET Framework|.NET]]-based CLI)\n* [[
Winbatch]]\n* Many shell command languages such as [[Unix shell]] or [[DIGITAL Command Language]] (DCL) on VMS have 
powerful scripting abilities.\n{{div col end}}\n\n== Stack-based languages ==\n{{Main category|Stack-oriented 
programming languages}}\n\nStack-based languages are a type of [[data-structured language]] that are based on the [[
Stack (abstract data type)|stack]] data structure.\n\n{{div col|colwidth=20em}}\n* [[Beatnik (programming 
language)|Beatnik]]\n* Canonware Onyx<ref>{{cite web |title=Canonware Onyx 
|url=http://www.canonware.com/onyx/index.html |work=[[Canonware.com]] 
|archive-url=https://web.archive.org/web/20170313205049/http://www.canonware.com/onyx/index.html |archive-date=March 
13, 2017 |access-date=July 7, 2018}}</ref>\n* [[colorForth]]\n* [[Factor (programming language)|Factor]]\n* [[Forth (
programming language)|Forth]]\n* [[Joy (programming language)|Joy]] (all functions work on parameter stacks instead 
of named parameters)\n* [[Piet (programming language)|Piet]]\n* [[Poplog]] via its implementation language [[
POP-11]]\n* [[PostScript]]\n* [[RPL (programming language)|RPL]]\n* [[S-Lang]]\n{{div col end}}\n\n== Synchronous 
languages ==\n{{Main category|Synchronous programming languages}}\n\n[[Synchronous programming language]]s are 
optimized for programming reactive systems, systems that are often interrupted and must respond quickly. Many such 
systems are also called [[Real-time computing|realtime systems]], and are used often in [[embedded 
system]]s.\n\nExamples:\n* [[Argus (programming language)|Argus]]\n* [[Averest]]\n* [[Esterel]]\n* [[Lustre (
programming language)|Lustre]]\n* [[SIGNAL (programming language)|Signal]]\n\n== Shading languages ==\n{{See also 
category|Category:Shading languages}}\n\nA [[shading language]] is a graphics programming language adapted to 
programming shader effects. Such language forms usually consist of special data types, like \"color\" and \"normal\". 
Due to the variety of target markets for 3D computer graphics.\n\n=== Real-time rendering ===\nThey provide both 
higher hardware abstraction and a more flexible programming model than previous paradigms which hardcoded 
transformation and shading equations. This gives the programmer greater control over the rendering process and 
delivers richer content at lower overhead.\n{{div col}}\n* Adobe Graphics Assembly Language (AGAL)<ref>{{cite 
web|last1=Scabia|first1=Marco|title=What is AGAL 
|url=https://www.adobe.com/devnet/flashplayer/articles/what-is-agal.html|website=Adobe Developer 
Connection|publisher=Adobe|access-date=8 May 2018|language=en}}</ref>\n* [[ARB assembly language]] (ARB assembly)\n* 
[[OpenGL Shading Language]] (GLSL or glslang)\n* [[High-Level Shading Language]] (HLSL) or DirectX Shader Assembly 
Language\n* [[PlayStation Shader Language]] (PSSL)\n* [[Metal (API)|Metal Shading Language]]\n* [[Cg programming 
language|Cg]]\n* Shining Rock Shading Language (SRSL)<ref>{{cite web|last=Hodorowicz|first=Luke|title=Shading 
Languages|url=http://www.shiningrocksoftware.com/2015-03-30-shading-languages/|website=www.shiningrocksoftware.com
|publisher=Shining Rock Software|access-date=8 May 2018}}</ref>\n* Spark<ref>{{cite 
web|last=Foley|first=Tim|last2=Hanrahan|first2=Pat|title=Spark: Modular, Composable Shaders for Graphics Hardware 
|url=https://software.intel.com/en-us/articles/spark-modular-composable-shaders-for-graphics-hardware|website=Intel 
Software|publisher=ACM|access-date=8 May 2018|language=en}}</ref>\n* Nitrous Shading Language<ref>{{cite 
web|title=Nitrous FAQ|url=http://oxidegames.com/products/nitrous-2/|website=oxidegames.com|access-date=8 May 
2018}}</ref>\n* Godot Shading Language<ref>{{cite 
web|last=Linietsky|first=Juan|last2=Manzur|first2=Ariel|title=Shading language \u2013 Godot Engine latest 
documentation|url=http://docs.godotengine.org/en/3.0/tutorials/shading/shading_language.html|website=docs.godotengine
.org|publisher=Godot community|access-date=8 May 2018|language=en}}</ref>\n{{div col end}}\n\n=== Offline rendering 
===\nShading languages used in offline rendering produce maximum image quality. Processing such shaders is 
time-consuming. The computational power required can be expensive because of their ability to produce photorealistic 
results.\n{{div col}}\n* [[RenderMan Shading Language]] (RSL)\n* Houdini VEX Shading Language (VEX)\n* [[Gelato (
software)|Gelato Shading Language]]\n* [[Open Shading Language]] (OSL)\n{{div col end}}\n\n== Syntax handling 
languages ==\nThese languages assist with generating [[Lexical analysis|lexical analyzers]] and [[parsing|parsers]] 
for [[context-free grammar]]s.\n\n* [[ANTLR]]\n* [[Coco/R]] (EBNF with semantics)\n* [[GNU bison]] (FSF's version of 
Yacc)\n* GNU [[Flex (lexical analyser generator)|Flex]] (FSF version of Lex)\n* glex/gyacc (GoboSoft compiler 
compiler to Eiffel)\n* [[lex (software)|lex]] (Lexical Analysis, from Bell Labs)\n* [[M4 (computer language)|M4]]\n* 
[[Parsing expression grammar]] (PEG)\n* [[Prolog]]\n* [[Emacs Lisp]]\n* [[Lisp (programming language)|Lisp]]\n* [[
Scheme (programming language)|Scheme]]\n* [[yacc]] (yet another compiler compiler, from Bell Labs)\n* [[
JavaCC]]\n\n== System languages ==\nThe '''system programming languages''' are for low level tasks like memory 
management or task management. A system programming language usually refers to a programming language used for system 
programming; such languages are designed for writing system software, which usually requires different development 
approaches when compared with application software.\n\nSystem software is computer software designed to operate and 
control the computer hardware, and to provide a platform for running application software. System software includes 
software categories such as operating systems, utility software, device drivers, compilers, and linkers. Examples of 
system languages include:\n\n{| class=\"wikitable sortable collapsible\"\n|-\n! Language !! Originator !! First 
appeared !! Influenced by !! Used for\n|-\n| [[Executive Systems Problem Oriented Language|ESPOL]] || [[Burroughs 
Corporation]] || 1961 || [[ALGOL 60]] || [[Burroughs MCP|MCP]]\n|-\n| [[PL/I]] || [[IBM]], 
[[SHARE (computing)|SHARE]] || 1964 || ALGOL, FORTRAN, some COBOL || [[Multics]]\n|-\n| [[PL360]] || [[Niklaus 
Wirth]] || 1968 || ALGOL 60 || [[ALGOL W]]\n|-\n| [[C (programming language)|C]] || [[Dennis Ritchie]] || 1969 || [[
BCPL]] || Most [[Kernel (operating system)|operating system kernels]], including [[Windows NT]] and most [[
Unix-like]] systems\n|-\n| [[PL/S]] || [[IBM]] || 196x || [[PL/I]] || [[OS/360]]\n|-\n| [[BLISS]] || [[Carnegie 
Mellon University]] || 1970 || ALGOL-PL/I<ref>{{cite journal|last=Wulf|first=W.A. |author2=Russell, 
D.B. |author3=Haberman, A.N.|title=BLISS: A Language for Systems Programming|journal=Communications of the 
ACM|date=December 1971|volume=14|issue=12|pages=780\u2013790|doi=10.1145/362919.362936 
|citeseerx=10.1.1.691.9765}}</ref> || [[OpenVMS|VMS]] (portions)\n|-\n| [[PL/I#Special purpose and system PL/I 
compilers|PL/8]] || [[IBM]] || 197x || [[PL/I]] || [[IBM AIX|AIX]]\n|-\n| [[PL-6]] || [[Honeywell, Inc.]] || 197x || 
[[PL/I]] || [[Honeywell CP-6|CP-6]]\n|-\n| [[SYMPL]] || [[Control Data Corporation|CDC]] || 197x || [[JOVIAL]] || [[
NOS (software)|NOS]] subsystems, most compilers, FSE editor\n|-\n| [[C++]] || [[Bjarne Stroustrup]] || 1979 || [[C (
programming language)|C]], [[Simula]] || See C++ Applications<ref>{{cite 
web|url=http://www.stroustrup.com/applications.html|title=C++ Applications}}</ref>\n|-\n| [[Ada (programming 
language)|Ada]] || [[Jean Ichbiah]], [[S. Tucker Taft]] || 1983 || [[ALGOL 68]], [[Pascal (programming 
language)|Pascal]], [[C++]], [[Java (programming language)|Java]], [[Eiffel (programming language)|Eiffel]] || 
Embedded systems, OS kernels, compilers, games, simulations, [[CubeSat]], air traffic control, and avionics\n|-\n| [[
D (programming language)|D]] || [[Digital Mars]] || 2001 || [[C++]] || Multiple domains<ref>[
https://dlang.org/orgs-using-d.html]</ref>\n|-\n| [[Nim (programming language)|Nim]] || Andreas Rumpf || 2008 || [[
Ada (programming language)|Ada]], [[Modula-3]], [[Lisp (programming language)|Lisp]], [[C++]], [[Object Pascal]], 
[[Python (programming language)|Python]], [[Oberon (programming language)|Oberon]] || OS kernels, compilers, 
games\n|-\n| [[Rust (programming language)|Rust]] || [[Mozilla Research]]<ref>{{cite web 
|url=https://www.mozilla.org/en-US/research/ |title=Mozilla Research |date=1 January 2014}}</ref> || 2010 || [[C++]], 
[[Haskell (programming language)|Haskell]], [[Erlang (programming language)|Erlang]], [[Ruby (programming 
language)|Ruby]] || [[Servo layout engine]], [[Redox OS]]\n|-\n| [[Swift (programming language)|Swift]] || [[Apple 
Inc.]] || 2014 || [[C (programming language)|C]], [[Objective-C]], [[Rust (programming language)|Rust]] || [[macOS]], 
[[iOS]] app development {{efn|Swift uses [[Automatic Reference Counting|automatic reference counting]].}}\n|}\n\n== 
Transformation languages ==\n{{Main|Transformation language}}\n\n== Visual languages ==\n{{Main category|Visual 
programming languages}}\n\n[[Visual programming language]]s let users specify programs in a two-(or more)-dimensional 
way, instead of as one-dimensional text strings, via graphic layouts of various types. Some [[dataflow programming]] 
languages are also visual languages.\n\n{{div col}}\n* [[Analytica (software)|Analytica]]\n* [[Blockly]]\n* [[
DRAKON]]\n* [[Fabrik (software)|Fabrik]]\n* G (used in [[LabVIEW]])\n* [[Lava (programming language)|Lava]]\n* [[
Limnor]]\n* [[Max (software)|Max]]\n* [[NXT-G]]\n* [[Pict (programming language)|Pict programming language]]\n* [[
Prograph]]\n* [[Pure Data]]\n* [[Quartz Composer]]\n* [[Scratch (programming language)|Scratch]] (written in and 
based on [[Squeak]], a version of [[Smalltalk]])\n* [[Snap! (programming language)|Snap!]]\n* [[Simulink]]\n* [[
Spreadsheet]]s\n* [[Stateflow]]\n* [[Subtext (programming language)|Subtext]]\n* [[ToonTalk]]\n* [[Agilent 
VEE|VEE]]\n* [[VisSim]]\n* [[Vvvv]]\n* [[XOD (programming language)]]\n* [[EICASLAB]]\n{{div col end}}\n\n== Wirth 
languages ==\nComputer scientist [[Niklaus Wirth]] designed and implemented several influential languages.\n\n{{div 
col}}\n* [[ALGOL W]]\n* [[Euler (programming language)|Euler]]\n* [[Modula]]\n** [[Modula-2]], [[Modula-3]], 
variants\n*** [[Obliq]] Modula 3 variant\n* [[Oberon (programming language)|Oberon]] (Oberon, Oberon-07, 
Oberon-2)\n** [[Component Pascal]]\n** [[Oberon-2 (programming language)|Oberon-2]]\n* [[Pascal (programming 
language)|Pascal]]\n** [[Object Pascal]] (umbrella name for [[Delphi (software)|Delphi]], [[Free Pascal]], 
[[Oxygene (programming language)|Oxygene]], others)\n{{div col end}}\n\n== XML-based languages ==\nThese are 
languages based on or that operate on [[XML]].<!--Not sure I understand this, I believe all three databases have XML 
support: \"Although the big-boy equivalents of Oracle/PostgreSQL/MSSQL don't yet exist for XML, there are languages 
to navigate through it and its more tree-oriented structure.\"-->\n\n{{div col}}\n* [[Apache Ant|Ant]]\n* [[
C\u03c9]]\n* [[ECMAScript for XML]]\n* [[MXML]]\n* [[OpenLaszlo|LZX]]\n* [[XAML]]\n* [[XPath]]\n* [[XQuery]]\n* [[
XProc]]\n* eXtensible Stylesheet Language Transformations ([[XSLT]])\n{{div col end}}\n\n== See also ==\n* [[
Programming paradigm]]\n* [[IEC 61131-3]] \u2013 a standard for [[programmable logic controller]] (PLC) languages\n* 
[[Educational programming language]]\n* [[Esoteric programming language]]\n\n== Notes ==\n{{Notelist}}\n\n== 
References ==\n{{Reflist}}\n\n{{DEFAULTSORT:List Of Programming Languages By Category}}\n[[Category:Lists of 
programming languages| ]]\n[[Category:Array programming languages]]"}]}}}} """
j = json.loads(s, strict=False)


def find_value_for_key(key, d):
    """ returns a value for 'key' in a dict 'd' """
    if type(d) == type([]):
        for x in d:
            return find_value_for_key(key, x)
    for k, v in d.items():
        if k == key:
            return v
        if type(v) == type({}) or type(v) == type([]):
            return find_value_for_key(key, v)


def parse_category(s):
    """ == Wirth languages == """
    return s.strip("= ")


def parse_lang(s):
    """
    * [[Pascal (programming language)|Pascal]]
    * [[XPath]]
    * [http://xmlmosaic.codeplex.com XMLmosaic]
    * [http://www.ozonehouse.com/mark/codeworks.html Glyphic Script]
    * Nemerle (compiled into Intermediate Language bytecode)
    * Sculptor
    """
    if "[[" in s:
        ss = s[s.find("[[") + 2: s.find("]]")].split("|")
        #        return s
        return ss[1] if len(ss) > 1 else ss[0]
    elif "[" in s:
        ss = s[s.find("[") + 1: s.find("]")].split()
        return " ".join(ss[1:])
    elif "(" in s:
        return s[:s.find("(")].strip("* ")

    return s.strip("* ")


def parse(s):
    langs = defaultdict(list)
    category = "?"

    for line in s.splitlines():
        if line.startswith("== See also"):
            break
        elif line.startswith("=="):
            category = parse_category(line)
        elif line.startswith("*"):
            langs[parse_lang(line)].append(category)

    return langs


def format_textile(d):
    cats = {}
    for k in d.keys():
        for c in d[k]:
            cats[c] = 1
    print("'\n,'".join(list(cats.keys())))
    with open("langs.json", "w") as f:
        d["Shell"] = ["Interpreted languages"]
        d["Assembly"] = ["Interpreted languages"]
        d["TeX"] = ["Interpreted languages"]
        d["Makefile"] = ["Interpreted languages"]
        d["Objective-C++"] = ["Compiled languages"]
        d["Pony"] = ["Compiled languages"]
        d["CMake"] = ["Interpreted languages"]
        d["TSQL"] = ["Interpreted languages"]
        d["WebAssembly"] = ["Compiled languages"]
        d["Reason"] = ["Compiled languages"]
        d["Batchfile"] = ["Interpreted languages"]
        d["Puppet"] = ["Interpreted languages"]
        d["Cuda"] = ["Compiled languages"]
        d["Hack"] = ["Garbage collected languages", "Object-oriented", "", "Single dispatch",
                     "Imperative languages"]
        d["HTML"] = ["Client side"]
        d["CSS"] = ["Client side"]
        d["Jupyter Notebook"] = []
        d["CoffeeScript"] = []
        d["Vue"] = ["Framework"]
        d["Dockerfile"] = []
        d["Roff"] = []
        d["Smarty"] = []
        d["Haxe"] = []
        d["HCL"] = []
        d["PLpgSQL"] = []
        d["Starlark"] = []
        d["MoonScript"] = []
        d["Gherkin"] = []
        d["1C Enterprise"] = []
        d["SaltStack"] = []
        d["V"] = []
        d["Nix"] = []
        d["Rich Text Format"] = []
        d["PureBasic"] = []
        d["LiveScript"] = []
        d["YARA"] = []
        d["Stan"] = []
        d["NSIS"] = []
        d["F*"] = []
        d["Ring"] = []
        d["Objective-J"] = []
        d["Jsonnet"] = []
        d["PicoLisp"] = []
        d["Solidity"] = []
        d["Eagle"] = []
        d["GDScript"] = []
        d["SWIG"] = []
        d["SQF"] = []
        d["Isabelle"] = []
        d["Apex"] = []
        d["GLSL"] = []
        d["MQL5"] = []
        json.dump(dict([(k.lower(), d[k]) for k in d.keys() if k != " "]), f)


if __name__ == '__main__':
    print(len(j))
    format_textile(parse(find_value_for_key("*", j["query"]["pages"]["144144"]['revisions'][0])))
