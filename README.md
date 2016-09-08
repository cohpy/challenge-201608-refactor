# The August 2016 COhPy challenge

In [A.K. Dewdney](https://en.wikipedia.org/wiki/Alexander_Dewdney)'s book,
["The Armchair Universe"](http://www.worldcat.org/title/armchair-universe-an-exploration-of-computer-worlds/oclc/16649548),
there is a chapter called
"[Wallpaper for the Mind](https://www.dropbox.com/s/4wub318265sw8no/Computer_Recreations_Column_1986_Wallpaper.pdf)".
In it, he describes a number of algorithms to make pretty pictures.

A pdf of of the original Computer Recreations column on which this chapter is
based can be found [here](https://www.dropbox.com/s/4wub318265sw8no/Computer_Recreations_Column_1986_Wallpaper.pdf?dl=0).

I have implemented one of those algorithms,
John E. Connett's "CIRCLE^2" in the Python program circle2.py.

The challenge this month is to
[refactor](https://en.wikipedia.org/wiki/Code_refactoring)
this program to:

1. Can you make the program better at accepting input?
   What should it do if you input bad data?

2. Can you document the program better?

3. Can you make the program faster?

4. Can you use generators to generate the plot?

5. Can you write tests for the program?


As a bonus, are there good inputs that result in pretty pictures?
Here are two:

1. -15 -20 87
2. -15 -20 9
3. -4506 21539 3.12

As another bonus, can you add color?
(HINT: the c%2 is a binary check (even/odd, white/black)).

As another bonus, play with different algorithms,
and be able to choose them from the command line.

See HOWTO-SUBMIT-ENTRY.md for how to submit an entry.
