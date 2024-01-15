import psutil
import socket
from colorama import Fore, Style

def cmn_if_addrs():
    cmntad = psutil.net_if_addrs()
    assert cmntad, cmntad # Doğrulama yapılır, boş ve ya değil

    # INET > IPv4
    # INET6 > IPv6
    # LINK > Ağ arabirimleri
    cmnAf = (socket.AF_INET, socket.AF_INET6, psutil.AF_LINK)

    # cmntad içindeki her bir eleman için belirli bir koşulu kontrol eden döngü
    # set(address), 'address' değişkenindeki elemanların benzersiz olmasını sağlar
    for cmn, address in cmntad.items():
        assert len(set(address)) == len(address) # address'in uzunluğunu alıyor
        for addr in address:
            assert isinstance(addr.family, int)
            assert isinstance(addr.address, str)
            assert isinstance(addr.netmask, (str, type(None)))
            assert isinstance(addr.broadcast, (str, type(None)))
            assert addr.family in cmnAf
            # Elemanlar bu for'da incelendi, koşullara uyulduğu kontrol edildi

            print('')
            print(Fore.LIGHTRED_EX + f"Arayüz Adı: {cmn}" + Style.RESET_ALL)
            print(Fore.CYAN + f"\tIP Adresi: {addr.address}" + Style.RESET_ALL)
            print(Fore.BLUE + f"\tAğ Maskesi: {addr.netmask}" + Style.RESET_ALL)
            print(Fore.LIGHTYELLOW_EX + f"\tBroadcast Adresi: {addr.broadcast}" + Style.RESET_ALL)
            print('')

print('')


if __name__ == "__main__":
    cmn_if_addrs()
