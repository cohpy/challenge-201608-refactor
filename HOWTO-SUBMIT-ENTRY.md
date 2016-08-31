# How to submit an entry.

For the examples below, the Github account name is "jdoe".
Of course, when you do these, use your actual Github account name.

Browse to github.com and log in to your Github account.

Browse to https://github.com/cohpy/challenge-201608-refactor
and "fork" it to your own account.

On your local computer, clone your "fork" of the repo.

    git clone https://github.com/jdoe/challenge-201608-refactor.git

Go into the directory of your local copy of that repo.

    cd challenge-201608-refactor

Make a new directory to put your stuff in and copy files into it.

    mkdir jdoe
    cp -p circle2.py jdoe
    cd jdoe

Edit the files to your heart's content,
then add and commit them to your local copy of the repo.

    vi circle2.py
    git add circle2.py
    git commit -m 'jdoe/circle2.py: Achieved perfection.'

Push your local changes to your "fork" of the repo on your Github account.

    git push origin master

Browse to github.com and log in to your Github account.

Browse to your "fork" of the repo at
https://github.com/jdoe/challenge-201608-refactor.

Click on "New pull request" button and follow the directions.

Extra bonus points for rebasing your branch on to cohpy's master branch.

If you need help using
[git](https://en.wikipedia.org/wiki/Git_%28software%29) and
[Github](github.com), come to the
[weekly dojos](http://www.meetup.com/Central-Ohio-Python-Users-Group/).
Try to figure out what you can beforehand.
There are plenty of on-line tutorials.
