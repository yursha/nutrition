with open('../database/data.json', 'r') as data_file:
  data = data_file.read()
  with open('index.html.tmpl', 'r') as f:
    html = f.read().replace('{{data}}', data)
    with open('public/index.html', 'w') as output:
      output.write(html)
