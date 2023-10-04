import psutil
from logs import log_error, log_info

def get_ssd_performance():
    try:
        ssd_partition = psutil.disk_partitions()[0].device
        ssd_usage = psutil.disk_usage(ssd_partition)

        ssd_performance = {
            'total_space_gb': ssd_usage.total / (1024 ** 3),
            'used_space_gb': ssd_usage.used / (1024 ** 3),
            'free_space_gb': ssd_usage.free / (1024 ** 3),
            'disk_stats': psutil.disk_io_counters(perdisk=True),
            'disk_partitions': psutil.disk_partitions(all=True)
        }

        # Log de información
        info_message = f"Proceso realizado con éxito"
        log_info(info_message)

        for key, value in ssd_performance.items():
            if isinstance(value, (int, float)):
                print(f'{key}: {value:.2f} GB')
            else:
                print(f'{key}: {value}')
            print("-----------------------------------------------------------------------------------------------------------------------------------")

        return ssd_performance
    except FileNotFoundError as e:
        log_error(e)
        raise FileNotFoundError("La unidad SSD no se ha encontrado")
    except psutil.Error as e:
        log_error(e)
        raise Exception(f"Error en la medición del rendimiento SSD: {e}")

if __name__ == "__main__":
    get_ssd_performance()
