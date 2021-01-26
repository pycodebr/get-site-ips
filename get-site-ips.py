import socket as s

# Host que você deseja descobrir o Ip #
host = 'google.com'

# Captura o Ip do Host desejado #
Ip = s.gethostbyname(host)

# Mostra resultados #
print('O IP do Host "' + host + '" é: ' + Ip)