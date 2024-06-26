import asyncio
import socket

'''
Популярные порты:
22: 'HTTP',
23: 'Telnet',
3389: 'RDP',
443: 'HTTPS',
20: 'FTP',
21: 'FTP',
139: 'SMB or CIFS',
445: 'SMB or CIFS',
2049: 'NFS',
25: 'SMTP',
110: 'POP3',
143: 'IMAP',
1433: 'Microsoft SQL Server',
3306: 'MySQL',
5432: 'PostgreSQL',
389: 'LDAP',
514: 'Syslog',
1812: 'RADIUS',
1813: 'RADIUS',
'''

async def check_port(ip, port, semaphore):
    async with semaphore:
        conn = asyncio.open_connection(ip, port)
        try:
            reader, writer = await asyncio.wait_for(conn, timeout=1)
            print(f"Port {port} on {ip} is open")
            writer.close()
            await writer.wait_closed()
        except:
            pass  # Порт закрыт или не отвечает


async def main(ip):
    semaphore = asyncio.Semaphore(500)  # Ограничение количества одновременных задач
    ports = range(1, 65536)  # Диапазон портов для сканирования
    tasks = [check_port(ip, port, semaphore) for port in ports]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    target_ip = "11.22.33.44"  # Замените на целевой IP-адрес
    asyncio.run(main(target_ip))
