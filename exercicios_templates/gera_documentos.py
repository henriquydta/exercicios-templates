from validate_docbr import CPF, CNPJ

def gera_doc(doc_escolhido):
    if(doc_escolhido == 'CPF'):
        documento = CPF()
        docs = []
        for i in range(5):
            doc = documento.generate(True)
            print(doc)
            docs.append(doc)    
        for doc in docs:
            print(documento.validate(doc))
        return docs
        
    elif(doc_escolhido == 'CNPJ'):
        documento = CNPJ()
        docs = []
        for i in range(5):
            doc = documento.generate(True)
            print(doc)
            docs.append(doc)
            
        for doc in docs:
            print(documento.validate(doc))
        return docs
    
    return 'Documento inválido'