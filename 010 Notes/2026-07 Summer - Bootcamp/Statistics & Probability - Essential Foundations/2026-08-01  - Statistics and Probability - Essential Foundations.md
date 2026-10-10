---
modified: 2026-08-09T10:27
created: 2026-07-17T21:34
---

---
## 2026-08-01 
###### 07:33am
---
# Note Meta
## Agenda

## Tags

- #statistics
- #probability
- #distributions
- #discreteDistribution
- #normalDistribution
- #binomialDistribution
- #expectedValue
- #variance
- #standardDeviation
- #howTo

## Summary

### I. Core Concepts & Distributions

*   **Random Variable:** A numerical description of an experiment's outcome.
*   **Probability Distribution:** Describes how probabilities are distributed over the possible values of a random variable ($f(x)$).
    *   **Key Rules:** For any distribution, $0 \leq f(x) \leq 1$, and the sum of all probabilities must equal 1 ($\sum f(x) = 1$).

### II. Discrete Probability Distributions (Countable Outcomes)

These distributions deal with countable outcomes (e.g., number of units sold).
*   **Measures of Central Tendency:**
    *   **Expected Value ($E[x]$ or $\mu$):** The weighted average; the theoretical mean outcome ($\sum x f(x)$).
    *   **Mode:** The value that occurs most frequently.
*   **Measures of Variability:**
    *   **Variance ($\operatorname{Var}(x)$ or $\sigma^2$):** Measures how spread out the data is around the mean ($\sum (x - \mu)^2 f(x)$).
    *   **Standard Deviation ($\sigma$):** The positive square root of the variance, returning variability to the original units.

#### 🎯 Binomial Distribution
Used when a problem meets four specific criteria:
1.  Fixed number ($n$) of identical trials.
2.  Only two outcomes per trial ("success" or "failure").
3.  Constant probability of success ($p$) for every trial.
4.  Trials are independent (no memory between trials).

### III. Continuous Probability Distributions (Measurable Outcomes)

These distributions deal with variables that can take any value within an interval (e.g., height, temperature).
*   **Probability Density Function (PDF):** Since a continuous variable cannot have a specific probability, we find the probability of an outcome falling within an **interval** by calculating the **area under the curve**.

#### 📈 Normal Distribution (The Most Important)
This is the standard model for many natural phenomena (heights, test scores).
*   **Characteristics:** It is perfectly symmetric. The mean ($\mu$), median, and mode are all located at the highest point of the curve.
*   **Empirical Rules (68-95-99.7):** These rules relate standard deviations to probability areas:
    *   $\mu \pm 1\sigma$: Contains $\approx 68.26\%$ of values.
    *   $\mu \pm 2\sigma$: Contains $\approx 95.44\%$ of values.
    *   $\mu \pm 3\sigma$: Contains $\approx 99.72\%$ of values.

#### Z-Scores and Standard Normal Distribution
*   **Standardization:** Any normal distribution can be converted to the **Standard Normal Distribution** (where $\mu=0$ and $\sigma=1$). This is done using the $Z$-score formula: $$Z = \frac{X - \mu}{\sigma}$$
*   **Calculating Probability:** Probabilities are found by calculating areas under the curve, typically using statistical software functions.

### IV. Practical Tools (Using R/Software)
Statistical software simplifies these calculations:
*   **Finding Area (Probability):** Use `pnorm(X, mean, standard_deviation)` to find $P(Z < X)$ or $P(X < x)$.
*   **Finding Value (Inverse Probability):** Use `qnorm(Area, mean, standard_deviation)` to find the value ($x$ or $z$) corresponding to a given probability.





## Questions

---
# Notes

## Chapter 5 Review

### Random variable
numerical description of the outcome of an experiment

Experiment - any process that generates well defined outcomes (we can list them and if we can't list them, we can describe them)

## Probability Distribution
for a random variable, describes how probabilities are distributed over the values of the random variable

## Discrete Probability Distribution
probability distribution for a random variable describes how probabilities are distributed over the values of the random variable

We can describe a probability distribution with a table, graph, or equation

Probability Distribution function:
$0 <= f(x) <= 1$
$\sum_{x=1}^{\infty} f(x) = 1$

Example: JSL Appliances

## Distributions 

White board work - Example: JSL Appliances (slide 3, chapter 5 slides)
(See slide 8 for what was done on the white board)

| **Units Sold** | **No of Days** |
| -------------- | -------------- |
| 0              | 80             |
| 1              | 50             |
| 2              | 30             |
| 3              | 10             |
| 4              | 20             |
| Total          | 200            |

Convert to probability distribution:

#### Probability Distribution Table

Using the table above to generate the probability distribution table

| **x** | **$f(x)$**    |
| ----- | ------------- |
| 0     | 0.4 (80/200)  |
| 1     | 0.25 (50/200) |
| 2     | 0.2 (40/200)  |
| 3     | 0.5 (10/200)  |
| 4     | 0.1 (20/200)  |
$f(x)$ = probability function

Remember $0 \leq f(x) \leq 1$ AND $\sum_{x=1}^{\infty} f(x) = 1$

This is one way to do a distribution, but now let's use a picture

### Using a Picture

2nd way to show a distribution 

Height of the bar corresponds with the probability


### Formula or Equation

Third way to show a distribution (3 ways to represent distribution: table, picture, equation)

$f(x) = \frac{1}{n}$   <-- ***the values of the random variable are equally likely***


## Expected Value and Variance

- Expected value - Mean
	- average
	- a random variable is a measure of its central location
	- $E(x) = \mu = \sum x f(x)$
	- Mean
		- Get an honest and serious tendency from the data (can ignore outliers)
	- Mode
		- Amount mentioned most frequently
		- What data shows up the most often?
		- Sometimes the dataset will have multiple modes (multi-mode)
		- Frequency of occurence
- Variance
	- Summarizes the variability in the values of a random variable
	- $\operatorname{Var}(x) = \sigma^2 = \sum (x - \mu)^2 f(x)$
	- Interested in how the data is distributed around the average
- Standard deviation
	- $\sigma$ is defined as the positive square root of the variance


Whiteboard example

JSL continued

| **x** | **$f(x)$**    |
| ----- | ------------- |
| 0     | 0.4 (80/200)  |
| 1     | 0.25 (50/200) |
| 2     | 0.2 (40/200)  |
| 3     | 0.5 (10/200)  |
| 4     | 0.1 (20/200)  |
| Total | 1.00          |

Want to find:
- Expected value $E(x) = \mu = \sum x f(x)$
- Variance $\operatorname{Var}(x) = \sigma^2 = \sum (x - \mu)^2 f(x)$
- Standard deviation $Dev(x) = $+\sqrt{\sigma^2}$
- 

$x*f(x)$ 


| $xf(x)$        | $(x-\mu)$                          | $(x-\mu)^2$ | $(x-\mu)^2*f(x)$                                              |
| -------------- | ---------------------------------- | ----------- | ------------------------------------------------------------- |
| 0.00 (0 * 0.4) | -1.20 (x=0, $\mu$=1.20, so 0-1.20) | 1.44        | 0.5760 *(1.44 * 0.4 (prev column * col 2 in previous table))* |
| 0.25 (1 * 0.2) | -0.2 (x=1, $\mu$=1.20, so 1-1.20)  | 0.04        | 0.01 (0.04 * 0.25)                                            |
| 0.40 (2 * 0.5) | 0.8                                | 0.64        | 0.128 (0.64 * 0.2)                                            |
| 0.15 (...)     | 1.8                                | 3.24        | 0.1620 (0.5 * 3.24)                                           |
| .40 (...)      | 2.8                                | 7.84        | 0.784 (0.1 * 7.84)                                            |
| 1.20           |                                    |             | 1.66                                                          |
Add these up: 1.20
1. $E(x) = \mu = \sum x f(x)$ = **1.20 TV sets** per day
2. $\operatorname{Var}(x) = \sigma^2 = \sum (x - \mu)^2 f(x)$ (add up values) = 1.66 (TV sets)^2
	1. What is this?  What does square TV sets mean?  
3. Standard deviation $Dev(x) = $+\sqrt{\sigma^2}$ = 1.28841 TV Sets <-- NOW this is in units we understand
	1. Might argue this doesn't make much sense in this context of TV sets

How far are is the random variable from the mean?  That's what the squaring is for and capture that deviation.  Take the positive square root of that "brings it back to Earth".  

Did what's on slides 12-13

## Binomial Distribution

*Number of successes* occurring in the $n$ trials
Used on trading options on future contracts.  Used to evaluate values for futures commodities 

Useful if we have a problem that is a binomial experiment.  

### 4 Properties of a Binomial Distribution

Ex: Flip a coin 3 times.  What is the probability that we will have 2 heads and 1 tail.  
See slide 14 for details

1. Must consist of a sequence of identical $n$ number of trials
2. Two outcomes on each trial
	1. Typically "success" and "failure"
	2. Keeping naming consistent for clarity
3. The probability of success is the same from trial to trial to trial
4. Trials are independent
	1. There's no memory between trials (coin doesn't remember last flip for example)

If all conditions above are met, then can use binomial distribution

### 3 Step Template for Binomial Distribution
For problems that may be described as a "binomial experiment"

1. Make sure all four properties are satisfied
	1. Must consist of a sequence of identical $n$ number of trials
	2. Two outcomes on each trial
	3. The probability of success is the same from trial to trial to trial
	4. Trials are independent
2. Define $n, x, p$
	1. $n$ = number of trials
	2. $x$ = number of "successes" in $n$ trials
	3. $p$ = probability of "success" in each trial
3. Find the probability 
	1. 3 ways to find probability
		1. Table 
			1. Not recommended
		2. Use the probability function $f(x)$
			1. Not recommended because we have software that can do this for us
		3. Use R

### The probability function 
(just so we can see it)

$f(x) = P(x|n,p) = \binom{n}{k} p^k (1-p)^{n-k}$

(3 2)(.05)^2 = (3)(0.5)^2(.05) = 0.3750
(3 2) = $3!/((2!)(3-2))$ = 3

## Using R

Write:
dbinom() has 3 arguments.  

> dbinom(x, n, p)

\> dbinom(2, 3, 0.5)
on TI89: binomPdf(n,p,x) so binomPdf(3, 0.5, 2)

Want to use R Studio.  Basic R is error prone and Studio will make it easier.  

How to show the entire distribution in R Studio? 

How many "heads" can we get in 3 flips.  We could get s = { 0, 1, 2, 3 }
The distribution should reflect that

\> dbinom(0:3, 3, 0.50)
Output:
> 0.125 0.375 0.375 0.125

This matches 0, 1, 2, 3 
Chance of 0 heads = 0.125
Chance of 1 and 2 = 0.375
Chance of 3 heads = 0.125

Can sum all the values:
> sum(dbinom(0:3, 3, 0.50))

Output: 1

## Continuous Probability Distributions
Chapter 6, slide 1

- Uniform Probability Distribution
- Normal Probability Distribution
- Exponential Probability Distribution

A ***continuous random variable*** can assume any value in an interval on the real line or in a collection of intervals

It is not possible to talk about the probability of the random variable assuming a particular value

Instead, we talk about the probability of the random variable assuming a value within a given interval 

The probability of the random variable assuming a value within some given interval from $x1$ to $x2$ is defined to the *area under the graph* of the *probability density function* between x1 and x2

## Normal Probability Distribution

Most important distribution for describing a continuous random variable 

Example: heights of people, scientific experiments, test scores, amounts of rainfall

## Normal Probability Distribution

$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$

Characteristics 
The distribution is *symmetric* 
Its skewness measure is zero

The *highest point* on the normal curve is at the <u>mean</u>, which is also the <u>median</u> and <u>mode</u>.

Probabilities for the normal random variable are given by *areas under the curve*. The total area under the curve is 1 (.5 to the left of the mean and .5 to the right)

The standard deviation determines the width of the curve:  larger values result in wider, flatter curves  (slide 14)

For any Normal Probability Distribution
- 68.26% of values of a normal random variable are within +/- 1 standard deviation of its mean
	- this cuts off an interval under the curve
	- This will be 68.26 of the values will be in this area
- 95.44% of values of a normal random variable are within +/- 2 standard deviations of its mean
- 99.72% of values of a normal random variable are within +/- 3 standard deviations of its mean

6-Sigma (+/- 6 standard deviations) - manufacturing settings, an error rate that is hardly ever happens.  Above, we're at 3-Sigma!

A random variable having a normal distribution with a mean of 0 and a standard deviation of 1 is said to have a *standard normal probability distribution*
mean = 0
standard deviation = 1

This is the **Standard Normal Probability Distribution**

The letter $z$ is used to designate the standard normal random variable (no longer called $x$)
- If you hear "z score" this is a standard normal probability distribution

Converting to the standard normal distribution (convert x to z)![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFkAAAArCAYAAAAT4SRlAAAAdklEQVRoQ+3SQQ0AAAgDMfBvGhXcqzWw5LId3u37AiIXPDkgckDkgMgBkQMiB0QOiBwQOSByQOSAyAGRAyIHRA6IHBA5IHJA5IDIAZEDIgdEDogcEDkgckDkgMgBkQMiB0QOiBwQOSByQOSAyAGRAyIHRA6IHDhjfAAs+b1WQQAAAABJRU5ErkJggg==)
$Z = \frac{X - \mu}{\sigma}$

Example:

1. p(z < -0.85)
	1. What is the probability that z will fall in this curve?

R Studio

pnorm(z, mean, standard deviation)

\> pnorm(-0.85, 0, 1))
= 0.1976625 <-- area that z < -0.85

Suppose we want to find:
1. What is the probability p(z > 0.85) = ?
	1. 1 - 0.1976625 ? = 0.802338?  

Using R:

\> 1 - pnorm(-0.85, 0, 1) = 0.8023

Second way:

Introduce a 4th argument
\> pnorm(-0.85, 0, 1, lower.tail=FALSE)

Same answer as first approach

What is the probability that z is between 0.53 and 2.42
p(0.53 < z < 2.42)

\> pnorm(2.42, 0, 1) calculate up to right side, but need to subtract the left side:
\> pnorm(2.42, 0, 1) - pnorm(0.53, 0, 1) = 0.2902957

Find a value for z such that the probability of a larger value is 0.025
1 - 0.025 = 0.975

What is the value of z = ?

qnorm(right hand side, mean, 1)
\> qnorm(0.025, 0, 1, lower.tail=FALSE) = 1.959964

ti89, qnorm is "invNorm(area, mu, sigma)" - you get negative value and you need to take the abs() for this question to get a positive number (to get the right side, the left side will be negative)

Ex: IQ scores are normally distributed with a mean of $\mu=100$ and standard deviation of $\sigma=15$
1. What is the probability p(x<95)?
	1. (not we're working with x and NOT z since we're no longer working with a standard deviation).  Standard deviation is 1, but in this problem it's 15! 
	2. x = 95, find the area of the curve below 95
		1. pnorm(95, 100, 15) = 0.3694413
2. p(x>110)?
	1. pnorm(110, 100, 15, lower.tail=FALSE) = 0.2524925
	2. could do: 1 - pnorm(110, 100, 15) = 0.2525
3. p(90 <= x <= 110) 
	1. pnorm(110, 100, 15) - pnorm(90, 100, 15) = 0.4950 (almost half of the people have an IQ in this range)
4. What test score places a person in the upper 2%?
	1. how do we find x?
	2. \> qnorm(0.02, 100, 15, lower.tail=FALSE) = 130.8062
	3. so x = 131





This review covers fundamental concepts in probability theory, focusing on how probabilities are modeled using both discrete and continuous distributions.

***

