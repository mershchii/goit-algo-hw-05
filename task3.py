import sys 
from pathlib import Path
from collections import Counter

def parse_log_line(line: str) -> dict:
    keys = ['date', 'time', 'level', 'message']

    parsed_line = line.split(None, maxsplit=3)
    if len(parsed_line) == 4:
        parsed_dict = dict(zip(keys, parsed_line))        
        return parsed_dict
    else:
        return None 

def load_logs(file_path: str) -> list:
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            logs_dict = []
            for line in file:
                parsed = parse_log_line(line)                
                if parsed is not None:
                    logs_dict.append(parsed)
            return logs_dict
    except FileNotFoundError:
        print(f"Error: File {file_path} not find")
        return []

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'].upper() == level.upper()]
    
def count_logs_by_level(logs: list) -> dict:
    return dict(Counter(log['level'] for log in logs))

def display_log_counts(counts: dict) -> None:
    print(f"{'Рівень логування':<16} | {'Кількість':<10}")
    print(f"{'-' * 16}-|-{'-' * 10}")
    for level, count in counts.items():
        print(f"{level:<16} | {count:<10}")
    

def main() -> None:

    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_logfile> [log_level]")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    

    if not logs:
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) > 2:
        level = sys.argv[2]
        filtered = filter_logs_by_level(logs, level)

        print(f'\n Log details for the level \'{level.upper()}\':')
        for log in filtered:
            print(f"{log['date']} {log['time']} - {log['message']}")
        

if __name__ == "__main__":
    main()