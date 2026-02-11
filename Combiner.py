import sublime, sublime_plugin, re, os, subprocess, urllib.request, urllib.parse, io, ssl

class CombinerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # ---
        # Definimos variables iniciales con soporte para Windows
        # ---
        full_name = self.view.file_name()
        if not full_name: 
            sublime.error_message("Combiner: Por favor, guarda el archivo antes de ejecutar el comando.")
            return
        
        extension = full_name.split('.')[-1]
        file_name = '.'.join(full_name.split('.')[0:-1])
        path = os.path.dirname(full_name) + os.sep

        allcontent = self.view.substr(sublime.Region(0, self.view.size()))

        # Patrones de búsqueda
        pattern_block = r'Combiner.*?\}'
        pattern_online = 'http'
        pattern_file = r'/{0,2}combine:*\"(.+)\" *,'
        pattern_output= r'/{0,2}output:*\"(.+)\" *'

        # Contexto SSL para evitar errores de certificados en Windows
        context = ssl._create_unverified_context()

        for temp_block in re.findall(pattern_block, allcontent, re.DOTALL):
            temp_content = ""
            
            # Bucle de elementos a concatenar
            for m in re.finditer(pattern_file, temp_block):
                temp_name = m.group(1)

                if pattern_online in temp_name:
                    # Caso: Archivo Online
                    try:
                        req = urllib.request.Request(temp_name, headers={'User-Agent': 'Mozilla/5.0'})
                        with urllib.request.urlopen(req, context=context) as response:
                            content = response.read().decode('utf-8')
                            temp_content += "\n" + content
                    except Exception as e:
                        print(f"Combiner Error (URL): {temp_name} -> {e}")
                else:
                    # Caso: Archivo Local
                    full_path_file = os.path.join(path, temp_name)
                    if os.path.exists(full_path_file):
                        with io.open(full_path_file, 'r', encoding='utf-8') as f:
                            content = f.read()
                            temp_content += "\n" + content
                    else:
                        print(f"Combiner Error (Local): No encontrado {full_path_file}")

            # Definición de archivo de salida
            try:
                out_match = re.search(pattern_output, temp_block)
                if out_match:
                    archive_output = os.path.join(path, out_match.group(1))
                else:
                    archive_output = file_name + '.comb.' + extension
            except:
                archive_output = file_name + '.comb.' + extension

            # Crear directorios si no existen
            carpetas = os.path.dirname(archive_output)
            if not os.path.exists(carpetas):
                os.makedirs(carpetas)

            # Escritura del archivo combinado
            with io.open(archive_output, 'w', encoding='utf-8') as f:
                f.write(temp_content)

            sublime.active_window().open_file(archive_output)


class MinifyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        full_name = self.view.file_name()
        if not full_name: return
        
        extension = full_name.split('.')[-1]
        file_name = '.'.join(full_name.split('.')[0:-1])

        # Endpoints actualizados de la API para evitar Redirect 308
        urls = {
            "js": "https://www.toptal.com/developers/javascript-minifier/api/raw",
            "css": "https://www.toptal.com/developers/cssminifier/api/raw",
            "html": "https://www.toptal.com/developers/html-minifier/api/raw",
            "htm": "https://www.toptal.com/developers/html-minifier/api/raw"
        }

        if extension not in urls:
            sublime.status_message(f"Combiner: Extensión .{extension} no compatible para minificar.")
            return

        url = urls[extension]

        try:
            # Leer el archivo fuente
            with io.open(full_name, 'r', encoding='utf-8') as f:
                file_content = f.read()

            # Preparar la petición POST
            postdata = urllib.parse.urlencode({'input': file_content}).encode('utf-8')
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'Content-Type': 'application/x-www-form-urlencoded'
            }
            
            # Contexto SSL para Windows
            context = ssl._create_unverified_context()

            req = urllib.request.Request(url, data=postdata, headers=headers)
            with urllib.request.urlopen(req, context=context) as handler:
                temp_content = handler.read().decode('utf-8')

            # Nombre de salida .min
            archive_output = file_name + '.min.' + extension

            # Guardar el resultado en UTF-8
            with io.open(archive_output, 'w', encoding='utf-8') as f:
                f.write(temp_content)

            # Abrir el archivo y mostrar mensaje de éxito
            sublime.active_window().open_file(archive_output)
            sublime.status_message(f"Minificado con éxito: {os.path.basename(archive_output)}")

        except Exception as e:
            sublime.error_message(f"Error al minificar: {e}")
