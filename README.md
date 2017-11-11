# Tiny Python Socket App
[Homework for 'Computer networks' course @ ELTE IK]

Basic server-client app, where the client sends a bitstring and a name of encoding to the server.
Then the server calculates the analog amplitudes for that specific bitstring (amplitude at start, middle and end of each bit) represented as 0 or 1, and sends this as an answer to the client. Finally the client prints this answer to the screen.

For example:

client sends: ("110011", "Manchester")

server answers: (100)(100)(011)(011)(100)(100)
