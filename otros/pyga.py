import pygal

line_chart = pygal.Line(interpolate='lagrange', x_title = "Cantidad de deals publicados")
line_chart.title = 'Promedio de ventas diarias'
line_chart.x_labels = [None, 1, None, 2, None, 3, None, 4, None, 5, None]
line_chart.add('Hotel', [None, 1100, None, 1200, None, 1250, None, 1270, None, 1280])
line_chart.add('Cota Inferior', [1090, None, 1090, None, None, None, None, None, None, None], dots_size = 0)
line_chart.add('Cota Inferior', [None, None, 1190, None, 1190, None, None, None, None, None], dots_size = 0)
line_chart.add('Cota Inferior', [None, None, None, None, 1240, None, 1240, None, None, None], dots_size = 0)
line_chart.add('Cota Inferior', [None, None, None, None, None, None, 1260, None, 1260, None], dots_size = 0)
line_chart.add('Cota Inferior', [None, None, None, None, None, None, None, None, 1270, None, 1270], dots_size = 0)
line_chart.add('Cota Superior', [1110, None, 1110, None, None, None, None, None, None, None], dots_size = 0)
line_chart.add('Cota Superior', [None, None, 1210, None, 1210, None, None, None, None, None], dots_size = 0)
line_chart.add('Cota Superior', [None, None, None, None, 1260, None, 1260, None, None, None], dots_size = 0)
line_chart.add('Cota Superior', [None, None, None, None, None, None, 1280, None, 1280, None], dots_size = 0)
line_chart.add('Cota Superior', [None, None, None, None, None, None, None, None, 1290, None, 1290], dots_size = 0)
line_chart.render_to_file("asdf.svg")