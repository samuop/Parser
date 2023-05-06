#importar librerias
import ply.lex as lex
import re 
import codecs
import os
import sys
import pathlib

titulo_nro=0
head=0
text_gen=0
imag_gen=0
link_gen=0
doc_html =""

reservadas = ['APERTURA_XML', 'VERSION_XML', 'ENCODING_VERSION', 'CIERRE_XML', 'APERTURA_RSS', 'VERSION_RSS', 'CIERRE_RSS', 'APERTURA_CHANNEL', 'CIERRE_CHANNEL', 'APERTURA_TITLE', 'CIERRE_TITLE', 'APERTURA_LINK', 'CIERRE_LINK', 'APERTURA_DESC', 'CIERRE_DESC', 'APERTURA_CAT', 'CIERRE_CAT', 'APERTURA_COPY', 'CIERRE_COPY', 'APERTURA_IMAG', 'CIERRE_IMAG', 'APERTURA_HEIGHT', 'CIERRE_HEIGHT', 'APERTURA_WIDTH', 'CIERRE_WIDTH', 'APERTURA_ITEM', 'CIERRE_ITEM', 'APERTURA_LANGUAGE', 'CIERRE_LANGUAGE', 'APERTURA_WEBMASTER', 'CIERRE_WEBMASTER', 'URL', 'APERTURA_ULTEDIT', 'CIERRE_ULTEDIT', 'APERTURA_AUTOR','CIERRE_AUTOR', 'APERTURA_BD', 'CIERRE_BD', 'APERTURA_GUID', 'CIERRE_GUID', 'APERTURA_TTL', 'CIERRE_TTL',
 ]

tokens = reservadas+['TXT', 'NUM']

t_APERTURA_XML =r'\<\?xml'
t_VERSION_XML =r'\ version="1.0"'
t_ENCODING_VERSION= r'\ encoding="UTF-8"'
t_CIERRE_XML= r'\?\>'
#tokens rss
#t_APERTURA_RSS=r'\<rss'
t_VERSION_RSS=r'\ version="2.0">'
#t_CIERRE_RSS=r'\</rss>'
#tokens tags generales
#t_APERTURA_CHANNEL = r'\<channel>'
t_CIERRE_CHANNEL = r'\</channel>' 
#t_APERTURA_TITLE = r'\<title>'
#t_CIERRE_TITLE = r'\</title>'
#t_APERTURA_LINK=r'\<link>'
#t_CIERRE_LINK=r'\</link>'
#t_APERTURA_DESC=r'\<description>'
#t_CIERRE_DESC=r'\</description>'
t_APERTURA_CAT=r'\<category>'
t_CIERRE_CAT=r'\</category>'
t_APERTURA_COPY=r'\<copyright>'
t_CIERRE_COPY=r'\</copyright>'
t_APERTURA_IMAG=r'\<image>'
t_CIERRE_IMAG=r'\</image>'
t_APERTURA_HEIGHT=r'\<height>'
t_CIERRE_HEIGHT=r'\</height>'
t_APERTURA_WIDTH=r'\<width>'
t_CIERRE_WIDTH=r'\</width>'
#t_APERTURA_ITEM=r'\<item>'
t_CIERRE_ITEM=r'\</item>'
t_APERTURA_LANGUAGE=r'\<language>'
t_CIERRE_LANGUAGE=r'\</language>'
t_APERTURA_WEBMASTER=r'\<webMaster>'
t_CIERRE_WEBMASTER=r'\</webMaster>'
t_APERTURA_ULTEDIT=r'\<pubDate>'
t_CIERRE_ULTEDIT=r'\</pubDate>'
t_APERTURA_AUTOR=r'\<author>'
t_CIERRE_AUTOR=r'\</author>'
t_APERTURA_BD=r'\<lastBuildDate>'
t_CIERRE_BD=r'\</lastBuildDate>'
t_APERTURA_GUID=r'\<guid>'
t_CIERRE_GUID=r'\</guid>'
t_APERTURA_TTL=r'\<ttl>'
t_CIERRE_TTL=r'\</ttl>'
t_ignore = '\t'

#   definición de tags que se escriben en el html
#---------------------------------------#

def t_APERTURA_RSS(t):
    r'<rss'
    doc_html.write("<html>")
    return t


def t_APERTURA_CHANNEL(t):
    r'<channel>'
    doc_html.write("<head>")
    return t

def t_APERTURA_ITEM(t):
    r'<item>'
    global head
    if head == 0:
        doc_html.write("</head>\n<body>")
    head=+1
    return t

def t_APERTURA_TITLE(t):
    r'<title>'
    global text_gen
    text_gen=1
    global titulo_nro
    global imag_gen
    if titulo_nro<=1:      
        doc_html.write("<H1>")
        titulo_nro+=1
    else:
        if imag_gen == 0:
            doc_html.write("<H3>")
    return t


def t_CIERRE_TITLE(t):
    r'</title>'
    global text_gen
    text_gen=0
    global titulo_nro
    global imag_gen
    if titulo_nro<=1:      
        doc_html.write("</H1>")
        titulo_nro+=1
    else:
        if imag_gen == 0:
            doc_html.write("</H3>")
    return t


def t_APERTURA_LINK(t):
    r'<link>'
    global link_gen
    if link_gen<=1:      
        doc_html.write("<a>")
        link_gen+=1
    return t

def t_CIERRE_LINK(t):
    r'</link>'
    global link_gen
    if link_gen<=1:      
        doc_html.write("</a>")
        link_gen+=1
    return t

def t_APERTURA_DESC(t):
    r'<description>'
    global text_gen
    text_gen=1
    doc_html.write("<p>")
    return t

def t_CIERRE_DESC(t):
    r'</description>'
    global text_gen
    text_gen=0
    doc_html.write("</p>")
    return t

def t_CIERRE_RSS(t):
    r'</rss>'
    global head
    if head == 0:
        doc_html.write("</head>\n<body>")

    doc_html.write("</body>\n</html>")
    return t

#        tokens genericos  
#--------------------------------------#
#definición de tokens de cadena de URL
def t_URL(t): 
    r'(https|http|ftps|ftp)\://([a-zA-Z]|[0-9]+|\?+|\=+|;|&|\-+|_+|\.+)+(\:[0-9]+|)(/([a-zA-Z]+|ñ|á|é|í|ó|ú|Á|É|Í|Ó|Ú|[0-9]+|\-+|_+|\?+|\=+|;|&|\.+|/+)+|)(\#([a-zA-Z]+|ñ|á|é|í|ó|ú|Á|É|Í|Ó|Ú|[0-9]+|\-+|_+|\?+|\=+|;|&|\.+|/+)+|)'
    if link_gen==1:
        file.write(t.value)
    return t

  
#definición de tokens de cadena de texto
def t_TXT(t): 
 r'([a-zA-Z]+|ñ+|[0-9]+|á|é|í|ó|ú|Á|É|Í|Ó|Ú|\-|_|\#|&|\(|\)|\?|\¿|!|¡|\,|\=|\.|/+|"|;|:|\ +)+'
 if t.value.upper() in reservadas:
		t.value = t.value.upper()
		t.type = t.value
    
 if text_gen==1 and imag_gen == 0:
   doc_html.write(t.value)
 return t
  

  
#definición de tokens de cadena de numeros
def t_NUM(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_TAB(t):
  r'\t'
  doc_html.write("\t")
  pass

def t_ESPACIO(t):
    r'\ '
    doc_html.write(" ")
    pass

#definición de salto de pagina
def t_newline(t):
    r'\n+'
    global lineas
    t.lexer.lineno += len(t.value)
    doc_html.write(os.linesep)


def t_COMMENT(t):
	r'\#.*'
	pass

def t_error(t):
    t.lexer.skip(1)

analizador = lex.lex()