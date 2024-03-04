import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="To-Do List App",
    page_icon="✅",
    layout="wide",
    initial_sidebar_state="expanded"
)

def init_dataframe():
    """Initialize or load the dataframe."""
    if 'lists' not in st.session_state:
        st.session_state.lists = {}

def add_task(list_name, task):
    """Add a new task to the specified list."""
    if list_name not in st.session_state.lists:
        st.session_state.lists[list_name] = []
    st.session_state.lists[list_name].append(task)

def display_todo_list(list_name):
    """Display the To-Do list in the app."""
    if list_name in st.session_state.lists:
        st.subheader(f"{list_name} To-Do List:")
        for index, task in enumerate(st.session_state.lists[list_name], start=1):
            st.write(f"{index}. {task}")
    else:
        st.write(f"No tasks added to {list_name} yet.")

def plot_chart():
    """Plot a bar chart based on the number of tasks in each list."""
    lists_counts = {list_name: len(tasks) for list_name, tasks in st.session_state.lists.items()}
    if lists_counts:
        df_counts = pd.DataFrame(lists_counts.items(), columns=['List', 'Number of Tasks'])
        fig, ax = plt.subplots()
        df_counts.plot(kind='barh', x='List', y='Number of Tasks', ax=ax)
        st.pyplot(fig)
    else:
        st.write("No data to display for the chart.")

def main():
    st.title("To-Do List App 📝")

    init_dataframe()

    
    st.markdown("---")
    st.sidebar.header("App Customization")
    background_color = st.sidebar.color_picker("Choose Background Color", "#f0f0f0")
    st.markdown(f"""<style>
                    .reportview-container {{
                        background-color: {background_color};
                    }}
                    </style>""", unsafe_allow_html=True)

   
    with st.sidebar:
        st.header("Add New Task")
        list_name = st.text_input("List Name", "My List")
        task = st.text_input("Task")
        add_button = st.button("Add Task")

    if add_button and task:  
        add_task(list_name, task)

    
    display_todo_list(list_name)

   
    st.markdown("---")
    st.subheader("Task Distribution Chart")
    plot_chart()

if __name__ == "__main__":
    main()


