
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
