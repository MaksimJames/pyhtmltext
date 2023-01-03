
# pyhtmltext

pyhtmltext is a usefull and flexible tool for extracting text from html.

# Help
See for more details.

# Installation
```
  pip install pyhtmltext
```

# Simple usage
```
  from pyhtmltext import Extractor


  html_string = '''<h2 class="widget-title"><span aria-hidden="true" class="icon-get-started"></span>Getting Started</h2><p>Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages. The following pages are a useful first step to get on your way writing programs with Python!</p>'''

  extractor = Extractor(html=html_string)

  # Extracting whole text from html with separator
  extractor.extract_text()
  #> "Getting Started|separator|Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages. The following pages are a useful first step to get on your way writing programs with Python!"

  # Extracting sentences from html
  extractor.extract_sentences()
  #> ['Getting Started', "Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages.", 'The following pages are a useful first step to get on your way writing programs with Python!']
```