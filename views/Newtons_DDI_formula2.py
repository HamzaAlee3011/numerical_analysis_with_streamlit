import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import sympy as sp


# Function for creating intervals at which the values of SF and BM is to be find
def create_intervals(x_list_original, interval):
    """
    Creates a list of specified intervals along the x-axis based on the original x_list.

    Parameters:
    x_list_original (list): A list of x-values (such as beam lengths).
    interval (float): The interval value at which to create points.

    Returns:
    list: A list of interval points along the x-values.
    """
    # Input validation with warnings
    if not x_list_original:
        st.warning("The list of x-values cannot be empty.")
        return []

    if interval <= 0:
        st.warning("Interval must be a positive number.")
        return []

    if x_list_original[-1] <= 0:
        st.warning("The maximum x-value must be positive.")
        return []

    if interval > (x_list_original[-1] - x_list_original[0]):
        st.warning("The interval is too large for the range of x-values.")
        return []

    # Initialize the list and starting point
    intervals = []
    current_point = x_list_original[0]

    # Generate intervals using a loop
    while current_point <= x_list_original[-1]:
        intervals.append(round(current_point, 2))  # Keep values rounded for consistency
        current_point += interval

    # Check if the last point (x_list_original[-1]) is already in the intervals (avoid rounding issues)
    if round(intervals[-1], 2) != round(x_list_original[-1], 2):
        intervals.append(round(x_list_original[-1], 2))

    return intervals


def scatter_plot_normal():
    # Creating scatter plot
    fig = go.Figure()

    if connect_interpolated_points:
        fig.add_scatter(x=x_list, y=y_list, mode='markers+lines', line_shape='spline', name='Data Points')
    else:
        fig.add_scatter(x=x_list, y=y_list, mode='markers', name='Data Points')

    # Add the predicted value to the plot
    fig.add_scatter(x=[x_to_predict], y=[result], mode='markers', name='Predicted Value',
                    marker=dict(color='red', size=7))

    # Updating layout for better visibility
    fig.update_layout(title='Scatter Plot with Predicted Value',
                      xaxis_title='X-axis',
                      yaxis_title='Y-axis',
                      showlegend=True)

    # Display the scatter plot
    st.plotly_chart(fig)


inter_polated_x_values = []
inter_polated_y_values = []


def scatter_plot_sympy_interploated():
    # Step 1: Define the symbol for x
    x = sp.Symbol('x')

    # Step 2: Data points (x-values and y-values in two separate lists)
    x_values = x_list  # From dataframe
    y_values = y_list  # From dataframe

    # Step 3: Combine the x and y values into pairs
    data_points = list(zip(x_values, y_values))

    # Step 4: Create the polynomial equation that fits the data points
    poly_eq = sp.interpolate(data_points, x)

    # Step 5: Extract coefficients and convert to exact fractions
    poly = sp.Poly(poly_eq, x)  # Get the polynomial
    fractional_coeffs = [sp.Rational(c).limit_denominator() for c in poly.all_coeffs()]  # Convert to Rational

    # Step 6: Rebuild the polynomial equation with fractional coefficients
    fractional_eq = sum(
        [fractional_coeffs[i] * x ** (len(fractional_coeffs) - 1 - i) for i in range(len(fractional_coeffs))])

    # Step 7: Generate y values for x values
    for i in create_intervals(x_values, interval=interval):
        y_value = poly_eq.subs(x, i)  # Substitute x = i into the equation
        inter_polated_x_values.append(i)
        inter_polated_y_values.append(float(y_value))  # Use float for plot

    # Creating scatter plot
    fig = go.Figure()

    if connect_interpolated_points:
        fig.add_scatter(x=inter_polated_x_values, y=inter_polated_y_values, mode='markers+lines', line_shape='spline',
                        name='Interpolated Data Points')
    else:
        fig.add_scatter(x=inter_polated_x_values, y=inter_polated_y_values, mode='markers',
                        name='Interpolated Data Points')

    # Adding original data points
    if connect_original_points:
        fig.add_scatter(x=x_values, y=y_values, mode='markers+lines', name='Original Data Points', line_shape='linear',
                        marker=dict(color='yellow', size=7))
    else:
        fig.add_scatter(x=x_values, y=y_values, mode='markers', name='Original Data Points',
                        marker=dict(color='yellow', size=7))

    # Add the predicted value to the plot
    fig.add_scatter(x=[x_to_predict], y=[result], mode='markers', name='Predicted Value',
                    marker=dict(color='red', size=7))

    # Updating layout for better visibility
    fig.update_layout(
        title=graph_title_input,
        xaxis_title=xaxis_title_input,
        yaxis_title=yaxis_title_input,
        showlegend=True,
        xaxis=dict(showgrid=True),  # Enable grid on the X-axis
        yaxis=dict(showgrid=True)  # Enable grid on the Y-axis
    )


    # Display the scatter plot
    st.plotly_chart(fig)

    # Display the equation in LaTeX format with fractional coefficients
    col1a, col1b = st.columns([1, 1], gap='small')
    with col1a:
        st.write("Fitted Polynomial f(x):")
        st.latex(sp.latex(fractional_eq))  # Display the equation with fractional coefficients

        # Convert the SymPy equation to string
        equation_str = str(fractional_eq)

        # Replace '**' with '^' for a more mathematical look
        equation_str = equation_str.replace('**', '^')

        st.code(f'y = {equation_str}')


# st.set_page_config(layout='wide')

st.header("Newton's Divided Difference Interpolation Method")
st.write('\n')

# Initial DataFrame with columns 'x' and 'y'
data = pd.DataFrame({'x': [], 'y': []})

# Radio button for input selection
input_selection = st.radio('Select Mode of Input of Data',
                           options=['From file (CSV)', 'Direct Manual Input'])

# Initialize final_data to avoid 'UnboundLocalError'
final_data = pd.DataFrame()

col1, col2 = st.columns([0.5, 2], gap='small')

# Input mode: From file (CSV)
if input_selection == 'From file (CSV)':
    uploaded_file = st.file_uploader('Upload Data File', type='csv')
    if uploaded_file:
        # Read uploaded file and extract CSV data
        final_data = pd.read_csv(uploaded_file)

        # Display uploaded data
        df_table = st.dataframe(final_data)

# Input mode: Direct Manual Input
else:
    with col1:
        st.write('Enter Data')
        # Create an editable DataFrame widget
        final_data = st.data_editor(data, num_rows='dynamic', use_container_width=True)

# Extract the 'x' and 'y' columns as lists if data is available
if not final_data.empty:
    x_list = final_data['x'].tolist()
    y_list = final_data['y'].tolist()

    # Define x and f(x) values (the known data points)
    x_values = x_list
    fx_values = y_list

    # Create a DataFrame to store x, f(x), and divided differences
    n = len(x_values)
    dd_table = pd.DataFrame(columns=['x', 'f(x)'] + [f'{i + 1} - DD' for i in range(n - 1)])

    # Initialize the table with x and f(x) values
    dd_table['x'] = x_values
    dd_table['f(x)'] = fx_values

    # Create a list of lists to store divided differences
    divided_diff = [fx_values.copy()]

    # Calculate the divided differences
    for level in range(1, n):  # Level represents 1st DD, 2nd DD, etc.
        current_diff = []
        for i in range(n - level):
            diff = (divided_diff[level - 1][i + 1] - divided_diff[level - 1][i]) / (x_values[i + level] - x_values[i])
            current_diff.append(diff)
        divided_diff.append(current_diff)

        # Fill the appropriate rows in the DataFrame with the current divided differences
        dd_table[f'{level} - DD'] = [*current_diff, *[None] * level]


    # Function to move None values to the start of each DD list
    def move_none_to_start(column_data):
        none_count = column_data.isna().sum()  # Count None (NaN) values
        new_list = [val for val in column_data if pd.notna(val)]  # Filter out NaN values
        new_list = [None] * none_count + new_list  # Prepend None values to the list
        return new_list


    # Apply the function to each divided difference column
    for col in dd_table.columns[2:]:  # Skip 'x' and 'f(x)'
        dd_table[col] = move_none_to_start(dd_table[col])

    # Display the results using Streamlit
    st.write("Newton's Divided Difference Table:")
    st.dataframe(dd_table, use_container_width=True)

    col3, col4 = st.columns([1, 2], gap='small', vertical_alignment='bottom')

    with col3:
        # Input for the x value to predict
        x_to_predict = st.number_input('x to predict', value=float(x_values[0]), format="%0.4f")

    y0 = fx_values[0]  # f(x0), where x0 is the first value in x_values
    result = y0

    # Apply the Newton's interpolation formula
    for level in range(1, n):
        term = divided_diff[level][0]
        for j in range(level):
            term *= (x_to_predict - x_values[j])  # Multiply by (x - xj)
        result += term

    with col4:
        # Display the interpolated result
        st.code(f'Result: {result}', language='python')

    with st.container(border=True):
        col6, col7 = st.columns(2, gap='small')

        with col6:
            # Checkbox for line connection of interpolated points
            connect_interpolated_points = st.checkbox('Connect interpolated points')

            # Checkbox for line connection of original points
            connect_original_points = st.checkbox('Connect original data points')

        with col7:
            # X-axis title
            xaxis_title_input = st.text_input('Title x-axis', value='x-axis')

            # Y-axis title
            yaxis_title_input = st.text_input('Title y-axis', value='y-axis')

            # Graph Title
            graph_title_input = st.text_input('Graph Title', value='Scatter Plot with Predicted Value')

    with st.container(border=True):
        col8, col9 = st.columns([0.6, 3], gap='small')

        with col8:
            # Interval at which the points have to find out
            interval = st.number_input('Intervals', value=0.0000, min_value=0.0000, format="%0.4f")

        with col9:
            # scatter_plot_normal()
            scatter_plot_sympy_interploated()

        with col8:
            # Displaying interpolated values of y at x

            interpolated_df = pd.DataFrame({'x': inter_polated_x_values,
                                            'y': inter_polated_y_values})

            interpolated_dataframe_table = st.dataframe(interpolated_df, use_container_width=True)


