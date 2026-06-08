current_report = None


def set_current_report(filename: str):
    global current_report
    current_report = filename


def get_current_report():
    return current_report