#Created by Luca Cottone 2/17/25
#This file is the main server architecture for PyRace
import socket
from _thread import *
import sys

#PUT YOUR IP HERE BEFORE USING (IP of computer running the server)
server = "35.50.4.208"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind server and port to socket
#throw error if port already in use
try:
    s.bind((server, port))
except socket.error as e:
    str(e) #print error

#listen for connections
s.listen(5) #opens up the port for 5 connections max
print("Waiting for a connection, server has started")

#start threaded function
def threaded_client(conn):
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8") #decrypt incoming traffic

            if not data: #disconnect from clients if any network issues
                print("Disconnected")
                break
            else:
                print("received", reply)
                print("Sending: ", reply)
            conn.sendall(str.encode(reply)) #encrypts outgoing traffic
        except:
            break

while True:
    #continuously look for connections
    conn, addr = s.accept() #accepts and stores connection and IP address
    print(f"Connected to: {addr}")

    start_new_thread(threaded_client, (conn)) #runs in the background while while loop is runs


