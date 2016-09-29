from string import uppercase
from string import lowercase

if __name__ == '__main__':
    asking = True

    print("Juan Questions")
    print("Presione 1 para salir")

    while asking == True:
        response = input("Pregunta algo: ")

        if response.endswith("?") :
            print("Ofi")
        elif response >= 'A' and response <= 'Z':
            print("Chillea")
        elif response == "" :
            print("mmm")
        elif response == " " :
            print("Me da igual")
        elif response == "1" :
            print("Salir")
            asking = False
            break
