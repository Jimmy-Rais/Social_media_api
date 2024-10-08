from fastapi import Depends,status,HTTPException
from jose import JWTError,jwt
from datetime import datetime,timedelta, timezone
from . import schemas,config
from fastapi.security import OAuth2PasswordBearer
Oauth2_scheme=OAuth2PasswordBearer(tokenUrl="token")
#Secret key and algorithm used for jwt auth
SECRET_KEY=config.settings.secret_key
ALGORITHM =config.settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = 60
def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp':expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return {'jwt_token':encoded_jwt,'token_type':'bearer'}
def verify_token(token:str,credentials_exception):
    try:
       payload= jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
       id:str=payload.get('id')
       if id is None:
         raise credentials_exception
       token_data=schemas.TokenData(id=str(id)) 
    except JWTError:
        raise credentials_exception
    return token_data
def get_current_user(token:str=Depends(Oauth2_scheme)):
    credentials_exception=HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,detail="Could not validate credentials",
        headers={"WWW-Authenticate":"Bearer"}
        )
    return verify_token(token,credentials_exception) 