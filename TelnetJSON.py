import json
import socket
import ipaddress

data = open('F:/Python/TestCaseProject/login_details.json','r').read()
FTP_LOGIN = json.loads(data)

first_index = 0

def getHostA():
    hostA_list = [FTP_LOGIN.get(ftp_login).get(key) for ftp_login in FTP_LOGIN for key in FTP_LOGIN.get(ftp_login) if(key == 'hostA')]
    myIpAddress = hostA_list[first_index]
    while(True):
        try:
            #socket.inet_aton(hostA_list[first_index])
            ipaddress.ip_address(myIpAddress)
            #print("No Exception")            
            break
        except ValueError:
            myIpAddress = input("Please enter a valid IP address: ")
            
    return str(myIpAddress)

def getHostB():
    hostB_list = [FTP_LOGIN.get(ftp_login).get(key) for ftp_login in FTP_LOGIN for key in FTP_LOGIN.get(ftp_login) if(key == 'hostB')]    
    return hostB_list[first_index]

def getUserName():
    uname_list = [FTP_LOGIN.get(ftp_login).get(key) for ftp_login in FTP_LOGIN for key in FTP_LOGIN.get(ftp_login) if(key == 'username')]    
    return uname_list[first_index]
    
def getPassword():
    pwd_list = [FTP_LOGIN.get(ftp_login).get(key) for ftp_login in FTP_LOGIN for key in FTP_LOGIN.get(ftp_login) if(key == 'password')]    
    return pwd_list[first_index]

def getIter():
    iter_list = [FTP_LOGIN.get(ftp_login).get(key) for ftp_login in FTP_LOGIN for key in FTP_LOGIN.get(ftp_login) if(key == 'iter')]    
    return iter_list[first_index]
