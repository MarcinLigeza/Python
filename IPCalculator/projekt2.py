import sys
import socket
import json

def addressCorrect(address):
    a = address
    tab = a.split('.',4)
    if (len(tab) != 4):
        print("Adres jest nie poprawny\n")
        return False

    mask = (tab[3].split('/'))[1]

    tab[3] = (tab[3].split('/'))[0]
    isCorrect = True

    if(len(tab) !=4):
        print("Adres jest nie poprawny\n")
        return False

    for i in range (len(tab)-1):
        if((int(tab[i])>255) | (int(tab[i])<0)):
            isCorrect = False

    if(int(mask)<0 | int(mask)>32):
        isCorrect = False


    if(isCorrect == True):
        print("Adres jest poprawny\n")
        return True
    else:
        print("Adres jest nie poprawny\n")
        return False

################################################### koniec sprawdzania adresu


def addressToBinary(address):
    a = address
    tab = a.split('.', 4)
    tab[3] = (tab[3].split('/'))[0]

    binary = ''

    for i in range(len(tab)):
        binary += format(int(tab[i]), "08b")

    return binary

################################################## koniec addressToBinary


def maskToBinary(ipAddress):

    tab = ipAddress.split('.')
    mask = (tab[3].split('/'))[1]


    m = int(mask)
    binary = ''
    for i in range(32):
        if(i<m):
            binary += '1'
        else:
            binary += '0'
        if(((i+1)%8)==0 and (i < 31)):
            binary = binary + '.'
    return binary

################################################ koniec maskToBinary

def networkAddress(ipAddress):
    aBin = addressToBinary(ipAddress)
    mBin = maskToBinary(ipAddress)

    netAddress = ''

    for i in range(32):
        netAddress = netAddress + (str(int(aBin[i])) and (int(mBin[i])))

    return netAddress

############################################## koniec networkAdress


def classAddress(ipAddress):

    ipAddress = networkAddress(ipAddress)

    if(ipAddress[0] == '0'):
        return 'A'
    if((ipAddress[0] == '1') & (ipAddress[1] == '0')):
        return 'B'
    if((ipAddress[0] == '1') & (ipAddress[1] == '1') & (ipAddress[2] == '0')):
        return 'C'
    if ((ipAddress[0] == '1') & (ipAddress[1] == '1') & (ipAddress[2] == '1') & (ipAddress[3] == '0')):
        return 'D'
    if ((ipAddress[0] == '1') & (ipAddress[1] == '1') & (ipAddress[2] == '1') & (ipAddress[3] == '1') & (ipAddress[4] == '0')):
        return 'E'
    else:
        return 'none'

############################################## koniec classAdress


def maskaDec(address):
    result = ''
    address = maskToBinary(address)

    iterator = 0
    for i in range(4):
        tmp = 0
        for j in range(8):
            if(int(address[iterator]) == 1):
                tmp += pow(2,7-j%8)
            iterator+=1
        result = result + str(tmp) + '.'


    return result

############################################## koniec maskaDec


def broadcast(address):
    aBin = addressToBinary(address)
    mBin = maskToBinary(address)

    result = ''

    for i in range(32):
        if(int(mBin[i]) == 1):
            result += aBin[i]
        else:
            result+='1'

    return result

############################################# koniec broadcast

def binToDec(bin):
    result = ''
    iterator = 0
    for i in range(4):
        tmp = 0
        for j in range(8):
            if (int(bin[iterator]) == 1):
                tmp += pow(2, 7 - j % 8)
            iterator += 1
        result = result + str(tmp) + '.'
    return result

############################################ koniec bin2dec


def hostMin(address):
    aBin = addressToBinary(address)
    mBin = maskToBinary(address)

    result = ''

    for i in range(32):
        if(i==31):
            result+='1'
        elif(int(mBin[i]) == 1):
            result += aBin[i]
        else:
            result+='0'

    return  result

###################################################koniec host min

def hostMax(address):
    aBin = addressToBinary(address)
    mBin = maskToBinary(address)

    result = ''

    for i in range(32):
        if(i==31):
            result+='0'
        elif(int(mBin[i]) == 1):
            result += aBin[i]
        else:
            result+='1'

    return  result


################################################# koniec host max


def hostCount(address):
    mBin = maskToBinary(address)
    counter = 0
    mask = (address.split('/'))[1]

    for i in range(int(mask),32):
        if(mBin[i]=='0'):
            counter+=1
    return (pow(2,counter))

################################################ koniec host count

def decToBin(number):
    return format(int(number), "08b")







address = ""

if len(sys.argv) > 1:
    address = (str(sys.argv[1]))

if address=="":
    print("Nie podano argumentu. Pobieram adres urządzenia\n")
    address = socket.gethostbyname(socket.gethostname())
    address += '/24'
    #address = "192.11.42.65/23"

addressCorrect(address)
print ("Adres tego komputera to {0}".format(address))
print ("Adres tego komputera binarnie to {0}\n".format((addressToBinary(address))))


print ("Adres sieci to {0}".format(networkAddress(address)))
print ("Adres sieci binarnie to {0}\n".format((binToDec(networkAddress(address)))))

print ("Klasa tej sieci to {0}\n".format(classAddress(address)))

print ("Maska sieci binarnie to {0}".format((maskToBinary(address))))
print ("Maska sieci decymalnie to {0}\n".format(binToDec(maskToBinary(address))))

print ("Adres broadcast sieci binarnie to {0}".format((broadcast(address))))
print ("Adres broadcast sieci decymalnie to {0}\n".format(binToDec(broadcast(address))))

print ("Adres broadcast sieci binarnie to {0}".format((broadcast(address))))
print ("Adres broadcast sieci decymalnie to {0}\n".format(binToDec(broadcast(address))))

print ("Adres pierwszego hosta binarnie to {0}".format((hostMin(address))))
print ("Adres pierwszego hosta decymalnie to {0}\n".format(binToDec(hostMin(address))))

print ("Adres ostatniego hosta binarnie to {0}".format((hostMax(address))))
print ("Adres ostatniego hosta decymalnie to {0}\n".format(binToDec(hostMax(address))))

print ("Maksmyalna ilosc hostów = {0}".format(hostCount(address)))
print ("Maksmyalna ilosc hostów binarnie = {0}".format(decToBin(hostCount(address))))

