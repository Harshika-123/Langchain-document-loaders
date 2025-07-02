from langchain_community.document_loaders import WebBaseLoader

url='https://www.hey.com/'
loader=WebBaseLoader(url,requests_kwargs={"verify": False} )
docs=loader.load()
print(len(docs))
print(docs[0].page_content)