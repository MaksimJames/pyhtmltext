# Terms

- **entities** - all entities in your html (tag, text, etc..)
- **outer tags** - tags that break html into semantic blocks. By default using tags list from **pythmltext/const.py** but you can use your own list of outer tags. For exaple ```Extractor(outer_tags=['div', 'h1', 'h2', 'whatever you need'])```.
- **inner tags** -  tags that not break html into semantic blocks. By default using tags list from **pythmltext/const.py** but you can use your own list of inner tags. For exaple ```Extractor(inner_tags=['a', 'span', 'whatever you need'])```.
- **non processing tags** - tags that you dont need to parse. For example ```<script>alert('Hello, how are you?')</script>``` if script tag on non processing tags that text ```alert('Hello, how are you?')``` does not parse
- **separator** - Some string-separator wich helps you to split text by semantic blocks

# class Extractor(html, separator, outer_tags, inner_tags, non_processing_tags)

- html - **required**. Your html you want to parse.
- separator - **not required**. By default using |separator|
- outer_tags - **not required**. Param if you want to use your own list of outer tags.
- inner_tags - **not required**. Param if you want to use your own list of inner tags.
- non_processing_tags - **not required**. Param if you want to use your own list of non processing tags.

# Methods

- get_text() - returns whole text from html splited by separator (if you need this)
- get_sentences() - return sentences from the text from html sentenized by razdel

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

## Usage with your own separator

```
from pyhtmltext import Extractor


  html_string = '''<h2 class="widget-title"><span aria-hidden="true" class="icon-get-started"></span>Getting Started</h2><p>Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages. The following pages are a useful first step to get on your way writing programs with Python!</p>'''

  extractor = Extractor(html=html_string, separator='$$')

  # Extracting whole text from html with separator
  extractor.extract_text()
  #> "Getting Started$$Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages. The following pages are a useful first step to get on your way writing programs with Python!"

  # Extracting sentences from html
  extractor.extract_sentences()
  #> ['Getting Started', "Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages.", 'The following pages are a useful first step to get on your way writing programs with Python!']
```

## Usage without separator

```
from pyhtmltext import Extractor


  html_string = '''<h2 class="widget-title"><span aria-hidden="true" class="icon-get-started"></span>Getting Started</h2><p>Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages. The following pages are a useful first step to get on your way writing programs with Python!</p>'''

  extractor = Extractor(html=html_string, separator=None)

  # Extracting whole text from html with separator
  extractor.extract_text()
  #> "Getting StartedPython can be easy to pick up whether you're a first time programmer or you're experienced with other languages. The following pages are a useful first step to get on your way writing programs with Python!"

  # Extracting sentences from html
  extractor.extract_sentences()
  #> ['Getting Started', "Python can be easy to pick up whether you're a first time programmer or you're experienced with other languages.", 'The following pages are a useful first step to get on your way writing programs with Python!']
```

## NOTE!

If you want to use your own separator try to use exotic separator string that not contains in your html

## Usage with default tags lists
```
  extractor = Extractor(html=html_string)
```

## Usage with your own tags lists
```
  extractor = Extractor(html=html_string, outer_tags=YOUR OUTER TAGS, inner_tags=YOUR INNER TAGS, non_processing_tags=YOUR NON PROCESSING TAGS)
```

## NOTE!

So with your own tags lists you can set Extractor as you want and what result you need
