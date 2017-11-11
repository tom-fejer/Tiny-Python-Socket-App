# coding=utf-8
import socket
import struct
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10001)
server.bind(server_address)
server.listen(1)

connection, client_address = server.accept()
data = connection.recv(1000)

unpacker = struct.Struct('14s 6s') # 14 és 6 Byte-os stringek
unpacked_data = unpacker.unpack(data)

def decoderDiffManchester(bitstring):
	amplitudes = ""
	lastAmplitude = 0
	for char in bitstring:
		if char == "0": # switches at start and middle
			if lastAmplitude == 0:
				amplitudes += "(100)"
				# lastAmplitude = 0
			elif lastAmplitude == 1:
				amplitudes += "(011)"
				# lastAmplitude = 1
		elif char == "1": # switches only at middle
			if lastAmplitude == 0:
				amplitudes += "(011)"
				lastAmplitude = 1
			elif lastAmplitude == 1:
				amplitudes += "(100)"
				lastAmplitude = 0
	return amplitudes

def decoderManchester(bitstring):
	amplitudes = ""
	for char in bitstring:
		if char == "0": # switches lo-to-hi at middle
			amplitudes += "(011)"
		elif char == "1": # switches hi-to-lo at middle
			amplitudes += "(100)"
	return amplitudes

def decoderRZ(bitstring):
	amplitudes = ""
	for char in bitstring:
		if char == "0": # low amplitude
			amplitudes += "(000)"
		elif char == "1": # switches hi-to-lo at middle
			amplitudes += "(100)"
	return amplitudes

def decoderNRZL(bitstring):
	amplitudes = ""
	for char in bitstring:
		if char == "0": # low
			amplitudes += "(000)"
		elif char == "1": # high
			amplitudes += "(111)"
	return amplitudes

def amplitudeCalc(encoding, bitstring):
	encoding = encoding.rstrip("\x00")
	bitstring = bitstring.rstrip("\x00")
	amplitudes = ""
	if encoding == "DiffManchester":
		amplitudes = decoderDiffManchester(bitstring)
	elif encoding == "Manchester":
		amplitudes = decoderManchester(bitstring)
	elif encoding == "RZ":
		amplitudes = decoderRZ(bitstring)
	elif encoding == "NRZ-L":
		amplitudes = decoderNRZL(bitstring)
	return amplitudes
  
result = amplitudeCalc(*unpacked_data)
connection.sendall('Result: ' + result)

connection.close()
server.close()