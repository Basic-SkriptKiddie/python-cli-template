import typer
import os
app = typer.Typer() #app init

@app.command() #specifies this is a command
def help(): #command name
    os.system('cls')
    print("OK documentation available here https://typer.tiangolo.com/ ")

@app.command()
def cmd2():
    os.system('cls')
    print("i think you get the point")
    
if __name__ == "__main__": #app init
    app()
