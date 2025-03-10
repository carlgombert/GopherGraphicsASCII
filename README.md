# Text Graphics Competition - Gopher Graphics Club
<p align="left">
<img src="https://github.com/carlgombert/GopherGraphicsASCII/blob/main/res/demo.gif"/>
</p>

## [Video Link](https://drive.google.com/file/d/127z1eB-aLx5_5_c9sOFPqbFuybVReoYL/view?usp=sharing)<br />
[One Last Breath original music video](https://www.youtube.com/watch?v=qnkuBUAwfe0)<br />
[Python Script](https://github.com/carlgombert/GopherGraphicsASCII/blob/main/Main.py)<br />

This is my submission to the ASCII graphics demo

For my demo I converted the "one last breath" music video by Creed to ASCII graphics<br />
I wrote the program for this in python, OpenCV has a lot of great functions for 
dealing with images and videos.

I parsed the original video frame by frame<br />
calculated the intensity of 8 by 8 kernels in each frame<br />
mapped the intensity to a character, the greater the intensity the more dense the character (" . : ; + x X $ @")<br />
drew the strings generated by each frame onto images and used them to create a new video<br />

The final video took something like 15 minutes to generate so you can imagine how frustrated I was when the first 4 tries didn't work. 
Firstly because it's python but also this is just an expensive process analyzing every pixel of every frame in a 4 minute video.

For this reason I was originally going to use C++ but I'm glad I didn't because however slow it was, python made the 
whole process so much smoother.
