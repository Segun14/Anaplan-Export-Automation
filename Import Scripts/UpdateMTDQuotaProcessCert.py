#Import modules
import os
from anaplanConnector import Connection
#import secret keys from a differt module
from AnaplanCertPasscode import get_anaplan_Certcredentials # type: ignore
privateKey, publicKey, workspace_id, Operating_model_id,Revenue_model_id, Commission_model_id= get_anaplan_Certcredentials()

from AnaplanPasscode import get_anaplan_credentials
anaplan_email, anaplan_password, workspace_id, Operating_model_id,Revenue_model_id, Commission_model_id= get_anaplan_credentials()

ProcessName = 'MTD Rev Quota Forecast Update'

#Define connection
#anaplan = Connection(authType='certificate', privateCertPath=privateKey,publicCertPath=publicKey, workspaceId=workspace_id, modelId=Commission_model_id)
anaplan = Connection(authType='basic', email=anaplan_email, password=anaplan_password,workspaceId=workspace_id, modelId=Commission_model_id)  

#get process Id
anaplan.runProcess(anaplan.getProcessIdByName(ProcessName))
