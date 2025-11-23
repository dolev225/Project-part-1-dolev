from function import function 
import json
import logging 



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
function.run_installer_nginx()
function.run_installer_pydantic()

#getting vm info form user and test it 
server=function.user_input()
if  server !='null' :
    function.save_file(server)
else :
    print("machine info is nothing will not save the info")
    logging.error("do to user stop the info in instances.json will not be saved")

logging.info("infra_simulator ended")
print("the infra_simulator ended ")