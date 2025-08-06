from ..auth.constants import response_status as status

def login_exception(status: str):
    match status:
        case status.success:
            return {"message": "Login Success", "code": "200"}
        case status.error:
            return {"message": "Login faild", "code": "500"}
    