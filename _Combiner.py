import sublime, sublime_plugin, re, os

class CombinerCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        # view = self.view
        # window = view.window()
        # # region = sublime.Region(0, view.size())
        # # allcontent = sublime.Region(0, self.view.size())

        # # path = '/'.join(self.view.file_name().split('/')[0:-1])

        archive_list=""
        pattern = '/{0,2}@import url\( *\'(.+)\' *\);' 
        full_name = self.view.file_name()
        extension = full_name.split('.')[-1]
        file_name = '.'.join(full_name.split('.')[0:-1])
        file=full_name.split('\\')[-1]
        path=full_name.split(file)[0]
        archive_output = file_name + '.comb.' + extension
        allcontent = sublime.Region(0, self.view.size())
        allcontent = self.view.substr(allcontent)

        # print (path)
        # print (file_name)
        # print (full_name)
        print (archive_output)
        # print (allcontent)

        for m in re.finditer(pattern, allcontent):
            # print('found:', m.start(), m.end())
            archivo_temp =sublime.Region(m.start(), m.end())
            archivo_temp = self.view.substr(archivo_temp)
            archivo_temp= m.group(1)
            print(archivo_temp)

            archive_list=archive_list+" "+path+archivo_temp


        arguments=archive_output+archive_list

        print ("-> concat -o "+arguments)
        
        os.system("concat -o "+arguments)


        #   i = self.view.find(test, 0)


        # m = re.search(content, text)
        # if m:
        #     found = m.group(1)
        #     print (found)
        



        # test = '/{0,2}@import url\( *\'(.+)\' *\);'
        # i = self.view.find(test, 0)

        # archive_output = file_name + '.cat.' + extension
        # print (archive_output)


        # if i:
        #     # print("go")
        #     # archive_output = file_name + '.cat.' + extension
        #     # print (archive_output)

        #     # new_view = window.new_file()
        #     # new_view.set_name(file_name + '.cat.' + extension)
        #     # region = sublime.Region(0, view.size())
        #     # content = view.substr(region)

            
        #     # try:
        #     #     print("gogo")
        #     #     # syntax_file = self.view.settings().get('syntax')
        #     #     # new_view.set_syntax_file(syntax_file)
        #     # except KeyError:
        #     #     print ('no syntax')
        #     #     pass

            
        #     # edit = new_view.begin_edit('cat')
        #     # new_view.insert(edit, 0, content)

        #     #print (new_view.find(test, 0))

        #     while new_view.find(test, 0):
        #         print("gogogo")
        #         i = new_view.find(test, 0)
        #         content = new_view.substr(i)
        #         m = re.search(test, content)
        #         print (content)
                
        #         print (m.group(1))
        #         included = m.group(1)
        #         archivo=path+included
        #         print (archivo)
        #         archive_list=" "+archive_list+" "+archivo
        #         print(archive_list)


        #         if m:
        #             print("gogogogogo")
        #             included = m.group(1)
        #             # archivo=path+included
        #             # print (archivo)
        #             # archive_list=" "+archive_list+" "+archivo
        #             # print(archive_list)
        #             try:
        #                 f = open(path + '/' + included)
        #                 # file_content = f.read()
        #                 # encoded_content = unicode(file_content, "utf-8")
        #                 # new_view.replace(edit, i, file_content)
        #                 # new_view.insert(edit, i, file_content)
        #                 print (file_content)
        #                 f.close()
                        
        #             except IOError:
        #                 print ('cannot open', included)
        #                 raise
        #             window.run_command("build")
        #             # new_view.end_edit(edit)
        #         print("fin?")

        #         # 
        #         # window.run_command("save")
                
        #     #ejecutamos el script de concat de nodejs
        #     # project_folder="W://XAMPP/htdocs/OnClick/WORKS/0nClick/web/"
        #     # os.system("concat -o "+project_folder+"css/style.css "+project_folder+"css/responsive.css "+project_folder+"css/feed.css")

        #     # project_folder=path
        #      # print ("-> concat -o "+archive_output+archive_list)

        #     os.system("concat -o "+archive_output+archive_list)
                



	# def run(self, edit):
 #        view = self.view
 #        window = view.window()
	# 	# meter un string en una posicion del documento actual
	# 	# self.view.insert(edit, 0, "Hello, World!")

	# 	# seleccionar una region del documento actual en una variable y reemplazarla por un string
	# 	allcontent = sublime.Region(0, self.view.size())
	# 	self.view.replace(edit, allcontent, 'Hello, world!')

	# 	filenames = ['test/script1.js', 'test/script2.js']

	# 	with open('comb.js', 'w') as outfile:
	# 	    for fname in filenames:
	# 	        with open(fname) as infile:
	# 	            for line in infile:
	#	                 outfile.write(line)

    # def run(self, edit):

    #     #ejecutamos el script de concat de nodejs
    #     # project_folder="W://XAMPP/htdocs/OnClick/WORKS/0nClick/web/"
    #     # os.system("concat -o "+project_folder+"css/style.css "+project_folder+"css/responsive.css "+project_folder+"css/feed.css")


    #     view = self.view
    #     window = view.window()
    #     # region = sublime.Region(0, view.size())
    #     # allcontent = sublime.Region(0, self.view.size())

    #     # path = '/'.join(self.view.file_name().split('/')[0:-1])
    #     full_name = self.view.file_name()
    #     extension = full_name.split('.')[-1]
    #     file_name = '.'.join(full_name.split('.')[0:-1])
    #     file=full_name.split('\\')[-1]
    #     path=full_name.split(file)[0]

    #     # print (path)
    #     # print (file_name)
    #     # print (full_name)

    #     test = '/{0,2}@import url\( *\'(.+)\' *\);'
    #     i = self.view.find(test, 0)

    #     if i:
    #         print("go")
    #         new_view = window.new_file()
    #         new_view.set_name(file_name + '.cat.' + extension)
    #         region = sublime.Region(0, view.size())
    #         content = view.substr(region)

            
    #         try:
    #             print("gogo")
    #             syntax_file = self.view.settings().get('syntax')
    #             new_view.set_syntax_file(syntax_file)
    #         except KeyError:
    #             print ('no syntax')
    #             pass

            
    #         # edit = new_view.begin_edit('cat')
    #         new_view.insert(edit, 0, content)

    #         print (new_view.find(test, 0))

    #         while new_view.find(test, 0):
    #             print("gogogo")
    #             i = new_view.find(test, 0)
    #             content = new_view.substr(i)
    #             m = re.search(test, content)
    #             print (content)
    #             print (i)
    #             if m:
    #                 print("gogogogogo")
    #                 included = m.group(1)
    #                 print (included)
    #                 try:
    #                     f = open(path + '/' + included)
    #                     file_content = f.read()
    #                     # encoded_content = unicode(file_content, "utf-8")
    #                     new_view.replace(edit, i, file_content)
    #                     # new_view.insert(edit, i, file_content)
    #                     print (file_content)
    #                     f.close()
                        
    #                 except IOError:
    #                     print ('cannot open', included)
    #                     raise
    #                 window.run_command("build")
    #                 new_view.end_edit(edit)
    #             print("fin?")

    #             # 
    #             # window.run_command("save")
                


    #         #metemos el tecxto en el nuevo archivo
    #         # new_view.insert(edit, 0, "Hello, World!")

    #         # new_view.end_edit(edit)
    #         # window.run_command("save")
    #         # window.run_command("build")


    #         # with open(path + "script1.js") as f:
    #         #     # return f.read()
    #         #     print(f.read())
