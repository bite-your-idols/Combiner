import sublime, sublime_plugin, re, os

class CombinerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
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
        # print (archive_output)
        # print (allcontent)

        for m in re.finditer(pattern, allcontent):
            # print('found:', m.start(), m.end())
            temp_name =sublime.Region(m.start(), m.end())
            temp_name = self.view.substr(temp_name)
            temp_name= m.group(1)
            print(temp_name)
            archive_list=archive_list+" "+path+temp_name

        arguments=archive_output+archive_list
        print ("-> concat -o "+arguments)
        os.system("concat -o "+arguments)