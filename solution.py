from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n Bueller Bueller Bueller"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientsocket = socket(AF_INET, SOCK_STREAM)
    clientsocket.connect((mailserver, port))

    # Fill in end

    recv = clientsocket.recv(1024).decode()
    # print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    helocommand = 'HELO Alice\r\n'
    clientsocket.send(helocommand.encode())
    recv1 = clientsocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailfrom = 'Mail From: <os28@nyu.edu>\r\n'
    clientsocket.send(mailfrom.encode())
    recv1 = clientsocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptto = 'RCPT TO: <ryuaan@gmail.com>\r\n'
    clientsocket.send(rcptto.encode())
    recv1 = clientsocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    data = 'DATA\r\n'
    clientsocket.send(data.encode())
    recv1 = clientsocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send message data.
    # Fill in start
    clientsocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientsocket.send(endmsg.encode())
    recv1 = clientsocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitcmd = 'QUIT\r\n'
    clientsocket.send(quitcmd.encode())
    clientsocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
