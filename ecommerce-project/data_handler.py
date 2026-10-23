def process_file(filepath):
    lines = []
    try:
        with open(filepath, 'r') as file:
            for line_num, line in enumerate(file, start=1):
                try:
                    lines.append(line.strip())
                 # Warn user and skip to the next line without crashing
                except (ValueError, IndexError) as error:
                    print(f"the bad line number is # {line_num} {error}")
                    continue
                finally:
                    print("File processing attempt complete.")
        return lines
    except FileNotFoundError:
        return "Error: raw_transactions.txt not found. Please check the file path."

p = process_file('raw_transactions.txt')

print(p)