#A user’s IP address is defanged to prevent the
#user from clicking on a malicious link.

def defangIP(address):
    new_address = ""
    split_address = address.split('.')
    print(split_address)
    print(type(split_address))
    seprator = "[.]"
    new_address = seprator.join(split_address)
    return new_address

if __name__ == "__main__":
    address = input("Enter your ip address:\n")
    ipaddress = defangIP(address)
    print("new IP address: ", ipaddress)

