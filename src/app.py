import seaborn as sns
import streamlit as st

from analysis.figures import make_correlation_heatmap
from data.data_import import import_sleep_data


def main():
    data = import_sleep_data()
    corr_mat = data.corr(numeric_only=True)  # print_correlation_matrix(data)
    corr_fig = make_correlation_heatmap(corr_mat)

    st.set_page_config(page_title="Data-Vis", layout="wide")
    st.title("Data")

    st.subheader("Raw Data")
    st.dataframe(data, hide_index=True)

    st.subheader("Correlation Matrix")
    st.dataframe(corr_mat)

    st.pyplot(corr_fig)


if __name__ == "__main__":
    main()
