# Anaplan-Export-Automation
This is a Anaplan connector designed for quick and easy integration with Anaplan using Python. 
It focuses on core functionalities such as uploading files, triggering processes, and exporting data.

# Proceedure
1. Ensure you have python installed on your pc
2. Export the desired data directly from Anaplan and ensure to check the option "save export" before final export.
3. Install anaplanConnector using this command
```shell
pip install anaplanConnector
```

# Command structure
Import anaplan connector
```shell
from anaplanConnector import Connection
```

# Intialize the connection
## Basic authentication
```shell
anaplan = Connection(authType='basic',email='email@example.com',password='SecurePassword',workspaceId='anaplanWorkspaceID',modelId='AnaplanModelID')
```
## Certificate authentication
```shell
anaplan = Connection(authType='certificate', privateCertPath='./AnaplanPrivateKey.pem', publicCertPath='./AnaplanPublicKey.pem', workspaceId='anaplanWorkspaceID', modelId='AnaplanModelID')
```

There are two auth types: "basic" and "certificate". If basic is supplied, then the fields "email" and "password" are required. If "certificate" is supplied, then the fields "privateCertPath" and "publicCertPath" are required.

## Get a list of Workspaces
```shell
workspaces = anaplan.getWorkspaces()
```

## Get a list of Models
```shell
models = anaplan.getModels()
```

## Get a list of files
```shell
files = anaplan.getFiles()
```

## Get the fileId from a filename
```shell
fileId = anaplan.getFileIdByFilename(filename)
```

## Load a file
```shell
anaplan.loadFile(filepath,fileId)
```

filepath = The local location and filename of the file to load (e.g. '/home/fileToLoad.csv')

fileId = The Anaplan file ID which can be found by running one of the above commands

## Get a list of processes
```shell
processes = anaplan.getProcesses()
```

## Get a processId from a process name
```shell
processId = anaplan.getProcessIdByName(processName)
```

## Run a process
```shell
anaplan.runProcess(processId)
```
## Get a list of exports
```shell
exports = anaplan.getExports()
```

## Get an exportId from an export name
```shell
exportId = anaplan.getExportIdByName(exportName)
```

## Export data
```shell
anaplan.export(exportId, filepath)
```

exportId = is Anaplan's Export ID that can be found with the above commands

filepath = is the location and filename of where you want to save the file (e.g. '/home/export.csv')

encoding (optional) = is the character encoding of the export file (default is utf-8)
