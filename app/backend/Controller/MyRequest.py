import csv

def download_file_csv(content, output_file):
    with open(output_file, "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f,delimiter=";")
        for row in content:
            writer.writerow(row)
    return "API IS DONE"
