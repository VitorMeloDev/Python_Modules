# Módulo 05 — Prática de módulos, pacotes e ambiente em Python

Este diretório é uma coleção de exercícios didáticos em Python que usa uma narrativa de alquimia e magia para ensinar conceitos fundamentais de organização de código, importação de módulos, uso de pacotes e gerenciamento de ambiente/configuração.

O projeto combina duas ideias:

- uma parte técnica, focada em programação em Python;
- uma parte metafórica, onde módulos, elementos e poções representam conceitos de engenharia de software.

A linguagem de “mágica” não é apenas estética: ela serve como analogia para a forma como o Python organiza o código em módulos, pacotes e APIs públicas/privadas.

## Visão geral do projeto

O repositório tem um caráter didático e experimental. Ele mostra:

- como um módulo pode ser importado e reutilizado;
- como um pacote expõe ou oculta funções por meio de `__init__.py` e `__all__`;
- como importar um arquivo em nível de módulo e como importar um pacote completo;
- como validar e configurar variáveis de ambiente;
- como verificar se o ambiente Python está isolado em um virtualenv;
- como lidar com dependências e versões usando `requirements.txt` e `pyproject.toml`.

Em outras palavras: o código ensina a “física” e a “química” do Python em um contexto imaginativo.

## Estrutura do diretório

```text
Module05bis/
├── alchemy/
│   ├── __init__.py
│   ├── elements.py
│   ├── potions.py
│   ├── grimoire/
│   │   ├── __init__.py
│   │   ├── dark_spellbook.py
│   │   ├── dark_validator.py
│   │   ├── light_spellbook.py
│   │   └── light_validator.py
│   └── transmutation/
│       ├── __init__.py
│       └── recipes.py
├── ex0/
│   ├── construct.py
│   ├── loading.py
│   ├── pyproject.toml
│   └── requirements.txt
├── ex1/
│   ├── .env.example
│   ├── .gitignore
│   ├── oracle.py
│   └── requirements.txt
├── elements.py
├── ft_alembic_0.py
├── ft_alembic_1.py
├── ft_distillation_0.py
├── ft_kaboom_0.py
├── ft_kaboom_1.py
├── ft_transmutation_0.py
└── README.md
```

## Os temas principais do código

### 1) Módulos e pacotes em Python

Python organiza código em módulos (.py) e pacotes (pastas com `__init__.py`).

Esse projeto usa a metáfora de alquimia para ilustrar esse conceito:

- `elements.py` representa um módulo genérico com funções básicas;
- `alchemy/` representa um pacote maior, que reúne vários submódulos;
- `alchemy.grimoire` representa um subpacote de magia; 
- `alchemy.transmutation` representa outro subpacote de transformações.

Na prática, o que é ensinado aqui é a forma como o interpretador resolve `import` e a diferença entre:

- `import elements` — módulo no nível raiz;
- `from alchemy.grimoire import light_spell_record` — import de um símbolo exportado de um pacote;
- `from alchemy.elements import create_air` — import direto de um módulo do pacote;
- `import alchemy.transmutation.recipes` — import de módulos aninhados.

### 2) API pública versus API interna

Um dos pontos mais importantes do projeto é mostrar que um pacote pode expor apenas algumas funções, deixando outras ocultas.

Isso é feito principalmente por:

- `__init__.py`;
- `__all__`;
- importações relativas (`from .... import ...`).

Exemplo:

- [alchemy/grimoire/__init__.py](alchemy/grimoire/__init__.py) expõe apenas `light_spell_record`;
- outros elementos, como a “dark” spellbook, existem no pacote, mas não são disponibilizados por padrão.

Isso ensina que um módulo pode ter funções internas que não fazem parte da API pública do pacote. Em código real, isso é uma boa prática para evitar que usuários acessem detalhes não suportados da implementação.

### 3) Importação relativa e importação absoluta

O projeto demonstra contrates entre:

- importação absoluta: `from alchemy.elements import create_air`;
- importação relativa: `from .light_validator import validate_ingredients`.

A importação relativa é usada dentro do mesmo pacote para manter a organização modular e evitar nomes longos ou ambiguidades. Isso mostra como a modularização se torna mais limpa em projetos maiores.

### 4) Namespaces, colisões e “quebra de expectativa”

Há também um conceito importante em Python: módulos podem ter nomes muito parecidos e viver em lugares diferentes. O projeto mostra isso quando uma mesma ideia (“elemento”, “poção”, “magia”) aparece em diferentes níveis da árvore do projeto.

Exemplo:

- [elements.py](elements.py) define `create_fire` e `create_water` no nível raiz;
- [alchemy/elements.py](alchemy/elements.py) define `create_earth` e `create_air` dentro do pacote;
- [alchemy/potions.py](alchemy/potions.py) combina os dois conjuntos em funções de poções.

Esse tipo de organização ilustra que o Python resolve nomes com base no namespace atual e no mecanismo de importação. Em projetos reais, isso exige disciplina para evitar confusão entre módulos de domínio e utilitários gerais.

### 5) Validação de entrada com regra de negócio

Em [alchemy/grimoire/light_spellbook.py](alchemy/grimoire/light_spellbook.py) e [alchemy/grimoire/light_validator.py](alchemy/grimoire/light_validator.py), existe um padrão simples de validação de ingredientes.

A função `validate_ingredients()`:

- converte a string para minúsculas;
- compara cada ingrediente informado com uma lista permitida;
- retorna `VALID` ou `INVALID`.

Isso mostra como a validação pode ser feita de maneira direta em Python, sem frameworks: apenas verificando se a entrada contém elementos permitidos.

O mesmo padrão aparece em [alchemy/grimoire/dark_validator.py](alchemy/grimoire/dark_validator.py), com uma lista de ingredientes mais “malignos” ou restritos.

### 6) Ambiente virtual e isolamento de dependências

A pasta [ex0](ex0) representa um laboratório de experimentos em Python, onde o foco é o ambiente de execução.

Arquivos importantes:

- [ex0/construct.py](ex0/construct.py): verifica se o programa está sendo executado dentro de um ambiente virtual (`venv`);
- [ex0/loading.py](ex0/loading.py): checa se dependências como `pandas` e `numpy` estão instaladas;
- [ex0/requirements.txt](ex0/requirements.txt): lista dependências;
- [ex0/pyproject.toml](ex0/pyproject.toml): configura a ferramenta Poetry.

Esse conjunto demonstra conceitos como:

- ambiente global vs. ambiente isolado;
- risco de instalar pacotes no sistema inteiro;
- uso de `venv` para isolar dependências;
- relação entre `requirements.txt` e `pyproject.toml` em projetos Python.

### 7) Variáveis de ambiente e segurança de configuração

A pasta [ex1](ex1) trata de configuração externa do sistema. O arquivo [ex1/oracle.py](ex1/oracle.py) lê variáveis de ambiente com `os.getenv()` e usa a biblioteca `python-dotenv` para carregar um arquivo `.env`.

Ele valida:

- `MATRIX_MODE`;
- `DATABASE_URL`;
- `API_KEY`;
- `LOG_LEVEL`;
- `ZION_ENDPOINT`.

A lógica mostra um padrão comum de produção: não exibir valores secretos no terminal, verificar se o ambiente está em desenvolvimento ou produção e avisar quando faltam variáveis críticas.

Isso é um exemplo clássico de configuração segura em aplicações reais.

## Análise detalhada dos arquivos

### [elements.py](elements.py)

Este é um módulo simples, no nível raiz do projeto. Ele contém duas funções:

```python
def create_fire() -> str:
    return "Fire element created"


def create_water() -> str:
    return "Water element created"
```

Essas funções servem como base para a “alquimia” do projeto. O módulo não depende de pacote interno, apenas define elementos básicos e estruturados.

### [alchemy/__init__.py](alchemy/__init__.py)

Esse arquivo é o ponto de entrada do pacote `alchemy`.

Ele faz:

- importar `create_air` do módulo `alchemy.elements`;
- importar `healing_potion` e `strength_potion` de [alchemy/potions.py](alchemy/potions.py);
- declarar `__all__`, definindo quais nomes devem ser exportados ao fazer `from alchemy import ...`.

Ou seja, ele controla o que o pacote “apresenta” ao mundo externo. Esse é um ótimo exemplo de API pública bem definida.

### [alchemy/elements.py](alchemy/elements.py)

Define dois elementos internos do pacote:

```python
def create_earth() -> str:
    return "Earth element created"


def create_air() -> str:
    return "Air element created"
```

Esses elementos são combinados com os definidos em [elements.py](elements.py) para criar poções e receitas mais sofisticadas.

### [alchemy/potions.py](alchemy/potions.py)

Aqui aparece a composição de módulos:

- `create_earth()` e `create_air()` vêm do pacote `alchemy`;
- `create_fire()` e `create_water()` vêm do módulo global [elements.py](elements.py).

As funções `healing_potion()` e `strength_potion()` retornam mensagens descrevendo combinações de elementos. Isso ilustra a ideia de “recursos compostos”: pequenos blocos se unem para formar algo maior.

### [alchemy/grimoire/__init__.py](alchemy/grimoire/__init__.py)

É um subpacote que expõe apenas a função `light_spell_record`.

Isso demonstra um controle de visibilidade muito útil:

- a magia leve é pública;
- a magia sombria fica acessível apenas por caminhos mais específicos.

### [alchemy/grimoire/light_spellbook.py](alchemy/grimoire/light_spellbook.py)

Faz a “lista branca” de ingredientes permitidos:

```python
["earth", "air", "fire", "water"]
```

A função `light_spell_record()` chama a validação e decide se o feitiço deve ser aceito ou rejeitado. Esse tipo de padrão erra pouco e é fácil de entender.

### [alchemy/grimoire/light_validator.py](alchemy/grimoire/light_validator.py)

Valida a string de ingredientes. Ela verifica se algum ingrediente permitido aparece na entrada e retorna uma mensagem do tipo:

```python
"Earth, wind and fire - VALID"
```

Esse arquivo demonstra que a validação pode ser separada do processamento principal, deixando o código mais modular, legível e reutilizável.

### [alchemy/grimoire/dark_spellbook.py](alchemy/grimoire/dark_spellbook.py)

Representa o “lado sombrio” da magia. Ele contém uma lista diferente de ingredientes e uma função `dark_spell_record()`. O padrão é semelhante ao da versão leve, porém com regra diferente.

Este módulo serve para mostrar que um pacote pode possuir múltiplas facetas, às vezes não expostas de forma geral.

### [alchemy/transmutation/recipes.py](alchemy/transmutation/recipes.py)

A “transmutação” é um bom exemplo de composição de vários elementos e efeitos. A função `lead_to_gold()` combina:

- `create_air()`;
- `strength_potion()`;
- `create_fire()`.

O resultado é uma mensagem que descreve a transformação de chumbo em ouro. Em termos de programação, isso simboliza a composição funcional: funções simples gerando uma operação complexa a partir de blocos menores.

## Os scripts `ft_` e o papel deles

Os arquivos `ft_` são scripts de exercícios práticos. Eles testam importações e comportamentos.

### [ft_alembic_0.py](ft_alembic_0.py)

Usa:

```python
import elements
```

E chama:

```python
elements.create_fire()
```

Esse exemplo mostra que um arquivo dentro do diretório raiz pode acessar um módulo do mesmo nível sem necessidade de empacotamento.

### [ft_alembic_1.py](ft_alembic_1.py)

Usa:

```python
import alchemy
```

Em seguida tenta acessar `alchemy.create_air()` e depois `alchemy.create_earth()`. O segundo acesso gera `AttributeError` porque `create_earth()` não foi exposto via `__all__` do pacote.

Isso aí é o ponto didático central: a importação do pacote não significa que tudo dentro dele é público.

### [ft_distillation_0.py](ft_distillation_0.py)

Importa diretamente:

```python
from alchemy.potions import healing_potion, strength_potion
```

E executa as poções. Este script mostra que o pacote se comporta como uma “linha de produção” de elementos/efeitos, combinando módulos e funções.

### [ft_kaboom_0.py](ft_kaboom_0.py)

Faz:

```python
from alchemy.grimoire import light_spell_record
```

Esse exemplo ilustra a importação direta de um símbolo público do pacote. É uma forma mais limpa de consumir a API pública da biblioteca.

### [ft_kaboom_1.py](ft_kaboom_1.py)

Tenta importar um módulo diretamente do “lado sombrio”:

```python
from alchemy.grimoire.dark_spellbook import dark_spell_record
```

Esse tipo de acesso é frequentemente usado para demonstrar que o código interno pode ser acedido sem passar pela camada pública, mas isso normalmente é evitado em software bem projetado.

### [ft_transmutation_0.py](ft_transmutation_0.py)

Importa a receita de transmutação:

```python
import alchemy.transmutation.recipes
```

E chama a função de transformação. Esse script representa o estágio mais “avançado” do laboratório: a combinação de múltiplos módulos para produzir um resultado mais complexo.

## O que esse projeto ensina de forma concreta

### 1) Como organizar código em Python

O repositório mostra uma boa divisão de responsabilidades:

- módulos simples para funções elementares;
- pacotes para agrupamento funcional;
- subpacotes para domínio específico;
- funções de validação separadas da lógica principal.

### 2) Como publicizar apenas o que é necessário

O uso de `__init__.py` e `__all__` mostra que o pacote pode ter uma API clara e controlada, e que a exposição pública não precisa ser “tudo o que existe”.

### 3) Como importar corretamente

Ele ensina a diferença entre:

- importar um módulo completo;
- importar diretamente uma função;
- importar um pacote e acessar símbolos públicos;
- importar um submódulo específico.

### 4) Como configurar um projeto Python

A pasta [ex0](ex0) e [ex1](ex1) introduzem os conceitos de:

- ambiente virtual;
- dependências;
- `.env`;
- `os.getenv()`;
- segurança de configuração.

### 5) Como escrever código didático e expressivo

A narrativa de alquimia torna a aprendizagem mais memorável. Em vez de nomes genéricos como “service”, “validator” e “helpers”, o código usa uma metáfora que traduz bem as relações entre operações e composição.

## Executando os exemplos

Dependendo do ambiente, os comandos podem ser:

```bash
python ft_alembic_0.py
python ft_distillation_0.py
python ft_transmutation_0.py
python ex0/construct.py
python ex1/oracle.py
```

Em sistemas Linux/macOS, pode ser necessário usar:

```bash
python3 ...
```

Se alguma dependência do ambiente não estiver instalada, os scripts de [ex0](ex0) e [ex1](ex1) mostram a forma correta de instalar e validar os requisitos.

## Conclusão

Este diretório não é apenas um conjunto de scripts aleatórios. Ele é um mini-laboratório de Python para ensinar, de forma visual e intuitiva, conceitos essenciais:

- módulos;
- pacotes;
- visibilidade de API;
- composição funcional;
- importação e namespace;
- gerenciamento de dependências;
- configuração por ambiente.

A metáfora da alquimia funciona muito bem porque ela traduz, de maneira acessível, a lógica concreta da organização de software em Python: pequenos elementos, combinados com regras definidas, geram sistemas maiores e mais complexos.

Em termos de aprendizado, esse repositório funciona como uma introdução madura a como o Python pensa em módulos, pacotes e organização de código em projetos reais.
