# %% Imports
import time
import streamlit as st
import datetime
from logging_config import log



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


class TimeFunctions:
    # Const
    CURRENT_DATE = time.gmtime()
    MONTHS = ("January", "February", "March", "April", "May", "June", "July",
              "August", "September", "Octuber", "November", "December")
    YEARS = tuple([years for years in range(CURRENT_DATE.tm_year - 7, CURRENT_DATE.tm_year)][::-1])

    def __init__(self):
        self.currentMonth = self.MONTHS[self.CURRENT_DATE.tm_mon - 1]
        self.currentYear = self.CURRENT_DATE.tm_year

    def get_current_month_and_year(self) -> tuple:
        """
        Obtain the current month in name format.
        :return: tuple, Year and the name of the month.
        """
        return self.currentYear, self.currentMonth

    def get_month_and_year(self) -> tuple:
        """
        Get the selected month.
        :return: str, the name of a selected month.
        """
        column1, column2 = st.columns(2)

        with column1:
            monthDate = st.selectbox("Month",
                                     self.MONTHS,
                                     index=self.CURRENT_DATE.tm_mon - 1,
                                     )
        with column2:
            yearDate = st.selectbox("Year",
                                    self.YEARS,
                                    )

        return yearDate, monthDate

    def get_past_month(self) -> tuple:
        """
        Get the previous month name.
        :return: tuple, the name of the previous month.
        """
        return self.currentYear, self.currentMonth
        pass




