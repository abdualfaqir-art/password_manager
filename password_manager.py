import random
import sys
import string

Login = {}
opt = dict(
    N='New entry',
    V='View all entries',
    S='Search by service name',
    U='Update password',
    D='Delete entry',
    E='Export report',
    X='Exit'
)

def menu():
    print("\n" + "-"*60)
    print("Menu Options:")
    for k, v in opt.items():
        print(f"[{k}] {v}")
    print("-"*60)

def getPW():
    print('Enter a password or enter R to generate a random password')
    PW = input()
    if PW != 'R':
        while len(PW) < 8 or ' ' in PW:
            print('Password must be 8 characters or longer with no spaces')
            PW = input()
    else:
        PW = ''.join(random.choices(string.digits + string.ascii_letters, k=random.randint(8, 16)))
    return PW

def ViewEntries():
    print(f"\n{'service name':<25}{'username':^25}{'password':>25}")
    print("-"*60)
    for k, v in Login.items():
        print(f"{k:<25}{v['user name']:^25}{v['password']:>25}")

def printEntry(k):
    print(f"{k:<25}{Login[k]['user name']:^25}{Login[k]['password']:>25}")

def getUsername():
    Username = input("Enter username: ")
    while not Username or ' ' in Username:
        print("Username must not be empty and must not contain spaces")
        Username = input("Enter username: ")
    return Username

def getServiceName():
    Service = input("Enter service name: ")
    while not Service.strip():
        print("Service name cannot be empty")
        Service = input("Enter service name: ")
    return Service

def main():
    while True:
        menu()
        IN = input("Choose option: ").upper()

        if IN == 'N':
            Service = getServiceName()
            Username = getUsername()
            Password = getPW()
            Login.setdefault(Service, {'user name': Username, 'password': Password})
            print("Entry added! Returning to menu...")

        elif IN == 'S':
            term = input("Enter search term: ").lower()
            matches = 0
            for k, v in Login.items():
                if term in k.lower():
                    printEntry(k)
                    matches += 1
            if matches == 0:
                print("No results found.")
            else:
                print(f"Total matches: {matches}")

        elif IN == 'V':
            if Login:
                ViewEntries()
            else:
                print("No entries yet.")

        elif IN == 'U':
            service = input("Enter service name: ")
            if service in Login:
                Username = getUsername()
                Password = getPW()
                Login[service]['user name'] = Username
                Login[service]['password'] = Password
                print("Update success! Returning to menu...")
            else:
                print("Service does not exist")

        elif IN == 'D':
            service = input("Enter entry you wish to delete: ")
            if service in Login:
                del Login[service]
                print("Entry deleted! Returning to menu...")
            else:
                print("Entry does not exist")

        elif IN == 'E':
            with open('saved_passwords.txt', 'w') as savedPasswords:
                savedPasswords.write(f"{'service name':<25}{'username':^25}{'password':>25}\n")
                savedPasswords.write("-"*60 + "\n")
                for k, v in Login.items():
                    savedPasswords.write(f"{k:<25}{v['user name']:^25}{v['password']:>25}\n")
            print("Export success! File saved as 'saved_passwords.txt'.")

        elif IN == 'X':
            print("Exiting program. Goodbye!")
            sys.exit()

        else:
            print("Unrecognized command. Try again.")

main()
