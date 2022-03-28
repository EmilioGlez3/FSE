def do_GET(self):
	# Revisamos si se accede a la raiz.
	# En ese caso se responde con la interfaz por defecto
	if self.path == ’/’:
		# 200 es el código de respuesta satisfactorio (OK)
		# de una solicitud
		self.send_response(200)
		# La cabecera HTTP siempre debe contener el tipo de datos mime
		# del contenido con el que responde el servidor
		self.send_header("Content-type", "text/html")
		# Fin de cabecera
		self.end_headers()
		# Por simplicidad, se devuelve como respuesta el contenido del
		# archivo html con el código de la página de interfaz de usuario
		self._serve_ui_file()
		# En caso contrario, se verifica que el archivo exista y se sirve
	else:
		self._serve_file(self.path[1:])