# Cosmic Data: Observatório de Validação Pydantic 🚀

Bem-vindo ao Observatório de Dados Cósmicos! Este repositório serve como um guia de referência para dominar a validação de dados em Python usando **Pydantic v2**. O projeto é dividido em três exercícios com temática espacial que introduzem progressivamente recursos mais avançados.

## Pré-requisitos
- Python 3.10+
- `pydantic` >= 2.0 (Instalado via `pip install pydantic`)

---

## 📚 Conceitos Aprendidos

### 1. Modelos Básicos e Campos (`ex0/space_station.py`)
- **`BaseModel`**: A classe fundamental do Pydantic. Ao herdar dela, as classes Python ganham automaticamente checagem de tipo, conversão e lógica de validação.
- **Função `Field`**: Usada para definir regras estritas em atributos individuais.
  - `min_length` / `max_length` para strings.
  - `ge` (maior ou igual a) / `le` (menor ou igual a) para números.
  - `default` / `default_factory` para fornecer valores base.
- **Coerção de Tipo**: O Pydantic analisa automaticamente tipos compatíveis (por exemplo, convertendo uma string padrão ISO-8601 `"2024-10-27T08:00:00Z"` em um objeto `datetime` nativo do Python).

### 2. Lógica de Negócios Customizada (`ex1/alien_contact.py`)
- **Integração com `Enum`**: Valida se uma string de entrada corresponde estritamente a categorias predefinidas (ex: Radio, Visual, Physical, Telepathic).
- **`@model_validator(mode='after')`**: No Pydantic v2, este decorador substitui os antigos `@validator` e `@root_validator`. Ele permite executar lógicas complexas de validação que abrangem múltiplos campos *após* o Pydantic ter confirmado que os tipos de dados individuais e as restrições do `Field()` estão corretos.
  - Exemplo: Garantir que `message_received` não possa estar vazio *se* `signal_strength` for maior que `7.0`.
  - A função validadora modifica ou checa `self` e deve retornar `self` quando a validação for bem-sucedida. Se falhar, o lançamento de um `ValueError` padrão aciona um `ValidationError` do Pydantic.

### 3. Modelos Aninhados e Relacionamentos (`ex2/space_crew.py`)
- **Composição**: Os modelos Pydantic podem ser usados como dicas de tipo (type hints) dentro de outros modelos Pydantic. Demonstramos isso aninhando uma lista de objetos `CrewMember` dentro de um objeto `SpaceMission`.
- **Restrições de Lista**: O Pydantic v2 aplica limites de tamanho em iteráveis diretamente na definição do `Field()` (ex: `crew: List[CrewMember] = Field(..., min_length=1, max_length=12)`).
- **Rastreamento Profundo de Validação**: Se um `CrewMember` tiver dados inválidos (ex: idade de 14 anos), o Pydantic propaga o erro de forma elegante, apontando o índice e o atributo exatos no dicionário de erros (`loc: ('crew', 0, 'age')`).

---

## 🛠 Executando os Exemplos
Navegue até o diretório raiz e execute os scripts individualmente para observar o Pydantic capturando os erros de validação:

```bash
python ex0/space_station.py
python ex1/alien_contact.py
python ex2/space_crew.py
```