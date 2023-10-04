import time
from processor_performance import get_processor_performance
from ssd_performance import get_ssd_performance
from ram_performance import get_ram_total_performance
from net_performance import get_net_stats
import pandas as pd
import os
from datetime import datetime

class PerformanceMonitor:
    """
    Clase principal para recopilar y exportar datos de rendimiento del sistema.
    """
    def __init__(self):
        self.processor_data = []
        self.ssd_data = []
        self.ram_data = []
        self.net_stats_data = []

    def collect_data(self, total_duration_hours=6, interval_minutes=10):
        """
        Recopila datos del sistema durante un período de tiempo especifico.
        Args:
            total_duration_hours (int): Duración total en horas para recopilar datos.
            interval_minutes (int): Intervalo de tiempo en minutos entre cada recopilación de datos.
        """
        total_intervals = (total_duration_hours * 60) // interval_minutes
        
        for interval in range(total_intervals):
            processor_usage = get_processor_performance()
            ssd_performance = get_ssd_performance()
            ram_performance = get_ram_total_performance()
            net_connections = get_net_stats()
            
            self.processor_data.append(processor_usage)
            self.ssd_data.append(ssd_performance)
            self.ram_data.append(ram_performance)
            self.net_stats_data.append({'net_connections': net_connections})
            
            time.sleep(interval_minutes * 60)

        self.processor_df = pd.DataFrame(self.processor_data)
        self.ssd_df = pd.DataFrame(self.ssd_data)
        self.ram_df = pd.DataFrame(self.ram_data)
        self.net_stats_df = pd.DataFrame(self.net_stats_data)

    def data_to_export(self):
        """
        Exporta los datos recopilados a archivos CSV.
        """
        path = r"C:\Users\Renso\Programs\collected_data"
        try:
            current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
            processor_csv_path = os.path.join(path, f"processor_{current_datetime}.csv")
            ssd_csv_path = os.path.join(path, f"ssd_{current_datetime}.csv")
            ram_csv_path = os.path.join(path, f"ram_{current_datetime}.csv")
            net_stats_csv_path = os.path.join(path, f"net_stats_{current_datetime}.csv")
            
            self.processor_df.to_csv(processor_csv_path, index=False)
            self.ssd_df.to_csv(ssd_csv_path, index=False)
            self.ram_df.to_csv(ram_csv_path, index=False)
            self.net_stats_df.to_csv(net_stats_csv_path, index=False)

            print("Data exported successfully.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    monitor = PerformanceMonitor()
    monitor.collect_data()
    monitor.data_to_export()
    
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print("Uso total del procesador (%):")
    print(monitor.processor_df)
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print("Uso total del SSD (Gb):")
    print(monitor.ssd_df)
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print("Uso total de RAM (%):")
    print(monitor.ram_df)
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print("Wi-Fi Stats (bytes):")
    print(monitor.net_stats_df)
