# Combiner
Combine a list of local or remote CSS and/or Javascript files into a single one with Sublime Text.


## How to use
Just place the following combiner declaration in any file:

```
/*
Combiner:{
  combine:"/path/to/file1.css",
  combine:"/path/to/file2.css",
  combine:"/path/to/file3.css",
  output:"/path/to/output.file.css"
}
*/
```

Also you can include multiple Combiner declaration in the same file:

```

  <head>
    ...
    <!-- CSS -->  
    <!--
      Combiner:{
        combine:"css/bootstrap.min.css",
        combine:"css/global.min.css",
        combine:"css/responsive.min.css",
        output:"css/style.css"
      }
    -->
    <link rel="stylesheet" href="css/style.css">
    ...
  </head>
  <body>
    <h1>Hello, world!</h1>
    ...
    <!-- JS -->
    <!--
      Combiner:{
        combine:"js/jquery-3.1.1.slim.min.js",
        combine:"js/bootstrap.min.js",
        combine:"js/global.js",
        output:"js/scripts.js"
      }
    -->
    <script src=js/scripts.js"></script>
  </body>

```

Or you can create an individual file (txt, json, cfg...) just for Combiner declarations:

```
{
  "Combiner_CSS":{
    combine:"/path/to/file1.css",
    combine:"/path/to/file2.css",
    combine:"/path/to/file3.css",
    output:"/path/to/output.file.css"
  },
  
  "Combiner_JS":{
    combine:"/path/to/file1.js",
    combine:"/path/to/file2.js",
    combine:"/path/to/file3.js",
    output:"/path/to/output.file.js"
  },
  
  "Combiner_LIB":{
    combine:"/path/to/file1.js",
    combine:"/path/to/file2.js",
    combine:"/path/to/file3.js",
    output:"/path/to/output.file.js"
  }
}

```

Everytime you want to combine files you can use the Context Menu inside the Sublime Text editor window, access the Combiner command under Tools menu in Sublime Text or use the keyboard shortcut: `ctrl (super in MacOs X) + shift + c`


#### Remote Files

You can get remote files and combine then in just one local file, only restriction is you have to declare in the same block the same type of files (remote or local)

```
{ 
  "Combiner_CSS_CDN":{
    combine:"https://remote/path/to/file1.css",
    combine:"https://remote/path/to/file2.css",
    combine:"https://remote/path/to/file3.css",
    output:"/local/path/to/output.file.css"
  },

  "Combiner_CSS":{
    combine:"/path/to/file1.css",
    combine:"/path/to/file2.css",
    combine:"/path/to/file3.css",
    output:"/path/to/output.file.css"
  },

  "Combiner_JS_LIBS":{
    combine:"https://remote/path/to/file1.js",
    combine:"https://remote/path/to/file1.js",
    combine:"https://remote/path/to/file1.js",
    output:"/local/path/to/output.file.js"
  },
  
  "Combiner_JS":{
    combine:"/path/to/file1.js",
    combine:"/path/to/file2.js",
    combine:"/path/to/file3.js",
    output:"/path/to/output.file.js"
  }
}

```

Or even you can use it just to download only a single remote file

```
{ 
  "Combiner_CSS":{
    combine:"https://remote/path/to/file1.css",
    output:"/local/path/to/output.file.css"
  },

  "Combiner_JS_LIBS":{
    combine:"https://remote/path/to/file1.js",
    output:"/local/path/to/output.file.js"
  }
}

```



<br><br>

## Installation
Open the Command Palette and select “Package Control: Install Package”. Search for “Combiner”.
