---
modified: 2026-09-07T19:46
created: 2026-08-01T06:58
---

---
## 2026-07-25 
###### 07:54am
---
#### Agenda

#### Tags

* #probability
* #statistics
* #randomVariable
* #conditionalProbability
* #independentEvents
* #discreteDistribution
* #expectedValue
* #sampleSpace
* #statisticsLecture


#### Summary


### I. Foundational Definitions
*   **Probability:** A measure ranging from $0$ (unlikely) to $1$ (very likely).
*   **Experiment:** Any process that generates well-defined outcomes.
*   **Sample Space ($S$):** The set of all possible experimental outcomes.
*   **Event:** A collection of specific sample points within the sample space.
*   **Counting Rules:** Used to determine the total number of outcomes (e.g., permutations and combinations).

#### Assigning Probabilities (Methods)
1.  **Classical Method:** Assumes all outcomes are equally likely (e.g., rolling a die).
2.  **Relative Frequency Method:** Based on historical data or repeated experimentation.
3.  **Subjective Method:** Probability assigned based on expert judgment, especially when information is incomplete.

### II. Core Probability Relationships and Laws
These laws allow calculation of event probabilities without knowing every single sample point.

| Concept                     | Notation                           | Definition / Formula            | Notes                                                        |
| :-------------------------- | :--------------------------------- | :------------------------------ | :----------------------------------------------------------- |
| **Complement**              | $A^{\complement}$                  | $P(A^{\complement}) = 1 - P(A)$ | The probability of an event *not* happening.                 |
| **Union (OR)**              | $P(A \cup B)$                      | $P(A) + P(B) - P(A \cap B)$     | Probability of A, or B, or both.                             |
| **Intersection (AND)**      | $P(A \cap B)$                      | Varies by relationship type.    | Probability of A *and* B occurring simultaneously.           |
| **Mutually Exclusive**      | $A$ and $B$ cannot occur together. | $P(A \cup B) = P(A) + P(B)$     | The intersection is zero, so the subtraction term drops out. |
| **Conditional Probability** | $P(A \mid B)$                      | $\frac{P(A \cap B)}{P(B)}$      | Probability of A *given* that B has already occurred.        |

#### Independence and Multiplication Laws
*   **Multiplication Law (General):** $P(A \cap B) = P(A) \cdot P(B \mid A)$
*   **Independent Events:** If the occurrence of one event does not change the probability of another ($P(A \mid B) = P(A)$).
    *   **Multiplication Law (Independent):** $P(A \cap B) = P(A) \cdot P(B)$

### III. Statistics vs. Probability
This is a critical conceptual distinction:
*   **Probability:** Given the full sample space/system ("the pail"), what is the likelihood of a specific outcome? (Predictive.)
*   **Statistics:** Given a limited set of observed data ("what's in your hand"), what can be inferred about the larger population or system ("what's in the pail")? (Inferential.)

### IV. Random Variables and Measures
*   **Random Variable ($X$):** A numerical description of an experiment's outcome.
    *   **Discrete RV:** Can only take on a finite, countable number of values (e.g., 0, 1, 2...).
*   **Probability Distribution Function $f(x)$:** Describes how probabilities are spread over the possible values of $X$. ($\sum f(x) = 1$).

#### Key Measures:
*   **Expected Value ($E[X]$ or $\mu$):** The theoretical mean or average outcome.
    $$E[X] = \sum x \cdot f(x)$$
*   **Variance ($\operatorname{Var}(X)$ or $\sigma^2$):** A measure of how spread out the data is from the mean.
    $$\operatorname{Var}(X) = \sum (x - \mu)^2 f(x)$$
*   **Standard Deviation ($\sigma$):** The positive square root of the variance, providing variability in the original units of measurement.

### V. Common Probability Distributions
These formulas model specific types of random variables:

1.  **Binomial Distribution:** Models the probability of getting a specific number of "successes" ($k$) in $n$ independent trials, where the chance of success ($p$) remains constant (e.g., coin flips).
2.  **Poisson Distribution:** Used to estimate the number of occurrences over a specified interval of time or space (e.g., calls received per hour).
3.  **Hypergeometric Distribution:** A variation of the binomial distribution used when trials are **not independent**, and the probability of success changes after each trial (sampling without replacement).


#### Questions

1. **The Central Limit Theorem (CLT) and Sampling Distributions:** The current material establishes measures of variance for single random variables ($\sigma^2$). How does this concept extend to the *distribution* of sample means or sums? Specifically, how does the CLT allow us to approximate distributions (like the normal distribution) even when the underlying population distribution is non-normal, and what are the conditions under which this approximation holds true?

2. **Transitioning from Discrete to Continuous Probability:** All distributions covered so far (Binomial, Poisson, etc.) are discrete. What mathematical framework (e.g., using integration vs. summation) must be learned to model continuous random variables (like height or temperature), and how do we calculate the probability that a variable falls within a specific range $[a, b]$?

3. **The Bayesian Approach (Updating Beliefs):** The current discussion on subjective probability suggests judgment is key. How does formal Bayesian statistics provide a mathematical framework for updating initial beliefs ($P(\text{Hypothesis})$) when new evidence or data becomes available? What are the core components (Prior, Likelihood, Posterior) and how do they differ fundamentally from classical frequentist methods?

4. **Assumptions and Model Selection:** Every distribution (Binomial, Poisson, etc.) relies on strict assumptions (e.g., independence, constant probability $p$). When these underlying assumptions are violated in real-world data, what alternative distributions or modeling techniques must be employed to accurately represent the process? (E.g., What if trials are *not* independent?)

5. **Hypothesis Testing Framework:** The current material calculates descriptive statistics ($\mu$, $\sigma^2$) and describes probability distributions. How does this knowledge translate into formal statistical inference—specifically, how do we use sample data to test a null hypothesis ($H_0$) about an unknown population parameter (like the true mean or proportion) and calculate a p-value?

6. **Maximum Likelihood Estimation (MLE):** When dealing with observed data, how can we mathematically determine the most plausible parameters ($\mu$, $\sigma^2$, $p$, etc.) for a given distribution? What is the principle of Maximum Likelihood Estimation, and how does it guide us in fitting the correct theoretical model to empirical data?

***
# Notes

## Review

Stats and Probability - a new way of thinking about things
Will lay the ground work.

Course is statistics and probability, but we're focusing on probability.  Probability lays the ground work.

Probability: 0-1 <-- 0 is unlikley, 1 is very likely.  Measured usually in percent.  Percent and probability is the same thing. Chance of rain, say 90% chance of rain, that is the probability of rain is 0.9

#### Experiment 
Any process that generated well-defined outcomes

#### Sample space
set of all experimental outcomes

#### Sample point
An experimental outcome 

#### Counting rules
1. Multiple step
2. Combinations
3. Permutations

Counting rules help us count the number of experimental outcomes.  

#### Purpose
Assign probabilities.

1. Classical method
	1. Equally likely outcomes (tossing a coin or die)
	2. For a die, S = { 1, 2, 3, 4, 5, 6 }
2. Relative Frequency method
	1. Based on experimentation or historical data
	2. Experiment typically known as "market research"
3. Subjective method
	1. assign by judgment
	2. World Cup was a wager where they assigned probability but it was subjective
		1. estimated $4-5 billion wagered, but hard to measure the exact amount
	3. We all live in a world with incomplete information and this method could be the best way to go


---
#### Event
A collection of sample points

#### Probability of any event
Equal to the sum of the probabilities of the sample points in the event

If we can identify all the sample points of an experiment and can assign a probability to each, we can compute the probability of an event.

A lot of cases, we can't identify all the sample points.  If so, we can't use this approach.

Probability is very practical, but the real world is messy.

#### Basic Relationships of Probability

Some ways to compute the probability of an event without knowledge of all sample points

1. Compliment of an Event
	1. All events NOT in A
	2. Venn Diagram
	3. $A^{\complement}$
2. Union of Two Events
	1. Two events together is a new event
	2. $A \cup B$
3. Intersection of Two Events
	1. $A \cap B$
	2. Addition law
		1. Way to compute probability of event A, or B, or both A and B occurring
		2. $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
4. Mutually Exclusive Events
	1. Event A and B are not touching (in intersection of 2 events, they ARE touching)
	2. When one event occurs, the other can NOT occur
	3. $P(A \cup B) = P(A) + P(B)$
		1. Same as addition law BUT drops the $- P(A \cap B)$

#### Conditional Probability
Probability of an event given that another event has occurred 

A conditional probability is computed as follows:

$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$

This a ratio or fraction

Remember $P(A \cap B)$ is the intersection

#### Example:
Is a son/daughters attending university related to the father's attending university?

Researchers went out and collected data.  

##### Data
$f_c$ = father attended college
$f_n$ = father did NOT attend college

|        | $S_c$ (Son Attended) | $S_n$ (Son did not attend) | Total        |
| ------ | -------------------- | -------------------------- | ------------ |
| $f_c$  | 22                   | 12                         | 34           |
| $f_n$  | 35                   | 31                         | 66           |
| Total: | 57                   | 43                         | 100 families |

A good way to answer this question: 

Recipe: $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$

$P(S_{c} \mid F_{c}) = \frac{P(S_{c} \cap F_{c})}{P(F_{c})}$

$P(S_{c} \mid F_{n}) = \frac{P(S_{c} \cap F_{n})}{P(F_{n})}$

Urn example:  Fill urn with 100 marbles, they're the same BUT label them $F_c$ $F_n$ $S_c$ $S_n$

n = 100

$S_cFc$ = 22
$S_nF_c$ = 12
$S_cF_n$ = 35
$S_nF_n$ = 31

$P(S_{c} \mid F_{c}) = \frac{P(S_{c} \cap F_{c})}{P(F_{c})}$

What the will the fraction will be?

P(S_{c} \cap F_{c}) = 22 out of 100
$P(F_{c})$ = 34

$\frac{P(S_{c} \cap F_{c})}{P(F_{c})} = \frac{22/100}{\frac{34}{100}}$ = 0.647

$P(S_c|F_n)$ = $\frac{P(S_{c} \cap F_{n})}{P(F_{n})}$ = (35/100) / (66/100) = 0.530

##### Interpretation or "The Point"?
Since P($S_c$|$F_c$) > P($S_c$|$F_n$) -- i.e., since 0.6471 > 0.5303 
The evidence is consistent with there being a relationship between the **son attending** and the **father attending** 

Statistics is more interested in correlation and how these are related together.

Edward Deming (6 Sigma father)
> In God we trust, in all others, they must bring data

### Multiplication Law
$P(A \cap B) = P(A) P(B \mid A)$

### Independent Events
If the probability of event A is not changed by the existence of event B, we would say that events A and B are independent

$P(A|B) = P(A)$
$P(B|A) = P(B)$

Example:
Get cautious going into MTA subway or bus (cold and flu season).  Going into the subway, I avoid folks with cold and flu.  What if I think people with blue eyes are more likely to pass along flu and I won't sit next to them.  Eye color and the ability to pass flu, these are independent.  One doesn't have anything to do with the other.  (A silly example of independent events)

### Multiplication Law of Independent Events
$P(A \cap B) = P(A)P(B)$

( P(A|B) = $P(A \cap B)$ / P(B) ) * P(B) --> $P(A \cap B) = P(A|B)P(B)$

Multiplication Law has 2 expressions (the one above) and this one:

Independent Events 
2 events are independent if 

P(A|B) = P(A)
P(B|A) = P(B)

Then A & B are independent --> A || B

2nd Law

If A || B then

$P(A \cap B) = P(A|B)P(B)$, then: 
$P(A \cap B) = P(A)P(B)$

#### Example
Suppose there's a community (Edison, NJ for example), it's known 84% of the households subscribe to the daily edition of the local paper.  It's also know, of those that take the daily, 75% take the Sunday paper.  Question:  If we randomly sample a household in this community, what is the probability they subscribe to both the daily and the Sunday?

Steps
1. Define events
	1. Event D: household subscribes to the daily edition
	2. Event S: household subscribes to the Sunday edition
2. Assign probabilities
	1. P(D) = 0.84
	2. P(S|D) = 0.75  <-- NOTE that those who take the DAILY take Sunday
3. Apply Multiplication Law
	1. $P(S \cap D) = P(S|D)P(D)$
	2. = (0.75)(0.84) = 0.63

So 63% of the households take both the daily and Sunday

## Statisticts vs Probability
Statistics: Given the information in your hand, what is in the pail?  (pail + hand open with hand full of marbles)
- the pail is a black box, based on what is in your hand, what is in the pail?

Probability: Given the information in the pail, what is in your hand (pail shows marble, hand is closed)

#### Example
It's known in a service station that customers pay different way.  80% of customers pay by credit card.  Other 20% could be bank cards, cash, or other.  What is the probability that the next 2 customers will both pay with a credit card?

Steps
	1. Define events
		1. Event A: First customer pays with a credit card 
		2. Event B: Second customer pays with a credit card
		3. Event $(A \cap B)$: event both first and second customers pay with a credit card
	2. Assign Probabilities
		1. P(A) = 0.80
		2. P(B) = 0.80
		3. $P(A \cap B)$ = ?
	3. Apply Multiplication Law
		1. $P(A \cap B) = P(A)P(B) = (0.80)(0.80) = 0.64$

Going to Chapter 5 slides

Random Variables
- a numerical description of the outcome of an experiment

#### Example: JSL Appliances
Discrete random variable with a finite number of values:
Let x = number of TVs sold at the store in one day, where x can take on 5 values (0, 1, 2, 3, 4)

#### Discrete Probability Distributions
probability distribution for a random variable describes how probabilities are distributed over the values of the random variable

We can describe a probability distribution with a table, graph, or equation

Probability Distribution function:
$0 <= f(x) <= 1$
$\sum_{x=1}^{\infty} f(x) = 1$

### Discrete Probability Distributions
- Using past data on TV sales
- A tabular representation of the probability distribution for TV sales was developed
- Tables hows "Units Sold", "Number of Days"

f(x) is defining the probability of the values of x

### Discrete Uniform Probability Distribution
simplest example of a disrete probability distribution given by a formula
f(x) = 1/n
n = number of values the random variable may assume

### Expected Value and Variance
- Expected value - Mean
	- average
	- a random varible is a measure of its central location
	- $E(x) = \mu = \sum x f(x)$
	- Mean
		- Get an honest and serious tendency from the data (can ignore outliers)
	- Mode
		- Amount mentioned most frequently
		- What data shows up the most often?
		- Sometimes the dataset will have multiple modes (multi-mode)
		- Frequency of occurence
- Variance
	- summarizes the variability in the values of a random variable
	- $\operatorname{Var}(x) = \sigma^2 = \sum (x - \mu)^2 f(x)$
	- Interested in how the data is distributed around the average
- Standard deviation
	- $\sigma$ is defined as the positive square root of the variance
	- 

Want to calculate the mean from the TV set example:
Going to use:
$E(x) = \mu = \sum x f(x)$
- just add all of x and f(x)
f(x):
0 - .40
1 - .25
2 - .20
3 - .05
4 - .10

See expected value slide:

0 * .4 = 0
1 * .25 = .25
2 * .2 = .4
3 * .05 = .15
4 * .10 = .40
E(x) = 1.20 --> will see about 1.2 TV sets per day

How much variability is there around the data set?
Use this recipe:
$\operatorname{Var}(x) = \sigma^2 = \sum (x - \mu)^2 f(x)$

see variance and standard deviation table on slide 13
Standard deviation of daily sales = 1.2884 TVs (square root of 1.660)

### Binomial Distribution

1. Experiment consists of a sequence of *n* identical trials
2. Two outcomes, *success* and *failure* are possible on each trial
3. The probability of a success, denoted by *p*, does not change from trial to trial
4. The trials are independent

We flip a coin 3 times and get results.
What is the probability in the 3 flips we will have 2 heads and 1 tail?
This is a binomial experiment.  Why?  The 4 properties are all met
- n = 3
- trials are all the same (pick up -> flip)
- two outcomes possible?  Yes (heads, tails)
	- success and failure are arbitrary - heads = success, tails = failure
- probability of success doesn't change, denoted by p, 
- Slide 16 has the function
### Poisson Distribution
- distributed random variable is often useful in estimating the number of occurrences over a *specified interval of time or space*
- It is a discrete random variable that may assume and *infinite sequence of values* (x = 0, 1, 2, ...)
### Hypergeometric Distribution
related to the binomial distribution
- trials are NOT independent AND
- probably of success changes from trial to trial
- see function on slide 25
- likely not covered in bootcamp, but in fall will run it



This summary organizes the key concepts into five major sections: Foundations, Core Probability Rules, Statistical Concepts, Measures of Central Tendency/Variability, and Specific Distributions.

***


