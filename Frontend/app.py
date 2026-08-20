import streamlit as st


def login():
    st.header("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin123":
            st.session_state["logged_in"] = True
            st.rerun()
        else:
            st.error("Invalid username or password. Please try again.")


def show_dashboard():

    st.title("Welcome!")

    st.success("Login successful! 🎉")

    st.write("Welcome to the application. You can now access the dashboard.")


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
        
    # Logout button    - dashboard
    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.rerun()


if __name__ == "__main__":
    main()