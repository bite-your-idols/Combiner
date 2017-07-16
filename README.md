# Combiner
Combine a list of CSS and/or Javascript files into a single one with Sublime Text.


## How to use
Just place the following combiner declaration in any file:

```css
/*
Combiner:{
  "combine":"/path/to/file1.css",
  "combine":"/path/to/file2.css",
  "combine":"/path/to/file3.css",
  "output":"/path/to/output.file.css"
}
*/
```

Also you can include multiple Combiner declaration in the same file:

```html

<!DOCTYPE html>
  <head>
    ...
    <!-- CSS -->  
    <!--
      Combiner:{
        "combine":"css/bootstrap.min.css",
        "combine":"css/global.min.css",
        "combine":"css/responsive.min.css",
        "output":"css/style.css"
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
        "combine":"js/jquery-3.1.1.slim.min.js",
        "combine":"js/bootstrap.min.js",
        "combine":"js/global.js",
        "output":"js/scripts.js"
      }
    -->
    <script src=js/scripts.js"></script>
  </body>
</html>

```

Or you can create an individual file (txt, json, cfg...) just for Combiner declarations:

```json
{
  "Combiner_CSS":{
    "combine":"/path/to/file1.css",
    "combine":"/path/to/file2.css",
    "combine":"/path/to/file3.css",
    "output":"/path/to/output.file.css"
  },
  
  "Combiner_JS":{
    "combine":"/path/to/file1.js",
    "combine":"/path/to/file2.js",
    "combine":"/path/to/file3.js",
    "output":"/path/to/output.file.js"
  },
  
  "Combiner_LIB":{
    "combine":"/path/to/file1.js",
    "combine":"/path/to/file2.js",
    "combine":"/path/to/file3.js",
    "output":"/path/to/output.file.js"
  }
}

```

Everytime you want to combine files you can use the Context Menu inside the Sublime Text editor window, access the Combiner command under Tools menu in Sublime Text or use the keyboard shortcut: `ctrl (super in MacOs X) + alt + c`

<br><br>

## Installation & Dependencies
Download latest zip file from [here](https://github.com/bite-your-idols/Combiner/releases) and unzip it in your Sublime Text Packages folder.

Windows: `%APPDATA%\Sublime Text 3\Packages\` | Mac OS X: `Support/Sublime\ Text\ 3/Packages/`
  
Combiner depends on [Concat](https://github.com/gko/concat) Node.js module to do its job, so right after installing this plugin you will need to install node and concat just as following:

- Visit [nodejs.org](https://nodejs.org/), download file and install it. Then make sure that node is in your PATH, open up a shell window and execute `node --version`. You should see a version number.
  
- From a shell window install concat npm module using the following command: `npm install -g concat`<br><br>
