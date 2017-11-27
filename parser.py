import re


def csv_to_html(csv_filename, header=True, sep=','):
    with open(csv_filename, 'r') as file:
        text = ''
        if header:
            text += '<thead><tr><th>'
            text += file.readline().replace(sep, '</th><th>')
            text += '</th></tr></thead>'
        text += '<tbody>'
        for line in file:
            text += '<tr><td>'
            text += line.replace(sep, '</td><td>')
            text += '</td></tr>'
        text += '</tbody>'
    return text


def string_to_html(string, connected=True, header=True, sep=','):
    if not connected:
        return ''
    text = ''
    lines = re.finditer('(\S|,| )+', string)
    if header:
        head = next(lines)
        head = head.group(0)
        if head != '':
            text += '<thead><tr><th>'
            text += head.replace(sep, '</th><th>')
            text += '</th></tr></thead>'
    text += '<tbody>'
    for line in lines:
        line = line.group(0)
        if line == '':
            continue
        text += '<tr><td>'
        text += line.replace(sep, '</td><td>')
        text += '</td></tr>'
    text += '</tbody>'
    return text
