from hashlib import md5, sha1, sha256, sha512
from sys import argv

def main():
    try:
        argm = argv[1]
    except:
        print("Error argument!")
        exit(0)
    
    print("\t██╗  ██╗ █████╗ ███████╗██╗  ██╗████████╗ ██████╗  ██████╗ ██╗     ")
    print("\t██║  ██║██╔══██╗██╔════╝██║  ██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     ")
    print("\t███████║███████║███████╗███████║   ██║   ██║   ██║██║   ██║██║     ")
    print("\t██╔══██║██╔══██║╚════██║██╔══██║   ██║   ██║   ██║██║   ██║██║     ")
    print("\t██║  ██║██║  ██║███████║██║  ██║   ██║   ╚██████╔╝╚██████╔╝███████╗")
    print("\t╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝\n")
    choice = input("Select hash:\n* 1)MD5\n* 2)SHA1\n* 3)SHA256\n* 4)SHA512\n:")

    if choice == "1":
        res = md5(str(argm).encode("ascii")).hexdigest()
        print("Hash -> {}".format(res))
    elif choice == "2":
        res = sha1(str(argm).encode("ascii")).hexdigest()
        print("Hash -> {}".format(res))
    elif choice == "3":
        res = sha256(str(argm).encode("ascii")).hexdigest()
        print("Hash -> {}".format(res))
    elif choice == "4":  
        res = sha512(str(argm).encode("ascii")).hexdigest()
        print("Hash -> {}".format(res))
    else:
        print("Error choice!")
        exit(0)
    
if __name__ == "__main__":
    main()