from machine import vm
import json
import logging 

def save_file(server):
    with open("configs/instances.json","w") as file:
        json.dump(server, file, indent=4)
    print("saving data as json file at configs/instances.json")
    logging.info("machine info has beed save at instances.json")

#define logging info
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    handlers=[ 
        logging.FileHandler('./logs/log.log')  
    ]
    )

#starting the code
logging.info("infra_simulator started")
print("infra_simulator started")

#installing inviermant
vm.run_installer_nginx()
vm.run_installer_pydantic()

#getting vm info form user and test it 
server=vm.user_input()
if  server !='null' :
    save_file(server)
else :
    print("machine info is nothing will not save the info")
    logging.error("do to user stop the info in instances.json will not be saved")

logging.info("infra_simulator ended")
print("the infra_simulator ended ")