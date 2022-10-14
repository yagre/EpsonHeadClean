import socket
import codecs

# Только цветные
hex_string_clean_col = "0000001b0140454a4c20313238342e340a40454a4c20202020200a1b401b401b285208000052454d4f544531544908000007e6061d0f34064348020000021b000000"
# Все
hex_string_clean_any = "0000001b0140454a4c20313238342e340a40454a4c20202020200a1b401b401b285208000052454d4f544531544908000007e60a061125184348020000001b000000"
# Черный
hex_string_clean_blk = "0000001b0140454a4c20313238342e340a40454a4c20202020200a1b401b401b285208000052454d4f544531544908000007e60a06112a3a4348020000011b000000"

raw_string = codecs.decode(hex_string_clean_col, "hex_codec")

#Send to printer`s socket via LAN
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.108", 9100))
s.send(raw_string) #.encode()
data  = s.recv(1024).decode()
s.send("quit".encode())
s.close()

#Save binary file to send from router
with open("EpsonHeadClean.bin", "wb") as binary_file:
    binary_file.write(raw_string)

# send from linux via cron
# monday/thursday at 08:00 am
# 0 8 * * 1,4  nc 192.168.0.108 9100 < /root/EpsonHeadClean.bin