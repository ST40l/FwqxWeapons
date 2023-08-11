import socket

def scan_target(ip_address, activity_type):
    target_ports = [80, 443, 22, 3389, 8080]  # Taranacak port numaraları

    for port in target_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Soket zaman aşımı ayarı

            result = sock.connect_ex((ip_address, port))  # Belirtilen IP ve port'a bağlanma denemesi

            if result == 0:  # Eğer bağlantı başarılıysa (port açık)
                print(f"Port {port} açık. [{activity_type}]")
                data = sock.recv(1024)  # Veri alımı
                print(f"Port {port} verileri: {data.decode('utf-8')}")  # Alınan verileri ekrana yazdır

            else:  # Bağlantı başarısızsa (port kapalı veya hedef cevap vermiyor)
                print(f"Port {port} kapalı. [{activity_type}]")

            sock.close()  # Soketi kapat

        except KeyboardInterrupt:
            print("Tarama kullanıcı tarafından iptal edildi.")
            break

        except socket.gaierror:
            print("Hostname çözümlenemedi. Geçersiz IP adresi.")
            break

        except socket.error as e:
            print(f"Sunucu ile bağlantı kurulurken bir hata oluştu: {e}")
            break

if __name__ == "__main__":
    activity_type = "Offensive"  # Etkinliğin tipi ("Defensive" veya "Offensive")

    print(f"İSTİHBARAT BİRLİĞİ: Siber suçlarla mücadele ve terörle mücadele kapsamında {activity_type} port tarama başlatılıyor...")
    
    target_ip = input("Hedef IP adresini girin: ")
    
    print(f"Seçilen hedef IP adresi: {target_ip}")
    
    scan_target(target_ip, activity_type)
