---
modified: 2026-09-26T07:57
created: 2026-07-17T21:34
---
# Statistics and Probability: Essential Foundations
## Instructor: Professor Robert Stinerock

> In these sessions, Professor Stinerock covers key concepts in statistics and probability that students will rely on in their credit-bearing courses. The sessions are designed for students who are new to statistics and probability, as well as for those who have studied the material before and would benefit from a focused refresher. For all students, the sessions help establish a shared foundation for the Fall 2026 semester.

##### Dates: Saturdays, July 18 and 25, and August 1
##### Time: 8:15 am – 12:30 pm, with 15-minute breaks at 9:45 am and 11:15 am
##### Zoom Link:
https://baruch.zoom.us/j/84119454158?pwd=YfRalVtpSg4B4bQET78EmxSm1ObH28.1
Meeting ID: 841 1945 4158
Passcode: 927970

---
## 2026-07-18 
###### 08:09am
---

# Table of Contents
- [[#Instructor: Professor Robert Stinerock|Instructor: Professor Robert Stinerock]]
			- [[#Dates: Saturdays, July 18 and 25, and August 1|Dates: Saturdays, July 18 and 25, and August 1]]
			- [[#Time: 8:15 am – 12:30 pm, with 15-minute breaks at 9:45 am and 11:15 am|Time: 8:15 am – 12:30 pm, with 15-minute breaks at 9:45 am and 11:15 am]]
			- [[#Zoom Link:|Zoom Link:]]
- [[#2026-07-18|2026-07-18]]
				- [[#Zoom Link:#08:09am|08:09am]]
		- [[#Agenda|Agenda]]
		- [[#Tags|Tags]]
		- [[#Summary|Summary]]
	- [[#2026-07-18#🗓️ I. Bootcamp Logistics & Schedule|🗓️ I. Bootcamp Logistics & Schedule]]
	- [[#2026-07-18#💻 II. Tools and Preparation|💻 II. Tools and Preparation]]
	- [[#2026-07-18#📊 III. Core Probability Concepts|📊 III. Core Probability Concepts]]
		- [[#📊 III. Core Probability Concepts#A. Counting Rules (Counting Outcomes)|A. Counting Rules (Counting Outcomes)]]
		- [[#📊 III. Core Probability Concepts#B. Assigning Probabilities to Events|B. Assigning Probabilities to Events]]
		- [[#📊 III. Core Probability Concepts#C. Basic Probability Relationships|C. Basic Probability Relationships]]
- [[#Key Takeaways|Key Takeaways]]
- [[#Explained like I'm 5|Explained like I'm 5]]
	- [[#Explained like I'm 5#🎲 What is Probability? (How Likely?)|🎲 What is Probability? (How Likely?)]]
	- [[#Explained like I'm 5#🧸 Counting All the Ways (Outcomes)|🧸 Counting All the Ways (Outcomes)]]
	- [[#Explained like I'm 5#✨ Finding Chances (Rules for Events)|✨ Finding Chances (Rules for Events)]]
	- [[#Explained like I'm 5#💡 Quick Summary:|💡 Quick Summary:]]
		- [[#💡 Quick Summary:#Questions|Questions]]
- [[#Agenda|Agenda]]
- [[#Experiments, counting rules, assigning probabilities|Experiments, counting rules, assigning probabilities]]
	- [[#Experiments, counting rules, assigning probabilities#Sample space|Sample space]]
- [[#Counting Rule for Multi-Step Experiments|Counting Rule for Multi-Step Experiments]]
- [[#Counting rule for combinations|Counting rule for combinations]]
- [[#Counting rule for permutations|Counting rule for permutations]]
- [[#Assigning probabilities to experimental outcomes|Assigning probabilities to experimental outcomes]]
	- [[#Assigning probabilities to experimental outcomes#Classical Method|Classical Method]]
	- [[#Assigning probabilities to experimental outcomes#Relative Frequency Method|Relative Frequency Method]]
	- [[#Assigning probabilities to experimental outcomes#Subjective Method|Subjective Method]]
	- [[#Assigning probabilities to experimental outcomes#Events and their Probabilties|Events and their Probabilties]]
	- [[#Assigning probabilities to experimental outcomes#Some Basic Relationships of Probability|Some Basic Relationships of Probability]]
	- [[#Assigning probabilities to experimental outcomes#Complement of an Event|Complement of an Event]]
	- [[#Assigning probabilities to experimental outcomes#Union of 2 Events|Union of 2 Events]]
	- [[#Assigning probabilities to experimental outcomes#Intersection of 2 Events|Intersection of 2 Events]]
	- [[#Assigning probabilities to experimental outcomes#Additional Law|Additional Law]]
	- [[#Assigning probabilities to experimental outcomes#Mutually Exclusive Events|Mutually Exclusive Events]]
- [[#Up next|Up next]]

#### Agenda
- How the bootcamp will run
- 
- 

#### Tags
* #probabilityTheory
* #statistics
* #countingRules
* #combinations
* #permutations
* #sampleSpace
* #dataAnalysis
* #rStats
* #lectureNotes

#### Summary
### 🗓️ I. Bootcamp Logistics & Schedule
*   **Format:** The course will run over **3 Saturdays**, held online via Zoom.
*   **Schedule:** Daily from **8:30 AM to 12:30 PM** (4 hours), with scheduled breaks (9:45–10:00 AM and 11:00–11:15 AM).
*   **Support:** There are no formal office hours. Students should send questions via **email** for the best response rate; otherwise, feel free to "yell/shout out" in the Zoom chat.
*   **Content Focus:** The material has been pruned ("less is more") but remains comprehensive. Learning relies heavily on **exercises**.
*   **Pacing Note:** If a concept isn't fully covered during the bootcamp, it will be revisited in the first few classes of the fall term.

### 💻 II. Tools and Preparation
*   **Calculator:** Bring something capable of computation (a phone is fine for today; a dedicated handheld calculator will be needed next week).
*   **Programming Language:** The recommended tool is **R**, as it has a richer statistics library than Python. R Studio is the graphical interface used.
*   **Syllabus/Grading:** Grading includes 2 exams (40%) and daily multiple-choice quizzes (20%). *Note: Do not buy the textbook; the PDF will be provided.*

### 📊 III. Core Probability Concepts
The course focuses on three main areas of probability theory: Counting, Assignment Methods, and Relationships.

#### A. Counting Rules (Counting Outcomes)
*   **Multi-Step Experiments:** The total number of outcomes is found by multiplying the possibilities at each step ($n_1 \times n_2 \times ...$).
*   **Combinations (Order Doesn't Matter):** Used when selecting a group where order is irrelevant. Formula: $\binom{N}{n} = \frac{N!}{n!(N-n)!}$.
*   **Permutations (Order Matters):** Used when the sequence of selection is important. Formula: ${}_NP_n = \frac{N!}{(N-n)!}$.

#### B. Assigning Probabilities to Events
Probabilities must meet two rules: $0 \le P(E) \le 1$, and the sum of all probabilities must equal 1. Three methods are used to assign these values:
1.  **Classical Method:** Assumes all outcomes are equally likely (e.g., rolling a standard die).
2.  **Relative Frequency Method:** Based on observable, historical data (Empirical evidence; e.g., calculating purchase rates from test market data).
3.  **Subjective Method:** Used when empirical data is unavailable or unreliable; probabilities are assigned based on expert judgment or degree of belief.

#### C. Basic Probability Relationships
*   **Complement ($A^c$):** The probability that an event *does not* happen. $P(A) + P(A^c) = 1$.
*   **Union ($A \cup B$):** The probability that A **or** B (or both) occurs. General Rule: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
*   **Intersection ($A \cap B$):** The probability that A **and** B occur simultaneously.
*   **Mutually Exclusive Events:** Two events that cannot happen at the same time (their intersection is 0). In this case, $P(A \cup B) = P(A) + P(B)$.

## Key Takeaways

**1. Probability Assignment Depends on Data Availability:**
The method used to assign a probability value must match the information available. If outcomes are equally likely, use the **Classical Method**. If historical data is available (e.g., sales calls), use the **Relative Frequency Method**. If no objective data exists, you must rely on subjective judgment.

**2. Counting Rules Distinguish Order Importance:**
When determining the size of a sample space, it is critical to know if the order of selection matters. Use **Combinations** ($C(N, n)$) when selecting items where the order does *not* matter (e.g., picking 5 cards for poker). Use **Permutations** ($P(N, n)$) when the order *is* important (e.g., assigning a 3-digit lock code).

**3. Probability Relationships Simplify Calculations:**
Instead of listing every possible outcome to find the probability of a complex event, use established relationships. The most common are:
*   **Complement:** $P(A^c) = 1 - P(A)$.
*   **Union (General Addition Rule):** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$, which prevents double-counting the overlapping outcomes.

**4. The Sample Space is the Foundation:**
Every probability calculation must begin by defining the **Sample Space ($S$)**, which represents *all* possible unique outcomes of an experiment. Once the sample space is defined, you can assign probabilities to individual points and then sum them up to find the probability of any specific event (a collection of those sample points).

## Explained like I'm 5

Imagine we are playing a super fun game with toys, and we want to guess what will happen next! All these big words—like probability and outcomes—are just fancy ways of talking about **how likely something is to happen.**

***

### 🎲 What is Probability? (How Likely?)

Probability is just a number that tells us the *chance* of something happening.

*   If the number is **0**, it means it will **never** happen (like raining when you are indoors).
*   If the number is **1**, it means it will **always** happen (like the sun coming up in the morning).
*   If the number is **0.5** (or half), it means it has a **fair chance** of happening, like flipping a coin!

***

### 🧸 Counting All the Ways (Outcomes)

Sometimes we need to count how many different things *could* happen. These are called "outcomes."

**Analogy: Picking Toys**
Let’s say you have two boxes of toys: one with **3 colored blocks** and one with **2 little cars**. If you pick one block AND one car, how many different pairs can you make?

You don't just add them (3 + 2 = 5). You multiply! Because for every single block you pick, you get to pair it with all the cars. So, $3 \times 2 = 6$ different ways!

**The Rule:** When you have to do two things—like picking socks *and* picking a shirt—you always multiply the choices together to find out how many total combinations there are.

***

### ✨ Finding Chances (Rules for Events)

When we talk about chances, we use three main ideas:

**1. The "NOT" Chance (Complement)**
If you know the chance of something happening is 80% (or 0.8), then the chance that it will **NOT** happen is always $1 - 0.8 = 0.2$ (or 20%).
*   *Example:* If your favorite toy truck has a 90% chance of working, its "not working" chance is only 10%.

**2. The "OR" Chance (Union)**
This means something can happen in *this way* **OR** *that way*. When we add these up, we have to be careful not to count the same thing twice!
*   *Example:* If you want a cookie that is either chocolate **OR** peanut butter. You just count all the cookies that fit those groups.

**3. The "AND" Chance (Intersection)**
This means two things must happen *together*. It's like needing to roll a 6 on the dice **AND** having your friend wear blue shoes. Both things have to be true at the same time!

***

### 💡 Quick Summary:

*   **Probability:** How likely something is (a number from 0 to 1).
*   **Counting:** If you do two things, you multiply their choices together.
*   **OR Chance:** Count all ways that fit one thing OR another.
*   **AND Chance:** Both things must happen at the same time!


#### Questions

1. **Distinguishing Counting Principles:** In complex, multi-stage experiments, how can I systematically determine whether the appropriate counting rule is a simple multiplication principle ($n_1 \cdot n_2 \dots$), a permutation ($\text{P}(N, n)$), or a combination ($\text{C}(N, n)$)? Specifically, what conceptual difference dictates whether order matters and whether replacement is allowed?

2. **The Relationship Between Independence and Mutual Exclusivity:** Mathematically, how are the concepts of "independent events" and "mutually exclusive events" differentiated? Can an event be both independent and mutually exclusive (other than the trivial case where $P(A)=0$ or $P(B)=0$), and what does that imply about the structure of the sample space?

3. **Applying Conditional Probability in Practice:** Since Bayes' Theorem was mentioned but skipped, what is the most intuitive approach to understanding conditional probability ($P(A|B)$) using real-world data (e.g., medical testing or market research)? How does this framework fundamentally change how we update our initial degree of belief (subjective probability) when new evidence becomes available?

4. **The Limitations of Probability Assignment:** In a scenario where historical data is unavailable and outcomes are not equally likely, what quantitative methods can be used to transition from pure subjective judgment toward an empirically defensible probability estimate, thereby mitigating cognitive bias in decision-making?

5. **Moving Beyond Discrete Sample Spaces (Continuous Variables):** The current focus relies on counting discrete sample points. When dealing with continuous variables—such as time or temperature—how must the concepts of "sample space," "event," and "probability" be redefined (e.g., moving from summing probabilities to integrating probability density functions)?

6. **Computational Verification:** Given that R is introduced as a primary tool, what are the most efficient ways to use R not just to *calculate* the results of counting rules or basic probability relationships, but also to *simulate* and empirically verify theoretical concepts (like the Law of Large Numbers) to build deeper intuition?

# Notes

32 participants

How the bootcamp will be run.
- Sent out files yesterday + course syllabus
- Send questions in Zoom chat, but may get missed so yell/shout out
- robert.stinerock@baruch.cuny.edu - just call him by "Robert" (no doctor or professor)
- Don't have office hours
	- Send email with questions or topics
	- Sensitive to not wasting time
	- Will respond by email or phone if desired
- 8:30-12:30 (4hrs)
	- breaks: 9:45am-10am, 11am-11:15am
- 3 Saturdays
- Having to meet online - will be using Zoom.  Not the best instruction platform but will work
- Content has been pruned (less is more)
	- Won't see everything that would be seen in the fall term course
	- The material can be bewildering - this is normal
- Best way to teach this material
	- Lots of exercises
	- If you don't get everything in the bootcamp, it'll be covered in the first few classes of the fall term (stats class is the first class of the day typically during the summer)
		- will have seen everything twice
- Video is recorded, but may not be ideal
- Professor is using a finance calculator, HP HF 12C

Reviewed syllabus
- Name, contact info
- Text book listed (don't buy the book) - is the author
	- will get it for free (it'll be the PDF)
- Fall schedule listed
- Evals given
	- 2 exams, 40% of grade
	- 20% end of class, 1 question, multiple choice quizzes reinforcing material covered that day
- Bring something that can do computations
	- phone is ok for today
	- next week: will need a handheld calculator 
	- Ideally: R stats programming package (the other is Python)
		- R has a richer stats library than Python
		- Python has machine learning and AI over R
		- Described on page 3 (in text book?)
		- will use R today to show us
		- R: https://cran.r-project.org
			- Is there R available for iPad?
		- R Studio <-- GUI
		- Using a Mac, there's a youtube video on how to install and use it

Discussion notes (Discussion Notes July 18 2026.pdf)
- Write up of what we're doing today
- Exercises  - go with the fall text book
- Included multiple choice questions
	- Here's a question and some solutions and then the correct solution below(?)

Viewing R, R Studio
- Going to be using the R console
- PDF slides - not instructors, but they do the job - "Slides for July 18 2026.pdf"
	- Chapter 4, Introduction to Probability
	- At end of the course, next week's material will be sent
- Can CoCalc help?

## Agenda
- Experiments, counting rules, assigning probabilities
- Events and their probability
- Basic relationships of probability
- Conditional probability
- Bayes' Theorem - likely won't be able to get to

## Experiments, counting rules, assigning probabilities
- used to model game of chance, gambling
- Could use for market place behavior
- We have to constantly make decisions based on incomplete evidence
- We don't want to over claim, it gives us ways to evaluate degrees of risk
	- What is the likely hood if course A works out versus course B or C
- Probability and statistics, at its best, gives us a way of evaluating the degree of risk we're exposed to when making a decision
- What is probability?
	- A number
	- The numeric measure of the likelyhood of an occurrence
	- 0-1 bound, 0 being low or unlikely, 1 being on the high end and likely
- Experiment
	- any process that generates well defined outcomes
	- process that you can think of generates outcomes
	- Sample space
		- all possible experimental outcomes
	- Experimental outcome is also a sample point

| Experiment           | Outcome                  |
| -------------------- | ------------------------ |
| Toss a coin          | S = { head, tail }       |
| Roll a die           | S = { 1, 2, 3, 4, 5, 6 } |
| Conduct a sales call | S = { sale, no sale }    |
|                      |                          |

### Sample space
- Deck of cards: 52 cards
- Common stock: all possible closing prices at time of close

## Counting Rule for Multi-Step Experiments
- Look at counting rule for multiple step experiments
- Experiment of *k* steps, in which there are *n1* possible results for the first step, *n2* possible results for the second steps, and so on, then the total number of experimental outcomes is given by *(n1)(n2)...(nk)*
$$
(n_1)(n_2)\dots(n_k)
$$
- Tree diagram can be helpful
- Examples
	- An experiment consists of tossing a coin 3 times.  How many experimental outcomes are there?
	- Approaches
		- Using counting rule
		- k steps, n1 results on the first step, n2 for the second step, ...
	- Counting Rule
		- How many steps? 
			- k = 3
		- How many outcomes are there on each step?
			- n1 = 2 (head or tail)
			- n2 = 2
			- n3 = 2
		- Apply counting rule, n1 * n2 * n3 = 8
		- 8 possible experimental outcomes
	- Use a tree diagram
		- step 1, first coin

| step 1: 1st coin | 2nd coin   | 3rd coin          | Sample Space                                                                              |
| ---------------- | ---------- | ----------------- | ----------------------------------------------------------------------------------------- |
| H T              | H T<br>H T | H T<br>H T<br>H T | S + {<br>(HHH),<br>(HHT),<br>(HTH),<br>(HTT),<br>(THH),<br>(THT),<br>(TTH),<br>(TTT)<br>} |
|                  |            |                   |                                                                                           |
		- Matches counting rule above - 8 results
		- 

- Example
	- "Facts"
		- 3 steps
		- 3 results possible on step 1
		- 2 results possible on step 2
		- 4 results possibel on step 3
	- How many experimental outcomes are possible
	- 3 * 2 * 4 = 24 outcomes ?
	- Solve
		- k = 3
		- n1 = 3
		- n2 = 2
		- n3 = 4
		- Counting rule
		- n1 * n2 * n3 
			- 3 * 2 * 4 = 24
	- 

## Counting rule for combinations
- Count the number of experimental outcomes when *n* objects are to be selected from a set of *N* objects
	- note about n vs N
- See expression syntax in PDF
- Whiteboard example given
- ! = factorial
- No of combinations of *N* objects taken *n* at 
	- (N/n) = (N!) / (n! * ((N-n)!)
- Simple experiment
- Example: How many combinations of *N = 3* objects can be taken *n = 2* at a time?
	- Let's say we have a vase and put in 3 marbles (they're identical)
	- Writing all experimental outcomes
	- Reach into vase and stir and grab 2 of the 3 marbles and see what numbers they are. Then we return them to the vase and repeat the process (stir, take out 2 marbles, write down the numbers).  Keep doing this and eventually exhaust possible sample space
	- S = { (1, 2), (1, 3), (2, 3) }
	- 3 outcomes or results
	- *(3 / 3)* NOT a fraction but a combination
	- *( 3 / 2 ) = (3!) / (2! * ((3 - 2)! ))* = *(3 * 2 * 1) / ((2 * 1) * (1))* = *6 / 2* = 3
	- N! = N(N - 1)(N-2) ... (2)(1) = ?
	- n! = n(n-1)(n-2) ... (2)(1) = ?
	- 
- self test
	- How many 5 card poker hands are possible from a deck of 52 cards
		- N = 52, n = 5 ?
		- 2598960
		- Answer
			- N = 52
			- Combination C(N/n)  = C(52/5) = (52 / 5) = 
			- 52! / (5! * ((52-5)!)) = 52! / (5! * ((47)!))
			- on a calculator = 52 * 51 ... 2 * 1 / ((5 * 4 * 3 * 2 * 1) * (57 * 46 * ... 2 * 1) -- can cancel out the (47 * 46 ... 2 * 1) so you get: 52 * 51 * 50 * 49 * 48 / (5 * 4 * 3  * 2 * 1) = 311875200 / 120 = *2598960 different hands of 5 are possible*
			- Switched to R for demo
				- `choose(52,5)`
				- On TI-89: `nCr(52,5)`
	- Department of motor vehicles wants to issue new license plates to 35,000,000 vehicles. They are proposing to use all numbers in 7 positions. Will they have sufficient unique license plates for each vehicle or will they fall short?
		- N = 10
		- n = 7
		- need 35,000,000 unique numbers
		- ~~got 120 but that doesn't seem right~~
		- Answer
			- Which counting rule should we use.  Combination?  But didn't seem to work
			- Counting rule for multiple step
			- k = 7
			- n1 = 10
			- n2 = 10
			- n3 = 10
			- ...
			- n7 = 10
			- apply the rule
				- *10 * 10 * 10 * 10 * 10 * 10 * 10* or 10^7 = 10,000,000
				- Not enough positions to handle 35,000,000
		- What if we add letters?
			- What if we use letters in the first 3 steps
			- n1 = 26, n2 = 26, n3 = 26
			- 26^3 * 10^4 = 175,760,000
			- This would meet the needs for 35,000,000


## Counting rule for permutations
- The order of selection is important
- Count the number of experimental outcomes when *n* objects are to be selected from a set of *N* objects **where the order of selection is important**
- Same as combination except that with permutations... order matters

- Marble example
	- S = { (1,2), (2,1), (1,3), (3,1), (2,3), (3,2) } ==> now have 6 combinations
- Could use counting rule: 
	- Number of permutations of *N objects* taken *n at a time*
	- 

Using 
- P(N,n) = n! (N,n) = n![(N! / (n!((N-n)!)))] = the n! is crossed out (note, this isn't in the slides the n! crossed out).  

$$
{}_NP_n = \frac{N!}{(N-n)!}
$$


- P(n,r) = 
$$
{}_nP_r = \frac{n!}{(n-r)!}
$$

P(3,2) = 3! / (3-2)! = (3 * 2 * 1) / 1 = *6*

## Assigning probabilities to experimental outcomes
- Only 2 rules we need
	1. Outcomes must be between 0 and 1.  General notation: Ei 0 <= (P(Ei) <= 1	
	2. Add them all up:  E P(Ei) = 1
![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGUAAAASCAYAAABCWxC2AAAAQ0lEQVRYR+3TMQ0AAAzDsJU/6dHwESOoFHUXzrhFKYqop4CKAioKqCigooCKAioKqCigooCKAioKqCigooCKAioK6AErEAAT1e7sogAAAABJRU5ErkJggg==)
- 3 methos for how probabilities are assigned
	- Classical Method
		- assign probabilities based on the assumption of equally likely outcomes
	- Relative Frequency Method
		- assigned probabilities on experimental or historical data
	- Subjective Method
		- Assign probabilities based on judgment 
		- can be problematic, but may be all we have

### Classical Method
If an experiment has *n* possible outcomes, this method would assign a probability of *1/n*to each outcome
- Example
	- Roll die
	- Sample space: S = { 1, 2, 3, 4, 5, 6 } 
	- Probabilities: Each sample point has a *1/6* chance of occurring
- Experiment
	- Toss a coin
	- Sample space: S = { head, tail }
	- *New:*  **assigning probabilities to each of these outcomes**
		- Must sum to 1
	- P(heads) = ? 
	- P(tails) = ?
	- So... 
	- *P(heads) = 0.5*, *P(tails) = 0.5* and each are 0 <= 1 and sum up = 1 so both properties satisfy the requirements
	- In the real world, outcomes are not always equal - so go to relative frequency method

### Relative Frequency Method
Grounded in observable world.  Empirically based.  
Product manager issue:  What's the probability customers will buy our new product.  Sales people will call customers to make a potential sale.  
- Experiment: Conduct a sales call on a potential customer
- Sample space: S = { sale, no sale }
- *New:* assign probabilities 
- P(sale) = 
- P(no sale) = 
- We know *P(sale) + P(no sale) = 1*
- 0.5 is the classical approach, but is it realistic?  No
- Can we do better?  yes!  (There are marketing books on it!)
- Product manager decides they want to role this out in a test market to evaluate and has sales people contact 400 customers.  Of the 400 customers, 100 purchase and 300 said no thanks.  
- We have repeated this experiment 400 times.  
- 100 purchased out of 400 = this is our real world data
- *P(sale) = 100/400 = 0.25* ✅
- *P(no sale) = 300/400 = 0.75* ✅
- *0.25 + 0.75 = 1*  ✅✅

### Subjective Method 
The classical and relative frequency methods may fail in certain situations.  And experimental outcomes are not equally likely or the relative frequency data is unavailable or uncollectable.  
- Experiment
	- Observe the outcome of the match between Spain and Argentina in the men's world cup finals tomorrow.  
	- Sample space: S = { Spain wins, Spain loses }
	- Assign probabilities to each of these possibilities
	- P(Spain wins) = 
	- P(Spain loses) =
	- Believed +$5 billion has been waged on this match
	- A lot of game attributes are subjective.  It's all we have to measure.  It's not great, but we have nothing better.
	- The probabilities we assign to anything have to reflect our own degree of belief or conviction.  


### Events and their Probabilties
- Slide 12
- An *event* is a collection of sample points
- The *probability of any event* is equal to the sum of the probabilities of the sample points in the event
- If we can **identify all the sample points** of an experiment and **assign probability to each**, we can compute the probability of the event

Example
- Consider the experiment of rolling a pair (2) dice.  Suppose we're interesterd in the sum of the values (face values) coming up on those two dice.  
- What can happen for any combination of values for the 2 die
	- 

(Taking Die 1 + Die 2 value)

| Die 1 | Die 2: 1 | Die 2: 2 | Die 2: 3 | Die 2: 4 | Die 2: 5 | Die 2: 6 |
| ----- | -------- | -------- | -------- | -------- | -------- | -------- |
| 1     | 2        | 3        | 4        | 5        | 6        | 7        |
| 2     | 3        | 4        | 5        | 6        | 7        | 8        |
| 3     | 4        | 5        | 6        | 7        | 8        | 9        |
| 4     | 5        | 6        | 7        | 8        | 9        | 10       |
| 5     | 6        | 7        | 8        | 9        | 10       | 11       |
| 6     | 7        | 8        | 9        | 10       | 11       | 12       |
|       |          |          |          |          |          |          |

- Questions
	- For this experiment, how many sample points are possible?  
		- S = 36 *(6 * 6)* 
		- use counting rule
		- *k = 2 steps*
		- *n1 = 6
		- *n2 = 6*
		- so *6 * 6 = 36*
	- Write out the sample space for this experiment 
		- S = { 
			- (1,1), (1,2), ... (1,6),
			- (2,1), (2,2), ... (2,6),
			- ...
			- (6,1),(6,2), ... (6,6)
			- }
	- What is the probability of obtaining the value of 7? (Here's where the matrix above comes in handy)
		- 1/6 
		- E7 = { (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) }
		- P(E7) = P(1,6) + P(2,5) + P(3,4) + P(4,3) + P(5,2) + P(6,1)
		- Need to assign probability to each of these outcomes
		- Use classical method here.  We are assuming these outcomes are equally likely and this is fair to look at this
		- P(1,6) = 1/36 so 
		- P(E7) = (1/36) + (1/36) + (1/36) + (1/36) + (1/36) + (1/36) +  = 6(1/36) = 1/6
		- If we played this game, out of 6 times, we'd have a sum of 7
	- What is the probability of obtaining a value of 9 or greater
		- There are 10 pairs
		- (1/36) * 10 = 10/36 = 5/18


### Some Basic Relationships of Probability
- Slide 13
- There are some *basic probability relationships* that can be used to compute the probability of an event without knowledge of all the sample point probabilities
	- Complement of an event
	- Union of 2 events
	- Intersection of 2 events
	- Mutually exclusive events

### Complement of an Event
- The *complement* of an event A is defined to be the event consisting of all sample points that are not in *A*
- The complement of *A* is denoted by *A^c*
- Ven diagram 
	- Whole diagram represents sample space
	- A is circle in the space
	- everything NOT in A is A compliment *A^c*
	- P(A) + P(A^c) = 1
	- We can find P(A) if we subtract P compliment --> P(A) = 1 - P(A^c)
	- In a class of 20 people, what is the probability of 2 of you will have the same 00birthday
		- Can use subtraction here to get to the answer

### Union of 2 Events
- A *union* of events *A* and *B* is the event containing all sample points that are in *A* or *B* or both
- The union of events *A* and *B* is denoted by A ∪ B

### Intersection of 2 Events
- The *intersection* of events *A* and *B* is the set of all sample points that are in both A and B
- The intersection of events A and B is denoted by A ∩ B (upside down arch)


- Example
	- Experiment: Roll a die
	- Sample space: S = { 1, 2, 3, 4, 5, 6 }
	- *New* Define 2 events
	- let event A = { 1, 2, 3, 4 }
	- let event B = { 3, 4, 5, 6 }
	- What is A ∪ B = { 1, 2, 3, 4, 5, 6 }
	- What is A ∩ B = { 3, 4 }
	- What is A^c = { 5, 6 } (stuff that is NOT in A)
	- What is B^c = { 1, 2 }
	- What is A^c ∪ B^c = { 1, 2, 5, 6 }
	- What is A^c ∩ B^c = { } or null


### Additional Law
- Slide 17?
- Provides a way to compute the probability of even A, or B, or both A and B occurring
- P(A∪B) = P(A) + P(B) - P(A ∩ B)
- *- P(A ∩ B)* takes into account the double counting -- if we didn't do this, we'd have a probability > 1


### Mutually Exclusive Events
- Two events are said to be mutually exclusive if the events have no sample points in common
- Two events are mutually exclusive if, when one event occurs, the other cannot occur
- Venn diagram
- Example
	- Class asked where you were born 
	- Event A: event person born in New York
	- Event B: event person born in California
	- event (A∩B) = event person born in both NY and CA.  <-- not possible
	- P(A∩B) = 0

P(A∪B) = P(A) + P(B) - P(A∩B)
IF A and B are mutually exlusive, P(A∩B) goes to 0 so...
P(A∪B) = P(A) + P(B)

Example
- According to the US CDC, over an 8 year period, average of 16375 teenagers died each year in the US.  Leading causes of death are accidents, 7860, homicide 2129, and suicide 1018.  What is the probability that someon in this cohort would die of accident, homicide, or suicide?  And what is the probablity someone dies form a cause other than accident, homicide, or suicide.  
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
- P^c = 1 - (P(A) + P(H) + P(S)) 
	- 1 - (0.48 + 0.13 + 0.11 = 1 - 0.72 = *0.28 chance of dying by some other cause*

## Up next
- Professor will send link to recording if all goes well
- Will send materials for next week with plenty of time to review
	- go through multiple choice and exercises to reinforce what was done today
- 



---
## 2026-07-25 
###### 07:54am
---
#### Agenda

#### Tags

#### Summary

#### Questions


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

|        | $S_c$ (Son Attended) | $S_n$ (Son did not attend) | Total        |     |
| ------ | -------------------- | -------------------------- | ------------ | --- |
| $f_c$  | 22                   | 12                         | 34           |     |
| $f_n$  | 35                   | 31                         | 66           |     |
| Total: | 57                   | 43                         | 100 families |     |

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

