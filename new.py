import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # Non-GUI backend for plotting
#Assumptions 
# q=1 , binary system 

# Show formulas of operating lines
st.markdown("### 🧾 Operating Line Equations")

st.latex(r"\textbf{Rectifying Line:} \quad y = \frac{R}{R + 1}x + \frac{x_D}{R + 1}")

st.latex(r"\textbf{Stripping Section:} \quad y = \left( \frac{L'}{V'} \right)x - \left( \frac{B}{V'} \right)x_B")
st.markdown(r"""
Where:
- \( R \) = Reflux Ratio  
- \( x_D \) = Distillate composition  
- \( x_B \) = Bottom composition  
- \( x_F \) = Feed composition  

""")


# --- Streamlit UI ---
st.set_page_config(page_title=" Distillation", layout="centered")
st.title("Binary Distillation Column Design")

st.sidebar.header("🔧 Input Parameters")
xF = st.sidebar.slider("Feed composition (xF)", 0.0, 1.0, 0.5, 0.01)
xD = st.sidebar.slider("Distillate composition (xD)", xF, 1.0, 0.9, 0.01)
xB = st.sidebar.slider("Bottom composition (xB)", 0.0, xF, 0.1, 0.01)
R = st.sidebar.slider("Reflux Ratio (R)", 0.5, 10.0, 2.5, 0.1)
alpha = st.sidebar.slider("Relative Volatility (α)", 1.1, 5.0, 2.5, 0.1)

# --- Equilibrium Curve ---
x = np.linspace(0, 1, 500)
y_eq = (alpha * x) / (1 + (alpha - 1) * x)

# --- Operating Lines ---
def rectifying_line(x): return (R / (R + 1)) * x + xD / (R + 1)
x_int = xF
y_int = rectifying_line(x_int)

def stripping_line(x): return ((y_int - xB) / (x_int - xB)) * (x - xB) + xB
# --- Construct only 2 trays starting from (xD, xD) ---
tray_steps_x = [xD]
tray_steps_y = [xD]

x_current = xD



# --- Plotting ---
fig, ax = plt.subplots(figsize=(7, 7))

# Plot Equilibrium
ax.plot(x, y_eq, label="Equilibrium Curve", color="blue")
ax.plot(x, x, '-', label="y = x", color="black")

# Plot Operating Lines
x_rect = np.linspace(xF, xD, 100)
ax.plot(x_rect, rectifying_line(x_rect), color="red", label="Rectifying Section")
x_strip = np.linspace(xB, xF, 100)
ax.plot(x_strip, stripping_line(x_strip), color="green", label="Stripping Section")

# Feed line goes from y_int to xF (where it intersects y = x line)
ax.plot([xF, xF], [xF, y_int], color="purple", linestyle="dashdot", label="Feed Line (q = 1)")


# Plot Stages (stepwise)


# Labels
ax.set_xlabel("x (Liquid mole fraction)")
ax.set_ylabel("y (Vapor mole fraction)")
ax.set_title("Operating Line representation")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.grid(True)
ax.legend()

# Show plot
st.pyplot(fig)
