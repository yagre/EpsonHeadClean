import socket
import codecs

# Только цветные
hex_string_clean_col = "0000001b0140454a4c20313238342e340a40454a4c20202020200a1b401b401b285208000052454d4f544531544908000007e6061d0f34064348020000021b000000"
# Все
hex_string_clean_any = "0000001b0140454a4c20313238342e340a40454a4c20202020200a1b401b401b285208000052454d4f544531544908000007e60a061125184348020000001b000000"
# Черный
hex_string_clean_blk = "0000001b0140454a4c20313238342e340a40454a4c20202020200a1b401b401b285208000052454d4f544531544908000007e60a06112a3a4348020000011b000000"
# IP принтера
printer_IP_addr = "192.168.0.108"

def string_decode(hex_string:str) -> str:
    return codecs.decode(hex_string, "hex_codec")

def send_binary_string_to_printer(raw_string,printer_IP_addr:str):    #Send to printer`s socket via LAN
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((printer_IP_addr, 9100))
    s.send(raw_string) #.encode()
    #data  = s.recv(1024).decode()
    s.send("quit".encode())
    s.close()

def save_binary_string_to_file(raw_string:str):   #Save binary file to send from router
    with open("EpsonHeadClean.bin", "wb") as binary_file:
        binary_file.write(raw_string)

def main():
    #send_binary_string_to_printer(string_decode(hex_string_clean_col),printer_IP_addr)
    save_binary_string_to_file(string_decode(hex_string_clean_col))

if __name__ == '__main__':
    main()

# send from linux via cron
# monday/thursday at 08:00 am
# 0 8 * * 1,4  nc 192.168.0.108 9100 < /root/EpsonHeadClean.bin