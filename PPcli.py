import typer
import socket
import os

app = typer.Typer() #app init

@app.command() #specifies this is a command
def help(): #command name
    os.system('cls')
    print("command list:\n scan - scans open ports to a given ip \n help - shows a list of commands \n netscan - displays information of your current newtwork | SCANLVLS-(full)(normal)")



@app.command()
def netscan(scanlvl: str):
    os.system('cls')
    if scanlvl == "full":
        #grabs network info
        os.system('ipconfig /all')
        os.system('netstat -an')
    elif scanlvl == "normal":
        os.system('ipconfig')

@app.command()
def scan(ip: str):
    os.system('cls')
    ports = [80, 20, 21, 22, 23, 25, 53, 443, 110, 161, 143, 993, 995] #list of ports to be scanned

    print('[!]''is an open port')
    print('[X]''is a closed port')

    print("STARTED SCANNING", ip)

    for port in ports:                                       #connects to given ip on the list of ports #
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#                                          #
        result = s.connect_ex((ip, port))                    ############################################
        if result == 0: #a result of 0 is an open port                                      
            print('port', port, '[!]' )
        else:
            print('port', port, '[X]' )

    print("scan done")
    
if __name__ == "__main__": #app init
    app()