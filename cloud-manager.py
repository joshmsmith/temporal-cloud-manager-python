# This is a simple sample python script about how you could orchestrate tcld.
# For now all it does is list namespaces and users.
# It uses tcld to do the heavy lifting, calling APIs.
# Before running, install tcld and login with tcld
#
# These examples are provided as-is, without support. They are intended as reference material only.
# 
import subprocess
import os
import json

def main():
    initialize()
    namespaces = get_namespaces()
    namespacesCSVFile = open("namespace-list.csv", "w+")
    namespacesCSVFile.write(f"Namespace,\n")
    for i in namespaces:
        namespacesCSVFile.write(f"{i},\n")

    namespacesCSVFile.close()
    
    usersCSVFile = open("user-list.csv", "w+")
    usersCSVFile.write(f"Namespace,Email, Account Role, State\n")
    for n in namespaces:
        users = []
        users.extend(get_users_for_namespace(n))
    
        for u in users:
            usersCSVFile.write(f"{n}, {u['spec']['email']},{u['spec']['accountRole']['role']},{u['state']},\n")
    usersCSVFile.close()
    
    cleanup()

def get_namespaces():
    morepages = True
    namespaces = []
    pagetoken = ""
    pagenum = 0
    while (morepages):
        pagenum += 1
        namespacesJSONFile = open("namespace-list.json", "w+")
        subprocess.run(f"tcld namespace list ", shell=True, stdout=namespacesJSONFile) 
        namespacesJSONFile.close()

        namespacesJSONFile = open("namespace-list.json", "r")
        namespacesDict = json.load(namespacesJSONFile)
        namespacesJSONFile.close()
        pagetoken = namespacesDict['nextPageToken']
        if pagetoken != "":
            print(f"Retrieving namespace page {pagenum}")
        else:
            print(f"Retrieved all namespace pages ({pagenum})")
            morepages = False

        for i in namespacesDict['namespaces']:
            namespaces.append(i)
    return namespaces

def get_users_for_namespace(namespace_name):
    morepages = True
    users = []
    pagetoken = ""
    pagenum = 0
    while (morepages):
        pagenum += 1
        usersJSONFile = open("users-list.json", "w+")
        subprocess.run(f"tcld user list --namespace {namespace_name} --page-token \"{pagetoken}\"", shell=True, stdout=usersJSONFile) 
        usersJSONFile.close()

        usersJSONFile = open("users-list.json", "r")

        usersDict = json.load(usersJSONFile)
        usersJSONFile.close()
        pagetoken = usersDict['nextPageToken']
        if pagetoken != "":
            print(f"Retrieving users page for {namespace_name}, page #{pagenum}")
        else:
            print(f"Retrieved all users pages for {namespace_name}, page #{pagenum}")
            morepages = False

        for i in usersDict['users']:
            users.append(i)

    return users
def initialize():    
    if(os.path.isfile("namespace-list.csv")):
        os.remove("namespace-list.csv")
    if(os.path.isfile("user-list.csv")):
        os.remove("user-list.csv")

def cleanup():   
    if(os.path.isfile("users-list.json")):
        os.remove("users-list.json")
    if(os.path.isfile("namespace-list.json")):
            os.remove("namespace-list.json")
    
    

if __name__ == "__main__":
    main()  

# check page token for namespaces
# concatenate all pages together
# output all namespaces to namespaces.CSV


# for each namespace, get users/roles
# check page token for users
# concatenate all pages together
# output all namespaces/users to namespaces-users.csv