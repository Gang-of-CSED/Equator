# Equator (Phase 2)

## Overview:

In this phase of the project, we applied the different numerical methods used for calculating the roots of equations. we used Python programming language as it gives us more power in terms of precision, data manipulation and also plotting. Using the `List` data structure to manipulate the values in the methods.
We used the **Sympy** library to help us with function parsing and manipulation. Using the `sympify` function to store the symbolic representation of the input equation.
For plotting we used Matplotlib, specifically the `pyplot` module.
For the user interface (UI) we used PySide6, specifically the `QtWidgets` module. 

---

## 1. Bisection

$$
x_{r} = \frac{x_{l} + x_{u}}{2}
\begin{cases}
    x_{u} = x_{r}, & \text{if } f(x_{l}) \cdot f(x_{r}) < 0 \\
    x_{l} = x_{r}, & \text{if } f(x_{l}) \cdot f(x_{r}) > 0 \\
    \text{root} = x_{\text{r}}, & \text{if } f(x_{l}) \cdot f(x_{r}) = 0
\end{cases}
$$

### Sample Run

$$
f(x) = -12 - 21x + 18x^2 - 2.75x^3
$$
![bisection sample run](screenshots\Find%20Root\Bisection\problem.png)

<details>
<summary style="font-size: 20px; font-weight: bold;">Steps</summary>

**Step 1:**
![bisection step 1](screenshots\Find%20Root\Bisection\Step1.png)
**Step 2:**
![bisection step 2](screenshots\Find%20Root\Bisection\Step2.png)
**Step 3:**
![bisection step 3](screenshots\Find%20Root\Bisection\Step3.png)
**Step 4:**
![bisection step 4](screenshots\Find%20Root\Bisection\Step4.png)
**Step 5:**
![bisection step 5](screenshots\Find%20Root\Bisection\Step5.png)
**Step 6:**
![bisection step 6](screenshots\Find%20Root\Bisection\Step6.png)
**Step 7:**
![bisection step 7](screenshots\Find%20Root\Bisection\Step7.png)
**Step 8:**
![bisection step 8](screenshots\Find%20Root\Bisection\Step8.png)
**Step 9:**
![bisection step 9](screenshots\Find%20Root\Bisection\Step9.png)
</details>

---

## 2. False-Position

$$
x_{r} = \frac{x_{l} \cdot f(x_{u}) - x_{u} \cdot f(x_{l})}{f(x_{u}) - f(x_{l})}
\begin{cases}
    x_{u} = x_{r}, & \text{if } f(x_{l}) \cdot f(x_{r}) < 0 \\
    x_{l} = x_{r}, & \text{if } f(x_{l}) \cdot f(x_{r}) > 0 \\
    \text{root} = x_{\text{r}}, & \text{if } f(x_{l}) \cdot f(x_{r}) = 0
\end{cases}
$$


### Sample Run

$$
f(x) = -12 - 21x + 18x^2 - 2.75x^3
$$

![false position sample run](screenshots\Find%20Root\False-Position\problem.png)

<details>
<summary style="font-size: 20px; font-weight: bold;">Steps</summary>

**Step 1:**
![false position step 1](screenshots\Find%20Root\False-Position\Step1.png)
**Step 2:**
![false position step 2](screenshots\Find%20Root\False-Position\Step2.png)
**Step 3:**
![false position step 3](screenshots\Find%20Root\False-Position\Step3.png)
**Step 4:**
![false position step 4](screenshots\Find%20Root\False-Position\Step4.png)
**Step 5:**
![false position step 5](screenshots\Find%20Root\False-Position\Step5.png)
**Step 6:**
![false position step 6](screenshots\Find%20Root\False-Position\Step6.png)
**Step 7:**
![false position step 7](screenshots\Find%20Root\False-Position\Step7.png)

</details>
---

## 3. Fixed Point

$$
x_{i+1} = g(x_{i}) 
$$

### Sample Run

$$
f(x) = \sin{\sqrt{x}} - x, \quad g(x) = \sin{\sqrt{x}}
$$

![fixed point sample run](screenshots\Find%20Root\Fixed%20Point\problem.png)

<details>
<summary style="font-size: 20px; font-weight: bold;">Steps</summary>

**Step 1:**
![fixed point step 1](screenshots\Find%20Root\Fixed%20Point\Step1.png)
**Step 2:**
![fixed point step 2](screenshots\Find%20Root\Fixed%20Point\Step2.png)
**Step 3:**
![fixed point step 3](screenshots\Find%20Root\Fixed%20Point\Step3.png)
**Step 4:**
![fixed point step 4](screenshots\Find%20Root\Fixed%20Point\Step4.png)
**Step 5:**
![fixed point step 5](screenshots\Find%20Root\Fixed%20Point\Step5.png)
**Step 6:**
![fixed point step 6](screenshots\Find%20Root\Fixed%20Point\Step6.png)
**Step 7:**
![fixed point step 7](screenshots\Find%20Root\Fixed%20Point\Step7.png)
**Step 8:**
![fixed point step 8](screenshots\Find%20Root\Fixed%20Point\Step8.png)
**Step 9:**
![fixed point step 9](screenshots\Find%20Root\Fixed%20Point\Step9.png)

</details>

---

## 4. Original Newton-Raphson

$$
x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)}
$$

### Sample Run

$$
f(x) = -0.9x^2 + 1.7x + 2.5
$$

![original newton sample run](screenshots\Find%20Root\Original%20Newton\problem.png)

<details>
<summary style="font-size: 20px; font-weight: bold;">Steps</summary>

**Step 1:**
![original newton step 1](screenshots\Find%20Root\Original%20Newton\Step1.png)
**Step 2:**
![original newton step 2](screenshots\Find%20Root\Original%20Newton\Step2.png)
**Step 3:**
![original newton step 3](screenshots\Find%20Root\Original%20Newton\Step3.png)
**Step 4:**
![original newton step 4](screenshots\Find%20Root\Original%20Newton\Step4.png)
**Step 5:**
![original newton step 5](screenshots\Find%20Root\Original%20Newton\Step5.png)

</details>

---

## 5. Modified Newton-Raphson

### **Modification 1:**

$$
x_{i+1} = x_i - m \cdot \frac{f(x_i)}{f'(x_i)}

$$

### Sample Run
$$
f(x) = x^3 - 5x^2 + 7x - 3
$$

![modified 1 newton sample run](screenshots\Find%20Root\Modified%20Newton%201\problem.png)

<details>
<summary style="font-size: 20px; font-weight: bold;">Steps</summary>

**Step 1:**
![modified 1 newton step 1](screenshots\Find%20Root\Modified%20Newton%201\Step1.png)
**Step 2:**
![modified 1 newton step 2](screenshots\Find%20Root\Modified%20Newton%201\Step2.png)
**Step 3:**
![modified 1 newton step 3](screenshots\Find%20Root\Modified%20Newton%201\Step3.png)
**Step 4:**
![modified 1 newton step 4](screenshots\Find%20Root\Modified%20Newton%201\Step4.png)

</details>

---

### **Modification 2:**

$$
x_{i+1} = x_i - \frac{f(x_i) \cdot f'(x_i)}{(f'(x_i))^2 - f(x_i) \cdot f''(x_i)}
$$

### Sample Run

$$
f(x) = x^3 - 5x^2 + 7x - 3
$$

![modified 2 newton sample run](screenshots\Find%20Root\Modified%20Newton%202\problem.png)

<details>
<summary style="font-size: 20px; font-weight: bold;">Steps</summary>

**Step 1:**
![modified 2 newton step 1](screenshots\Find%20Root\Modified%20Newton%202\Step1.png)
**Step 2:**
![modified 2 newton step 2](screenshots\Find%20Root\Modified%20Newton%202\Step2.png)
**Step 3:**
![modified 2 newton step 3](screenshots\Find%20Root\Modified%20Newton%202\Step3.png)
**Step 4:**
![modified 2 newton step 4](screenshots\Find%20Root\Modified%20Newton%202\Step4.png)

</details>

---

## 6. Secant Method

$$
x_{i+1} = x_i - \frac{f(x_i) \cdot (x_i - x_{i-1})}{f(x_i) - f(x_{i-1})}
$$

### Sample Run

$$
f(x) = x^3 - 6x^2 + 11x - 6.1
$$

![secant sample run](screenshots\Find%20Root\Secant\problem.png)

<details>
<summary style="font-size: 20px; font-weight: bold;">Steps</summary>

**Step 1:**
![secant step 1](screenshots\Find%20Root\Secant\Step1.png)
**Step 2:**
![secant step 2](screenshots\Find%20Root\Secant\Step2.png)
**Step 3:**
![secant step 3](screenshots\Find%20Root\Secant\Step3.png)

</details>
---
