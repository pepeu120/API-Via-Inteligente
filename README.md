
# API-Via-Inteligente

## Sobre o Projeto
API para detecção, registro e aprovação de acidentes de trânsito utilizando Django Rest Framework.

---

## Requisitos

- Python 3.10 ou superior
- pip
- Ambiente virtual configurado
- Django e dependências necessárias listadas no `requirements.txt`

---

## Passo a Passo para Configuração Inicial

### 1. Clonar o Repositório
```bash
git clone https://github.com/pepeu120/API-Via-Inteligente.git
cd API-Via-Inteligente
```

### 2. Configurar o Ambiente Virtual
Crie o ambiente virtual e ative-o:
```bash
python -m venv .env
```

No Windows:
```bash
.env\Scripts\activate
```

No Linux/Mac:
```bash
source .env/bin/activate
```

### 3. Instalar Dependências
Com o ambiente virtual ativado, instale as dependências:
```bash
pip install -r requirements.txt
```

### 4. Configurar o Django
1. Navegue até o diretório principal do projeto:
   ```bash
   cd core
   ```
2. Execute as migrações:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

### 5. Criar o Superusuário
Para acessar o painel administrativo, crie um superusuário:
```bash
python manage.py createsuperuser
```

### 6. Executar o Servidor
Inicie o servidor para verificar se a API está funcionando:
```bash
python manage.py runserver
```

---

## Funcionalidades do Projeto

1. **Autenticação:** Configurado para usar `TokenAuthentication` do DRF.
2. **Documentação:** Utiliza `drf-spectacular` para a geração de documentação OpenAPI/Swagger.
3. **Filtros:** Configurado `django-filter` para aplicar filtros nas consultas.

---

## Convenções de Código

- Utilize **PEP8** para o estilo de código. 
  - Para instalar o Autopep8 no VSCode, acesse o [link oficial](https://marketplace.visualstudio.com/items?itemName=ms-python.autopep8).
- Commit messages devem ser descritivos: `Adicionei o endpoint para detecção de acidentes`.

---

## Contribuição
1. Crie um branch para sua feature:
   ```bash
   git checkout -b feature/<nome-da-feature>
   ```
2. Envie suas alterações para revisão:
   ```bash
   git push origin feature/<nome-da-feature>
   ```
3. Abra um Pull Request no repositório principal.

---

## Configuração do Git Ignore
O projeto já está configurado para ignorar arquivos desnecessários como:
- Ambientes virtuais (`.env/`)
- Cache do Python (`__pycache__/`)
- Arquivos estáticos (`staticfiles/`) e de mídia (`media/`)
- Logs (`*.log`) e migrações desnecessárias

Consulte o arquivo `.gitignore` para mais detalhes.
