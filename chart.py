import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_file
from datetime import datetime

def create_bitrate_chart():
    # Menyiapkan output ke file HTML
    output_file("line_chart_speed_sender.html")

    # Membaca file data soal_chart_bokeh.txt
    file_path = 'soal_chart_bokeh.txt'  

    # Parsing file
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            # Mencari line yang berisi data speed
            if 'Timestamp' in line:
                timestamp_str = line.split('Timestamp: ')[1].strip()
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            elif '[ ID]' in line or '[  5]' in line:  # line dengan data speed
                if 'sec' in line and 'Mbits/sec' in line:
                    parts = line.split()
                    bitrate = float(parts[6])  # Kecepatan dalam Mbits/sec
                    data.append((timestamp, bitrate))

    # Membuat DataFrame dari data yang telah diparsing
    df = pd.DataFrame(data, columns=['Timestamp', 'Speed (Mbps)'])

    # Membuat figure Bokeh
    p = figure(title="Testing Jaringan - Speed Sender", 
               x_axis_label='DATE TIME', y_axis_label='Speed (Mbps)',
               x_axis_type='datetime', width=900, height=400)

    # Tambahkan line chart
    p.line(df['Timestamp'], df['Speed (Mbps)'], legend_label="Speed", line_width=2, color="blue")

    # Sesuaikan tampilan sumbu Y dan sumbu X
    p.y_range.start = 0  
    p.y_range.end = df['Speed (Mbps)'].max() + 10 
    p.legend.location = "top_left"  

    show(p)

if __name__ == "__main__":
    create_bitrate_chart()