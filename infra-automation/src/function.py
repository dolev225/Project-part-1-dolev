from pydantic import BaseModel, ValidationError, field_validator
import logging 
import subprocess
from machine import Machine
import json

user_input=[]

class function  :
    #def log info
    logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    handlers=[ 
        logging.FileHandler('./logs/log.log')  
    ]
    )
        # reading form user
    def user_input():
        while True :    
        
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
                _machine= Machine(name=vm_name_input, os=vm_os_input,ram=vm_ram_input,cpu=vm_cpu_input)
                print(" User input is  valid :")
                instance_data = {"name": vm_name_input, "os": vm_os_input, "cpu": vm_cpu_input, "ram": vm_ram_input}
                user_input.append(instance_data) 
                logging.info("machine info is vlaid")
                return(user_input)
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

    def save_file(server):
        with open("configs/instances.json","w") as file:
            json.dump(server, file, indent=4)
        print("saving data as json file at configs/instances.json")
        logging.info("machine info has beed save at instances.json")



