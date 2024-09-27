import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# st.set_page_config(layout='wide')

st.header("Newton's Divided Difference Interpolation Method")
st.write('\n')
# Initial DataFrame with columns 'x' and 'y'
data = pd.DataFrame({'x': [], 'y': []})

col1, col2 = st.columns([0.5, 2], gap='small', vertical_alignment='top')

with col1:

    st.write('Enter Data')
    # Create an editable DataFrame widget
    edited_data = st.data_editor(data, num_rows='dynamic', use_container_width=True)

# Extract the 'x' and 'y' columns as lists if there are rows
if not edited_data.empty:
    x_list = edited_data['x'].tolist()
    y_list = edited_data['y'].tolist()

    # st.write("X values:", x_list)
    # st.write("Y values:", y_list)

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

        # Create a new list without None values
        new_list = [val for val in column_data if pd.notna(val)]  # Use pd.notna to filter out NaN values

        # Insert None values at the start
        new_list = [None] * none_count + new_list  # Prepend None values to the list

        return new_list


    # Apply the function to each divided difference column
    for col in dd_table.columns[2:]:  # Skip 'x' and 'f(x)'
        dd_table[col] = move_none_to_start(dd_table[col])

    with col2:
        # Display the results using Streamlit
        st.write("Newton's Divided Difference Table:")
        st.dataframe(dd_table, use_container_width=True)

    with col1:
        st.write('\n')
        st.write('\n')
        # Newton's divided difference interpolation to find y(15)
        x_to_predict = st.number_input('x to predict')
    y0 = fx_values[0]  # f(x0), where x0 is the first value in x_values
    result = y0

    # Apply the Newton's interpolation formula
    for level in range(1, n):  # Start from the first divided difference
        term = divided_diff[level][0]  # Get the first term of the divided difference for the current level
        for j in range(level):
            term *= (x_to_predict - x_values[j])  # Multiply by (x - xj)
        result += term  # Add to the result

    with col1:
        # Display the result
        st.write(f"$$Estimated \ value \ : \ $$`{result}`")
        connect_lines = st.checkbox('Connect lines')

    # Creating scatter plot
    fig = go.Figure()

    if connect_lines:
        # Add actual data points with a label for the legend
        fig.add_scatter(x=x_list, y=y_list, mode='markers+lines', name='Data Points')

    else:
        # Add actual data points with a label for the legend
        fig.add_scatter(x=x_list, y=y_list, mode='markers', name='Data Points')

    # Add predicted value with a label for the legend
    fig.add_scatter(x=[x_to_predict], y=[result], mode='markers', name='Predicted Value',
                    marker=dict(color='red', size=7))

    # # Adding annotations for the predicted value
    # fig.add_annotation(x=x_to_predict, y=result, text='Predicted Value', showarrow=True, arrowhead=2)

    # Updating layout for better visibility
    fig.update_layout(title='Scatter Plot with Predicted Value',
                      xaxis_title='X-axis',
                      yaxis_title='Y-axis',
                      showlegend=True)

    with col2:
        st.write('\n')
        st.write('\n')
        # Displaying scatter plot
        st.plotly_chart(fig)