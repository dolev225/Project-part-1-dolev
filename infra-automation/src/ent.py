from pydantic import BaseModel, ValidationError, field_validator
import logging

 #def log info
logging.basicConfig(
level=logging.INFO,
format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
handlers=[ 
    logging.FileHandler('./logs/log.log')  
]
)

class machine(BaseModel):
    name: str
    os: str
    ram :int
    cpu:int

    # crreating chaking  for info
    @field_validator("name")
    def validate_name(cls, value):
        if len(value) > 20:
            logging.error("user enter more then 20 characters")
            raise ValueError(" Name cannot exceed 20 characters")
        return value

    @field_validator("os")
    def validate_os(cls, value):
        if value.lower() == 'windows' or value.lower()== 'ubuntu':
            return value
        else:
            logging.error("user enter rowng os ")
            raise ValueError(" OS must be either 'windows' or 'ubuntu'")
    
    @field_validator("ram")
    def validate_ram(cls, value):
        if  not ((1 <= value) and (value <=1024)):
            logging.error("user enter rowng rum number")
            raise ValueError("ram amont is in 1 to 1024kb'")
        return value

    @field_validator("cpu")
    def validate_cpu(cls, value):
        if not ((1 <= value) and (value <=64)) :
            logging.error("user enter rowng cpu number")
            raise ValueError("cpu mast be betin 1 <64")
        return value
    
    