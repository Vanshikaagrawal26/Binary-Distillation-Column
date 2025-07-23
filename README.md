# 🧪 McCabe-Thiele Distillation Visualizer

An interactive Streamlit app to visualize the **McCabe-Thiele method** for binary distillation.  
This tool helps you understand how **equilibrium stages**, **operating lines**, and **feed conditions** determine the design of a distillation column.

---

## 📌 Features

- Interactive sliders for:
  - Feed composition (`xF`)
  - Distillate composition (`xD`)
  - Bottom composition (`xB`)
  - Reflux ratio (`R`)
  - Relative volatility (`α`)
- Assumes **q = 1** (saturated liquid feed)
- Plots:
  - Equilibrium curve
  - Rectifying section line
  - Stripping section line
  - Feed line (vertical, since `q = 1`)
  - Only **2 trays** (stepwise construction)
- Displays **operating line equations** in both:
  - Slope-intercept form
  - Flow-rate form

---

## 🧮 Operating Line Equations

**Rectifying Section:**

y = (R / (R + 1)) * x + xD / (R + 1)


**Stripping Section:**

y = ((y_int − xB) / (xF − xB)) * (x − xB) + xB


**Flow-based Stripping Line:**

y = (L′ / V′) * x − (B / V′) * xB
