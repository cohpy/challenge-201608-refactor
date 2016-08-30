# The August 2016 COhPy challenge

In [A.K. Dewdney](https://en.wikipedia.org/wiki/Alexander_Dewdney)'s book,
["The Armchair Universe"](http://www.worldcat.org/title/armchair-universe-an-exploration-of-computer-worlds/oclc/16649548),
there is a chapter called "Wallpaper for the Mind".
In it, he describes a number of algorithms to make pretty pictures.

A pdf of of the original Computer Recreations column on which this chapter is
based can be found [here](https://www.dropbox.com/s/4wub318265sw8no/Computer_Recreations_Column_1986_Wallpaper.pdf?dl=0).

I have implemented one of those algorithms,
John E. Connett's "CIRCLE^2" in the Python program circle2.py.

The challenge this month is to refactor this program to:

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

## How to submit an entry.

If you are not familiar with using
 [git](https://en.wikipedia.org/wiki/Git_%28software%29) and
 [Github](github.com), go to the
[weekly dojos](http://www.meetup.com/Central-Ohio-Python-Users-Group/).

For the examples below, the Github account name is
"[aneuman](https://en.wikipedia.org/wiki/Alfred_E._Neuman)".
Of course, when you do these, use your actual Github account name.

Log in to your Github account.

Browse to https://github.com/cohpy/challenge-201608-refactor
and "fork" it to your own account.

On your local computer, clone your forked repo.

    git clone https://github.com/aneuman/challenge-201608-refactor.git

Go into your local copy of that repo.

    cd challenge-201608-refactor

Make a new directory to put your version of stuff in
and copy the files into it.

    mkdir aneuman
    cp -p circle2.py aneuman
    cd aneuman

Edit the files to your heart's content,
then add and commit them to your local copy of the repo.

    vi circle2.py
    git add circle2.py
    git commit -m 'aneuman/circle2.py: Achieved perfection.'

Push your local changes to your "fork" of the repo on your Github account.

    git push origin master

Log in to your Github account.

Browse to your "fork" of the repo at
https://github.com/aneuman/challenge-201608-refactor.

Click on "New pull request" button and follow the directions.
