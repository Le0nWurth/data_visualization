import seaborn as sns
import streamlit as st

from analysis.figures import make_correlation_heatmap, make_scatter_plot
from data.data_import import import_sleep_data


def main():
    data = import_sleep_data()
    corr_mat = data.corr(numeric_only=True)  # print_correlation_matrix(data)
    corr_fig = make_correlation_heatmap(corr_mat)

    # Scatterplots
    sleep_efficiency_deep_sleep = make_scatter_plot(
        data, "Sleep efficiency", "Deep sleep percentage", "Exercise frequency"
    )
    sleep_efficiency_light_sleep = make_scatter_plot(
        data, "Sleep efficiency", "Light sleep percentage"
    )
    sleep_efficiency_awakenings = make_scatter_plot(
        data, "Sleep efficiency", "Awakenings"
    )
    sleep_efficiency_caffeine = make_scatter_plot(
        data, "Sleep efficiency", "Caffeine consumption"
    )
    sleep_efficiency_alcohol = make_scatter_plot(
        data, "Sleep efficiency", "Alcohol consumption"
    )
    sleep_efficiency_exercise = make_scatter_plot(
        data, "Sleep efficiency", "Exercise frequency"
    )

    # UI

    st.set_page_config(page_title="Data-Vis", layout="wide")
    st.title("Data")
    st.subheader("Raw Data")
    st.dataframe(data, hide_index=True)
    col1, col2, col3 = st.columns(3)

    col1.subheader("Correlation Heatmap")
    col1.pyplot(corr_fig)

    col2.subheader("Sleep efficency - Deep sleep - Exercise")
    col2.pyplot(sleep_efficiency_deep_sleep)

    col3.subheader("")
    col3.pyplot(sleep_efficiency_light_sleep)

    col1.subheader("")
    col1.pyplot(sleep_efficiency_awakenings)

    col2.subheader("")
    col2.pyplot(sleep_efficiency_alcohol)

    col3.subheader("")
    col3.pyplot(sleep_efficiency_exercise)

    col1.subheader("")
    col1.pyplot(sleep_efficiency_caffeine)


if __name__ == "__main__":
    main()
