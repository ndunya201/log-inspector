from parser import parse_log, filter_errors, filter_by_user
from reporter import get_error_summary, get_user_summary, write_csv, write_html

def run_inspector(filepath, mode='summary', username=None, output='print'):
    """
    Main function that wires parser and reporter together.

    modes:    'summary'     - shows error + user summary
              'errors-only' - shows only errors
              'user'        - shows entries for a specific user

    output:   'print'  - prints to screen
              'csv'    - saves CSV files
              'html'   - saves HTML files
    """

    # Step 1 - parse the log file
    logs = parse_log(filepath)

    # Step 2 - filter based on mode
    if mode == 'errors-only':
        results = filter_errors(logs)
        print(f"\n--- Errors Only ({len(results)} found) ---")
        for entry in results:
            print(f"  [{entry['user']}] {entry['message']}")

    elif mode == 'user':
        if not username:
            print("Error: please provide a username with mode='user'")
            return
        results = filter_by_user(logs, username)
        print(f"\n--- Logs for '{username}' ({len(results)} entries) ---")
        for entry in results:
            print(f"  [{entry['code']}] {entry['message']}")

    elif mode == 'summary':
        error_summary = get_error_summary(logs)
        user_summary = get_user_summary(logs)

        if output == 'print':
            print("\n--- Error Summary ---")
            for error, count in error_summary:
                print(f"  {count:>3}x  {error}")
            print("\n--- User Summary ---")
            print(f"  {'Username':<20} {'INFO':>6} {'ERROR':>6}")
            print(f"  {'-'*34}")
            for user, info, error in user_summary:
                print(f"  {user:<20} {info:>6} {error:>6}")

        elif output == 'csv':
            write_csv(error_summary, ['Error', 'Count'], 'error_summary.csv')
            write_csv(user_summary, ['Username', 'INFO', 'ERROR'], 'user_summary.csv')

        elif output == 'html':
            write_html(error_summary, ['Error', 'Count'], 'error_summary.html')
            write_html(user_summary, ['Username', 'INFO', 'ERROR'], 'user_summary.html')


if __name__ == "__main__":
    run_inspector('sample_logs/syslog.log', mode='summary', output='print')