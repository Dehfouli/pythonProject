import socket

target = '185.78.20.130'

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False
portlist = {
    20:'FTP-Data Transfer',
    21:'FTP-Command Control',
    22:'SSH',
    23:'Telnet ',
    25:'SMTP',
    53:'DNS',
    80:'HTTP',
    110:'POP3',
    119:'NNTP',
    123:'NTP',
    143:'IMAP',
    161:'SNMP',
    194:'IRC',
    443:'HTTPS'
}
for i in portlist:
    if portscan(i):
        print('\033[1;30;43m {} is Open: {} \033[1;0m'.format(i,portlist[i]))
    else:
        print('{} is Closed: {}'.format(i,portlist[i]))


