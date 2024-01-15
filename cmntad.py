import argparse
import cmniface
from colorama import Style, Fore

def main():
    cmn_parse = argparse.ArgumentParser()
    usage='cmntad.py --iface',
    description='cmndtad interface bilgilerini gösterir...'

    cmn_parse.add_argument('--iface', action='store_true', help='Mevcut interface bilgilerini gösterir')

    args = cmn_parse.parse_args()

    if args.iface:
        cmniface.cmn_if_addrs()
    else:
        print(Fore.LIGHTRED_EX + "Lütfen --iface kullanın.")

if __name__ == "__main__":
    main()
