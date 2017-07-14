import sublime, sublime_plugin, re, os, subprocess

class CombinerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # ---
        # definimos variables iniciales
        # ---
        archive_list=""
        pattern = '/{0,2}@combine_css\( *\'(.+)\' *\)' 
        pattern_output= '/{0,2}@output_css\( *\'(.+)\' *\)' 

        full_name = self.view.file_name()
        extension = full_name.split('.')[-1]
        # file_name = '.'.join(full_name.split('.')[0:-1])
        file=full_name.split('\\')[-1]
        path=full_name.split(file)[0]

        allcontent = sublime.Region(0, self.view.size())
        allcontent = self.view.substr(allcontent)

        # print (path)
        # print (file_name)
        # print (full_name)
        # print (archive_output)
        # print (allcontent)

        # ---
        # cogemos el archivo de destino
        # ---
        try:
            archive_output = re.search(pattern_output,allcontent).group(1)
            archive_output = path + archive_output
        except AttributeError:
            archive_output = path + '.comb.' + extension

        print(archive_output)


        # ---
        # loop cogiendo los elementos a concatenar
        # ---
        for m in re.finditer(pattern, allcontent):
            # print('found:', m.start(), m.end())
            temp_name =sublime.Region(m.start(), m.end())
            temp_name = self.view.substr(temp_name)
            temp_name= m.group(1)
            # print(temp_name)
            archive_list=archive_list+" "+path+temp_name


        # ---
        # con todo definido ejecutamos el concatenado
        # ---
        # opcion 1: abrir una consola del OS
        # arguments=archive_output+archive_list
        # print ("-> concat -o "+arguments)
        # os.system("concat -o "+arguments)
        # subprocess.Popen(["concat -o "+arguments])

        # opcion 2: usando subprocess no hace falta abrir una ventana de cmd
        arguments=archive_output+archive_list
        print ("-> concat -o "+arguments)
        USE_SHELL = sublime.platform() == 'windows'
        POPEN_ENV = ({'PATH': ':'.join(['/usr/local/bin', os.environ['PATH']])}) if sublime.platform() == 'osx' and os.path.isdir('/usr/local/bin') else None
        cmd="concat -o "+arguments
        subprocess.Popen(cmd, stderr=subprocess.PIPE, shell=USE_SHELL, env=POPEN_ENV)


        # ---
        # despues habria que abrir el archivo generado
        # ---