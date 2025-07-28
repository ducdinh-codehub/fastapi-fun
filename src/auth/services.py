
from auth.exceptions import login_exception

def login(user_account: str, user_password: str):
    
    response_status = login_exception("success")

    return response_status