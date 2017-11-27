
def string_to_html(head, datos, connected=True, header=True, sep=','):
    if not connected:
        return ''
    text = ''
    if header and head != []:
        text += '<thead><tr><th>'
        text += '</th><th>'.join(head)
        text += '</th></tr></thead>'
    text += '<tbody>'
    for line in datos:
        if type(line) is not list or len(line) < 3:
            continue
        if type(line[2]) is float:
            line[2] = str(round(line[2], 0))
        text += '<tr><td>'
        text += '</td><td>'.join(line)
        text += '</td></tr>'
    text += '</tbody>'
    table = '<div class="table-responsive"><table class="table table-striped"' \
            '>' + text + '</table></div>'
    return table

print(string_to_html(['hola1', 'hola2', 'hola3'], []))
