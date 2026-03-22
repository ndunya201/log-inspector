import re

def parse_log(filepath):
    """
    Reads a log file and returns a list of dicts.
    Each dict has keys: 'code', 'message', 'user'
    """
    entries = []
    with open(filepath, mode='r', encoding='UTF-8') as f:
        for line in f:
            match = re.search(
                r"ticky: ([\w+]*):? ([\w' ]*)[\[[#0-9]*\]?]? ?\((.*)\)$",
                line
            )
            if match:
                entries.append({
                    'code':    match.group(1),
                    'message': match.group(2).strip(),
                    'user':    match.group(3)
                })
    return entries


def filter_by_user(logs, username):
    """Returns only log entries for a specific user."""
    return [entry for entry in logs if entry['user'] == username]


def filter_errors(logs):
    """Returns only ERROR entries."""
    return [entry for entry in logs if entry['code'] == 'ERROR']