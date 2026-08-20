import streamlit as st      # streamlit library for building web apps


def login():
    st.header("Login Page")

    username = st.text_input("Username" , help="Enter your username" , placeholder="admin")
    password = st.text_input("Password", value="admin123", help="Enter your password", placeholder="admin123")

    st.info('Please enter above username and password to login. (Hint: admin/admin123)')

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