import asyncio
import time

async def tcp_response_client():
    """
    The client establishes connection with the server using TCP/IP
    client server problem.

    parameters: choice, input_msg, data_info
    output: the choice will be selected by the user.
    The input msg will be displayed to the user and user selects an
    option.
    The data_info encodes and decodes the data entered by the client
    """
    read_data, write_data = await asyncio.open_connection('127.0.0.1', 8898)
    data_info = await read_data.read(100)
    input_msg = data_info.decode().strip()
    print(input_msg)
    ch = input()
    write_data.write(ch.encode())
    if ch == '1':
        data_info = await read_data.read(100)
        input_msg = data_info.decode().strip()
        input_name = input(input_msg)
        write_data.write(input_name.encode())
        data_info = await read_data.read(100)
        input_msg = data_info.decode().strip()
        user_id = input(input_msg)
        write_data.write(user_id.encode())
        data_info = await read_data.read(100)
        input_msg = data_info.decode().strip()
        psw = input(input_msg)
        write_data.write(psw.encode())
        data_info = await read_data.read(100)
        input_msg = data_info.decode().strip()
        print(input_msg)
        print("\t\t\tNow you can Login\t\t\t")
    if ch != '1':
        data_info = await read_data.read(100)
        input_msg = data_info.decode().strip()
        user_id = input(input_msg)
        write_data.write(user_id.encode())
        data_info = await read_data.read(100)
        input_msg = data_info.decode()
        psw = input(input_msg)
        write_data.write(psw.encode())
        data_info = await read_data.read(10000)
        input_msg = data_info.decode().strip()
        print(input_msg)
        if input_msg == "You have logged in already\nAccess Denied" or input_msg == "Incorrect username or password...":
            exit()
        while True:
            option = input("Enter your choice : ")
            write_data.write(option.encode())
            if option == '1':
                file_name = input("Enter a folder name : ")
                write_data.write(file_name.encode())
                data_info = await read_data.read(100)
                input_msg = data_info.decode().strip()
                print(input_msg)
            elif option == "2":
                data_info = await read_data.read(50)
                input_msg = data_info.decode().strip()
                folder_name = input(input_msg)
                write_data.write(folder_name.encode())
                data_info = await read_data.read(50)
                input_msg = data_info.decode().strip()
                filename = input(input_msg)
                write_data.write(filename.encode())
                data_info = await read_data.read(50)
                input_msg = data_info.decode().strip()
                input_data_info = input(input_msg)
                write_data.write(input_data_info.encode())
                data_info = await read_data.read(100)
                input_msg = data_info.decode().strip()
                print(input_msg)
            elif option == "3":
                data_info = await read_data.read(100)
                input_msg = data_info.decode().strip()
                fol_name = input(input_msg)
                write_data.write(fol_name.encode())
                data_info = await read_data.read(100)
                input_msg = data_info.decode().strip()
                filename = input(input_msg)
                write_data.write(filename.encode())
                data_info = await read_data.read(100)
                input_msg = data_info.decode().strip()
                print(input_msg)
            elif option == "4":
                data_info = await read_data.read(100)
                input_msg = data_info.decode().strip()
                print(input_msg)
                write_data.write("WELCOME".encode())
                data_info = await read_data.read(100)
                str_name = data_info.decode().strip()
                list_name = list(str_name.split(" "))
                write_data.write("HI".encode())
                data_info = await read_data.read(20)
                str_size = data_info.decode().strip()
                list_size = list(str_size.split(" "))
                write_data.write("HELLO".encode())
                data_info = await read_data.read(90)
                str_curr = data_info.decode().strip()
                curr = list(str_curr.split("  "))
                write_data.write("HELLO".encode())
                data_info = await read_data.read(90)
                str_mod = data_info.decode().strip()
                mod = list(str_mod.split("  "))
                write_data.write("HELLO".encode())
                for folder in range(len(list_name)):
                    print(f"{list_name[folder]}  {list_size[folder]}   {curr[folder]}  {mod[folder]}")
            elif option == '5':
                data_info = await read_data.read(100)
                input_msg = data_info.decode().strip()
                res = input(input_msg)
                write_data.write(res.encode())
                data_info = await read_data.read(100)
                input_msg = data_info.decode().strip()
                print(input_msg)
            elif option == "0":
                break
        data_info = await read_data.read(100)
        input_msg = data_info.decode().strip()
        print(input_msg)
    write_data.close()
asyncio.run(tcp_response_client())
