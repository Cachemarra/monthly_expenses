# %% Imports
import streamlit as st
from time_functions import get_month_and_year, get_current_month_and_year, TimeFunctions
from logging_config import log

timeFunctions = TimeFunctions()


def init_page():
    st.set_page_config("Monthly expenses",
                       "🧮",
                       initial_sidebar_state="expanded",
                       layout="wide",
                       )

    st.header(" ")
    initialize_sidebar()

    body()


    pass

# %% Functions
def initialize_sidebar():
    with st.sidebar :
        st.title("Budgets")
        # st.sidebar.markdown("## Select Month")
        radioMonth = select_month_radio()

        # Selecting the date
        if radioMonth == "Other":
            year, month = timeFunctions.get_month_and_year() # get_month_and_year()

        else:
            year, month = timeFunctions.get_current_month_and_year() # get_current_month_and_year()
            st.markdown(f"**{year}, {month}**")

        log.debug(f"Year: {year}, month: {month}")


def body():
    st.title("Monthly expenses project")







def select_month_radio():
    return st.radio("## Select Month",
                    ("Actual Month", "Other"),
                    )


