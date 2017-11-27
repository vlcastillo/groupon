
def string_to_html(head, datos, connected=True, header=True, sep=','):
    if not connected:
        return ''
    text = ''
    if header and head != '':
        text += '<thead><tr><th>'
        text += '</th><th>'.join(head)
        text += '</th></tr></thead>'
    text += '<tbody>'
    for line in datos:
        if line == '':
            continue
        if type(line[3]) is float:
            line[3] = str(round(line[3], 0))
        text += '<tr><td>'
        text += '</td><td>'.join(line)
        text += '</td></tr>'
    text += '</tbody>'
    table = '<div class="table-responsive"><table class="table table-striped"' \
            '>' + text + '</table></div>'
    return table
