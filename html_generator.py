 
 # program to automate output of notes into an HTML file. 
 
import webbrowser
import os

def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
    <p><p>  ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

# Wrapper function will add header, chapter and footer to the html string\
# to complete the HTML code
def wrapper_concept_html(body_html):
    header_html_text = '''
<!DOCTYPE html>
<head> 
   <meta charset="UTF-8">
    <title> Larry's Notes </title>
  <link rel="stylesheet" href="style.css"> 
</head>
<body>
<div class="concept-chapter"> </div> 
'''
    tail_html_text = '''
<div class="concept-chapter"> </div> 
</body>
'''
    full_body = header_html_text + body_html + tail_html_text 
    return full_body

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description

''' create breaks in the page by adding a chapter function '''
def chapter_concept_html():
    chapter = ''' <div class="concept-chapter">
        
        </div> '''
    
    return chapter
    
def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter += 1
        start_of_concept_string = text.find('TITLE:')
        end_of_concept_string   = text.find('TITLE:', start_of_concept_string + 1)
        if end_of_concept_string >= 0:
            concept = text[start_of_concept_string:end_of_concept_string]
        else: 
            end_of_concept_string = len(text)
            concept = text[start_of_concept_string:]
        text = text[end_of_concept_string:]
    return concept

print "\n Input file: 'lesson_notes.txt' Output file: 'autocode.html' in web browser."
print "\n File: style.css should be located in the same directory. \n" 


# Read from file 'lesson_notes.txt'
textstr = ' '
fileo = open("lesson_notes.txt", "r+")
textstr = fileo.read();
fileo.close()

def generate_all_html(text):
    counter = 1
    concept = get_concept_by_number(text, counter)
    body_html = ''
    while concept != '':
        title = get_title(concept)
        description = get_description(concept)
        concept_html = generate_concept_HTML(title, description)
        body_html = body_html + concept_html
        counter = counter + 1
        if counter % 5 == 0:
            chapter = chapter_concept_html()
            body_html = body_html + chapter
        concept = get_concept_by_number(text, counter)
        
    return wrapper_concept_html(body_html)

# Send output to file 'autocode.html'

f = open('autocode.html', 'w')
f.write (generate_all_html(textstr))
f.close()
 
# Close the file and get the path name and directory 
          
from urllib import pathname2url
 
url = 'file:{}'.format(pathname2url(os.path.abspath('autocode.html')))

# After getting the path and filename stored in url, open a 
# web browser with the filename
  
webbrowser.open(url)
 
