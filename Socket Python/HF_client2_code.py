# coding=utf-8
import socket
import struct
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10001)

values1 = ("DiffManchester", "110011")
values2 = ("Manchester", "110011")
values3 = ("RZ", "110011")
values4 = ("NRZ-L", "110011")

packer = struct.Struct('14s 6s')
packed_data = packer.pack(*values1)

client.connect(server_address)
client.sendall(packed_data)

data = client.recv(1000)
print data

client.close()