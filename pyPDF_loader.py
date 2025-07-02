from langchain_community.document_loaders import PyPDFLoader
#Pypdf loder not perform good on scannned PDF and complex
# simple clean pdf - Pypdfloder

#pdf with tables /columns - PDFPlumberLoader

#pdf with scanned images- UnstructuredPDFLoader or AmazonTextractPDFLoader

#pdf with need layout and image data -PyMuPDFLoader

#want best structure extraction - UnstructuredPDFLoader

loader=PyPDFLoader('dl-curriculum.pdf')

docs=loader.load()

print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)
