import numpy as np
import streamlit as st

def calculate_stdev(values):
    mean = np.mean(values)
    st_dev = np.sqrt(np.sum((values - mean)**2) / (len(values) - 1))
    return st_dev

def main():
    st.title("Standard Deviation Calculator")

    input_values = st.text_input("Enter values (comma-separated):")
    values = [int(x.strip()) for x in input_values.split(',') if x.strip()]

    if len(values) >= 2:
        st_dev = calculate_stdev(values)
        st.success(f"Standard Deviation: {st_dev:.2f}")
    elif input_values:
        st.warning("Enter at least two values.")

if __name__ == "__main__":
    main()
