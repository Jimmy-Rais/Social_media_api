from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["Bcrypt"])
def hash(password:str):
    return pwd_context.hash(password)
def verify(password_test,password):
    return pwd_context.verify(password_test,password)