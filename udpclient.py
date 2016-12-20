# This is part of a project based on the Black Hat Python book.
# for reference: p.29

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto("AAABBBCCC", (target_host, target_port))

data, addr = client.recvfrom(4096)

print data
