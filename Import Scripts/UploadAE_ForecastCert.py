#Import modules
import os
from anaplanConnector import Connection
#import secret keys from a differt module
from AnaplanCertPasscode import get_anaplan_Certcredentials # type: ignore
privateKey, publicKey, workspace_id, Operating_model_id,Revenue_model_id, Commission_model_id= get_anaplan_Certcredentials()

from AnaplanPasscode import get_anaplan_credentials
anaplan_email, anaplan_password, workspace_id, Operating_model_id,Revenue_model_id, Commission_model_id= get_anaplan_credentials()

ProcessName = 'Update Opportunity Revenue Forecast by AE'
fileName = 'AE Forecast.csv'
filePath = r'G:\Shared drives\Confidential.Finance\Finance.Squad\Confidential Finance\FP&A\PowerBi\1. Datasets and Uploads'

#Define connection
anaplan = Connection(authType='certificate', privateCertPath=privateKey,publicCertPath=publicKey, workspaceId=workspace_id, modelId=Commission_model_id )
#anaplan = Connection(authType='basic', email=anaplan_email, password=anaplan_password,workspaceId=workspace_id, modelId=Commission_model_id)       
#Get all the imported files
#print(anaplan.getFiles())

#get the file id
#print(anaplan.getFileIdByFilename(fileName))

# Use os.path.join() to concatenate the filePath and fileName
fullFilePath = os.path.join(filePath, fileName)

#upload data
anaplan.loadFile(fullFilePath,'113000000153')

#get process Id
anaplan.runProcess(anaplan.getProcessIdByName(ProcessName))

