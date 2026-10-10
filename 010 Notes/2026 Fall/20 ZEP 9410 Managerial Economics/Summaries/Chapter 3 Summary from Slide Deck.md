---
modified: 2026-10-09T17:21
created: 2026-09-27T13:43
---
From Gemini, 2026-09-27

Here is a summary of Chapter 3: **Quantitative Demand Analysis** from the slide deck:

### **1. The Core Concept of Elasticity**

- Elasticity measures how responsive one variable is to percentage changes in another variable.
    
- Mathematically, the general elasticity between $G$ and $S$ is expressed as $E_{G,S} = \frac{\%\Delta G}{\%\Delta S}$ or via calculus as $E_{G,S} = \frac{dG}{dS}\frac{S}{G}$.
    
- The magnitude of the absolute value indicates responsiveness: $\vert{}E\vert{} > 1$ means highly responsive (elastic), while $\vert{}E\vert{} < 1$ means slightly responsive (inelastic).
    

### **2. Own Price Elasticity of Demand**

- Measures the percentage change in quantity demanded of good X resulting from a percentage change in its own price. Due to the law of demand, its sign is negative.
    
- **Total Revenue Test:** Total revenue is maximized when demand is unitary elastic ($E = -1$).
    
    - In the **elastic** range ($\vert{}E\vert{} > 1$), decreasing price increases total revenue.
        
    - In the **inelastic** range ($\vert{}E\vert{} < 1$), increasing price increases total revenue.
        
- **Three main factors influencing elasticity:** (1) availability and number of substitutes, (2) time/duration of purchase horizon, and (3) expenditure share of consumers' budgets.
    
- **Marginal Revenue (MR):** Linked to price and own price elasticity through the formula $MR = P[\frac{1+E}{E}]$.
    

### **3. Other Major Elasticities**

- **Cross-Price Elasticity ($E_{Q_X^d, P_Y}$):** Measures responsiveness of demand for good X to a price change in good Y. A positive value indicates substitutes, whereas a negative value indicates complements.
    
- **Income Elasticity ($E_{Q_X^d, M}$):** Measures responsiveness of demand to changes in consumer income. Positive values signify normal goods, while negative values signify inferior goods.
    
- **Advertising Elasticities:** Measure the percentage change in consumption resulting from a percentage change in advertising expenditure for the same or related goods.
    

### **4. Calculating Elasticities from Demand Functions**

- **Linear Demand Functions:** Given a linear demand equation, elasticities can be computed directly using coefficients and current values (e.g., own price elasticity is $\alpha_X \frac{P_X}{Q_X}$).
    
- **Log-Linear Demand Functions:** For non-linear relationships, log-linear specifications directly yield constant elasticities from their regression coefficients (e.g., own price elasticity is $\beta_X$).
    

### **5. Empirical Estimation via Regression Analysis**

- Regression techniques (such as ordinary least squares) allow analysts to estimate demand curves and test hypotheses using field or experimental data.
    
- Output tables provide coefficients, standard errors, t-statistics, p-values, and confidence intervals to evaluate the statistical significance and magnitude of each explanatory variable (like price, advertising, or distance).


---

 Equation: Q = 60 − 2P + 0.01M + 7PR

Identifying the coefficients and their impact: 

- **Own-Price Coefficient (e.g., $-2P$):**
    
    - **Negative:** Follows the Law of Demand (Price $\uparrow$, Quantity $\downarrow$).
        
    - _Note:_ A positive own-price coefficient would violate the Law of Demand and describe a rare "Giffen good," but standard problems will always have a negative sign here.
        
- **Income Coefficient ($M$):**
    
    - **Positive ($+$):** **Normal good** (Income $\uparrow$, Quantity $\uparrow$).
        
    - **Negative ($-$):** **Inferior good** (Income $\uparrow$, Quantity $\downarrow$).
        
- **Related Price Coefficient ($P_R$):**
    
    - **Positive ($+$):** **Substitute good** (Price of related good $\uparrow$, Quantity $\uparrow$).
        
    - **Negative ($-$):** **Complement good** (Price of related good $\uparrow$, Quantity $\downarrow$).

---

NOTE, if say production increases, that impacts the SUPPLY equation only and does NOT change demand! 

So when production costs go up, market demand **will not change** and the market supply **will decrease**.  (supply decreased, the supply curve shifts left - draw it out and see what happens to the price!)

The equilibrium price will **increase** and the equilibrium quantity will **decrease**

### Step 6: What Happens to Total Revenue?

this depends entirely on the elasticity 

- Recall the **Elasticity and Total Revenue Rule**:
    
    - If demand is **elastic** ($\vert{}E_d\vert{} > 1$), price and total revenue move in **opposite** directions. (Price goes up $\rightarrow$ Total Revenue goes down).
        
    - If demand is **inelastic** ($\vert{}E_d\vert{} < 1$), price and total revenue move in the **same** direction. (Price goes up $\rightarrow$ Total Revenue goes up).
        
    - If **unit elastic** ($\vert{}E_d\vert{} = 1$), total revenue stays maximized.

Note the "expected change" is a delta and means subtract the new from the old!  

