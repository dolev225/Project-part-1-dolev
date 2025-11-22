from pydantic import BaseModel, ValidationError, field_validator
import logging 
import subprocess


class vm  :
    #def log info
    logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    handlers=[ 
        logging.FileHandler('./logs/log.log')  
    ]
    )
    def user_input():
        machines = [] 
        while True:
            class user(BaseModel,):
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
            # reading form user
            out=input("to stop tipe stop : ")
            if out =='stop':
                logging.info("user stop the reading vm info")
                logging.info("vm info is null do to user stop")
                print("user stop the reading vm info")
                return('null')
            vm_name_input = input("meashin name: ")
            vm_os_input = input(" os : ")
            vm_ram_input = input("ram amount : ")
            vm_cpu_input = input(" cpu amuont: ")


            #validat info is good
            try:
                vm= user(name=vm_name_input, os=vm_os_input,ram=vm_ram_input,cpu=vm_cpu_input)
                print(" User input is  valid :")
                instance_data = {"name": vm_name_input, "os": vm_os_input, "cpu": vm_cpu_input, "ram": vm_ram_input}
                machines.append(instance_data) 
                logging.info("machine info is vlaid")
                return(machines)
            except ValidationError as err:
                print(" Validation error :")
                print("try agine")
                print(err)

    def  run_installer_nginx():
        try:
            result = subprocess.run(
                ["bash", "scripts/install_nginx.sh"],
                check=True,
                capture_output=True,
                text=True
            )
            print("script output:")
            print(result.stdout)
            logging.info("install nginx correctly")
        except subprocess.CalledProcessError as err:
            print("script failed with error:")
            logging.error(f"failed to install nginx do yo {err}")
            print(err.stderr)

        except FileNotFoundError:
            print("cant not found bash script ")

    def  run_installer_pydantic():
        try:
            result = subprocess.run(
                ["bash","scripts/install_pydantic.sh"],
                check=True,
                capture_output=True,
                text=True
            )
            print("script output:")
            logging.info("install pydantic correctly")
            print(result.stdout)

        except subprocess.CalledProcessError as err:
            print("script failed with error:")
            logging.error(f"failed to install pydantic do too {err}")
            print(err.stderr)

        except FileNotFoundError:
            print("cant not found bash script ")
    


