'''
# Pyhtos top level client interface:
##  Back-end, CLI interface



This is the higest level client interface meaning that there may be more features 
buried deeper in the repository. Each level may have a client module. This is 
not always the case. good luck 

'''

from modules.menu import initialize_menu, choose_from_menu, quit_menu

 


def help_menu():
    '''
    TODO: Internal documentation for interacting with the client interface
    '''
    print(
        """
        you found the help page.
        have you even read the source code? 
        did you actually read it though?


        the best help is the help you give yourself
        """
    )
    inp = input('> ')


def genmatrix():
    from modules.matix.main import matrix
    el1 = int(input('el1> '))
    el2 = int(input('el2> '))
    matrix(el1, el2)


# MAIN MENU DICT 
# menu.py for more documentation
infinity_menu = {
    "matrix": genmatrix,
    'HELP MENU': help_menu,
    'Quit': quit_menu
}

def matrixm():
    # Launch the terminal menu interface 
    initialize_menu(infinity_menu, 'BB Main Menu') 


from time import sleep
import os

login = False
run = True
titlestat = [0]

if login == False:
    titlestat.clear()
    titlestat.append(2)


#### Classes
class Admin:

    def __init__(self, username, password):
        self.username = username
        self.password = password

class DateTime():
    def dt(self):
        import datetime
        return datetime.datetime.now()

#define the class instances
admin1 = Admin('admin', 'password')
# hint: this line 
dt1 = DateTime()


def title():
    # running titlebar
    print('=' * 80)
    print('PYTHOS\t\t\t\t\t', dt1.dt())
    #print('=' * 80)
    
    # subtitle
    if titlestat[0] == 0:
        print('\n\t\tLOGIN')
        print('=' * 80)
    
    elif titlestat[0] == 1:
        print('\n\t\tLOGIN FAILED')
        print('=' * 80)
    
    elif titlestat[0] == 2:
        print('\n\t\tNODE_ADMIN')
        print('=' * 80)

def clear():
    try:
        os.system('cls')
    
    except:
        
        import platform
        ops = platform.system()
        if ops == 'Darwin':
            os.system('clear')

def refresh_screen():
    clear()
    title()




####### LOGIN SEQUENCE #######
while login:
    title()
    usn = input('username: ')
    if usn != admin1.username:
        titlestat.clear()
        titlestat.append(1)
        refresh_screen()
                
    elif usn == admin1.username:
        titlestat.clear()
        titlestat.append(0)
        refresh_screen()
        pasw = input('password: ')

        if pasw == admin1.password:
            titlestat.clear()
            titlestat.append(2)
            refresh_screen()
            print('You are logging in as ', usn)
            refresh_screen()
            break


def rfsm():
    path = input('path>')
    p = rfs(path)
    print(p)

def rfs(pathname):
    index = 0
    tsizevar = 0
    '''
    for root, dirs, files in os.walk(".", topdown=True):
        for file in files:
            print(os.path.join(root, file))

        for name in dirs:
            print(os.path.join(root, name))
    '''
    print('\n\nINDEX\t\tSIZE\t\tDIRECTORY')
    print('=' * 80)
    for root, dirs, files in os.walk(pathname):
        for file in files:
            pathname = os.path.join(root, file)
            size = os.path.getsize(pathname)
            tsizevar += size
            print(index, '\t\t', size, '\t\t', pathname)
            index += 1

    returndata = {'indexed files': index,'totalsize': tsizevar}
    print(returndata)
    input('>')
    return returndata


    '''
        for dir in dirs:
            dirpath = os.path.join(root, dir)
            dirsize = os.path.getsize(dirpath)
            print(index, '\t\t', dirsize, '\t\t', dirpath)
            index += 1
    '''     



def rootfile_list():
    spath = 'C:/'
    rootfilelist = os.listdir(spath)
    root_dict = rootfilelist
    try:
        for i in range(0, len(root_dict)):
                path = 'C:/' + root_dict[i]
                subroot = os.listdir(path)
                print('\t', path)
                
                for j in range(0, len(subroot)):
                    print('\t\t',j, subroot[j])

    except (TypeError, NotADirectoryError):
        #print('type error')
        pass
    input('rootfile_list>\t')
    return rootfilelist


def rootfile_list_2():
    spath = 'C:/'
    rootfilelist = os.listdir(spath)
    root_dict = rootfilelist
    
    for i in range(0, len(rootfilelist)):
        print(i, spath + rootfilelist[i])

    input('rootfile_list>\t')
    return rootfilelist
        


mm = {
    'root file system list': rootfile_list,
    'root file system list 2': rootfile_list_2,
    'directory info': rfsm,
    'matrix': matrixm
}


######## APP INTERFACE ########
while run:
    refresh_screen()
    command = input('>')
    if command == '0':
        refresh_screen()
        print('LOGING OUT OF THE MATRIX')
        clear()
        break

    elif command == '1':
        refresh_screen()              
        initialize_menu(mm, 'ROOT FILE SYSTEM MAIN MENU')

    elif command == '2':
        path = input('path >\t')
        rfs(path)
        command = input('>')

