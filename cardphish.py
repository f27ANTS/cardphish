import os

import threading

import webbrowser

import subprocess

#just to be here ;)))))

def print_banner():

    banner = '''

\033[34m---------f27 ANTS---------\033[0m

'''

    print(banner)

def start_ssh_server():

    subprocess.run("sshd")

# adress, ocasionalu not working

def get_ip_address():

    result = subprocess.run("ip a", capture_output=True, text=True, shell=True)

    output = result.stdout

    lines = output.splitlines()

    for line in lines:

        if "inet" in line and "wlan0" in line:  # Adjust the interface name if needed (e.g., eth0)

            ip_address = line.split()[1].split("/")[0]

#mwnu            return ip_address

def display_menu():

    print_banner()

    print("\033[3m(Menu)\033:")

    print("\033[34m(1)\033[0m Start server")

    print("\033[34m(2)\033 the ANTS info ;)")

    print("\033[31m(3)\033 Exit")

#to get your link lmao |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\×`×`π`π÷`°`=¢÷¢°¢=¢÷¢×¢\\\\\

def get_link():

    link = "http://localhost:8270"

    styled_html = '''

    <html>

    <head>

        <title>Localhost Link</title>

        <style>

        #css

        </style>

    </head>

    <body>

        #html

    </body>

    </html>

    '''.replace("#html", get_example_html()).replace("#css", get_example_css())

    with open("index.html", "w") as file:

        file.write(styled_html)

    webbrowser.open_new_tab("index.html")

# whyyyy?

def get_example_html():

    html = '''
    #your html that will display in Chrome/ can copy the cards html's from web 
    '''
    
    return html                    
  
  
  
# tffff?                                       




def get_example_css():                       
  css = '''
  #your css here/do like Html/ from web
    '''
  
  return css

#understood now?                                                                        def start_server():

    os.system("php -S localhost:8270")

def main():

    while True:

        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":

            get_link()                                                                              threading.Thread(target=start_server).start()

        elif choice == "2":

            print("\033[34mf27 AMTS info: This is not an illegal tool; it is just for e>

        elif choice == "3":

            break

        else:

            print("Invalid choice. Please try again.")

# nigga ;)

if __name__ == "__main__":

    main()
  
  
  
