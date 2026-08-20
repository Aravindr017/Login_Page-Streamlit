import streamlit as st


def login():
    st.header("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "aravind-admin" and password == "aravind123":
            st.session_state["logged_in"] = True
            st.rerun()
        else:
            st.error("Invalid username or password. Please try again.")


def show_dashboard():

    st.title("Portugal Election 2019")

    st.write(
        "Welcome to the Portugal Election 2019 Dashboard!"
    )

    st.write(
        "This dashboard provides insights and visualizations "
        "related to the 2019 elections in Portugal."
    )

    st.write(
        "Use the sidebar to navigate between different sections "
        "of the dashboard."
    )

    st.sidebar.title("Navigation")

    section = st.sidebar.selectbox(
        "Section",
        ["Overview", "Results", "Analysis"]
    )

    if section == "Overview":

        st.header("Overview")

        st.write(
            "This section provides an overview of the 2019 elections "
            "in Portugal, including key statistics and information "
            "about the electoral process."
        )

    elif section == "Results":

        st.header("Results")

        st.write(
            "This section presents the election results, including "
            "vote counts, percentages, and visualizations of the data."
        )

    elif section == "Analysis":

        st.header("Analysis")

        st.write(
            "This section offers in-depth analysis of the election "
            "results, including trends, comparisons, and insights "
            "derived from the data."
        )

    st.write(
        "Thank you for visiting the Portugal Election 2019 Dashboard!"
    )


def main():

    st.set_page_config(
        page_title="Portugal Election 2019",
        layout="wide"
    )

    # Create login state if it doesn't exist
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    # Decide which page to show
    if st.session_state["logged_in"]:
        show_dashboard()
    else:
        login()
        
    # Logout button    
    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.rerun()


if __name__ == "__main__":
    main()