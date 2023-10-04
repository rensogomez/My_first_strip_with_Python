import psutil
from logs import log_info, log_error

def get_processor_performance(threshold=1):
    """
    This function is used to detect and measure the processor's performance during an x (duration) interval.
    """    
    try:
        processor_usage = psutil.cpu_percent(interval=1, percpu=True)
        
        # Calcula el uso total del CPU sumando los porcentajes de cada núcleo
        total_usage = sum(processor_usage)
        
        # Imprime el uso de cada núcleo y el núcleo restante
        for core_number, core_usage in enumerate(processor_usage):
            remaining_core_usage = total_usage - core_usage
            print(f"Núcleo {core_number} utilizado: {core_usage}%, Núcleo restante: {remaining_core_usage}%")
        
        # Imprime el uso total del procesador
        print(f'Uso total del procesador: {total_usage}%')
        print("-----------------------------------------------------------------------------------------------------------------------------------")
  
        # Log de información
        log_info("Processor performance data collected successfully.")
        
    except psutil.NoSuchProcess as e:
        log_error(e)
        raise e
    except Exception as e:
        log_error(e)
        raise e
    
    return processor_usage

if __name__ == "__main__":
    get_processor_performance()
