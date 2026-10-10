---
modified: 2026-09-19T08:42
created: 2026-07-17T21:34
---

---
## 2026-08-29 
###### 08:33am
---
# Note Meta
## Agenda

## Tags
* #statistics
* #probability
* #countingRule
* #combinations
* #bayesTheorem
* #sampleSpace
* #rProgramming
* #lectureNotes

## Summary

### 🗓️ Logistics & Course Structure
*   **Class Time:** 8:30 AM – 11:00 AM (with a break at 9:45 AM).
*   **Contact:** Email questions to robert.stinerock@baruch.cuny.edu, specifying the chapter/material in question. Use robert.stinerock@gmail.com if the instructor is out of town.
*   **Schedule Note:** The class is off for the next two weeks; return date is 2026-09-19.
*   **Course Focus:** This is a skills-based class, relying heavily on lecture material rather than group work.
*   **Tools:** Uses **R statistics programming** (download R and R Studio).
*   **Assessment:** The final grade

## Questions

## Tasks

- [x] Review pages 98-105, chapter 4 📅 2026-09-19 ✅ 2026-09-05
- [x] Ch 4 Exercises 1-20 📅 2026-09-19 ✅ 2026-09-19


---
# Notes

BrightSpace: https://brightspace.cuny.edu/d2l/home/1294332

# Intro

- Reviewed syllabus 
- How to reach
	- Send email to robert.stinerock@baruch.cuny.edu
		- Send details around what chapter and material you have questions on 
- 8:30-11am
	- break at 9:45am
- Have off the next 2 weeks
- Return 2026-09-19

# Syllabus

- Course info
- Text book - PDF book
- Course outline & schedule
	- No dates - sometimes we slow down
- Eval
	- 2 exams, 40% of final grade each (take home, given a few weeks to do it)
		- submit as a Word doc
	- 20% end of class, 1 question, multiple choice quiz reinforce what we've done in class
- Using R stats programming
	- Could have used Python.  R has more stats capability
- Download R and then R Studio
	- Page 3 has install instructions
- A lot of lecture material, not much group work. This is a skills based class.  
- Zoom invite available (link is on BrightSpace)
- For the next 2 weeks, instructor may be out of the country, if you need to reach the instructor:  robert.stinerock@gmail.com

# Chapter 4 - Introduction to Probability

- Experiments, Counting Rules, and Assigning Probabilities
- Events and Their Probability
- Some basic relationships of probablity
- Conditional Probability
- Bayes' Theorem


# Probability as a Numeric Measure of the Likelihood of Occurrence

Probability: 0 --> .5 --> 1
0 = unlikely
.5 = just as likely as unlikely
1 = almost certain to occur

# An Experiment and its Sample Space

- An **experiment** is any process that generates well-defined outcomes
- The **sample space** for an experiment is the set of all experimental outcomes
- An experimental outcome is also called a **sample point**

S = { } <-- sample space, Set

| Experiment        | Experimental Outcomes    |
| ----------------- | ------------------------ |
| Toss a coin       | S = { Head, Tail }       |
| Roll a die        | S = { 1, 2, 3, 4, 5, 6 } |
| Conduct sals call | S = { sale, no sale }    |
|                   |                          |

Need to know the difference to pass the class:
die = singular
dice = plural

# Counting Rule

Be able to identify the sample points and be able to count them.  The counting rules can help us count them.  

## Counting Rule for Multiple-Step Experiments

- If an experiment consists of a sequence of *k* steps in which there are *$n_1$* possible results for the first step, *$n_2$* possible results for the second step, and so no, then the total number of experimental outcomes is given by ($n_1$)($n_2$)...($n_k$)

Example: An experiment consists of tossing a coin 3 times. How many experimental outcomes are there? 

2 approaches

### 1. Apply the Counting Rule

How many steps? 3
*k* = 3 steps

How many results are possible on each step?
$n_1$ = 2
$n_2$ = 2   
$n_3$ = 2

$n_1 * n_2 * n_3$ = (2)(2)(2) = 8


### 2. Tree Diagram
These are not preferred, but showing as an example

(Drawn as a tree):

| Step 1:  | Step 2:  | Step 3:  |     |
| -------- | -------- | -------- | --- |
| 1st Coin | 2nd Coin | 3rd Coin | S   |
|          |          | H        | HHH |
|          | H        | T        | HHT |
| H        | T        | H        | HTH |
| T        | H        | T        | THT |
|          | T        | H        | TTH |
|          |          | T        | THT |
|          |          |          | TTH |
|          |          |          | TTT |
You get the following paths:

S = { (HHH), (HHT), (HTH), (HTT), (THH), (THT), (TTH), (TTT) }


>***Need to know the process to understand which rule to apply***

These are like story problems. Need to figure out which framework to apply.

## Counting Rule for Combinations

Number of **Combinations** of ***N* Objects** taken $n$ at a time

$\Huge \binom{N}{n} = \frac{N!}{n!(N-n)!}$
or
$\huge \binom{n}{k} = \frac{n!}{k!(n-k)!}$


where $N!$ = N(N-1)(N-2)...(2)(1)
$n!$ = n(n-1)(n-2)...(2)(1)
0! = 1

How many combinations of 3 objects can be taken 2 at a time?

Let's say we have a vase.  In the vase, we put in 3 marbles.  Marbles are numbered 1-3.  We stir or *randomize* and take out 2.  We write them done and repeat for 3 total pulls.  

N = 3
n = 2

S = { (1, 2), (1, 3), (2, 3) }  (the number of combinations)

$\frac{3!}{2!(3-2)!} = \frac{3!}{2!1!} = \frac{3*2*1}{(2*1)(1)} = \frac{6}{2} = 3$

##### How many unique 5 card poker hands are possible out of 52 cards?
N = 52
n = 5

$\frac{52!}{5!(52-5)!} = \frac{52!}{5!47!} = \frac{52*51*50\dots*2*1}{(5*4*3*2*1)(47*46*45*\dots*2*1)} = 2598960$
2598960 combinations

In R, enter: 
`choose(52,5)`

First number is the "population" size.  Second number is the number of choices to make

##### Example 4.2 in textbook:  
Department of motor vehicles wants to issue new license plates to 35 million vehicles in that state next year. They are proposing to use all numbers and arranged in 7 positions on the license plate. Will they have sufficient number of license plates?

_ _ _ - _ _ _ _ 

N = 10
n = 7

**Multiple step experiment**
How many steps? 7
k = 7
How many possibilities? 10
S = { 0-9 }

These are called the *ingredients*
$n_1$ = 10
...
$n_{7}$ = 10

Apply *recipe*
$n_1, n_2, ... n{7}$
(10)(10)(10)(10)(10)(10)(10) = (10)^7
= 10,000,000 total

This is less than 35 million needed.

Not enough, can we use letters in the first 3 places?

(26)(26)(26)(10)(10)(10)(10)
$26^3 * 10^4 = 175,760,000$

This will do!  

In R
`10&7`

Can set options in R to change the scientific notation:
`options(scipen = 999)`


# Two Requirements of Probability Assignment

1. For any experiment outcome $E_i$
2. 0 <= p($E_i$) <= 1
3. $\Sigma(p(E_{i})) = 1$




