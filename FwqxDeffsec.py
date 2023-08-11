import socket

def scan_target(ip_address, activity_type):
    target_ports = [80, 443, 22, 3389, 8080]  # Taranacak port numaraları

    for port in target_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((ip_address, port))

            if result == 0:
                print(f"Port {port} açık. [{activity_type}]")

            else:
                print(f"Port {port} kapalı. [{activity_type}]")

            sock.close()

        except KeyboardInterrupt:
            print("Tarama kullanıcı tarafından iptal edildi.")
            break

        except socket.gaierror:
            print("Hostname çözümlenemedi. Geçersiz IP adresi.")
            break

        except socket.error:
            print("Sunucu ile bağlantı kurulurken bir hata oluştu.")
            break

# Örnek kullanım
if __name__ == "__main__":
    activity_type = "Defensive"  # Etkinliğin tipini "Defensive" olarak ayarlayın.

    print(f"İSTİHBARAT BİRLİĞİ: Siber saldırılara karşı koruma kapsamında {activity_type} port tarama başlatılıyor...")
    
    target_ip = input("Hedef IP adresini girin: ")
    
    print(f"Seçilen hedef IP adresi: {target_ip}")
    
    scan_target(target_ip, activity_type)
