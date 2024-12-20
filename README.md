## Overview

This Python script provides tools for solving ordinary differential equations (ODEs) using **Multiscale Expansion** and **WKB Approximation** techniques. These methods are commonly used in perturbation theory to approximate solutions of ODEs involving a small parameter $ \epsilon $.

---

1. **Multiscale Expansion (`Multiscale_Ansantz`)**:\
   This is used when we see that the frequency is constant over time but amplitude changes.
   - We assume there exists a solution $f$ such that $f = f_0 + f_1 + \cdots$
   - We assume there are slow and fast timescales such that $f(t) = f(t_s, t_f)$ where $t_s = \epsilon t$ and $t_f = t.$
   - Then
     $\begin{align*}
     \frac{d}{dt} &= \frac{\partial }{\partial t_s} \frac{\partial t_s}{t} + \frac{\partial }{\partial t_f} \frac{\partial t_f}{t} \\
     &= \epsilon \frac{\partial }{\partial t_s} + \frac{\partial}{\partial t_f}\\
     \frac{d^2}{dt^2} &= \epsilon^2\frac{\partial^2}{\partial t_s^2} + 2\frac{\partial^2}{\partial t_s \partial t_f} + \frac{\partial^2}{\partial t_f^2}
     \end{align*}
     $

- We expand the solution f and derivatives with these ansatz
- Terms are collected and then displayed in LaTeX format.

---

2. **WKB Approximation (`WKB_Ansantz`)**: \
   This is used when amplitude changes as a function of time

- We assume there exists a solution $f$ such that $f = f_0 + f_1 + \cdots$
- We assume there are slow and fast timescales such that $f(t) = f(t_s, t_f)$ where $t_s = \frac{g(t)}{\epsilon}$ and $t_f = t$
- Then
  $\frac{d}{dt} &= \frac{\partial }{\partial t_s} \frac{\partial t_s}{t} + \frac{\partial }{\partial t_f} \frac{\partial t_f}{t} $ \\
  $&= \frac{\partial}{\partial t_s} + \frac{g'(t)}{\epsilon} \frac{\partial}{\partial t_f} $\\
  $\frac{\partial^2}{\partial t^2}&= \frac{\partial^2}{\partial t_s^2} + \frac{g''(t)}{\epsilon} \frac{\partial}{\partial t_f} + 2 \frac{g'(t)}{\epsilon} \frac{\partial^2}{\partial t_f \partial t_s} + \frac{(g'(t))^2}{\epsilon^2}\frac{\partial^2}{\partial t_f^2}$
- Now we substitute the expansions of $f$ and it's derivatives.
- The script collects and displays the terms based on powers of $\epsilon$ in LaTeX format.

---

### Prerequisites

Python Packages:

- **SymPy**:
- **NumPy**
- **IPython.display**: For rendering equations in LaTeX format.

---

## Example Workflow: WKB Approximation

```python
  t = symbols('t')
  f_t = symbols('f_t')
  d2 = symbols("d2")
  d = symbols("d")
  epsilon = symbols("epsilon")
  ode = Eq(d2*f_t + (1/epsilon**2)*(t+1)**2*f_t, 0)
  latex_displ = WKB_Ansantz(ode, epsilon, d2, d, f_t)
  display(Math(latex_displ))
```

## Future Improvements

1.
