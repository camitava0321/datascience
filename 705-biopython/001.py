# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 11:42:02 2018

@author: ibm
"""

from Bio.Seq import Seq

#%% - The Sequence Class
#Central object in bioinformatics is sequence. 
#A sequence is a string of letters like ‘AGTACACTGGT’. 
myseq = Seq("AGTACACTGGT")
print (myseq)

#This is a sequence object with a generic alphabet
# - reflecting the fact we have not specified if this is a DNA or protein sequence 

print (myseq.complement())
print (myseq.reverse_complement())

#%% - The Sequence Record Class
#The next most important class
#A Sequence Record holds a sequence (as a Seq object) 
#with additional annotation including an identifier, name and description. 
#The Bio.SeqIO module for reading and writing sequence file formats works with SeqRecord objects

#This covers the basic features and uses of the Biopython sequence class. 
#Now that you’ve got some idea of what it is like to interact with the Biopython libraries, 
#it’s time to delve into the fun, fun world of dealing with biological file formats!

#An example - A plant based example - Lady Slipper Orchids
#A molecular study of Lady Slipper evolution
#Orchidaceae family - Cypripedioideae sub-family 
#5 genera: Cypripedium, Paphiopedilum, Phragmipedium, Selenipedium and Mexipedium.
#We’ll start with sequence parsing in Section 2.4, 
#but the orchids will be back later on as well - 
#for example we’ll search PubMed for papers about orchids and 
#extract sequence data from GenBank in Chapter 9, 
#extract data from Swiss-Prot from certain orchid proteins in Chapter 10, and 
#work with ClustalW multiple sequence alignments of orchid proteins in Section 6.4.1.

#%% - Parsing sequence file formats
#A large part of much bioinformatics work involves 
#dealing with the many types of file formats designed to hold biological data. 
#These files are loaded with interesting biological data, and 
#a special challenge is parsing these files into a format so that 
#you can manipulate them with some kind of programming language. 
#However the task of parsing these files can be frustrated by the fact that 
#the formats can change quite regularly, and 
#that formats may contain small subtleties which can break even the most well designed parsers.

#the Bio.SeqIO module – you can find out more in Chapter 5. 
#We’ll start with an online search the lady slipper orchids. 
#To keep this introduction simple, 
#we’re just using the NCBI website by hand. 
#Let’s just take a look through the nucleotide databases at NCBI, 
#using an Entrez online search (http://www.ncbi.nlm.nih.gov:80/entrez/query.fcgi?db=Nucleotide) for everything mentioning the text Cypripedioideae (this is the subfamily of lady slipper orchids).
#When this tutorial was originally written, 
#this search gave us only 94 hits, which we saved as a FASTA formatted text file and 
#as a GenBank formatted text file 
#(files ls_orchid.fasta and ls_orchid.gbk, 
#also included with the Biopython source code under docs/tutorial/examples/).
#If you run the search today, you’ll get hundreds of results! 
#When following the tutorial, if you want to see the same list of genes, 
#just download the two files above or copy them from docs/examples/ in the Biopython source code
#In Section 2.5 we will look at how to do a search like this from within Python.

#%% - Simple FASTA parsing example
#lady slipper orchids FASTA file ls_orchid.fasta
#Contains 94 records, each has a line starting with “>” (greater-than symbol) 
#followed by the sequence on one or more lines. 

from Bio import SeqIO
for seq_record in SeqIO.parse("ls_orchid.fasta", "fasta"):
    print (seq_record.id)
    print (repr(seq_record.seq))
    print (len(seq_record))
for seq_record in SeqIO.parse("ls_orchid.gbk", "genbank"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
from Bio.Alphabet import IUPAC
codingDNA = Seq('ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG',IUPAC.unambiguous_dna)
print (codingDNA)
templateDNA = codingDNA.reverse_complement()
print (templateDNA)
messengerRNA = codingDNA.transcribe()

