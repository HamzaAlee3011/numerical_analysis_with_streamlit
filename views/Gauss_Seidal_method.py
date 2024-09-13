import streamlit as st
from sympy import symbols, Eq, solve, sympify
import pandas as pd
import re

@st.dialog('Instructions')
def instruction():
    # Display the instructions
    st.markdown(
        """
        ### Important Points
        - The system of equations should only include variables **x**, **y**, and **z**.
        - Equations must be input in a form consistent with a **Diagonally Dominant System**; otherwise, the solver may not converge to a solution.

        #### Example Equations
        Below are examples of equations that fit the required format:

        - $6x - 2y + z = 11$
        - $3x - 5y - 0.2z = 75$
        - $2x + 3y + 11z = 43$

        #### Example of a Diagonally Dominant Matrix
        A matrix is considered diagonally dominant if, in each row of the matrix, the absolute value of the diagonal element is greater than or equal to the sum of the absolute values of the other elements in that row.

        Here is an example of a diagonally dominant matrix:
        """
    )

    # Display the matrix
    st.latex(
        r"""
        \begin{pmatrix}
        10 & -1 & 2 \\
        -1 & 11 & -1 \\
        2 & -1 & 10
        \end{pmatrix}
        """
    )


colf1, colf2, colf3 = st.columns([1, 2, 1], gap='small')
with colf2:
    st.header('Gauss Seidel Method')
    st.write('\n')

# Instruction Button
inst_button = st.button('Instructions')
if inst_button:
    instruction()

# Define symbols
x, y, z = symbols('x y z')

# Input equations from user
eq1_input = st.text_input("1st equation")
eq2_input = st.text_input("2nd equation")
eq3_input = st.text_input("3rd equation")
iteration = st.number_input('No. of Iterations', min_value=0, value=0)

# Function to add multiplication symbol between numbers and variables
def preprocess_equation(eq):
    # Insert * between a number and a variable (e.g., "3x" becomes "3*x")
    return re.sub(r'(\d)([a-zA-Z])', r'\1*\2', eq)

# Lists for storing x, y, and z values for display as table
i_values = []
x_values = []
y_values = []
z_values = []



if eq1_input and eq2_input and eq3_input:
    try:
        # Preprocess the input equations to add multiplication symbols
        eq1_input = preprocess_equation(eq1_input)
        eq2_input = preprocess_equation(eq2_input)
        eq3_input = preprocess_equation(eq3_input)

        # Parse the input equations using sympify
        eq1_converted = Eq(sympify(eq1_input.split('=')[0]), sympify(eq1_input.split('=')[1]))
        eq2_converted = Eq(sympify(eq2_input.split('=')[0]), sympify(eq2_input.split('=')[1]))
        eq3_converted = Eq(sympify(eq3_input.split('=')[0]), sympify(eq3_input.split('=')[1]))

        # Solve for x, y, and z
        x0 = solve(eq1_converted, x)[0]
        y0 = solve(eq2_converted, y)[0]
        z0 = solve(eq3_converted, z)[0]

        yi = 0
        zi = 0

        for j in range(iteration):
            # Substitute current values of y and z into the equation for x
            substituted_x0 = x0.subs({y: float(yi), z: float(zi)})

            # Substitute current values of x and z into the equation for y
            substituted_y0 = y0.subs({x: float(substituted_x0), z: float(zi)})

            # Substitute current values of x and y into the equation for z
            substituted_z0 = z0.subs({x: float(substituted_x0), y: float(substituted_y0)})

            yi = substituted_y0
            zi = substituted_z0


            # Store values for displaying in the table without rounding

            # x_values.append(eval(str(substituted_x0)))
            # y_values.append(eval(str(substituted_y0)))
            # z_values.append(eval(str(substituted_z0)))

            i_values.append(j)
            x_values.append(substituted_x0)
            y_values.append(substituted_y0)
            z_values.append(substituted_z0)
        # Display the results in a table
        table = pd.DataFrame({'Iteration': i_values,
                              'x': x_values,
                              'y': y_values,
                              'z': z_values})

        st.write('\n')
        # Display the results in a table with full precision
        st.dataframe(
            table,
            hide_index=True,
            use_container_width=True
        )

        if i_values:
            st.write(f'### x =  :blue-background[***{x_values[-1]}***]')
            st.write(f'### y = :blue-background[***{y_values[-1]}***]')
            st.write(f'### z = :blue-background[***{z_values[-1]}***]')

    except Exception as e:
        st.error(f"Error parsing the equation: {e}")
