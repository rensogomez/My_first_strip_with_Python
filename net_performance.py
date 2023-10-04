import psutil
from logs import log_error, log_info

def get_net_stats(interface_name="Wi-Fi"):
    try:
        net_counters = psutil.net_io_counters(pernic=True)
        net_connections = psutil.net_connections(kind='tcp')

        if interface_name not in net_counters:
            raise Exception(f"La interfaz de red '{interface_name}' no está disponible.")

        wifi_net_counters = net_counters[interface_name]
        wifi_net_connections = [conn for conn in net_connections if interface_name in conn.laddr]

        # Imprime estadísticas de transferencia de datos de Wi-Fi
        print(f"Bytes enviados: {wifi_net_counters.bytes_sent}")
        print(f"Bytes recibidos: {wifi_net_counters.bytes_recv}")

        # Imprime detalles de las conexiones de red de Wi-Fi
        print("Detalles de las conexiones de red Wi-Fi:")
        for conn in wifi_net_connections:
            print(f"Local Address: {conn.laddr.ip}:{conn.laddr.port} -> Remote Address: {conn.raddr.ip}:{conn.raddr.port}")

        print("-----------------------------------------------------------------------------------------------------------------------------------")
        # Log de información
        log_info("Wi-Fi network stats collected successfully.")

        return wifi_net_counters, wifi_net_connections
    except psutil.NoSuchProcess as e:
        log_error(e)
        raise e
    except Exception as e:
        log_error(e)
        print(f"Error inesperado al obtener estadísticas de la red Wi-Fi: {e}")

    return None, None  # Devuelve valores predeterminados o None en caso de error

if __name__ == "__main__":
    get_net_stats()
