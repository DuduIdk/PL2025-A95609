import re
import sys

def md2html(mdtext):
    
    #different header levels (# Header -> <h1>Header</h1>)
    mdtext = re.sub(r'(?m)^# (.+)$', r'<h1>\1</h1>', mdtext)
    mdtext = re.sub(r'(?m)^## (.+)$', r'<h2>\1</h2>', mdtext)
    mdtext = re.sub(r'(?m)^### (.+)$', r'<h3>\1</h3>', mdtext)
    #mdtext = re.sub(r'(?m)^#### (.+)$', r'<h4>\1<h4>', mdtext)
    #mdtext = re.sub(r'(?m)^##### (.+)%', r'<h5>\1<h5>', mdtext)
    #mdtext = re.sub(r'(?m)^###### (.+)%', r'<h6>\1<h6>', mdtext)
    
    #bold text (**Bold** -> <b>Bold</b>)
    mdtext = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', mdtext)

    #italic text (*Italic* -> <i>Italic</i>)
    mdtext = re.sub(r'\*(.*?)\*', r'<i>\1</i>', mdtext)
    
    #ordered lists (1. text  -> <ol><li>text</li></o>)
    mdtext = re.sub(r'(?m)^\d+\. (.+)$', r'<li>\1</li>', mdtext)
    mdtext = re.sub(r'(?s)(<li>.*?</li>)', r'<ol>\1</ol>', mdtext)
    
    #links ([página da UC](http://www.uc.pt) -> <a href="http://www.uc.pt">página da UC</a>)
    mdtext = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', mdtext)
    
    #images (![alternative text](path to the image))
    mdtext = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', mdtext)
    
    return mdtext
"""    
def convertFile(input_file, output_file):
    f = open(input_file,'r', encoding='utf-8')
    md = md2html(f.read())
    f.close()

    html = md2html(md)
    
    f.open(output_file, 'w', encoding='utf-8')
    f.write(html)
    
    f.close()
    """
    
def convertFile(input_file, output_file):
    # Open and read the markdown file
    with open(input_file, 'r', encoding='utf-8') as f:
        md_content = f.read()
    
    # Convert Markdown to HTML
    html_content = md2html(md_content)
    
    # Open and write to the output HTML file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python markdown_to_html.py input.md output.html")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convertFile(input_file, output_file)
        print(f"Converted {input_file} to {output_file}")
