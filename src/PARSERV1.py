import ply.yacc as yacc
#importo las mismas librerias que el lexer
import os
import codecs
import re
from lex import tokens
from sys import stdin
import msvcrt


#Sigma
def p_sigma(p):
	'''sigma : aperturaxml aperturarss'''
	print ("\nFelicidades")
	print ("Su codigo es sintacticamente correcto")

#xml
def p_aperturaxml(p):
	'''aperturaxml : APERTURA_XML VERSION_XML ENCODING_VERSION CIERRE_XML'''
	print ("TAG Apertura XML")


#rss
def p_aperturarss(p):
	'''aperturarss : APERTURA_RSS VERSION_RSS canal CIERRE_RSS'''
	print ("TAG Apertura RSS")

#tag CHANNEL
def p_canal_basico(p):
	'''canal : APERTURA_CHANNEL titulo LINK desc item CIERRE_CHANNEL
					 | APERTURA_CHANNEL titulo desc LINK item CIERRE_CHANNEL
					 | APERTURA_CHANNEL titulo LINK desc opc item CIERRE_CHANNEL
					 | APERTURA_CHANNEL titulo desc LINK opc item CIERRE_CHANNEL'''
	print ("TAG channel")
	file.write("<head>")

def p_item(p):
  '''item : APERTURA_ITEM titulo LINK desc CIERRE_ITEM
  				| APERTURA_ITEM titulo desc LINK CIERRE_ITEM
  				|
  				|
  				|
  				'''
  print("TAG ITEM")
  file.write("</head>\n<body>")

def p_item2(p):
  '''item : '''
  print("TAG ITEM")
def p_item_recursivo(p):
  '''item : APERTURA_ITEM titulo LINK desc CIERRE_ITEM item'''
  print("TAG ITEM")

def p_item_recursivo2(p):
  '''item : APERTURA_ITEM titulo desc LINK CIERRE_ITEM item'''
  print("TAG ITEM")

def p_item_opcionales(p):
  '''item : APERTURA_ITEM titulo LINK desc opc CIERRE_ITEM'''
  print("TAG ITEM")

def p_item_opcionales2(p):
  '''item : APERTURA_ITEM titulo desc LINK opc CIERRE_ITEM'''
  print("TAG ITEM")

def p_item_opcionales_recursivo(p):
  '''item : APERTURA_ITEM titulo LINK desc opc CIERRE_ITEM item'''
  print("TAG ITEM")
def p_item_opcionales_recursivo2(p):
  '''item : APERTURA_ITEM titulo desc LINK opc CIERRE_ITEM item'''
  print("TAG ITEM")

def p_titulo(p):
	'''titulo : APERTURA_TITLE TXT CIERRE_TITLE'''
	print ("TAG titulo")

def p_LINK(p):
	'''LINK : APERTURA_LINK URL CIERRE_LINK'''
	print ("TAG link")

def p_desc(p):
	'''desc : APERTURA_DESC TXT CIERRE_DESC'''
	print ("TAG descripción")

#                     TAGS OPCIONALES
#--------------------------------------------------------------#
#TAG CATEGORIA
def p_opc1(p):
	'''opc : categoria'''

def p_categoria(p):
	'''categoria : APERTURA_CAT TXT CIERRE_CAT'''
	print ("TAG categoria")

#TAG COPYRIGHT
def p_opc2(p):
	'''opc : copyright'''

def p_copyright(p):
	'''copyright : APERTURA_COPY TXT CIERRE_COPY'''
	print ("TAG copyright")

#TAG IMAGE
def p_opc3(p):
	'''opc : image'''

def p_image1(p):
	'''image : APERTURA_IMAG URL titulo LINK CIERRE_IMAG'''
	print ("TAG image")

#imagen con elementos opcionales
def p_image2(p):
	'''image : APERTURA_IMAG URL titulo LINK opcimag CIERRE_IMAG'''
	print ("TAG image")

#elementos opcionales de imagen (largo-ancho, largo, ancho)
def p_opcimag1(p):
	'''opcimag : height width'''

def p_opcimag2(p):
	'''opcimag : height'''

def p_opcimag3(p):
	'''opcimag : width'''

def p_height(p):
	'''height : APERTURA_HEIGHT NUM CIERRE_HEIGHT'''

def p_width(p):
	'''width : APERTURA_WIDTH NUM CIERRE_WIDTH'''

def p_opc4(p):
	'''opc : lenguaje'''

def p_lenguaje(p):
	'''lenguaje : APERTURA_LANGUAGE TXT CIERRE_LANGUAGE'''
	print ("TAG language")

def p_opc5(p):
	'''opc : webmaster'''

def p_WEBMASTER(p):
	'''webmaster : APERTURA_WEBMASTER TXT CIERRE_WEBMASTER'''
	print ("TAG webmaster") 

def p_opc6(p):
	'''opc : ultedit'''

def p_pubdate(p):
	'''ultedit : APERTURA_ULTEDIT TXT CIERRE_ULTEDIT'''
	print ("TAG pubdate")

def p_opc7(p):
	'''opc : autor'''

def p_autor(p):
	'''autor : APERTURA_AUTOR TXT CIERRE_AUTOR'''
	print ("TAG author")

def p_opc8(p):
	'''opc : lastbuilddate'''

def p_lastbuilddate(p):
	'''lastbuilddate : APERTURA_BD TXT CIERRE_BD'''
	print ("TAG lastBuildDate")

def p_opc9(p):
	'''opc : guid'''

def p_guid(p):
	'''guid : APERTURA_GUID TXT CIERRE_GUID'''
	print ("TAG guid")

def p_opc10(p):
	'''opc : ttl'''

def p_ttl(p):
	'''ttl : APERTURA_TTL TXT CIERRE_TTL'''
	print ("TAG ttl")
# fin elementos opcionales ----------------------------------------#



def p_error(p):
	print ("Error de sintaxis "), p
	print ("Error en la linea "+str(p.lineno))

def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print (str(cont)+". "+file)
		cont = cont+1

	while respuesta == False:
		numArchivo = input('\nNumero del test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print ("Tags reconocidos en el archivo \"%s\" \n" %files[int(numArchivo)-1])

	return files[int(numArchivo)-1]

print ("analizador sintactico")
print ("Por favor, ingrese por teclado la dirección de la carpeta en donde se encuntra los archivos.rss")
directorio = input() +'/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()


# archivo input rss 
fin = open(test)
# archivo output html
fout = open(("prueba.html"), "wt")

file.write("<!DOCTYPE html>")
file.write("<html>")

parser = yacc.yacc()
result = parser.parse(cadena)

file.write("</html>")

print (result)


# iteracion
buffer = fin.read()
	# reemplazo
buffer = buffer.replace('<title>', '<h1>')
buffer = buffer.replace('</title>', '</h1>')
buffer = buffer.replace('<description>', '<p>')
buffer = buffer.replace('</description>', '</p>')
buffer = buffer.replace('<link>', '<a>')
buffer = buffer.replace('</link>', '</a>')
buffer = buffer.replace('<url>', '<a>')
buffer = buffer.replace('</url>', '</a>')

fout.write(buffer)
fin.close()
fout.close()



msvcrt.getch()