---
modified: 2026-10-02T21:21
created: 2026-07-17T21:34
---

---
## 2026-09-26 
###### 07:57am
---
# Note Meta
## Agenda
- Class remote due to nor'easter
- Experiments, counting rules, and assigning probabilities
- Events and their probability
- Basic relationships of probability
- Conditional probability
- Bayes' Theorem


## Tasks

- [x] 1st exam can be started, #7 & #10 ✅ 2026-10-02
- [x] quiz 1: https://brightspace.cuny.edu/d2l/le/content/1294332/viewContent/43820336/View ✅ 2026-10-02
- [x] Ch 5 exercises 1-9 ✅ 2026-10-01
## Tags
* #probabilityTheory 
* #statistics
* #studyGuide
* #conditionalProbability
* #bayesTheorem
* #multiplicationLaw
* #additionLaw
* #independentEvents

## Key Takeaways

**1. The Addition Law Governs "OR" Probabilities ($P(A \cup B)$)**
To find the probability of Event A **or** Event B occurring (the union), you must use the formula $P(A) + P(B) - P(A \cap B)$. This subtraction is critical because it prevents double-counting any outcomes that are common to both events (the intersection). If events are *mutually exclusive* (they cannot happen together), the simple addition rule applies: $P(A \cup B) = P(A) + P(B)$.

**2. Conditional Probability Determines Dependence ($P(A|B)$)**
Conditional probability calculates the likelihood of Event A occurring, *given that* Event B has already occurred. This relationship is fundamental because it measures how much one event influences another. The calculation $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ allows you to adjust your sample space based on known information.

**3. The Multiplication Law Governs "AND" Probabilities ($P(A \cap B)$)**
To find the probability of Event A **and** Event B occurring (the intersection), you must use the multiplication law, which generally states $P(A \cap B) = P(B)P(A|B)$. This rule is essential for calculating joint probabilities when events are dependent.

**4. Independence Simplifies Calculations ($P(A)P(B)$)**
If knowing that Event A occurred does *not* change the probability of Event B, the two events are independent. In this specific case, conditional probability simplifies to the marginal probability, allowing you to use the simplest form of the multiplication law: $P(A \cap B) = P(A)P(B)$.

**5. Bayes' Theorem Reverses Conditional Probability**
Bayes' Theorem is a specialized application of conditional probability that allows you to calculate a *prior* probability (the likelihood of an event before new information) using a *posterior* probability (the likelihood after incorporating new evidence). It provides the formal structure for updating beliefs based on observed data.

## Summary
### 📝 I. Exam Information & Format
*   **Format:** Take-home exam over several weeks.
*   **Grading:** Self-graded learning experience.
*   **Structure:** Multiple choice (10 choices), comprehensive.
*   **Requirement:** Students **must show their work**, which involves providing the equation and solution using R code/R Studio output.

### 📘 II. Core Probability Concepts & Definitions
The review material focuses on calculating probabilities of compound events using specific relationships:

*   **Event Definition:** An event is simply a collection of sample points. The probability of an event is the sum of the probabilities of its constituent sample points.
*   **Relationships Between Events:**
    *   **Complement ($A^c$):** All outcomes that are *not* in Event A.
    *   **Union ($A \cup B$):** Outcomes that are in A, or in B, or both (A OR B).
    *   **Intersection ($A \cap B$):** Outcomes that are in **both** A and B (A AND B).

### <0xF0><0x9F><0xA7><0xAE> III. Key Formulas and Laws
These laws provide the methods for calculating complex probabilities:

#### 1. Addition Law (Calculating $P(A \cup B)$)
This law calculates the probability of A, or B, or both occurring.
*   **General Rule:** $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
*   **Mutually Exclusive Events (Special Case):** If events cannot happen at the same time ($P(A \cap B) = 0$), the formula simplifies to: $P(A \cup B) = P(A) + P(B)$.

#### 2. Conditional Probability (Calculating $P(A|B)$)
This is the probability of Event A happening **given** that Event B has already occurred.
*   **Formula:** $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$

#### 3. Multiplication Law (Calculating $P(A \cap B)$)
This law calculates the probability of two events occurring together (the intersection).
*   **General Rule (Dependent Events):** $P(A \cap B) = P(B) \cdot P(A|B)$
*   **Independent Events (Special Case):** If one event does not affect the other, the formula simplifies to: $P(A \cap B) = P(A) \cdot P(B)$.

***
### 💡 Summary of Application Focus Areas
The material emphasizes applying these laws in three main contexts:
1.  **Joint Probability:** Finding the chance that multiple events happen together (e.g., subscribing to both daily and Sunday paper).
2.  **Conditional Probability & Bayes' Theorem:** Calculating probabilities when new information limits the possible outcomes (using tables/diagrams).
3.  **Compound Events:** Determining combined probability for sequences of actions (e.g., two customers paying by credit card).



## Questions


---
# Notes

- Exam - is take home and will have several weeks to complete. It's a learning experience and you can grade yourself as you go. It'll be multiple choice (10 choices).  You'll have to show your work. It's comprehensive.  

## Review

- Experiments, counting rules, and assigning probabilities
- Events and their probability
	- an *event* is a collection of sample points
	- *probability of any event* is equal to the sum of the probabilities of the sample points in the event
- Basic relationships of probability
	- Complement of an event
	- Union of two events
	- Intersection of two events
	- Mutually exclusive events
- Conditional probability
- Bayes' Theorem


### Event Relationships

*Complement* of an event *A* is defined to be the event consisting of all sample points that are not in *A*

The compliment of *A* is denoted by *$A^c$*

The *union* of events A and B is the event containing all sample points that are in A or B or both

The union of events A and B is denoted by $A \cup B$

The *intersection* of events A and B is the set of all sample points that are in both A and B

The intersection of events A and B is denoted by $A \cap B$

## Addition Law

The *addition law* provides a way to compute the probability of event A, or B, or both A and B occurring

The law is written as: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$

### Mutually Exclusive Events

Two events are said to be *mutually exclusive* if the events have no sample points in common.

Two events are mutually exclusive if, when one event occurs, the other can not occur

If events A and B are mutually exclusive, $P(A \cap B) = 0$

$P(A \cup B) = P(A) + P(B)$

### Conditional Probability

The probability of an event given that another event has occurred is called a *conditional probability*

The conditional probability of *A given B* is denoted by $P(A|B)$

A conditional probability is computed as follows:

$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$

Will apply this with a few other ideas, for review

### Independent Events

If the probability of event A is not changed by the existence of event B, we would say that the events A and B are *independent*

Two events A and B are independent if:

$P(A|B) = P(A)$ or $P(B|A) = P(B)$

### Multiplication Law

The *multiplication law* provides a way to compute the probability of the **intersection** of two events

Written as:

$P(A \cap B) = P(B)P(A|B)$

**if we have independent events** can collapse to 

$P(A \cap B) = P(A)P(B)$


# Exam 1

Word document.  Have 10 pages, 10 questions, 10 multiple choice each (roughly)

Should be able to answer SOME questions (but not all, yet).  

Some test chapter 5 & 6 material which we haven't gotten to yet.  Once we do that, we should be able to handle the exam.  

PLEASE SHOW HOW YOU ARRIVED TO EACH SOLUTION.

Enter the letter of your choice at the underline **THEN enter the R code** you used to answer the question.  

To show your work, use the R Studio and copy the equation AND answer and paste it in the exam.  

#### Questions we likely can do: 
1 (if we can get through today's material)
2 - no
3 - no
4 - no
5 - no
6 - no
7 - yes
8 - no
9 - no
10 - yes

## Conditional Probability
From the textbook, section 4.6, page 109

See example 4.16.  

Page 113, Table 4.6 Bayesian theorem

Example 4.18, pg 114

Example 4.19, pg 116

Go through these questions and that will help.

Chapter 4 exercises in BrightSpace:

1. If we have a two-step experiment in which we flip a coin and cast a die...
2. Consider a class of first-year statistics students in which 20 undergraduate students are enrolled...


## Examples
(done on the whiteboard)

What is the probability that a randomly sampled household subscribes to both the daily and Sunday editions of the paper?

##### Facts
84% of households subscribe to the daily edition of the a newspaper
of these households, 75% also subscribe to the Sunday edition.

##### Question
What is the probability that a randomly selected household subscribes to both the daily and the Sunday edition of a newspaper

##### Template
1. Define the events
	1. Event D: households subscribes to the daily edition
	2. Event S: households subscribes to the Sunday edition
2. Assign probabilities to the events
	1. $p(D) = 0.84$
	2. $p(S|D) =  0.75$ conditional probability -> takes the daily AND also takes the Sunday
3. Apply the **Multiplication Law**
	1. What is the probability that the household subscribes to both the daily and Sunday?  (these events are NOT independent)
	2. $P(A \cap B) = P(A|B)P(B)$
	3. $P(S \cap D) = P(S|D)P(D)$
	4. (0.75)(0.84) = 0.63
4. Answer: 63% probability that a randomly selected household subscribes to both the daily AND Sunday newspaper


##### Example
What is the probability the next 2 customers come in and pay by credit card?

80% of customers use a credit card to pay

1. Define the events
	1. Event A: 1st customer uses a credit card
	2. Event B: 2nd customer uses a credit card
2. Assign probabilities to the events
	1. $P(A) = 0.80$
	2. $P(B) = 0.80$
3. Apply the Multiplication Law
	1. Suggest these events are independent. The driver in the first car doesn't influence the driver of the second car pays. Need multiplication law since the events are independent.
	2. $P(A \cap B) = P(A)P(B)$
	3. so (0.80)(0.80) = 0.64
4. Answer
	1. 64% chance that not only the next customer will pay by a credit card, but so will the one that comes in after

##### Example
The blood types in the general population.  Could be 10s of thousands of people.


|        | A    | B    | AB   | O    |      |
| ------ | ---- | ---- | ---- | ---- | ---- |
| $Rh^+$ | 0.34 | 0.09 | 0.04 | 0.38 | 0.85 |
| $Rh^-$ | 0.06 | 0.02 | 0.01 | 0.06 | 0.15 |
|        | 0.40 | 0.11 | 0.05 | 0.44 | 1.00 |
(table is considered joint probabilities)

Question: What is the probability will have type O blood?

What is $P(O)$?

How to find:

a. $P(O) = P(O \cap Rh^+)+P(O \cap Rh^-) = 0.38 + 0.06 = 0.44$
(Will need this reasoning for Bayes)

b. What would be the probability a randomly selected person would be $Rh^-$
$P(Rh^-) = 0.06 + 0.02 + .0.01 + 0.06 = 0.15$

c. What is the probability a person will have type B blood when they're $Rh^+$
$P(B|Rh^+) = \frac{P(B \cap Rh^+)}{P(Rh^+)} = \frac{0.09}{0.85} = 0.1059$

d. What is the probability that a married coupled will both be $Rh^-$? 
W = wife, H = husband
$P(Rh_W^- \cap Rh_H^-) = P(Rh_W^-)P(Rh_H^-) = (0.15)(0.15) = 0.0225$

1. Events
2. Assign probabilities
3. Apply the Multiplication Law
4. Answer


