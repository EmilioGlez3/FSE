def do_POST(self):
	# Primero se obtiene la longitud de la cadena de datos recibida
	content_length = int(self.headers.get(’Content-Length’))
	if content_length < 1:
		return
	# Después se lee toda la cadena de datos
	post_data = self.rfile.read(content_length)
	# Finalmente, se decodifica el objeto JSON y se procesan los datos.
	# Se descartan cadenas de datos mal formados
	try:
		jobj = json.loads(post_data.decode("utf-8"))
		self._parse_post(jobj)
	except:
		print(sys.exc_info())
		print("Datos POST no recnocidos")