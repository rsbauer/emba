---
modified: 2026-10-09T17:46
created: 2026-07-17T21:34
---

---
## 2026-10-03 
###### 08:24am
---
# Note Meta
## Agenda
- Chapter 5
	- Random variables
	- Discrete probability distributions
	- Expected Value and Variance
	- Binomial distribution
	- Poisson distribution
	- Hypergeometric distribution

## Tasks

- [x] Question to think about over the week ✅ 2026-10-07

## Tags
- #probability
- #statistics
- #randomVariable
- #discreteDistribution
- #binomial
- #hypergeometric
- #expectedValue
- #variance
- #studyNotes


## Summary

## I. Core Concepts & Definitions
*   **Experiment:** A process that generates well-defined outcomes (e.g., flipping a coin).
*   **Sample Space:** The set of all possible outcomes of an experiment.
*   **Random Variable (RV):** A numerical description assigned to the outcome of an experiment.
    *   **Discrete RV:** Can only take on a finite or countable number of values (e.g., number of TVs sold: 0, 1, 2, 3...).
    *   **Continuous RV:** Can take any value within an interval (not covered in detail here).
*   **Probability Distribution:** A function ($f(x)$) that describes the probability for every possible value of a discrete random variable.
    *   **Conditions:** $0 \leq f(x) \leq 1$ and $\sum f(x) = 1$.

## II. Measures of Central Tendency & Variability
These formulas apply generally to any discrete distribution:

| Measure | Symbol | Formula | Meaning |
| :--- | :--- | :--- | :--- |
| **Expected Value (Mean)** | $\mu$ | $\mu = \sum xf(x)$ | The average or central location of the data. |
| **Variance** | $\sigma^2$ | $\sigma^2 = \sum (x-\mu)^2 f(x)$ | Measures how spread out the values are. |
| **Standard Deviation** | $\sigma$ | $\sigma = \sqrt{\text{Var}(x)}$ | The positive square root of the variance, measured in the original units. |

## III. Key Probability Distributions (Formulas & Rules)

### 1. Discrete Uniform Distribution
*   **When to Use:** When every outcome is equally likely.
*   **Formula:** $f(x) = \frac{1}{n}$ (where $n$ is the total number of outcomes).

### 2. Binomial Distribution
*   **Concept:** Used for a fixed number ($n$) of independent trials, where each trial has only two possible outcomes (Success/Failure), and the probability of success ($p$) remains constant.
*   **Crucial Check:** Must satisfy all four properties:
    1. Fixed number of identical trials ($n$).
    2. Only two outcomes (Success or Failure).
    3. Constant probability of success ($p$) for every trial.
    4. Trials are independent.
*   **Probability Formula:** $$P(X=x) = \binom{n}{x} p^x(1-p)^{n-x}$$
*   **R Functions:**
    *   Exact Probability: `dbinom(x, size, prob)`
    *   Cumulative Probability ($\leq x$): `pbinom(q, size, prob)`
*   **Tip for "At Least":** Use the complement rule. $P(X \geq k) = 1 - P(X < k)$.

### 3. Hypergeometric Distribution
*   **Concept:** Used when sampling **without replacement**. The probability of success changes on each draw because the population size decreases and the number of successes/failures changes (e.g., drawing marbles from an urn).
*   **Crucial Distinction:** Trials are **NOT independent**, unlike the Binomial distribution.
*   **Formula:** $$P(X=x) = \frac{\binom{r}{x} \binom{N-r}{n-x}}{\binom{N}{n}}$$
    *   $N$: Total population size (Total items).
    *   $n$: Sample size (Items drawn).
    *   $r$: Number of successes in the total population.
    *   $x$: Number of observed successes in the sample.
*   **R Function:** `dhyper(x, r, N-r, n)`

***
### 💡 Summary Comparison Table

| Feature | Binomial Distribution | Hypergeometric Distribution |
| :--- | :--- | :--- |
| **Sampling Method** | With Replacement (or infinite population) | Without Replacement |
| **Independence** | Yes (Trials are independent) | No (Trials are dependent) |
| **Probability ($p$)** | Constant throughout all trials | Changes with every draw |
| **Key Use Case** | Coin flips, quality control checks | Drawing cards, selecting marbles from an urn |

## Questions


---
# Notes

Exam on chapters 4, 5, 6

# Chapter 5 Discrete Probability Distributions

**Experiment** - generate well defined outcomes ("well defined" = we can list all the outcomes)

**Sample space** - set of all possible outcomes


## Random Variables

*Random variable* is a numerical description of the outcome of an experiment

*Discrete random variable* may assume either a finite number of values or an infinite sequence of values

*Continuous random variable* may assume any numerical value in an interval or collection of intervals

### Example: JSL Appliances

Discrete random variable with a **finite** number of values

Let x = number of TVs sold at the store in one day, where x can take on 5 values (0, 1, 2, 3, 4)


## Discrete Probability Distributions

The *probability distribution* for a random variable describes how probabilities are distributed over the values of the random variable

We can describe a discrete probability distribution with a table, graph, or equation

The probability distribution is defined by a *probability function* denoted by $f(x)$, which provides the probability for each value of the random variable

The required conditions for a discrete probability function are:

$0 <= f(x) <= 1$ 

$\sum f(x) = 1$

(slides show $f(x) >= 0$ which isn't the full story)

### Ex: JSL Appliances

Let **x** be the number of TVs sold at JSL per day

| Units Sold | Num Days |
| ---------- | -------- |
| 0          | 80       |
| 1          | 50       |
| 2          | 40       |
| 3          | 10       |
| 4          | 20       |
Over the last 200 days

We can convert this into a probability function 

##### Probability distribution:

$f(x)$ is the **probability function**
The table is the **probability distribution**

| $x$ | $f(x)$ --> | $f(x)$ |
| --- | ---------- | ------ |
| 0   | 80/200     | 0.40   |
| 1   | 50/200     | 0.25   |
| 2   | 40/200     | 0.20   |
| 3   | 10/200     | 0.05   |
| 4   | 20/200     | 0.10   |
### Random Variables

A **random variable** a numerical description of the outcome of an experiment

##### Probability Distribution Graph

![[Screenshot 2026-10-03 at 8.58.52 AM.png]]

### Discrete Uniform Probability Distribution

The **discrete uniform probability distribution** is the simplest example of a discrete probability distribution given by a formula

$f(x) = 1/n$

## Expected Value and Variance

The **expected value** or mean, of a random variable is a measure of its central location

$\sum (x) = \mu = \sum xf(x)$

Basically, the data in the middle

The **variance** summarizes the variability in the values of a random variable

$Var(x) = \sigma ^2 = \sum (x-\mu)^2f(x)$

The **standard deviation** $\sigma$ is defined as the positive square root of the variance


## Binomial Distribution

This will help with the exam questions

### Four Properties of Binomial Experiment
1. The experiment consists of a sequence of n identical trials
2. Two outcomes, **success** and **failure**, are possible on each trial
3. The probability of a success, denoted by $p$, does not change from trial to trial
4. The trials are independent


#### Example

Flip a coin 3 times
What is the probability there will be 2 heads and 1 tail

What's really going on here? Run the question through the 4 properties above. If yes for all 4 above, then it's a binomial distribution

1. A sequence of $n$ identical trials. The $n$ here would be 3 for the 3 trials.  
2. Only 2 outcomes - yes (heads or tails)
3. Does $p$ change from trial to trial? No, it stays the same here
4. Trials independent? Yes

```
dbinom(x, size, prob)
pbinom(q, size, prob)
```

Calculate EXACT probability
`dbinom(x, size, prob)`, x = num successes, size = trials, prob = probability of success

Calculate cumulative probability
`pbinom(q, size, prob)`, q = num successes, size = trials, prob = probability of success

### 3 Step Template for Potential Binomial Problems

1. Confirm that the all 4 properties of the binomial experiment are satisfied (or met). If so, go to 2
2. Define the following:
	1. $n$ = number of trials
	2. $x$ = number of successes
	3. $p$ = probability of success on each trial
3. Find the probability (the answer to the question)

So...
$n = 3$ 
$x = 2$
$p = 0.5$

#### 3 ways to do this

1. Look up in a table the probabilities
2. Use probability function $f(x) = \binom{n}{x} p^x(1-p)^{n-x}$
3. Use R

#### Using R

`dbinom(x, size, prob)   # as seen in R Studio` 
OR
`dbinom(x, n, p)   # as seen in class`

$f(x) = \binom{3}{2} 0.5^2(1-0.5)^{3-2}$

Remember: $\binom{3}{2} = \frac{3!}{2! 1!} = 3$

OR

`dbinom(2, 3, 0.5)` = 0.375

### Another Question

What is the probability there will be at least 1 head in 3 tosses

$p(x >= 1) = p(x = 1) + p(x = 2) + p(x = 3)$

`dbinom(1, 3, 0.5) + dbinom(2, 3, 0.5) + dbinom(3, 3, 0.5) = 0.8750`

Another way to write this:

`sum(dbinom(1:3, 3, 0.5)) = 0.875`

Another way to do this:

`1 - dbinom(0, 3, 0.5) = 0.875`

## Poisson Distribution

Not going to get into this, "it's not helpful to us"

## Hypergeometric Distribution

Slide 24

The **hypergeometric distribution** is closely related to the binomial distribution.

However, for the hypergeometric distribution:
- Trials are not independent and
- the probability of success changes from trail to trail

$f(x) = \frac{\binom{r}{x} \binom{N-r}{n-x}}{\binom{N}{n}}$ 

for $0 \leq x \leq r$

### Example: Urn and Marbles

An urn contains 5 marbles and the marbles are colored: 3 black, 2 white

If we select 3 marbles, what is the probability we will have 2 blacks an 1 white?

First: 
Define 'black' as 'Success', 'White' as 'Failure'

#### Method 1: Brute Force

List all possible "triples" (taking 3 marbles)

Identify members: { $B_1$, $B_2$, $B_3$, $W_1$, $W_2$ }

Create a table of all possible outcomes.  
10 outcomes, 6 match our question of 3 black, 2 white, so:

$(1/10)*6 = 0.60$
Can give answer in % or decimal

#### Method 2: Use the Probability Function $f(x)$

This method will help us write the R code

$\huge f(x) = \frac{\binom{r}{x} \binom{N-r}{n-x}}{\binom{N}{n}}$ 

$N$ = population size (everyone/everything)
$n$ = sample size 
$r$ = number of successes to begin with
$x$ = successes

N = 5 (population size)
n = 3 (took out in our hand)
r = 3 (black marbles in the urn, number of successes in the urn)
x = 2 (black marbles in our hand)

$\huge f(x) = \frac{\binom{3}{2} \binom{5-3}{3-2}}{\binom{5}{3}} = \frac{\binom{3}{2} \binom{2}{1}}{\binom{5}{3}} = \frac{3*2}{10} = \frac{6}{10} = 0.60$

##### Remember: Combination Definition

$\binom{N}{n} = \frac{N!}{n!(N-n)!}$  


#### Method 3: Use R

R shows dhyper vars as `dhyper(x, m, n, k)`

`dhyper(x, r, N-r, n)`

`dhyper(2, 3, 2, 3) = 0.60`

r and N-R represents the population and one part success and one part failure


### Question to think about over the week

Draw 5 cards from a deck of 52
1. What is the probability of a **pair of aces**?
2. What is the probability of **1 ace**?
3. What is the probability of **no aces**?
4. What is the probability of **at least one ace**?



