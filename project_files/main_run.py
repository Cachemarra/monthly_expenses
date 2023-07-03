# %% Imports
import streamlit as st
from logging_config import log
from layout import init_page


# Execution function
def run():
    init_page()
    pass


# %% Main run
if __name__ == "__main__":
    log.basicConfig(level=log.DEBUG)

    run()


