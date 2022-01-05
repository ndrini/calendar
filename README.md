# Reasons for this code

Dokuwiki is a PHP software that allows creation of wikipedia like web pages (without using any database).

The page content is formatted using its own codification (
https://github.com/mizunashi-mana/dokuwiki-plugin-mdpage )

However, at least one, markdown plugins is available (https://www.inmotionhosting.com/support/edu/dokuwiki/format-doku-content/)

# Warning
Due to the fact that my mother tongue language is Italian, I set the calendar in Italian. 
Just change constants.yaml with your language, if necessary. 

# How to run
Run

    $ python3 text_creator.py

and then **follow the guided path ** by answering the questions.
 
The output (that can be copied/pasted in dokuwiki page) will be available in the as standard output.

# Test 
Run, after installing pytest if necessary: 

    $ python3 -m pytest text_creator_test.py

or just 

    $ pytest text_creator_test.py
