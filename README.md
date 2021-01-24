# Reasons for this code

Dokuwiki is a PHP software that allows creation of wikipedia like web pages (without using any database).

The page content is formatted using its own codification (
https://github.com/mizunashi-mana/dokuwiki-plugin-mdpage )

However, at least one, markdown plugins is available (https://www.inmotionhosting.com/support/edu/dokuwiki/format-doku-content/)


# How to run
Change the last line of text_creater.py 
by input month, week_day, week_number,
like this
    
    c = text_creator(4, "giovedì", 14)

Then run

    python3 text_creator.py


The output will be available in the as standard output.
