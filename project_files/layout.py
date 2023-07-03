# %% Imports
import streamlit as st
from time_functions import get_month_and_year, get_current_month_and_year, get_current_semester
from logging_config import log



def init_page():
    initialize_sidebar()
    pass

# %% Functions
def initialize_sidebar():
    with st.sidebar :
        st.title("Budgets")
        # st.sidebar.markdown("## Select Month")
        radioMonth = select_month_radio()

        # Selecting the date
        if radioMonth == "Other":
            year, month = get_month_and_year()

        else:
            year, month = get_current_month_and_year()
            st.markdown(f"**{year}, {month}**")

        log.debug(f"Year: {year}, month: {month}")


def body():







def select_month_radio():
    return st.radio("## Select Month",
                    ("Actual Month", "Other"),
                    )


