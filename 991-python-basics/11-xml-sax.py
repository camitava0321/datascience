'''
Created on Jun 10, 2016

@author: Amitava Chakraborty

Simple API for XML (SAX) : 
SAX is a standard interface for event-driven XML parsing.
One registers callbacks for events of interest and then let the parser proceed through the document. 
This is useful when documents are large or system has memory limitations. 
The parser parses the file as it reads it from disk.
Entire file is never stored in memory.

SAX obviously cannot process information as fast as DOM can when working with large files. 
On the other hand, using DOM exclusively can really kill system resources, especially if used on a lot of small files.

SAX is read-only, while DOM allows changes to the XML file. 
Since these two different APIs literally complement each other, they ca both be used in large projects.
'''
#!/usr/bin/python
import os
import xml.sax

'''
Parsing XML with SAX APIs
We need to create a ContentHandler by subclassing xml.sax.ContentHandler.
This ContentHandler handles the particular tags and attributes of of the XML file. 
A ContentHandler object provides methods to handle various parsing events. 
Its owning parser calls ContentHandler methods as it parses the XML file.

The method startDocument is called at the start of the XML file.
The method endDocument is called at the end of the XML file. 
'''
class MovieHandler( xml.sax.ContentHandler ):
   #initialise the contentHandler
   def __init__(self):
      self.CurrentData = ""
      self.type = ""
      self.format = ""
      self.year = ""
      self.rating = ""
      self.stars = ""
      self.description = ""
   '''
    The ContentHandler is called at the start and end of each element. 
    If the parser is not in namespace mode, the methods startElement(tag, attributes) and endElement(tag) are called.
    Otherwise, the corresponding methods startElementNS and endElementNS are called. 
    Here, tag is the element tag (movie), and attributes is an Attributes object (title).
   '''
   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "movie":
         print ("*****Movie*****")
         title = attributes["title"]
         print ("Title:", title)

   # Call when an elements ends
   def endElement(self, tag):
      if self.CurrentData == "type":
         print ("Type:", self.type)
      elif self.CurrentData == "format":
         print ("Format:", self.format)
      elif self.CurrentData == "year":
         print ("Year:", self.year)
      elif self.CurrentData == "rating":
         print ("Rating:", self.rating)
      elif self.CurrentData == "stars":
         print ("Stars:", self.stars)
      elif self.CurrentData == "description":
         print ("Description:", self.description)
      self.CurrentData = ""

   # The method characters(text) is passed character data of the XML file via the parameter text.
   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "type":
         self.type = content
      elif self.CurrentData == "format":
         self.format = content
      elif self.CurrentData == "year":
         self.year = content
      elif self.CurrentData == "rating":
         self.rating = content
      elif self.CurrentData == "stars":
         self.stars = content
      elif self.CurrentData == "description":
         self.description = content
  
if ( __name__ == "__main__"):
   
   BASE_DIR = os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(__file__)))) #"..\\..\\..\\")) # This is the Project Root
   print (os.getcwd())
   print(BASE_DIR)

   '''
    The make_parser Method
    creates a new parser object and returns it. 
    The parser object created will be of the first parser type the system finds.
    Syntax:
    xml.sax.make_parser( [parser_list] )
    
    Parameters:
        parser_list: The optional argument consisting of a list of parsers to use which must all implement the make_parser method.
   '''
   # create a SAX parser
   parser = xml.sax.make_parser()

   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = MovieHandler()
   parser.setContentHandler( Handler )
   
   resourceName=BASE_DIR+"\\resources\\movies.xml"
   print(resourceName)   

   '''
    The parse Method
    creates a SAX parser and uses it to parse a document.
    
    Syntax:
    xml.sax.parse( xmlfile, contenthandler[, errorhandler])
    
    Parameters 
        xmlfile: This is the name of the XML file to read from.
        contenthandler: This must be a ContentHandler object.
        errorhandler: If specified, errorhandler must be a SAX ErrorHandler object.
   '''
   parser.parse(resourceName)

   '''
    The parseString Method
    one more method to create a SAX parser and to parse the specified XML string.
    
    Syntax:
    xml.sax.parseString(xmlstring, contenthandler[, errorhandler])
    
    Parameters: 
        xmlstring: This is the name of the XML string to read from.
        contenthandler: This must be a ContentHandler object.
        errorhandler: If specified, errorhandler must be a SAX ErrorHandler object.
   '''
   xmlString="""
    <collection shelf="New Arrivals">
    <movie title="Enemy Behind">
       <type>War, Thriller</type>
       <format>DVD</format>
       <year>2003</year>
       <rating>PG</rating>
       <stars>10</stars>
       <description>Talk about a US-Japan war</description>
    </movie>
    </collection>
    """
   xml.sax.parseString(xmlString, Handler)
