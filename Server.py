"""The code below runs using asyncio"""
import asyncio
import signal
import fileinput
#import time
#import os
from Testserver import TestServer
signal.signal(signal.SIGINT, signal.SIG_DFL)

async def user_registration(read_data, write_data):
    """
    The user_registration function is responsible for registering
    a user.
    parameters: input_msg
    Returns: Takes the input from the client, encodes it using
    write_data and read_data which are parameters declared inside
    the function definition.
    """
    input_msg = "Enter your name :"
    write_data.write(input_msg.encode())
    data_info = await read_data.read(100)
    input_msg = "Create a User Name : "
    write_data.write(input_msg.encode())
    data_info = await read_data.read(100)
    user_id = data_info.decode().strip()
    input_msg = "create a Password :"
    write_data.write(input_msg.encode())
    data_info = await read_data.read(100)
    psw = data_info.decode().strip()
    AUTH = False
    with open(r"C:\Users\ADMIN\Downloads\my assignment\Assignment_3\root\admin\Register.txt", 'r') as r:
        for read_line in r:
            if user_id in read_line:
                if psw in read_line:
                    AUTH = True
                    break
    if not AUTH:
        with open(r"C:\Users\ADMIN\Downloads\my assignment\Assignment_3\root\admin\Register.txt", 'a') as w:
            w.write(user_id + ':')
            w.write(psw + ', \n')
        input_msg = "User Registered Succcessfully."
        write_data.write(input_msg.encode())
    else:
        input_msg = "Request Denied\nYou are already Registered"
        write_data.write(input_msg.encode())

async def user_login(read_data, write_data):
    """
    After the user registration, the user can login with the
    credentials.

    parameters: read_data, write_data, input_msg
    Returns: The read_data and write_data encodes and
    decodes the msg input given by the user.
    """
    input_msg = """Login Form
                Enter User_Name   : """
    write_data.write(input_msg.encode())
    data_info = await read_data.read(100)
    user_id = data_info.decode().strip()
    input_msg = "    Enter Password : "
    write_data.write(input_msg.encode())
    data_info = await read_data.read(100)
    psw = data_info.decode().strip()
    login_file_path = r"C:\Users\ADMIN\Downloads\my assignment\Assignment_3\root\admin\Register.txt"
    BOOL_VALUE = 0
    LOGIN = True
    with open(login_file_path, 'r') as path:
        for read_line in path:
            if user_id in read_line:
                if psw in read_line:
                    BOOL_VALUE = 1
                    if "logged" in read_line:
                        input_msg = "You have logged in already\nAccess Denied"
                        write_data.write(input_msg.encode())
                        LOGIN = False
                        break

    if LOGIN:
        for read_line in fileinput.FileInput(login_file_path, inplace=1):
            if user_id in read_line:
                if psw in read_line:
                    read_line = read_line.rstrip()
                    read_line = read_line.replace(read_line, read_line + "logged\n")
            print(read_line, end='')
    if BOOL_VALUE != 1:
        input_msg = "Incorrect username or password..."
        write_data.write(input_msg.encode())
    elif BOOL_VALUE == 1 and LOGIN:
        try:
            input_msg = """
            WELCOME
            COMMANDS:
            1.CREATE_FOLDER
            2.WRITE_FILE
            3.READ_FILE
            4.LIST_OF_DIRECTORIES
            5.CHANGE_FOLDER
            0.QUIT"""
            write_data.write(input_msg.encode())
            user = TestServer(user_id)
            while True:
                data_info = await read_data.read(100)
                option = data_info.decode().strip()
                if option == '1':
                    data_info = await read_data.read(100)
                    f_name = data_info.decode().strip()
                    BOOL_VALUE = user.create_folder(f_name)
                    if BOOL_VALUE:
                        input_msg = "Folder created succesfully!"
                        write_data.write(input_msg.encode())
                    else:
                        input_msg = "Folder already exists..."
                        write_data.write(input_msg.encode())
                elif option == '2':
                    input_msg = "Enter folder name : "
                    write_data.write(input_msg.encode())
                    data_info = await read_data.read(50)
                    folder_name = data_info.decode().strip()
                    input_msg = "Enter file name : "
                    write_data.write(input_msg.encode())
                    data_info = await read_data.read(50)
                    input_file = data_info.decode().strip()
                    input_msg = "Enter the message : "
                    write_data.write(input_msg.encode())
                    data_info = await read_data.read(50)
                    input_data = data_info.decode().strip()
                    is_possible = user.write_file(folder_name, input_file, input_data)
                    if is_possible:
                        input_msg = "File Created successfully"
                        write_data.write(input_msg.encode())
                elif option == '3':
                    input_msg = "Enter folder name : "
                    write_data.write(input_msg.encode())
                    data_info = await read_data.read(100)
                    folder_name = data_info.decode().strip()
                    input_msg = "Enter file name : "
                    write_data.write(input_msg.encode())
                    data_info = await read_data.read(100)
                    input_file = data_info.decode().strip()
                    read_file_data = str(user.read_file(folder_name, input_file))
                    write_data.write(read_file_data.encode())
                elif option == '4':
                    list_names, list_size, list_curr, list_modified = user.list_of_directories()
                    input_msg = "Name      Size         Created           Modified"
                    write_data.write(input_msg.encode())
                    data_info = await read_data.read(100)
                    input_msg = data_info.decode().strip()
                    str_name = str(" ".join(list_names))
                    write_data.write(str_name.encode())
                    data_info = await read_data.read(100)
                    input_msg = data_info.decode().strip()
                    str_size = str(" ".join(map(str, list_size)))
                    write_data.write(str_size.encode())
                    data_info = await read_data.read(100)
                    input_msg = data_info.decode().strip()
                    str_curr = str("  ".join(map(str, list_curr)))
                    write_data.write(str_curr.encode())
                    data_info = await read_data.read(100)
                    input_msg = data_info.decode().strip()
                    str_mod = str("  ".join(map(str, list_modified)))
                    write_data.write(str_mod.encode())
                    data_info = await read_data.read(100)
                    input_msg = data_info.decode().strip()
                elif option == '5':
                    input_msg = "Enter old Folder name : "
                    write_data.write(input_msg.encode())
                    data_info = await read_data.read(100)
                    old_folder_name = data_info.decode().strip()
                    mod = user.change_folder_path(old_folder_name)
                    if mod:
                        input_msg = "FILE PATH CHANGED SUCCESSFULLY"
                    else:
                        input_msg = "FILE DOESN'T EXIST"
                    write_data.write(input_msg.encode())

                elif option == '0':
                    break
        except Exception as exp:
            print(exp)
        finally:
            for read_line in fileinput.FileInput(login_file_path, inplace=1):
                if user_id in read_line:
                    if psw in read_line:
                        read_line = read_line.rstrip()
                        read_line = read_line.replace(read_line, f"{user_id}:{psw},\n")
                print(read_line, end='')
            input_msg = "LOGGED OUT SUCCESSFULLY"
            write_data.write(input_msg.encode())

async def choice(read_data, write_data):
    """
    The client will be given two options i.e,; to either register or
    login.
    If the client has already registered before, then user can
    directly login with the credentials.

    parameters: input_msg
    Output: Prints the options to the user and the user selects
    any one of those two options.
    """
    input_msg = """1. Register  2. Login\nEnter your choice :"""
    write_data.write(input_msg.encode())
    data_info = await read_data.read(100)
    option = data_info.decode().strip()
    if option == '1':
        await user_registration(read_data, write_data)
    else:
        await user_login(read_data, write_data)

async def main():
    """The server runs on port 8898"""
    server = await asyncio.start_server(choice, '127.0.0.1', 8898)

    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
#asyncio.run(main())
