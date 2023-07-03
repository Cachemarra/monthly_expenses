# %% Imports
import time
import streamlit as st
import datetime
from logging_config import log


# Const
CURRENT_DATE = time.gmtime()
MONTHS = ("January", "February", "March", "April", "May", "June", "July",
          "August", "September", "Octuber", "November", "December")
YEARS = tuple([years for years in range(CURRENT_DATE.tm_year - 7, CURRENT_DATE.tm_year)][::-1])



# %% Functions
def get_current_month_and_year() -> tuple:
    """
    Obtain the current month in name format.
    :return: str, the name of the month.
    """
    return CURRENT_DATE.tm_year, MONTHS[CURRENT_DATE.tm_mon]



def get_current_semester():
    pass


def get_past_month() -> str:
    """
    Get the previous month name.
    :return: str, the name of the previous month.
    """
    pass


def get_month_and_year() -> tuple:
    """
    Get the selected month.
    :return: str, the name of a selected month.
    """
    column1, column2 = st.columns(2)

    with column1:
        monthDate = st.selectbox("Month",
                                 MONTHS,
                                 index=CURRENT_DATE.tm_mon,
                                )
    with column2:
        yearDate = st.selectbox("Year",
                                YEARS,
                               )

    return yearDate, monthDate







