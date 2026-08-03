import sys 

def parse_log_line(line: str) -> dict:
    keys = ['date', 'time', 'level', 'message']

    parsed_line = line.split(None, maxsplit=3)
    if len(parsed_line) == 4:
        parsed_dict = dict(zip(keys, parsed_line))        
        return parsed_dict
    else:
        return None 


def main() -> None:
    log = "2024-01-22 "

    print(parse_log_line(log))


if __name__ == "__main__":
    main()