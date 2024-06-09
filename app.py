# Brian Lesko  
# 6/6/2024
# Derive the equations of motion for a mass-spring-damper system
# and simulate the system 

import numpy as np
import plotly.graph_objects as go
import streamlit as st
import scipy 

with st.sidebar: 
    st.header('The math behind this simulation:')
    # Show the schematic of the mass-spring-damper system
    st.markdown('## Mass-Spring-Damper System')
    st.image("schematic.png", use_column_width=True)
    st.write("""
            f(t)	=	external force applied on mass  (input)  
            z(t)	=	position	unknown  (output)  
            m	=	mass  
            k	=	spring constant  
            b	=	damping coefficient  
            """)

    # Show the free body diagram of the mass-spring-damper system
    st.markdown('## Free Body Diagram')
    st.image("free_body_diagram.png", use_column_width=True)

    # The equation of motion for the mass-spring-damper system is given by:
    st.write("The equation of motion for the mass-spring-damper system is given by:")
    st.write("m*x'' + c*x' + k*x = F(t)")

    st.write("The Laplace transform of the equation of motion is:")
    st.write("m*s^2*X(s) + c*s*X(s) + k*X(s) = F(s)")

    st.write("solving for X(s)/F(s) the output over the input gives:")
    st.write("X(s)/F(s) = 1/(m*s^2 + c*s + k)")
    st.write("This is called the transfer function of the system")

    # show the block diagram of the mass-spring-damper system
    st.markdown('## Block Diagram')
    st.image("block_diagram.png", use_column_width=True)


# Define the mass-spring-damper system
num = [1]
den = [1, 1, 1]
sys = scipy.signal.TransferFunction(num, den)

# Define the time vector
t = np.linspace(0, 10, 10000)

# Step response
t, y = scipy.signal.step(sys, T=t)

st.title("Mass-Spring-Damper System Simulations")

# plot the step response and impulse response
fig = go.Figure()
fig.add_trace(go.Scatter(x=t, y=y))
fig.update_layout(title='Step Response: constant 1 N force', xaxis_title='Time (s)', yaxis_title='Position (m)')
st.plotly_chart(fig)

# impulse response
t, y = scipy.signal.impulse(sys, T=t)

fig = go.Figure()
fig.add_trace(go.Scatter(x=t, y=y))
fig.update_layout(title='Impulse Response: 1 Ns input at t=0', xaxis_title='Time (s)', yaxis_title='Position (m)')
st.plotly_chart(fig)