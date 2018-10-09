# A Brief History of Computer Science

You may have never heard the names Blaise Pascal, Ada Lovelace, Charles Babbage, Alan Turing, or John von Neumann, but you wouldn't be programming today if it weren't for the foundational work they did in computer science, mathematics, and computational theory. Today we'll discuss early analogue computing, development of digital computers, and up to the beginnings of higher-level programming languages and the internet.

### Before we start...

Let's define a few words so we're all on the same page about what they mean

| Word | Definition in this Context |
| ---------------- | ------------------------------------------------------ |
| Mechanical | relating to physical forces or motion; physical. |
| Analogue | relating to or using signals or information represented by a continuously variable physical quantity such as spatial position or voltage. |
| Compute | To calculate or evaluate |
| Turing-Complete | Computationally universal - can model/solve any problem |

### What is a computer?

The word `computer` originally referred to the *person* who was doing the computing. More specifically to frame the history of computing, what we'll start out discussing is the history of machine-assisted human computation.

## Antiquity

### The Abacus

![](https://res.cloudinary.com/briezh/image/upload/v1539028604/abacus_nv0wmx.jpg)

Yes, the first computing tool was an abacus - an early, manual calculator. To the best of anyone's knowledge, it was invented by the ancient Sumerians between 2700 and 2300 BC.

Notice an abacus, like other early computing devices were mechanical (meaning dictated by physical forces), not electrical. The ideas of computing and algorithms are rooted in mathematics.

### The Antikythera Mechanism

![](https://res.cloudinary.com/briezh/image/upload/v1539028604/Antikythera_mechanism_vgzsyu.jpg)

The Antikythera Mechanism is thought to be the first **analog computer**, and was developed in ancient Greece around the first or second century BC. It is so named because it was discovered in a shipwreck off the coast of the Greek island Antikythera in 1901. 

Antikythera is northwest of Crete. Here is a map of the area:

![](https://res.cloudinary.com/briezh/image/upload/v1539027855/map_antikythera_qyyz3e.jpg)

It was used for various astronomical calculations such as predicting eclipses and irregularities in the moon's orbit, and for tracking all then-known heavenly bodies. The importance and sophistication of this artifact was overlooked until 2006 because it was originally thought to be far too advanced for the time period. In fact, it precedes any other known clockwork mechanisms of similar complexity by more than a milennia. 

[According to Wikipedia](https://en.wikipedia.org/wiki/Antikythera_mechanism), "The quality and complexity of the mechanism's manufacture suggests that it has undiscovered predecessors made during the Hellenistic period". The Hellenistic period is the time period between the death of Alexander the Great and the emergence of the Roman Empire.

### Other Early Advancements

Roughly contemporary with the Antikythera mechanism, an Indian mathematician named [Pingala](https://en.wikipedia.org/wiki/Pingala), is credited with the first use of a binary number system. It used long and short dashes and was similar to Morse code.

## Middle Ages

During this time period, advancements in mathematics and further understanding of things like binary numbers and floating point numbers set the stage for future developments. Mechanical clocks and geared mechanisms became more advanced. The first true computers were based on clocks and calculators.

## Early and Mid-Modern Era

### Pascal's Calculators

In 1642, while still a teenager helping his father with tax collection duties in France, [Blaise Pascal](https://en.wikipedia.org/wiki/Blaise_Pascal) invented a mechanical calculator. These were later known as Pascal's Calculators or Pascalines. While other attempts had been made, this was the first fully functional and properly working version.

![](https://upload.wikimedia.org/wikipedia/commons/6/68/17th-century-mechanical-calculators_-Detail.jpg)

The programming language [Pascal](https://en.wikipedia.org/wiki/Pascal_(programming_language)) is named in honor of Blaise Pascal.

### Babbage's Analytical Engine

Charles Babbage designed a new kinds of mechanical calculator - his [analytical engine](https://en.wikipedia.org/wiki/Analytical_Engine). This went beyond his original design of a differential engine (basically an advanced mathematical calculator), and provided the first idea of a programmable computer. It's the first design for a computer that could be considered [Turing-Complete](https://en.wikipedia.org/wiki/Turing_completeness) in the modern sense of how we think of computers, although when Babbage was designing his analytical engine, Alan Turing was not even born yet.

Babbage's analytical engine's design was ground-breaking. No one, up until that point had designed any machines that were this general in usage. The analytical engine was not built in Babbage's lifetime, but later models suggest his machine would have worked. 

#### Details

![](https://res.cloudinary.com/briezh/image/upload/v1539124205/Charles_Babbage_uv2dmm.jpg)

Babbage's analytical engine took input of 'formulae' and 'data' - which were to be fed into the machine via punchcards - similar to mechanical looms of that time period. There was to be a 'store' which had room for 1000 40-digit numbers (or about 16kB). The internal operations supported included basic mathematical operators, comparison operators, and square roots. Loops and conditionals were also possible. The language used would be similar to modern-day assembly languages.

![](https://res.cloudinary.com/briezh/image/upload/v1539124205/AdaLovelace_kf1tuk.jpg)

[Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace) corresponded with Babbage during his development of the analytical engine, and developed a working relationship and friendship with him. She wrote an algorithm that would allow the engine to compute [Bernoulli numbers](http://numbers.computation.free.fr/Constants/Miscellaneous/bernoulli.html) (a recurring theme in number theory), and is thus credited as the first programmer, even though no programming languages had been invented yet. She wrote the first algorithm intended to be carried out by a machine.

### US Census

In the United States, census data is collected every ten years. In 1880, the US Census count took seven years. Population trends indicated that the 1890 census might take over 10 years, so they looked for another solution by holding a contest to find a better way to do it. A census department employee named Herman Hollerith won the contest. He would later go on to found the Tabulating Machine Company, which later became IBM. His solution used punchcards to input the data and mechanical relays to increment the count.

## Modern Era

### Alan Turing

![](https://res.cloudinary.com/briezh/image/upload/v1539104015/Alan_Turing_Aged_16_qi8uza.jpg)

Alan Turing is considered the father of theoretical computer science and artificial intelligence. He formalized the meanings of words `algorithm` and `computation`. He worked at Cambridge University and later performed [critical code breaking work for the British during World War 2](https://en.wikipedia.org/wiki/Cryptanalysis_of_the_Enigma).

Turing also developed the idea of a Turing machine. A Turing machine, simply stated, is a machine that can model any kind of algorithm with an answer. For the sake of argument, we usually don't consider any memory constraints. For a more detailed explanation in layman's terms, see [this reddit post](https://www.reddit.com/r/explainlikeimfive/comments/4umot5/eli5_what_does_turing_complete_mean/).

### The 1940s: World War 2 and Early Digital Computers

While discussing the advent of the modern computer, it's nearly impossible to avoid discussing the second world war. Many advancements in the field of computing on both sides were made to further the war effort. While people like Turing were working on decryption for the allied forces, people like [Konrad Zuse](https://en.wikipedia.org/wiki/Konrad_Zuse) were working in Germany. Zuse's work was ignored or understated for a long time due to the fact that he worked for the Nazis. For his part, he never became a member of the Nazi party but also never expressed any qualms about working for them. An exerpt from Wikipedia says the following:

*"While Zuse never became a member of the Nazi Party, he is not known to have expressed any doubts or qualms about working for the Nazi war effort. Much later, he suggested that in modern times, the best scientists and engineers usually have to choose between either doing their work for more or less questionable business and military interests in a Faustian bargain, or not pursuing their line of work at all."*

Make of that what you will - this is a history lesson, and not meant to put a value judgment on a person's choices, this is merely meant to summarize advancements in the field of computing. In fact, Zuse's [Z3](https://en.wikipedia.org/wiki/Z3_(computer)) computer is considered the first modern, Turing-complete, fully-programmable digital computer, and the programming language he used, [Plankalkül](https://en.wikipedia.org/wiki/Plankalk%C3%BCl) was the first high-level programming language. 

#### Plankalkül Features/Limitations

* Only local variables
* No recursion
* Only call by value
* Composite types: arrays and tuples
* Conditionals (if, else)
* For and while loops
* Only primitive data type is a single bit

### ENIAC, EDVAC, and EDSAC

```
“Computers in the future may weigh no more than 1.5 tons.”
— Popular Mechanics in 1949, forecasting the relentless march of science.
```

Meanwhile in the United States, the ENIAC (Electronic Numerical Integrator and Computer) was created by the US Army's Ballistic Research Laboratory. [John Von Neumann](https://en.wikipedia.org/wiki/John_von_Neumann) was a mathematician working on the hydrogen bomb at Los Alamos. When he heard about the ENIAC, Los Alamos became heavily involved with it as well, and ran the first program on the ENIAC, which was a test of the feasibility of a thermonuclear weapon. The I/O for this test used 1 million punchcards.

John Von Neumann subsequently worked on the [EDVAC](https://en.wikipedia.org/wiki/EDVAC) (Electronic Discrete Variable Automatic Computer). Unlike the ENIAC, it used a binary number system rather than a decimal system. When describing the design of this computer, Von Neumann described the basic architecture of the modern computer. This is known as [Von Neumann architecture](https://en.wikipedia.org/wiki/Von_Neumann_architecture).

The [EDSAC](https://en.wikipedia.org/wiki/Electronic_delay_storage_automatic_calculator) (Electronic Delay Storage Automatic Calculator) was inspired by the EDVAC and was the second computer to use Von Neumann's architecture.

### The Interesting Life of John Von Neumann 

(Summarized from [Wikipedia](https://en.wikipedia.org/wiki/John_von_Neumann))

![](https://res.cloudinary.com/briezh/image/upload/v1539117174/JohnvonNeumann-LosAlamos_cihpl8.gif)

John Von Neumann was noted for his cognitive abilities even among other intellectuals. At age 6 he could divide 2 8-digit numbers in his head and coverse in Ancient Greek. At 8, he was familiar with differential and integral calculus. College professors of Von Neumann admitted that he would often come back the next day having solved a previously unsolved problem. He had an eidetic memory, meaning he had a high degree of recall with only brief exposure. He had memorized the phone book and was known to entertain friends by asking them to call out a page and he would recite the names, numbers, and addresses on it. According to [Herman Goldstine](https://en.wikipedia.org/wiki/Herman_Goldstine), who worked on ENIAC, Von Neumann could recite every book he ever read.

Von Neumann was one of the [Martians](https://en.wikipedia.org/wiki/The_Martians_(scientists)) - a group of prominent Hungarian-American Scientists whose acheivements are briefly listed below. Besides Von Neumann, the other Martians included:

| Name | Notable Acheivements |
| --------------------- | -------------------------------------------- |
| Theodore von Kármán | Contributions in aeronatics/astronautics, advancements in aerodynamics, worked at JPL, awarded National Medal of Science by JFK |
| George de Hevesy | Nobel Prize in Chemistry, discovered element Hafnium, developed radioactive isotope tracers |
| Leó Szilárd | Patented nuclear reactor, wrote a letter with Einstein that resulted in the Manhattan project, cured his own cancer with cobalt 60 treatment he developed himself, numerous contributions and awards |
| Dennis Gabor | Nobel Prize in Physics for invention of holography/holographic methods, numerous other awards |
| Eugene Wigner | Nobel Prize in Physics for contributions to theory on atomic nuclei and elementary particles, work on the Manhattan project, numerous other contributions and awards |
| Edward Teller | 'The father of the hydrogen bomb', numerous contributions to nuclear and molecular physics, spectroscopy, and surface physics |
| Paul Erdős | Extensive contributions to mathematics (discrete mathematics, graph theory, number theory, set theory, probability theory, etc.) - 1500 papers, still unsurpassed |

One of them, Eugene Wigner, was asked why the Hungary of his generation had produced so many geniuses. Wigner, who won the Nobel Prize in Physics in 1963, replied that Von Neumann was the only genius.

Edward Teller admitted that he *'never could keep up with him'*. Teller also said *'von Neumann would carry on a conversation with my 3-year-old son, and the two of them would talk as equals, and I sometimes wondered if he used the same principle when he talked to the rest of us.'*

> Fun Fact: John Von Neumann invented the merge sort algorithm - he wrote down the algorithm - with pen and paper - on 23 pages!

## The 1950s and the Advent of High-Level Programming Languages

With the development of the first Turing-complete computers, soon followed the development of programming languages to use on them. The four biggest ones from the 1950's were:

* [FORTRAN](https://en.wikipedia.org/wiki/Fortran) (1957) - First to use a compiler
* [LISP](https://en.wikipedia.org/wiki/Lisp_(programming_language)) (1958) - First procedural programming language
* [ALGOL](https://en.wikipedia.org/wiki/ALGOL) (1958)
* [COBOL](https://en.wikipedia.org/wiki/COBOL) (1959)

(Beware - acronym-overload!)

#### FORTRAN

[FORTRAN](https://en.wikipedia.org/wiki/Fortran), first released in 1957, stands for 'FORmula TRANslation'. It is considered a high-level language and was the first language to use a compiler to translate high-level code down into machine code. It is known for being very fast. FORTRAN is the predecessor to several later languages, the most widely known one is [BASIC](https://en.wikipedia.org/wiki/BASIC) (an acronym for Beginner's All-purpose Symbolic Instruction Code).

Here is a simple program written in FORTRAN:

```FORTRAN
C AREA OF A TRIANGLE WITH A STANDARD SQUARE ROOT FUNCTION
C INPUT - TAPE READER UNIT 5, INTEGER INPUT
C OUTPUT - LINE PRINTER UNIT 6, REAL OUTPUT
C INPUT ERROR DISPLAY ERROR OUTPUT CODE 1 IN JOB CONTROL LISTING
      READ INPUT TAPE 5, 501, IA, IB, IC
  501 FORMAT (3I5)
C IA, IB, AND IC MAY NOT BE NEGATIVE OR ZERO
C FURTHERMORE, THE SUM OF TWO SIDES OF A TRIANGLE
C MUST BE GREATER THAN THE THIRD SIDE, SO WE CHECK FOR THAT, TOO
      IF (IA) 777, 777, 701
  701 IF (IB) 777, 777, 702
  702 IF (IC) 777, 777, 703
  703 IF (IA+IB-IC) 777, 777, 704
  704 IF (IA+IC-IB) 777, 777, 705
  705 IF (IB+IC-IA) 777, 777, 799
  777 STOP 1
C USING HERON'S FORMULA WE CALCULATE THE
C AREA OF THE TRIANGLE
  799 S = FLOATF (IA + IB + IC) / 2.0
      AREA = SQRTF( S * (S - FLOATF(IA)) * (S - FLOATF(IB)) *
     +     (S - FLOATF(IC)))
      WRITE OUTPUT TAPE 6, 601, IA, IB, IC, AREA
  601 FORMAT (4H A= ,I5,5H  B= ,I5,5H  C= ,I5,8H  AREA= ,F10.2,
     +        13H SQUARE UNITS)
      STOP
      END
```

> Fun Fact: Code for NASA's probes Voyager 1 and Voyager 2 were written in FORTRAN

FORTRAN is still used and is now known simply as 'Fortran' (without the capital letters). Today, Fortran is mostly used for super-computing tasks in the scientific and engineering communities. As web developers, you're unlikely to ever encounter it unless you go out searching for it!

#### LISP

*"Lisp has jokingly been called "the most intelligent way to misuse a computer". I think that description is a great compliment because it transmits the full flavor of liberation: it has assisted a number of our most gifted fellow humans in thinking previously impossible thoughts."*

- [Edsger Dijkstra](https://en.wikiquote.org/wiki/Edsger_W._Dijkstra)

The name [LISP](https://en.wikipedia.org/wiki/Lisp_(programming_language)) is derived from 'LISt Processor', and one of the major types used in LISP are linked lists. LISP is based on Lambda calculus and quickly became a favorite language for artificial intelligence research at that time. It is known for its clean syntax and elegant structure. A person who writes a LISP program will spend more time thinking than typing.

LISP is the 2nd oldest programming language in use today. The most common LISP dialects in use today are [Scheme](https://en.wikipedia.org/wiki/Scheme_(programming_language)) and Common LISP. It's the first language to use [read-eval-print-loop](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) or an interactive shell. 

LISP pioneered many of the structures and concepts in modern-day computer science such as tree-based data structures, dynamic typing, recursion, higher-order functions, and others. The languages you know and love today would not exist without these concepts.


Here is an [example function](https://www.cs.trinity.edu/~jhowland/ccsc97/ccsc97/node10.html) definition in Scheme:

```Scheme
(define square
    (lambda (x)
      (* x x)))
```

Then, invoking the function in a REPL:

```Scheme
> (square 10)
100
```

Because it is so elegant, programmers have popularly referred to LISP (some more or less jokingly) as the language of God. Here is your relevant XKCD:

![](https://imgs.xkcd.com/comics/lisp.jpg)


#### ALGOL

[ALGOL](https://en.wikipedia.org/wiki/ALGOL) stands for 'ALGOrithmic Language'. While it is no longer in common use today, ALGOL defined some fundamentals of syntax that are still in use today, such as code blocks, scope, and nested functions. Most modern languages have syntax that is 'ALGOL-like', and ALGOL was a predecessor to many other languages, including C and Pascal.

#### COBOL

[COBOL](https://en.wikipedia.org/wiki/COBOL) (COmmon Businuess Oriented Language) is still widely used in legacy applications. It is declining in popularity and most usage is to maintain old projects/existing applications.

## The Beginnings of the Internet

#### DARPAnet

TODO

### Advent of Operating Systems

#### Linux

#### Windows

## Resources 

* [Visual Timeline/Chart](https://www.worldsciencefestival.com/infographics/a_history_of_computer_science/)
* [Wikipedia - History of CS](https://en.wikipedia.org/wiki/History_of_computer_science)
* [Antikythera Mechanism](https://en.wikipedia.org/wiki/Antikythera_mechanism)
* [Blaise Pascal](https://en.wikipedia.org/wiki/Blaise_Pascal)
* [Charles Babbage](https://en.wikipedia.org/wiki/Charles_Babbage)
* [Turing-Complete](https://en.wikipedia.org/wiki/Turing_completeness)
* [ELI5 Turing-Complete](https://www.reddit.com/r/explainlikeimfive/comments/4umot5/eli5_what_does_turing_complete_mean/)
* [Cryptanalysis of the Enigma](https://en.wikipedia.org/wiki/Cryptanalysis_of_the_Enigma)
* [History of Programming Languages](https://en.wikipedia.org/wiki/History_of_programming_languages)
