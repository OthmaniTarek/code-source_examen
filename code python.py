from netmiko import (
  ConnectHandler,
)

cisco_router = {
    'device_type': 'cisco_ios',
    'host': 'sandbox-iosxr-1.cisco.com', 
    'username': 'admin',
    'password': 'C1sco12345',
    'secret': 'enablepass',
    'port': 22,
}
conn = ConnectHandler(**cisco_router)
output = conn.send_command('show ip int br')
print(output)

print("Affichage de la date du routeur:")
show_clock = net_connect.send_command('show clock')
print(show_clock)


print("\nAffichage des interfaces du routeur et sauvegarde dans interfaces.txt:")
interfaces = net_connect.send_command('show ip interface brief')
with open('interfaces.txt', 'w') as f:
    f.write(interfaces)

print("Les interfaces ont été sauvegardées dans interfaces.txt.")


print("\nConfiguration de l'interface Loopback avec l'adresse IP 10.8.8.8/28:")
config_commands = [
    'conf t',                  # Passer en mode configuration globale
    'interface loopback 0',    # Accéder à l'interface loopback
    'ip address 10.8.8.8 255.255.255.240',  # Configurer l'IP
    'no shutdown',             # Activer l'interface
]
output = net_connect.send_config_set(config_commands)
print(output)


print("\nSauvegarde de la configuration:")
net_connect.save_config()


net_connect.disconnect()

print("\nOpérations terminées avec succès.")
