from auth.constants import response_status

def login_exception(status: str):
    match status:
        case response_status.success:
            return {"message": "Login Success", "code": "200"}
        case response_status.error:
            return {"message": "Login faild", "code": "500"}
    