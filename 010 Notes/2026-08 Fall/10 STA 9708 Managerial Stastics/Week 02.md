---
modified: 2026-09-22T16:02
created: 2026-07-17T21:34
---

---
## 2026-09-19 
###### 08:22am
---
# Note Meta
## Agenda

- Review
- New Material
- Chapter 4, Slide 1
	- Experiments
	- Counting rules
	- Assigning Probabilities
	- Events & probabilities
	- Relationships of probabilities
	- Conditional probabilities
- 

## Tags
* #probability
* #statistics
* #classicalMethod
* #relativeFrequency
* #subjectiveMethod
* #conditionalProbability
* #setTheory
* #notes
## Summary

### I. Methods of Assigning Probabilities (The Three Approaches)

Probabilities can be assigned using three distinct methods:

1.  **Classical Method:** Assumes all outcomes are equally likely (e.g., tossing a fair coin).
2.  **Relative Frequency Method:** Based on empirical data or repeated experimentation (calculating probability as $\text{Frequency} / \text{Total Trials}$).
3.  **Subjective Method:** Used when historical data is unavailable or inappropriate, relying instead on expert judgment or informed opinion.

***Key Principle:*** For any set of probabilities covering all possible outcomes, the sum must equal 1.0.

### II. Events and Sample Space

*   **Event:** A collection of specific sample points within an experiment's total outcome set (the sample space).
*   **Probability of an Event:** Calculated by summing the probabilities of all individual sample points belonging to that event.
*   **Counting Rules:** Used to determine the size of the sample space for multi-step experiments ($N = n_1 \times n_2 \times ...$).

### III. Basic Probability Relationships (Rules)

These rules allow calculation without knowing every possible outcome:

| Concept | Notation | Definition | Key Formula |
| :--- | :--- | :--- | :--- |
| **Complement** | $A^c$ | All outcomes *not* in event A. | $P(A) + P(A^c) = 1$ |
| **Union (OR)** | $A \cup B$ | Event A occurs, or B occurs, or both occur. | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| **Intersection (AND)** | $A \cap B$ | Both event A and event B must occur simultaneously. | *(Used in the Union formula)* |
| **Mutually Exclusive** | N/A | Events that cannot happen at the same time (their intersection is zero). | $P(A \cup B) = P(A) + P(B)$ |

### IV. Conditional Probability

Conditional probability measures the likelihood of one event occurring *given* that another event has already occurred.

*   **Notation:** $P(A \mid B)$ (The probability of A given B).
*   **Formula:** The conditional probability is calculated by finding the intersection of both events and dividing it by the probability of the conditioning event:
    $$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

***Key Insight:*** Comparing a conditional probability (e.g., $P(\text{Son Attends} \mid \text{Father Attended})$) to another ($P(\text{Son Attends} \mid \text{Father Did Not Attend})$) helps determine if the two events are related or independent.


## Questions

## Tasks

- [x] Quiz 2 - use R.  Answers to be sent after class and uses R (went sent via email today) ✅ 2026-09-22
- [x] Read Ch 4: pp 109 - 116 ✅ 2026-09-22
- [x] 🚅 Ch 4 Exercises: 21 - 28 ✅ 2026-09-22


---
# Notes

## Review

Reviewed chapter 4 slides 

### Counting Rule for Permutations

Like combinations, but order matters

# New

# Assigning Probabilities
## Classical Method
- Assigning probabilities based on the assumption of **equally likely outcomes**

## Relative Frequency Method
- Assigning probabilities based on **experimentation or historical data**

## Subjective Method
- Assigning probabilities based on **judgment**

> In god we trust, and in all others they must bring data


## 3 Methods of Assigning Probabilities

### 1. Classical Method
Experiment: toss a coin
Sample space:  { head, tail }

*NEW:* Probabilities: each probability added together MUST add up to 1
p(Head) = 0.5
p(Tail) = 0.5
probability = 0.5 + 0.5 = 1.0

### 2. Relative Frequency Method

Experiment: conduct a sales call on a potential costumer <-- repeated 400 times
Sample space: { sale, no sale }

Assign probabilities: 
p(sale) = 100/400 = 0.25
p(no sale) = 300/400 = 0.75
probability must = 1.0 --> 0.25 + 0.75 = 1.0

### 3. Subjective Method
Couldn't get relative frequency data or the data is not classical.

Experiment: Observe 2026 Men's World Cup Final between Spain and Argentina.  
Sample space = S = { Spain Wins, Spain Loses }
Probabilities: 
p(Spain Wins) = ?
p(Spain Loses) = ?
must equal = 1.0

Classical method would assign 0.5 to both outcomes.  But not realistic.  

## Events and Their Probabilities
(slide 12)

An **event** is a collection of sample points.

The **probability of any event** is equal to the sum of the probabilities of the sample points in the event.

If we can identify all the sample points of an experiment and assign a probability to each, we can compute the probability of an event.  

### Example

Experiment: Roll a pair of dice. Suppose we are interested in the sum of the face values showing on the dice. 

Die 1 sum Die 2 combinations

| **Die 1** | **Die 2: 1** | **2** | **3** | **4** | **5** | **6** |
| --------- | ------------ | ----- | ----- | ----- | ----- | ----- |
| **1**     | 2            | 3     | 4     | 5     | 6     | 7     |
| **2**     | 3            | 4     | 5     | 6     | 7     | 8     |
| **3**     | 4            | 5     | 6     | 7     | 8     | 9     |
| **4**     | 5            | 6     | 7     | 8     | 9     | 10    |
| **5**     | 6            | 7     | 8     | 9     | 10    | 11    |
| **6**     | 7            | 8     | 9     | 10    | 11    | 12    |

#### Question: how many sample points are possible?  
Can use a counting rule. Can use counting rule for multiple step experiment.  
6 * 6 = 36

k = 2 
$n_1$ = 6
$n_2$ = 6 

$n_1$, $n_2$ = 6 * 6 = 36

Sample space = S = { (1, 1), (1, 2), ... (1, 6) ... (6, 6) }

What is the probability of obtaining a value of 7?

$E_7$ = { (6, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6) }  <-- event

p($E_7$) = P(1,6), + p(2, 5) + P(3,4) + p(4,3) + p(5,2) + p(6,1)
p(6,1) = 1/36
p($E_7$) = 1/36 + 1/36 ... + 1/36 = 6/36 = 1/6

The probability of obtaining a value of 7 = 1/6

#### Question: What is the probability of obtaining a value of 9 or greater?

1/36 * 10 = 10/36 = 5/18

the probability is 5/18

## Some Basic Relationships of Probability

There are some **basic probability relationships** that can be used to compute the probability of an event without knowledge of all the sample point probabilities

- Complement of an event
- Union of two events
- Intersection of two events
- Mutually exclusive events

### Complement of an Event
(slide 14)
- The *complement* of an event A is defined to be the event consisting of all sample points that are not in *A*
- The complement of *A* is denoted by *$A^c$*
- Ven diagram 
	- Whole diagram represents sample space
	- A is circle in the space
	- everything NOT in A is A compliment *$A^c$*
	- P(A) + P($A^c$) = 1
	- We can find P(A) if we subtract P compliment --> P(A) = 1 - P($A^c$)
	- In a class of 20 people, what is the probability of 2 of you will have the same 00birthday
		- Can use subtraction here to get to the answer

### Union of 2 Events
(slide 15)
- A *union* of events *A* and *B* is the event containing all sample points that are in *A* or *B* or both
- The union of events *A* and *B* is denoted by A ∪ B

### Intersection of 2 Events
(slide 16)
- The *intersection* of events *A* and *B* is the set of all sample points that are in both A and B
- The intersection of events A and B is denoted by A ∩ B (upside down U)

### Additional Law
(Slide 17)

- Provides a way to compute the probability of even A, or B, or both A and B occurring
- P(A∪B) = P(A) + P(B) - P(A ∩ B)
- *- P(A ∩ B)* takes into account the double counting -- if we didn't do this, we'd have a probability > 1

### Mutually Exclusive Events
- Two events are said to be mutually exclusive if the events have no sample points in common
- Two events are mutually exclusive if, when one event occurs, the other cannot occur
- Venn diagram

Experiment: Roll die
Sample space: S = { 1, 2, 3, 4, 5, 6 }

2 Events:
Event A = { 1, 2, 3, 4 }
Event B = { 3, 4, 5, 6 }

A∪B = { 1, 2, 3, 4, 5, 6 }
A∩B = { 3, 4 }

$A^c$ = { 5, 6 }
$B^c$ = { 1, 2 }
$A^c∪B^c$ = { 1, 2, 5, 6 }
$A^c∩B^c$ = { } $\varnothing$ (empty set)

 ![InkDrawing](<002 MBA/010 Notes/2026-08 Fall/10 STA 9708 Managerial Stastics/attachments/Ink/Drawing/2026.9.19 - 10.13am.svg>) [Edit Drawing](https://youtu.be/2arL1jh8ihA?type=inkDrawing&width=500&aspectRatio=1.778&viewBoxX=0&viewBoxY=0&viewBoxW=2000&viewBoxH=1125)



### Mutually Exclusive Events

 ![InkDrawing](<002 MBA/010 Notes/2026-08 Fall/10 STA 9708 Managerial Stastics/attachments/Ink/Drawing/2026.9.19 - 10.16am.svg>) [Edit Drawing](https://youtu.be/2arL1jh8ihA?type=inkDrawing&width=500&aspectRatio=1.778&viewBoxX=0&viewBoxY=0&viewBoxW=2000&viewBoxH=1125)

A: Born in CA
B: Born in NY

A union B = impossible

#### Two forms of the addition law
P(A∪B) = P(A) + P(B) - P(A ∩ B)
P(A∪B) = P(A) + P(B) - 0 = p(A) + p(B)


### Example 4.15 from text book
pg 109 in textbook

According to the US CDC, over an 8 year period, average of 16375 teenagers died each year in the US.  Leading causes of death are accidents, 7860, homicide 2129, and suicide 1018.  What is the probability that someon in this cohort would die of accident, homicide, or suicide?  And what is the probablity someone dies form a cause other than accident, homicide, or suicide.  
- "Facts"
	- 16375 die each year
		- 7860 by accident (A)
		- 2129 by homicide (H)
		- 1801 by suicide (S)
- What is the probability of each of these events?
	- P(A) = A/S = 7860/16375 = 12/25 = 0.48
	- P(H) = H/S = 2129/16375 = 0.13
	- P(S) = S/Sample = 1801/16375 = 0.11
- What is the probability by death by accident or homicide?
	- P(A∪H) = P(A) + P(H) - (P(A∩H)
		- 0.48 + 0.13 - ? =
			- What's the probability they die by accident AND homicide - it's probably 0.  One of either will kill you, but can both kill you at the same time?  ehh... 
			- So ? = 0
			- 0.48 + 0.13 - 0 = 0.61
- What is the probability other than A, H, or S?
- $P^c$ = 1 - (P(A) + P(H) + P(S)) 
	- 1 - (0.48 + 0.13 + 0.11) = 1 - 0.72 = *0.28 chance of dying by some other cause*

## Conditional Probability

The probability of an event given that another event has occurred is called a *conditional probability*

The conditional probability of *A given B* is denoted by P(A|B)

A conditional probability is computed as follows:

$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$

### Conditional probability of A given B

$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$

Whatever is no the right hand side is in the denominator, so A|B --> p(B) will be the bottom part of the fraction

#### Example

Is a son/daughters attending university related to the father's attending university?

Researchers went out and collected data.  

##### Data
$f_c$ = father attended college
$f_n$ = father did NOT attend college

|        | $S_c$ (Son Attended) | $S_n$ (Son did not attend) | Total        |     |
| ------ | -------------------- | -------------------------- | ------------ | --- |
| $f_c$  | 22                   | 12                         | 34           |     |
| $f_n$  | 35                   | 31                         | 66           |     |
| Total: | 57                   | 43                         | 100 families |     |

A good way to answer this question: 

Recipe: $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$

$P(S_c \mid F_c)$ = $\frac{P(S_c \cap F_c)}{P(F_c)}$ = $\frac{22/100}{34/100}$ = 0.6471
$P(S_c \mid F_N)$ = $\frac{P(S_c \cap F_N)}{P(F_N)}$ = $\frac{35/100}{66/100}$ = 0.5303

Then compare the one probability with the other. 

The point?  Since the $P(S_c \mid F_c) \geq P(S_c \mid F_N)$ 0.6471 > 0.5303 we conclude the data/evidence is consistent with there being a relationship...



