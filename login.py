import yaml
import streamlit as st
from streamlit import Server
import streamlit_authenticator as stauth

from yaml.loader import SafeLoader
with open('../config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Load configuration from YAML file
with open('../config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

# Define Streamlit session state
def get_session():
    return Server.get_current()._session_info.session

def login():
    session = get_session()
    if session.state.authentication_status:
        authenticator.logout('Logout', 'main')
        st.write(f'Welcome *{session.state.name}*')
        st.title('Some content')
    elif session.state.authentication_status == False:
        st.error('Username/password is incorrect')
    elif session.state.authentication_status is None:
        st.warning('Please enter your username and password')

# Authenticator class
class Authenticator:
    def __init__(self, credentials, cookie_name, cookie_key, cookie_expiry_days, preauthorized):
        self.credentials = credentials
        self.cookie_name = cookie_name
        self.cookie_key = cookie_key
        self.cookie_expiry_days = cookie_expiry_days
        self.preauthorized = preauthorized

    def login(self, username, password):
        # Your authentication logic goes here
        pass

    def logout(self, logout_message, redirect_key):
        # Your logout logic goes here
        pass

# Create an instance of Authenticator
authenticator = Authenticator(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# Main authentication logic
if __name__ == "__main__":
    name, authentication_status, username = authenticator.login('Login', 'main')
    login()

