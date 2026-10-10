---
modified: 2026-10-10T11:06
created: 2026-07-17T21:34
---

---
## 2026-10-10 
###### 06:22am
---
# Note Meta

## Tasks

- [ ] Exam 📅 2026-10-31 
## Agenda

## Tags
* #statistics
* #probability
* #normalDistribution
* #standardNormal
* #continuousVariable
* #studyNotes

## Summary

## Questions


---
# Notes

# dhyper Review

dhyper(x, r, N-r, n) <-- r and N are the composition, n = sample size, x = number of successes

dhyper(x, 3, 2, ?)  <-- 3+2 should equal our big N (the total) so this is 5 and we have 5 marbles in the urn

dhyper(2, 3, 2, 3)   - x = 2 is the number of successes, and the last 3 is the number of chances

# Exam

- You can check yourself, the correct answer is in the list
- "Exams can be learning opportunities"
- We need to read the book since class has been compressed from 15 weeks to 11
- Read the sections in the book that we've been asked to read
- Exam due: Get it in whenever. Get it in before the end of the month (October)
	- Will be starting new material soon and don't want to worry about the old material while learning new material
- Send these in by email. Just copy and paste and email.
- Will acknowledge the exam has been received and when the last exam has been sent in, then the answer key will be sent

# Continuous Probability Distributions - Chapter 6

> The material today will complete the material on the exam

Quiz today. More time will be given. Will be interpretting a normal probability distribution. This will be the last of the PDF slides. Chapters 8-10+ will be statistics. Need to get probability situated first before getting into statistics.

- Uniform probability distribution
- Normal probability distribution
- Exponential probability distribution

- A **continuous random variable** can assume any value in an interval on the real line or in a collection of intervals
- it is not possible to talk about the probability of the random variable assuming a particular value
- Instead, we talk about the probability...

Calculate the area under the curve between $x_1$ and $x_2$. We can do it by hand, but we'll use R

- The probability of the random variable assuming a value within some given interval from $x_1$ to $x_2$ is defined to be the **area under the graph** of the **probability density function** between $x_1$ and $x_2$

## Normal Probability Distribution
- The **normal probability distribution** is the most important distribution for describing continuous probability...

Used to find: heights of people, scientific measurements, test scores, amounts of rainfall

- Normal probability density function:

## Characteristics 

- **highest point** on the curve is the **mean**
- Total area under the curve is 1 (.5 to the left of the mean and .5 to the right)

Mean = $\mu$
Standard deviation = $\sigma$

### 3 Characteristics
- Share same shape
- Interested in the mean
- Measurement of the spread (how are the values are distributed around the central tendency 

- Standard deviation determines the width of the curve: larger values result in wider, flatter curves

Slide 13

- The mean can be any numeric value: negative, zero, or positive
- **68.26%** of values of a normal random variable are within **+/- 1 standard deviation** of its mean
	- slide 17
	- $\mu-1\sigma$ and $\mu+1\sigma$
- **95.44%** of values of a normal random variable are within **+/- 2 standard deviations** of its mean
- **99.72%** of values of a normal random variable are within **+/- 3 standard deviations** of its mean

## Standard Normal Probability Distribution

A random variable having a normal distribution with a mean of 0 and a standard deviation of 1 is said to have a **standard normal probability distribution**
$\sigma = 1$
The letter $z$ is used to designate the standard normal random variable
"What is the $z$ score?" - this is what is being referenced (not x)

Converting to the standard normal distribution:

$z = \frac{x-\mu}{\sigma}$

Think of z as a measure of the number of standard deviations x is from $\mu$

Switched to using R
- What is the probability that z is less than 0.85?
	- $P(z < -0.85)$ ?
	- `pnorm(-0.85)` = 0.1977
	- `pnorm(-0.85, 0, 1)` <-- 0 = mean, 1 = deviation

To graph in R Studio?
```
curve(dnorm(x, mean = 0, sd = 1), from = -4, to = 4, main = "Normal Distribution AUC")
x_vals <- seq(-4, -0.85, length.out = 100)
y_vals <- dnorm(x_vals)
polygon(c(-4, x_vals, -0.85), c(0, y_vals, 0), col = "skyblue")
```
![[Screenshot 2026-10-10 at 9.24.12 AM.png|287]]

- What is the probability that z will be greater than -0.85?
	- $P(z>-0.85)$
	- `1 - pnorm(-0.85, 0, 1)` = 0.8023
	- `pnorm(-0.85, 0, 1, lower.tail = FALSE)` = 0.80233 <-- same as above, but without the -1
		- This tells R to give the upper tail


- $P(0.53 < z < 2.42)$ ?
	- subtract $P(z > 0.53)$ from $P(z < 2.42)$
		- $P(z < 2.42) = 0.9922$
			- `pnorm(2.42, 0, 1)` = 0.9922
		- $P(z > 0.53)$
			- `pnorm(0.53, 0, 1)`? = 0.7019
		- Can we answer? No. 
			- We need to subtract: `0.9922 - 0.7019 = 0.2903`
	- With R
		- `pnorm(2.42,0,1) - pnorm(0.53,0,1)` = 0.2903
		- or?
		- `diff(pnorm(c(0.53, 2.42)))` = 0.2903
- 1 standard deviation:
	- `pnorm(1,0,1) - pnorm(-1,0,1)` = 0.6827
- 2 standard
	- `> pnorm(2,0,1) - pnorm(-2,0,1)` = 0.9545
- 3 standard
	- `> pnorm(3,0,1) - pnorm(-3,0,1)` = 0.9973

- What value of z cuts off an area of 0.025 in the upper tail of the std normal?
	- `qnorm(0.025, 0, 1, lower.tail=FALSE)` = 1.96
	- other side is 0.975 (1 - 0.025 = 0.975)
	- Can do `qnorm(0.025, 0, 1)` minus the lower.tail=FALSE to get the left side OR
	- `qnorm(1 - 0.025, 0, 1)` seemed to work too
- pnorm = area under the curve
- qnorm = value of z for the given area

A lot of problems for the chapter.  So practice practice practice

- Example: average male is 5'9" tall (or 69") with a standard deviation is 3" $\sigma = 3$.  
	- $\mu = 69$
	- $\sigma = 3$
	- What's the probability that a randomly sampled male will have a height of 6' or more? (72")
		- Or what proportion of American males have a height of 72" or more?
		- $P(x > 72)$
		- `1 - pnorm(72, 69, 3)` = 0.1587
			- pnorm(x, $\mu$, $\sigma$)`
- What's the probability are less than 60"?
	- `pnorm(60, 69, 3)` = 0.0013
- What's the probability of an adult male who's height is between 5'6" and 5'10"
	- 66 = 5'6" and 70 = 5'10"
	- `pnorm(70, 69, 3) - pnorm(66, 69,3)` = 0.4719 ?
- What height places you in the upper 1% (qnorm)
	- `qnorm(0.01, 69, 3, lower.tail=FALSE)` = 75.9790 inches
		- can do `qnorm(0.99, 69, 3)` where 1 - 0.01 = 0.99
		- 
- 


