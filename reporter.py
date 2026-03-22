import csv
import operator

def get_error_summary(logs):
    """
    Returns a list of (error_message, count) tuples,
    sorted from most common to least common.
    """
    errors = {}
    for entry in logs:
        if entry['code'] == 'ERROR':
            msg = entry['message']
            errors[msg] = errors.get(msg, 0) + 1

    return sorted(errors.items(), key=operator.itemgetter(1), reverse=True)


def get_user_summary(logs):
    """
    Returns a list of (username, INFO count, ERROR count) tuples,
    sorted alphabetically by username.
    """
    users = {}
    for entry in logs:
        user = entry['user']
        if user not in users:
            users[user] = {'INFO': 0, 'ERROR': 0}
        users[user][entry['code']] += 1

    sorted_users = sorted(users.items(), key=operator.itemgetter(0))
    return [(user, counts['INFO'], counts['ERROR']) for user, counts in sorted_users]


def write_csv(data, headers, filepath):
    """Writes summary data to a CSV file."""
    with open(filepath, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)
    print(f"CSV saved to {filepath}")


def write_html(data, headers, filepath):
    """Writes summary data to an HTML file with a styled table."""
    header_row = "".join(f"<th>{h}</th>" for h in headers)
    data_rows = ""
    for row in data:
        cells = "".join(f"<td>{cell}</td>" for cell in row)
        data_rows += f"<tr>{cells}</tr>\n"

    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Log Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; }}
        table {{ border-collapse: collapse; width: 60%; }}
        th {{ background-color: #4CAF50; color: white; padding: 10px; text-align: left; }}
        td {{ padding: 8px; border-bottom: 1px solid #ddd; }}
        tr:hover {{ background-color: #f5f5f5; }}
    </style>
</head>
<body>
    <h2>Log Inspector Report</h2>
    <table>
        <tr>{header_row}</tr>
        {data_rows}
    </table>
</body>
</html>"""

    with open(filepath, 'w') as f:
        f.write(html)
    print(f"HTML saved to {filepath}")