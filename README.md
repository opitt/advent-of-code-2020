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
* I learned to include images in github markdown. See below.

_Python_
* I practiced the zip function. Until I found out during refactoring, I did not need it.
* PIL (pillow) package: I created my first animated gif with pillow:
* os ... refreshed my kowledge on reading files from a directory.
* And I nearly forgot the amazing generators. I used it for the first time to create a function, that yields always the next file name and content (sorted).

![Day 11 simulation](https://github.com/opitt/advent-of-code-2020/blob/main/day11/sim_data/sim_82.gif)

_Resources_
* [Create animated gifs with PIL](https://note.nkmk.me/en/python-pillow-gif/)
* [Saving gif with PIL](https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#saving)
* [Color pallet generator](https://coolors.co/0e4749-95c623-e55812)
* [Github markdown](https://guides.github.com/features/mastering-markdown/)
* [Read/write files (Real Python)](https://realpython.com/read-write-files-python/#iterating-over-each-line-in-the-file)
* [Understanding Generators (Real Python)](https://realpython.com/lessons/understanding-generators/)

## Day 14
_Python_
* Convert an integer to binary with a defined length (f"{value:036b}) and back to an integer (using int(value, 2))
* Getting used to the zip function. Zipped the mask with the binary value.

## Day 15
_General_
* Reminder! Pen and paper is essential to develop an algorithm. From intuition to explicit rules (code) it's a long way ...

_Python_
* Used the profiler package cProfile to find out where the performance is lost. It was the index() function. Obviously the longer the list, the longer it takes ... and 300000000 is very long ...

_Resources_
* [cProfile documentation](https://docs.python.org/3/library/profile.html)

## Day 16
_General_
* My brain needs a rest. Long working days are not good for a night of AoC.

_Python_
* Working with sets. Good to know, that you can't directly access set elements (as they are unsorted). Bad to find that out, when you need the elements. OMG, I wrote something like this: [{"type"}][0] (don't tell anyone).

## Day 17
_General_

* I fall behind. 

_Python_
* The unpacking of iterables is not really intuitive yet (for me) - in the context of list comprehensions. More to learn for me.

## Day 18 
_Python_

* I remembered the reduce function from the functools library. Together with a lambda function it multiplies the content of a list very nicely (pythonic). 
```result = reduce(lambda x, y: x*y, [1,2,3,4])```

## Day 19
_Python_
* re: Named matching groups ```(?P<MG1>    )``` and matching groups, that are not captured: ```(?:  )```
* re: it's not possible to count with regular expressions
* I got really frustrated with re (and learned a lot). Finally I used a cheat (hard coded max limit) - recommended by a colleague. I could not find out how to validated the recursive rule: ```11: 42 31 | 42 11 31```. I simpified it to ```42 (42 (42...31) 32) 31``` with "+" occurances. But we can't write it like ```(42)+(31)+``` because both rules 42 and 31 need to have the same occurance. How do we find out, if the matches are valid, i.e. matched the same times? I gave the match groups a name ```(?P<AA>(42)+)(?P<BB>(31)+)```- and accessed it after a match. But I actually did not find out, how many times each of them matched ... if you have a tip - please reach out!

_Resources_
* [Regex101, and amazing site to learn and test regular expressions](https://regex101.com/)

_General_
* Need to practice my markdown skills more ... just noticed, that my README looked awfull.

## Day 20 
_General_
* It's getting complex here. Spent the whole day - finally I solved part 1 and got stuck on part 2. How to turn and flip the tiles ... 

_Python_
* The zip function, I practicesd it a lot today. Very handy to access columns of list of lists. But still somewhat ... confuse. Since you need to convert the result from sets to lists to strings ...
