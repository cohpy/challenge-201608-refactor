This refactor starts with Jim Prior's refactor. Thank you Jim!

Much of Jim's comments shows iterations over some "m" search space, like 1/width, 2/width, 3/width, etc.

The goal of this refactor was to generate a bunch of images to disk, rather than display interactively.
This allows searching the "m" space quickly and allows for making movies.

You need to create an images directory prior to running.

This refactor:

1. Moves image generation into a function so it can be run a number of times
2. Generates the image with Pillow and saves to a PNG rather than Tk and the screen
3. Iterates through a sequence of 500 images, which you can use to define your "m" space

Todo:

1. Be able to pass in image size into the program
2. Be able to pass the "m" search algorithm in the command line
3. Be able to specify the directory where images are stored in the command line
4. Create the passed in directory if it doesn't exist
5. Be able to pass in the number of colors in the command line

Ideas:

1. Iterate over the number of colors


To make a movie:

```
# ffmpeg -r 12 -i images/%05d.png circle2.mp4
```

Where "12" is the number of frames per second.
