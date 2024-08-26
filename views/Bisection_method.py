import streamlit as st
import sympy as sp

tab1, tab2 = st.tabs(["Main Application", "Symbols Guide"])

with tab1:
    # Main function for calculating root upto iterations
    def calculate_upto_iteration():
        global a, b, iteration, convert_function
        for i in range(iteration):
            ai = a
            bi = b
            i += 1
            x_mid = (a + b) / 2
            fx = convert_function.subs(x, x_mid).evalf()

            if fx < 0:
                a = x_mid
            else:
                b = x_mid

            xi.append(x_mid)
            iteration_list.append(i)
            a_list.append(str(ai))  # Convert the number to a string to preserve full precision
            b_list.append(str(bi))
            xi_list.append(str(x_mid))
            fx_list.append(str(fx))

        return xi_list[iteration-1]

    # Main function for calculating root upto accuracy
    def calculate_upto_accuracy():
        global a, b, accuracy, convert_function
        i = -1
        iteration = 0
        while True:
            ai = a
            bi = b
            i += 1
            iteration += 1
            x_mid = (a + b) / 2
            fx = convert_function.subs(x, x_mid).evalf()

            if fx < 0:
                a = x_mid
            else:
                b = x_mid

            # Format x_mid to the desired accuracy and compare
            if f"{x_mid:.{accuracy}f}" == f"{xi[i]:.{accuracy}f}":
                break

            xi.append(x_mid)
            iteration_list.append(iteration)
            a_list.append(str(ai))  # Convert the number to a string to preserve full precision
            b_list.append(str(bi))
            xi_list.append(str(x_mid))
            fx_list.append(str(fx))

    with st.container(border=True):
        mode = st.radio('Mode of Analysis',
                        ["Finding root upto (n) number of decimal places", "Finding root upto (n) number of iterations"])

    st.write('\n')
    input_function = st.text_input("Function (fx)", value='')

    # Check if the input function is valid
    if not input_function:
        st.error("Please provide a function to calculate the root.")
    else:
        try:
            x = sp.symbols('x')
            # Convert the input function using sympy
            convert_function = sp.sympify(input_function)
        except sp.SympifyError:
            st.error("Invalid function syntax. Please check your input and try again.")
        else:
            st.write('\n')
            col1a, col1b, col1c = st.columns(3, gap='small')
            with col1a:
                a = st.number_input('**a (-)**', help='must be giving negative value when inputted into function')
            with col1b:
                b = st.number_input('**b (+)**', help='must be giving positive value when inputted into function')
            with col1c:
                if mode == "Finding root upto (n) number of decimal places":
                    accuracy = st.number_input('**Accuracy**', min_value=0, max_value=100,
                                               help='Upto n decimal places the value is to be find')

                else:
                    iteration = st.number_input('**No. of Iterations**', min_value=1,
                                                help='Upto n iterations the value is to be find')

            xi = [0]  # initial xi value

            # Table data preparation
            iteration_list = []
            a_list = []
            b_list = []
            xi_list = []
            fx_list = []

            table_data = {"Iteration": iteration_list,
                          "a": a_list,
                          "b": b_list,
                          'xi': xi_list,
                          "f(xi)": fx_list}

            if mode == "Finding root upto (n) number of decimal places":
                calculate_upto_accuracy()
            else:
                calculate_upto_iteration()

            st.dataframe(table_data, use_container_width=True)

            if mode == "Finding root upto (n) number of decimal places":
                st.write(f'### Desired Root: :blue-background[***{xi[-1]:.{accuracy}f}***]')
            else:
                st.write(f'### Desired Root: :blue-background[***{calculate_upto_iteration()}***]')


with tab2:
    st.title("Symbolic Expression Guide")
    st.write("""
    Welcome to the Symbolic Expression Guide! This guide will help you write mathematical expressions in a format that is compatible with the python program.
     """)

    with st.expander('Basic Arithmetic Operations'):
        st.write("""
        - **Addition**: `+`
        - **Subtraction**: `-`
        - **Multiplication**: `*`
        - **Division**: `/`
        - **Square Root**: `sqrt()` (e.g., `sqrt(x)` for $$\sqrt{x}$$)
        - **Exponentiation**: `^` (e.g., `x^2` for $$x^2$$)
        """)

    with st.expander("Exponential and Logarithmic Functions"):
        st.write("""
        - **Exponential Function**: `exp(x)` for $$e^x$$
        - **Natural Logarithm**: `log(x)` for $$\ln(x)$$
        - **Logarithm with Base 10**: `log(x, 10)` for $$\log_{10}(x)$$
        - **Logarithm with Custom Base**: `log(x, base)` for $$\log_{{base}}(x)$$
        """)

    with st.expander("Trigonometric Functions"):
        st.write("""
        - **Sine**: `sin(x)` for $$\sin(x)$$
        - **Cosine**: `cos(x)` for $$\cos(x)$$
        - **Tangent**: `tan(x)` for $$tan(x)$$
        - **Cotangent**: `cot(x)` for $$\cot(x)$$
        - **Secant**: `sec(x)` for $$\sec(x)$$
        - **Cosecant**: `csc(x)` for $$\csc(x)$$
        """)

    with st.expander("Inverse Trigonometric Functions"):
        st.write("""
        - **Arcsine**: `asin(x)` for $$\sin^{-1}(x)$$
        - **Arccosine**: `acos(x)` for $$\cos^{-1}(x)$$
        - **Arctangent**: `atan(x)` for $$tan^{-1}(x)$$
        - **Arccotangent**: `acot(x)` for $$\cot^{-1}(x)$$
        - **Arcsecant**: `asec(x)` for $$\sec^{-1}(x)$$
        - **Arccosecant**: `acsc(x)` for $$\csc^{-1}(x)$$
        """)

    with st.expander("Hyperbolic Functions"):
        st.write("""
        - **Hyperbolic Sine**: `sinh(x)` for $$\sinh(x)$$
        - **Hyperbolic Cosine**: `cosh(x)` for $$\cosh(x)$$
        - **Hyperbolic Tangent**: `tanh(x)` for $$tanh(x)$$
        - **Hyperbolic Cotangent**: `coth(x)` for $$\coth(x)$$
        - **Hyperbolic Secant**: `sech(x)` for $${sech}(x)$$
        - **Hyperbolic Cosecant**: `csch(x)` for $${csch}(x)$$
        """)

    with st.expander("Inverse Hyperbolic Functions"):
        st.write("""
        - **Inverse Hyperbolic Sine**: `asinh(x)` for $$\sinh^{-1}(x)$$
        - **Inverse Hyperbolic Cosine**: `acosh(x)` for $$\cosh^{-1}(x)$$
        - **Inverse Hyperbolic Tangent**: `atanh(x)` for $$tanh^{-1}(x)$$
        - **Inverse Hyperbolic Cotangent**: `acoth(x)` for $$\coth^{-1}(x)$$
        - **Inverse Hyperbolic Secant**: `asech(x)` for $${sech}^{-1}(x)$$
        - **Inverse Hyperbolic Cosecant**: `acsch(x)` for $${csch}^{-1}(x)$$
        """)

    with st.expander("Common Constants"):
        st.write("""
        - **Pi**: `pi` for $$\pi$$
        - **Euler's Number**: `E` for $$e$$
        - **Imaginary Unit**: `I` for $$i$$ (the square root of -1)
        """)

    st.subheader("Example Expressions")
    st.write("""
    Here are a few example expressions to illustrate how to use these symbols in practice:
    - **Quadratic Equation**: `x**2 + 3*x + 2`
    - **Exponential Growth**: `exp(x) + 5`
    - **Sine Wave**: `sin(2*pi*x)`
    - **Logarithmic Decay**: `log(x, 10) - x/2`
    """)
    st.write("""
    You can copy and paste these examples directly or modify them according to your needs.
    """)
