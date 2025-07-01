class Pessoa:
    def __init__(self,email,telefone):
        self.__email = email
        self.__telefone = telefone


    @property
    def email(self):
        return self.__email

    # metodo set
    @email.setter
    def email(self,email):
        self.__email = email
    
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self,telefone):
        self.__telefone = telefone

class PessoaFisica(Pessoa):
    def __init__(self,nome,cpf,profissao,email,telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__profissao = profissao
        super().__init__(email=email,telefone=telefone)

        @property
        def nome(self):
            return self.__nome
        
        @nome.setter
        def nome(self,nome):
            self.__nome = nome
        
        @property
        def cpf(self):
            return self.__cpf
        
        @cpf.setter
        def cpf(self,cpf):
            self.__cpf = cpf
        
        @property
        def profissao(self):
            return self.__profissao
        
        @profissao.setter
        def profissao(self,profissao):
            self.__profissao = profissao

class PessoaJuridica(Pessoa):
    def __init__(self,razao_social,nome_fantasia,cnpj,email,telefone):
        self.__razao_social = razao_social
        self.__nome_fantasia = nome_fantasia
        self.__cnpj = cnpj
        super().__init__(email=email,telefone=telefone)

        @property
        def razao_social(self):
            return self.__razao_social
        
        @razao_social.setter
        def razao_social(self,razao_social):
            self.__razao_social = razao_social

        @property
        def nome_fantasia(self):
            return self.__nome_fantasia
        
        @razao_social.setter
        def nome_fantasia(self,nome_fantasia):
            self.__nome_fantasia = nome_fantasia

        @property
        def cnpj(self):
            return self.__cnpj
        
        @cnpj.setter
        def cnpj(self,cnpj):
            self.__cnpj = cnpj