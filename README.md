# Equator

## Index

0. [Introduction](#introduction)
1. [Phase 1: System of Linear Equations](#phase-1-system-of-linear-equations)
    1. [Gauss Elimination](#1-gauss-elimination)
    2. [Gauss Jordan](#2-gauss-jordan)
    3. [LU Decomposition](#3-lu-decomposition)
        1. [Doolittle's Method](#a-doolittles-method)
        2. [Crout's Method](#b-crouts-method)
        3. [Cholesky's Method](#c-choleskys-method)
    4. [Gauss Seidel](#4-gauss-seidel)
    5. [Jacobi-Iteration](#5-jacobi-iteration)
2. [Phase 2: Root Finding](#phase-2-root-finding)
    1. [Bisection](#1-bisection)
    2. [False-Position](#2-false-position)
    3. [Fixed Point](#3-fixed-point)
    4. [Original Newton-Raphson](#4-original-newton-raphson)
    5. [Modified Newton-Raphson](#5-modified-newton-raphson)
        1. [Modification 1](#modification-1)
        2. [Modification 2](#modification-2)
    6. [Secant Method](#6-secant-method)

---

# Introduction
The project "Equator" stands as a robust mathematical toolkit, built upon the foundation of Python and PyQt, enriched by the inclusion of powerful libraries such as NumPy, SymPy, and Matplotlib. Its overarching goal is to deliver efficient numerical solutions to a diverse array of mathematical challenges, with a specific emphasis on problems related to linear algebra and root finding. The project is divided into two phases, each of which is further subdivided into several modules. The first phase is dedicated to the solution of systems of linear equations, while the second phase is dedicated to the solution of root finding problems. The project is designed to be user-friendly, with a simple and intuitive graphical user interface (GUI) that allows the user to easily interact with the program and obtain the desired results.

---
# Phase 1: System of Linear Equations

## 1. Gauss Elimination


$$
\begin{align*}
    &\text{Forward Elimination:} \\ 
    &\begin{bmatrix}
    \begin{array}{ccc|c}
        a_{11} & a_{12} & a_{13} & b_1 \\
        a_{21} & a_{22} & a_{23} & b_2 \\
        a_{31} & a_{32} & a_{33} & b_3 \\
    \end{array}
    \end{bmatrix}
    \sim
    \begin{bmatrix}
    \begin{array}{ccc|c}
        a_{11} & a_{12} & a_{13} & b_1 \\
        0 & a_{22}' & a_{23}' & b_2' \\
        0 & 0 & a_{33}'' & b_3'' \\
    \end{array}
    \end{bmatrix}\\
    &\text{Backward Substitution:} \\
    &\begin{aligned}
        x_3 &= \frac{b_3''}{a_{33}''} \\
        x_2 &= \frac{b_2' - a_{23}'x_3}{a_{22}'} \\
        x_1 &= \frac{b_1 - a_{12}x_2 - a_{13}x_3}{a_{11}} \\
    \end{aligned}
\end{align*}
$$

### Sample Run

$$
\begin{aligned}
    2x_1 + 3x_2 - 2x_3 &= 1 \\
    4x_1 + 4x_2 - 3x_3 &= 5 \\
    2x_1 - x_2 + 2x_3 &= 3 \\
\end{aligned}
$$
![gauss elimination sample run](screenshots/System%20of%20Equations/Gauss%20Elimination/problem.png)

<details>
<summary style="font-size: 20px; font-weight: bold;">Steps</summary>

**Step 1:**
![gauss elimination step 1](screenshots/System%20of%20Equations/Gauss%20Elimination/Step1.png)
**Step 2:**
![gauss elimination step 2](screenshots/System%20of%20Equations/Gauss%20Elimination/Step2.png)
**Step 3:**
![gauss elimination step 3](screenshots/System%20of%20Equations/Gauss%20Elimination/Step3.png)
**Step 4:**
![gauss elimination step 4](screenshots/System%20of%20Equations/Gauss%20Elimination/Step4.png)
**Step 5:**
![gauss elimination step 5](screenshots/System%20of%20Equations/Gauss%20Elimination/Step5.png)
**Step 6:**
![gauss elimination step 6](screenshots/System%20of%20Equations/Gauss%20Elimination/Step6.png)
**Step 7:**
![gauss elimination step 7](screenshots/System%20of%20Equations/Gauss%20Elimination/Step7.png)
**Step 8:**
![gauss elimination step 8](screenshots/System%20of%20Equations/Gauss%20Elimination/Step8.png)
**Step 9:**
![gauss elimination step 9](screenshots/System%20of%20Equations/Gauss%20Elimination/Step9.png)
**Step 10:**
![gauss elimination step 10](screenshots/System%20of%20Equations/Gauss%20Elimination/Step10.png)
</details>

---

## 2. Gauss Jordan

$$
\begin{align*}
    &\text{Forward and Backward Elimination:} \\
    &\begin{bmatrix}
    \begin{array}{ccc|c}
        a_{11} & a_{12} & a_{13} & b_1 \\
        a_{21} & a_{22} & a_{23} & b_2 \\
        a_{31} & a_{32} & a_{33} & b_3 \\
    \end{array}
    \end{bmatrix}
    \sim
    \begin{bmatrix}
    \begin{array}{ccc|c}
        a_{11} & 0 & 0 & b_1'' \\
        0 & a_{22}' & 0 & b_2'' \\
        0 & 0 & a_{33}'' & b_3'' \\
    \end{array}
    \end{bmatrix} \\ \\
    &\text{Normalization:} \\
    &\begin{bmatrix}
    \begin{array}{ccc|c}
        1 & 0 & 0 & b_1''/a_{11} \\
        0 & 1 & 0 & b_2''/a_{22}' \\
        0 & 0 & 1 & b_3''/a_{33}'' \\
    \end{array}
    \end{bmatrix}
    \begin{aligned}
        x_1 = \frac{b_1''}{a_{11}},\quad
        x_2 = \frac{b_2''}{a_{22}'} ,\quad
        x_3 = \frac{b_3''}{a_{33}''} \\      
    \end{aligned}
\end{align*}
$$

### Sample Run

$$
\begin{aligned}
    2x_1 + 3x_2 - 2x_3 &= 1 \\
    4x_1 + 4x_2 - 3x_3 &= 5 \\
    2x_1 - x_2 + 2x_3 &= 3 \\
\end{aligned}
$$

![gauss jordan sample run](screenshots/System%20of%20Equations/Gauss%20Jordan/problem.png)

<details>
<summary style="font-size: 20px; font-weight: bold;">Steps</summary>

**Step 1:**
![gauss jordan step 1](screenshots/System%20of%20Equations/Gauss%20Jordan/Step1.png)
**Step 2:**
![gauss jordan step 2](screenshots/System%20of%20Equations/Gauss%20Jordan/Step2.png)
**Step 3:**
![gauss jordan step 3](screenshots/System%20of%20Equations/Gauss%20Jordan/Step3.png)
**Step 4:**
![gauss jordan step 4](screenshots/System%20of%20Equations/Gauss%20Jordan/Step4.png)
**Step 5:**
![gauss jordan step 5](screenshots/System%20of%20Equations/Gauss%20Jordan/Step5.png)
**Step 6:**
![gauss jordan step 6](screenshots/System%20of%20Equations/Gauss%20Jordan/Step6.png)
**Step 7:**
![gauss jordan step 7](screenshots/System%20of%20Equations/Gauss%20Jordan/Step7.png)
**Step 8:**
![gauss jordan step 8](screenshots/System%20of%20Equations/Gauss%20Jordan/Step8.png)
**Step 9:**
![gauss jordan step 9](screenshots/System%20of%20Equations/Gauss%20Jordan/Step9.png)
</details>

---

## 3. LU Decomposition

$$
A = LU  \text{ where } L \text{ is a lower triangular matrix and } U \text{ is an upper triangular matrix}\\
$$

$$
LUx = b \implies Ux = y \text{ and } Ly = b
$$

## a. Doolittle's Method

$$
\begin{bmatrix}
    a_{11} & a_{12} & a_{13} \\
    a_{21} & a_{22} & a_{23} \\
    a_{31} & a_{32} & a_{33} \\
\end{bmatrix}
=\begin{bmatrix}
    1 & 0 & 0 \\
    l_{21} & 1 & 0 \\
    l_{31} & l_{32} & 1 \\
\end{bmatrix}
\begin{bmatrix}
    u_{11} & u_{12} & u_{13} \\
    0 & a_{22} & u_{23} \\
    0 & 0 & u_{33} \\
\end{bmatrix}
$$

### Sample Run

$$
\begin{aligned}
    3x_1 + 2x_2 - x_3 &= 1 \\
    2x_1 + 3x_2 + 2x_3 &= 2 \\
    5x_1 - x_2 + 4x_3 &= 3 \\
\end{aligned}
$$

![doolittle sample run](screenshots/System%20of%20Equations/Doolittle%20LU/problem.png)

<details>
<summary style="font-size: 20px; font-weight: bold;">Steps</summary>

**Step 1:**
![doolittle step 1](screenshots/System%20of%20Equations/Doolittle%20LU/Step1.png)
**Step 2:**
![doolittle step 2](screenshots/System%20of%20Equations/Doolittle%20LU/Step2.png)
**Step 3:**
![doolittle step 3](screenshots/System%20of%20Equations/Doolittle%20LU/Step3.png)
**Step 4:**
![doolittle step 4](screenshots/System%20of%20Equations/Doolittle%20LU/Step4.png)
</details>

---

## b. Crout's Method

$$
\begin{bmatrix}
    a_{11} & a_{12} & a_{13} \\
    a_{21} & a_{22} & a_{23} \\
    a_{31} & a_{32} & a_{33} \\
\end{bmatrix}
=\begin{bmatrix}
    l_{11} & 0 & 0 \\
    l_{21} & l_{22} & 0 \\
    l_{31} & l_{32} & l_{33} \\
\end{bmatrix}
\begin{bmatrix}
    1 & u_{12} & u_{13} \\
    0 & 1 & u_{23} \\
    0 & 0 & 1 \\
\end{bmatrix}
$$

### Sample Run

$$
\begin{aligned}
    3x_1 + 2x_2 - x_3 &= 1 \\
    2x_1 + 3x_2 + 2x_3 &= 2 \\
    5x_1 - x_2 + 4x_3 &= 3 \\
\end{aligned}
$$

![crout sample run](screenshots/System%20of%20Equations/Crout%20LU/problem.png)

<details>
<summary style="font-size: 20px; font-weight: bold;">Steps</summary>

**Step 1:**
![crout step 1](screenshots/System%20of%20Equations/Crout%20LU/Step1.png)
**Step 2:**
![crout step 2](screenshots/System%20of%20Equations/Crout%20LU/Step2.png)
**Step 3:**
![crout step 3](screenshots/System%20of%20Equations/Crout%20LU/Step3.png)
**Step 4:**
![crout step 4](screenshots/System%20of%20Equations/Crout%20LU/Step4.png)
</details>

---

## c. Cholesky's Method

$$
A = A^T \implies A = LL^T \\ 
$$

$$
\begin{bmatrix}
    a_{11} & a_{12} & a_{13} \\
    a_{21} & a_{22} & a_{23} \\
    a_{31} & a_{32} & a_{33} \\
\end{bmatrix}
=\begin{bmatrix}
    l_{11} & 0 & 0 \\
    l_{21} & l_{22} & 0 \\
    l_{31} & l_{32} & l_{33} \\
\end{bmatrix}
\begin{bmatrix}
    l_{11} & l_{21} & l_{31} \\
    0 & l_{22} & l_{32} \\
    0 & 0 & l_{33} \\
\end{bmatrix}
$$

### Sample Run

$$
\begin{aligned}
    5x_1 + 2x_2 + x_3 &= 1 \\
    2x_1 + 6x_2 + 2x_3 &= 2 \\
    3x_1 + 2x_2 + 7x_3 &= 3 \\
\end{aligned}
$$

![cholesky sample run](screenshots/System%20of%20Equations/Cholesky%20LU/problem.png)

<details>
<summary style="font-size: 20px; font-weight: bold;">Steps</summary>

**Step 1:**
![cholesky step 1](screenshots/System%20of%20Equations/Cholesky%20LU/Step1.png)
**Step 2:**
![cholesky step 2](screenshots/System%20of%20Equations/Cholesky%20LU/Step2.png)
**Step 3:**
![cholesky step 3](screenshots/System%20of%20Equations/Cholesky%20LU/Step3.png)
**Step 4:**
![cholesky step 4](screenshots/System%20of%20Equations/Cholesky%20LU/Step4.png)
**Step 5:**
![cholesky step 5](screenshots/System%20of%20Equations/Cholesky%20LU/Step5.png)
**Step 6:**
![cholesky step 6](screenshots/System%20of%20Equations/Cholesky%20LU/Step6.png)
**Step 7:**
![cholesky step 7](screenshots/System%20of%20Equations/Cholesky%20LU/Step7.png)
</details>

---

## 4. Gauss Seidel

$$
\begin{aligned}
    x_1^{(k+1)} &= \frac{b_1 - a_{12}x_2^{(k)} - a_{13}x_3^{(k)}}{a_{11}} \\
    x_2^{(k+1)} &= \frac{b_2 - a_{21}x_1^{(k+1)} - a_{23}x_3^{(k)}}{a_{22}} \\
    x_3^{(k+1)} &= \frac{b_3 - a_{31}x_1^{(k+1)} - a_{32}x_2^{(k+1)}}{a_{33}} \\
\end{aligned}
$$

### Sample Run

$$
\begin{aligned}
    &4x_1 + 2x_2 + x_3 &= 11 \\
    &-1x_1 + 2x_2  &= 3 \\
    &2x_1 + x_2 + 4x_3 &= 16 \\
    &x_0 = (1, 1, 1) \\
\end{aligned}
$$

![gauss seidel sample run](screenshots/System%20of%20Equations/Gauss%20Seidel/problem.png)

<details>
<summary style="font-size: 20px; font-weight: bold;">Steps</summary>

**Step 1:**
![gauss seidel step 1](screenshots/System%20of%20Equations/Gauss%20Seidel/Step1.png)
**Step 2:**
![gauss seidel step 2](screenshots/System%20of%20Equations/Gauss%20Seidel/Step2.png)
**Step 3:**
![gauss seidel step 3](screenshots/System%20of%20Equations/Gauss%20Seidel/Step3.png)
**Step 4:**
![gauss seidel step 4](screenshots/System%20of%20Equations/Gauss%20Seidel/Step4.png)
**Step 5:**
![gauss seidel step 5](screenshots/System%20of%20Equations/Gauss%20Seidel/Step5.png)
**Step 6:**
![gauss seidel step 6](screenshots/System%20of%20Equations/Gauss%20Seidel/Step6.png)
</details>

---

## 5. Jacobi-Iteration

$$
\begin{aligned}
    x_1^{(k+1)} &= \frac{b_1 - a_{12}x_2^{(k)} - a_{13}x_3^{(k)}}{a_{11}} \\
    x_2^{(k+1)} &= \frac{b_2 - a_{21}x_1^{(k)} - a_{23}x_3^{(k)}}{a_{22}} \\
    x_3^{(k+1)} &= \frac{b_3 - a_{31}x_1^{(k)} - a_{32}x_2^{(k)}}{a_{33}} \\
\end{aligned}
$$

### Sample Run

$$
\begin{aligned}
    &4x_1 + 2x_2 + x_3 &= 11 \\
    &-1x_1 + 2x_2  &= 3 \\
    &2x_1 + x_2 + 4x_3 &= 16 \\
    &x_0 = (1, 1, 1) \\
\end{aligned}
$$

![jacobi sample run](screenshots/System%20of%20Equations/Jacobi-Iteration/problem.png)

<details>
<summary style="font-size: 20px; font-weight: bold;">Steps</summary>

**Step 1:**
![jacobi step 1](screenshots/System%20of%20Equations/Jacobi-Iteration/Step1.png)
**Step 2:**
![jacobi step 2](screenshots/System%20of%20Equations/Jacobi-Iteration/Step2.png)
**Step 3:**
![jacobi step 3](screenshots/System%20of%20Equations/Jacobi-Iteration/Step3.png)
**Step 4:**
![jacobi step 4](screenshots/System%20of%20Equations/Jacobi-Iteration/Step4.png)
**Step 5:**
![jacobi step 5](screenshots/System%20of%20Equations/Jacobi-Iteration/Step5.png)
**Step 6:**
![jacobi step 6](screenshots/System%20of%20Equations/Jacobi-Iteration/Step6.png)
**Step 7:**
![jacobi step 7](screenshots/System%20of%20Equations/Jacobi-Iteration/Step7.png)
**Step 8:**
![jacobi step 8](screenshots/System%20of%20Equations/Jacobi-Iteration/Step8.png)
**Step 9:**
![jacobi step 9](screenshots/System%20of%20Equations/Jacobi-Iteration/Step9.png)
**Step 10:**
![jacobi step 10](screenshots/System%20of%20Equations/Jacobi-Iteration/Step10.png)
**Step 11:**
![jacobi step 11](screenshots/System%20of%20Equations/Jacobi-Iteration/Step11.png)
</details>

---

# Phase 2: Root Finding

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

![bisection sample run](screenshots/Find%20Root/Bisection/problem.png)

<details>
<summary style="font-size: 20px; font-weight: bold;">Steps</summary>

**Step 1:**
![bisection step 1](screenshots/Find%20Root/Bisection/Step1.png)
**Step 2:**
![bisection step 2](screenshots/Find%20Root/Bisection/Step2.png)
**Step 3:**
![bisection step 3](screenshots/Find%20Root/Bisection/Step3.png)
**Step 4:**
![bisection step 4](screenshots/Find%20Root/Bisection/Step4.png)
**Step 5:**
![bisection step 5](screenshots/Find%20Root/Bisection/Step5.png)
**Step 6:**
![bisection step 6](screenshots/Find%20Root/Bisection/Step6.png)
**Step 7:**
![bisection step 7](screenshots/Find%20Root/Bisection/Step7.png)
**Step 8:**
![bisection step 8](screenshots/Find%20Root/Bisection/Step8.png)
**Step 9:**
![bisection step 9](screenshots/Find%20Root/Bisection/Step9.png)
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

![false position sample run](screenshots/Find%20Root/False-Position/problem.png)

<details>
<summary style="font-size: 20px; font-weight: bold;">Steps</summary>

**Step 1:**
![false position step 1](screenshots/Find%20Root/False-Position/Step1.png)
**Step 2:**
![false position step 2](screenshots/Find%20Root/False-Position/Step2.png)
**Step 3:**
![false position step 3](screenshots/Find%20Root/False-Position/Step3.png)
**Step 4:**
![false position step 4](screenshots/Find%20Root/False-Position/Step4.png)
**Step 5:**
![false position step 5](screenshots/Find%20Root/False-Position/Step5.png)
**Step 6:**
![false position step 6](screenshots/Find%20Root/False-Position/Step6.png)
**Step 7:**
![false position step 7](screenshots/Find%20Root/False-Position/Step7.png)

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

![fixed point sample run](screenshots/Find%20Root/Fixed%20Point/problem.png)

<details>
<summary style="font-size: 20px; font-weight: bold;">Steps</summary>

**Step 1:**
![fixed point step 1](screenshots/Find%20Root/Fixed%20Point/Step1.png)
**Step 2:**
![fixed point step 2](screenshots/Find%20Root/Fixed%20Point/Step2.png)
**Step 3:**
![fixed point step 3](screenshots/Find%20Root/Fixed%20Point/Step3.png)
**Step 4:**
![fixed point step 4](screenshots/Find%20Root/Fixed%20Point/Step4.png)
**Step 5:**
![fixed point step 5](screenshots/Find%20Root/Fixed%20Point/Step5.png)
**Step 6:**
![fixed point step 6](screenshots/Find%20Root/Fixed%20Point/Step6.png)
**Step 7:**
![fixed point step 7](screenshots/Find%20Root/Fixed%20Point/Step7.png)
**Step 8:**
![fixed point step 8](screenshots/Find%20Root/Fixed%20Point/Step8.png)
**Step 9:**
![fixed point step 9](screenshots/Find%20Root/Fixed%20Point/Step9.png)
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

![original newton sample run](screenshots/Find%20Root/Original%20Newton/problem.png)

<details>
<summary style="font-size: 20px; font-weight: bold;">Steps</summary>

**Step 1:**
![original newton step 1](screenshots/Find%20Root/Original%20Newton/Step1.png)
**Step 2:**
![original newton step 2](screenshots/Find%20Root/Original%20Newton/Step2.png)
**Step 3:**
![original newton step 3](screenshots/Find%20Root/Original%20Newton/Step3.png)
**Step 4:**
![original newton step 4](screenshots/Find%20Root/Original%20Newton/Step4.png)
**Step 5:**
![original newton step 5](screenshots/Find%20Root/Original%20Newton/Step5.png)

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

![modified 1 newton sample run](screenshots/Find%20Root/Modified%20Newton%201/problem.png)

<details>
<summary style="font-size: 20px; font-weight: bold;">Steps</summary>

**Step 1:**
![modified 1 newton step 1](screenshots/Find%20Root/Modified%20Newton%201/Step1.png)
**Step 2:**
![modified 1 newton step 2](screenshots/Find%20Root/Modified%20Newton%201/Step2.png)
**Step 3:**
![modified 1 newton step 3](screenshots/Find%20Root/Modified%20Newton%201/Step3.png)
**Step 4:**
![modified 1 newton step 4](screenshots/Find%20Root/Modified%20Newton%201/Step4.png)

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

![modified 2 newton sample run](screenshots/Find%20Root/Modified%20Newton%202/problem.png)

<details>
<summary style="font-size: 20px; font-weight: bold;">Steps</summary>

**Step 1:**
![modified 2 newton step 1](screenshots/Find%20Root/Modified%20Newton%202/Step1.png)
**Step 2:**
![modified 2 newton step 2](screenshots/Find%20Root/Modified%20Newton%202/Step2.png)
**Step 3:**
![modified 2 newton step 3](screenshots/Find%20Root/Modified%20Newton%202/Step3.png)
**Step 4:**
![modified 2 newton step 4](screenshots/Find%20Root/Modified%20Newton%202/Step4.png)
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

![secant sample run](screenshots/Find%20Root/Secant/problem.png)

<details>
<summary style="font-size: 20px; font-weight: bold;">Steps</summary>

**Step 1:**
![secant step 1](screenshots/Find%20Root/Secant/Step1.png)
**Step 2:**
![secant step 2](screenshots/Find%20Root/Secant/Step2.png)
**Step 3:**
![secant step 3](screenshots/Find%20Root/Secant/Step3.png)
</details>

