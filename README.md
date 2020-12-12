# advent-of-code-2020
My Python solutions for the advent of code 2020.
A nice challenge for everyday learning a coding language.
# Today I learned...
These are some things I learned along the way.
## Day 5
_General_
* Thanks to Björn Söderqvist aka cybear for the inspiration to track learning in the README.md file

_About Github_
* Finally learned (again) to create a public github repo and add my daily solutions to it.

_About Python_
* I wanted to practice the zip and map functions. I noticed that the [map()] creates a list containing a map object, instead the content of the mapping operation. Instead list(map()) works as I wanted. 

## Day 6
_About Python_
* Learned to apply set operations on a list of sets
* Learned more about the unpacking \*

_About Github_
* Start to get familiar with markdown

_Resources_
* [Real Python](https://realpython.com/python-sets/#operating-on-a-set)
* [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)

_About Visual Studio Code_
* Learned to debug with VSC

## Day 7
_About Python_
* Using os.path.dirname(os.path.realpath(__file__)) to open a file in the same directory as the script. (KUDOS to @dogmatic69)

_General_
* Giving variables a meaningful name is an art. I think I changed my vars 5 times each, until it mades sense (to me).

## Day 8
_Python_
* Deep copy vs shallow copy: I knew about the difference, but used list.copy() without understanding, it is a shallow copy. Then I found the package copy with the deepcopy() function. Nice. Until I refactored a solution, that doesn't need to copy the list at all. Much better performance ...

## Day 9
_General_
* Reading the assignment is critical (really?). Smallest and biggest number ... I interpreted as lowest and highest index ... Wrong assumption. RTF rules!

## Day 10
_General_
* Pen and paper is still an excellent tool to understand a problem.
* Breaking down a problem into smaller problems is a very good strategy.
* After having a solution - it is so much easier and fun to refactor the code. I even found a totally different solution in 4 lines. Find a solution that proofs you understand the problem at hand. Then, and only then, optimise your code.
* I notice, that every day during this challenge my code gets nicer to look at. Better structure, better comments (I hope) better variable names.
* Debugging is the only way to find errors in complex situations. My code left out the last "adapter group". I only saw that in the debugger ...

_Python_
* Removing items from a list ... sometimes the simple things are just gone from the brain ... Thank you Google.
* Using the zip function to calculate the difference of elements in a list. Sooo neat ...

## Day 11
_General_
* Matrix is a challenge. Rows, coluns, ... diagonal movements ...
* Part 1 was fairly easy but part two took me long to code. Easy on paper though ...

_Python_
* I get used to the itertools. count was cool to use for one generic function, that can go in all directions through a matrix. I just pass the -1,0,+1 step value as parameter to the function. Inside I use count and the given step. 
* Used copy.deepcopy again. 

## Day 12
_General_
* Rotating, coordinations, moving relative, ... a nice mind challenge. Still much easier than yesterday's seating simulation.
* Pen and paper have proven again to be super useful.
* Started with just find "a" solution - with a lot of repeated code. When it worked, I refactored and deduplicated. It's much neater code to maintain - but is it easier to understand? I doubt.

_Python_
* I practiced the zip function. Until I found out during refactoring, I did not need it.
* PIL (pillow) package: I created my first animated gif with pillow. 
![Day 11 simulation](https://github.com/opitt/advent-of-code-2020/blob/main/day11/sim_data/sim_82.gif)

_Resources_
*[Create animated gifs with PIL](https://note.nkmk.me/en/python-pillow-gif/)
