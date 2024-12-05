import argparse
import re
from datetime import datetime

def filter_log_file(input_file, output_file=None, search_phrase=None, 
                    start_date=None, end_date=None, log_level=None):
    """
    Advanced log file filtering utility with multiple filtering options.
    
    Args:
        input_file (str): Path to the input log file
        output_file (str, optional): Path to save filtered logs
        search_phrase (str, optional): Phrase to search for in log entries
        start_date (str, optional): Start date for filtering (YYYY-MM-DD)
        end_date (str, optional): End date for filtering (YYYY-MM-DD)
        log_level (str, optional): Specific log level to filter (INFO, ERROR, etc.)
    """
    # Compile regex patterns
    phrase_pattern = re.compile(search_phrase, re.IGNORECASE) if search_phrase else None
    
    # Parse date formats if provided
    start = datetime.strptime(start_date, '%Y-%m-%d') if start_date else None
    end = datetime.strptime(end_date, '%Y-%m-%d') if end_date else None
    
    # Determine output destination
    output = open(output_file, 'w') if output_file else None
    
    try:
        with open(input_file, 'r') as file:
            filtered_logs = []
            
            for line in file:
                # Skip empty lines
                if not line.strip():
                    continue
                
                # Phrase filtering
                if phrase_pattern and not phrase_pattern.search(line):
                    continue
                
                # Log level filtering
                if log_level and log_level not in line:
                    continue
                
                # Date filtering (assumes standard datetime format)
                try:
                    log_date = datetime.strptime(line.split()[0], '%Y-%m-%d')
                    if start and log_date < start:
                        continue
                    if end and log_date > end:
                        continue
                except (ValueError, IndexError):
                    # Skip lines without parseable date
                    continue
                
                filtered_logs.append(line)
            
            # Output results
            if output:
                output.writelines(filtered_logs)
            else:
                for log in filtered_logs:
                    print(log.strip())
    
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
    except PermissionError:
        print(f"Error: No permission to read {input_file}.")
    finally:
        if output:
            output.close()

def main():
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description='Advanced Log File Filter')
    parser.add_argument('input_file', help='Path to input log file')
    parser.add_argument('-o', '--output', help='Path to output filtered log file')
    parser.add_argument('-p', '--phrase', help='Search phrase to filter logs')
    parser.add_argument('-s', '--start-date', help='Start date (YYYY-MM-DD)')
    parser.add_argument('-e', '--end-date', help='End date (YYYY-MM-DD)')
    parser.add_argument('-l', '--log-level', help='Specific log level')
    
    args = parser.parse_args()
    
    filter_log_file(
        args.input_file, 
        args.output, 
        args.phrase, 
        args.start_date, 
        args.end_date, 
        args.log_level
    )

if __name__ == '__main__':
    main()
