import psutil
from logs import log_error, log_info

def get_ram_total_performance():
    try:
        ram_swap = psutil.swap_memory()
        ram_global = psutil.virtual_memory()

        # Imprime información de memoria de intercambio
        print(f"Memoria de Intercambio Total: {ram_swap.total / (1024 ** 3):.2f} GB")
        print(f"Memoria de Intercambio Usada: {ram_swap.used / (1024 ** 3):.2f} GB")
        print(f"Memoria de Intercambio Libre: {ram_swap.free / (1024 ** 3):.2f} GB")
        print(f"Porcentaje de Memoria de Intercambio Usada: {ram_swap.percent}%")

        # Imprime información de RAM global
        print(f"RAM Total: {ram_global.total / (1024 ** 3):.2f} GB")
        print(f"RAM Disponible: {ram_global.available / (1024 ** 3):.2f} GB")
        print(f"RAM Usada: {ram_global.used / (1024 ** 3):.2f} GB")
        print(f"Porcentaje de RAM Usada: {ram_global.percent}%")
        print("-----------------------------------------------------------------------------------------------------------------------------------")
        
        # Log de información
        log_info("RAM performance data collected successfully.")
        
        return ram_swap, ram_global  # Devolver solo los valores necesarios
    except psutil.AccessDenied as e:
        log_error(e)
        print(f"Error de acceso a la información de la memoria RAM: {e}")
    except psutil.TimeoutExpired as e:
        log_error(e)
        print(f"Tiempo de espera agotado al obtener información de la memoria RAM: {e}")
    except Exception as e:
        log_error(e)
        print(f"Error no específico al obtener información de la memoria RAM: {e}")

    return None, None  # Devuelve valores predeterminados o None en caso de error

if __name__ == "__main__":
    get_ram_total_performance()

