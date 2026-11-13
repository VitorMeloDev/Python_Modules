# Module06bis - Code Nexus

## Visão geral

Este diretório é um laboratório de arquitetura de software em Python. Ele reúne dois blocos de estudo conectados entre si:

1. processamento de fluxos de dados heterogêneos;
2. simulação de criaturas e combate com padrões de projeto.

A ideia central do projeto é demonstrar como construir sistemas extensíveis, desacoplados e fáceis de evoluir, sem transformar o código em uma sequência de condicionais complexas. Em vez disso, o módulo usa abstrações, protocolos, fábricas e estratégias para separar responsabilidades.

O nome “Code Nexus” funciona como metáfora: este projeto é um ponto de conexão entre distintos conceitos de engenharia de software — de processamento de eventos, validação de entrada e exportação de dados, até modelagem de entidades em um mundo de batalha.

---

## Estrutura do diretório

```text
Module06bis/
├── battle.py
├── capacitor.py
├── data_pipeline.py
├── data_processor.py
├── data_stream.py
├── tournament.py
├── ex3/
│   ├── __init__.py
│   ├── creatures.py
│   └── factories.py
├── ex4/
│   ├── __init__.py
│   └── strategies.py
└── README.md
```

### O que cada parte faz

- `battle.py`: demonstra a criação de criaturas e uma disputa simples entre duas fábricas.
- `capacitor.py`: mostra o comportamento de uma “capacidade” especial em entidades transformáveis.
- `data_processor.py`: define os processadores de dados baseados em tipos.
- `data_stream.py`: constrói um stream de dados e roteia itens por processadores registrados.
- `data_pipeline.py`: evolui a ideia anterior com exportadores em CSV/JSON e representação mais formal de pipeline.
- `tournament.py`: simula um torneio em que estratégias diferentes são aplicadas a criaturas diversas.
- `ex3/`: contém o modelo de criaturas e suas fábricas.
- `ex4/`: contém a camada de estratégias para o combate.

---

## Tema principal: engenharia orientada a abstrações

O projeto não foca em um único domínio de negócio; ele ensina princípios gerais de software aplicados em duas pequenas “arenas” diferentes:

- arena de dados: validação, ingestão, ordenação e exportação;
- arena de combate: criação, transformação e estratégia de ação.

Em ambas as áreas, a abordagem é a mesma: definir uma interface de contrato, permitir múltiplas implementações concretas e deixar o código cliente depender do comportamento, não da classe concreta.

---

## 1) Processamento de dados: abstração e polimorfismo

Os arquivos `data_processor.py`, `data_stream.py` e `data_pipeline.py` implementam uma arquitetura de processamento de dados baseada em classes e em rotinas sobre uma interface comum.

### A classe base `DataProcessor`

A base `DataProcessor` herda de `abc.ABC` e define o contrato mínimo que qualquer processador precisa respeitar:

- `validate(data) -> bool`
- `ingest(data) -> None`
- `output() -> tuple[int, str]`

Isso é um exemplo clássico de “classe abstrata” em Python. Ela expressa que existem vários tipos de processadores, mas todos devem seguir a mesma convenção.

Além disso, cada instância guarda:

- `storage`: fila de itens processados;
- `rank_counter`: contador usado para numerar entradas.

Isso permite que o sistema mantenha uma ordem de processamento e gere uma sequência estável de saídas.

### Processadores concretos

Os tipos concretos são:

- `NumericProcessor`: aceita inteiros, floats e listas numéricas;
- `TextProcessor`: aceita strings e listas de strings;
- `LogProcessor`: aceita dicionários com chaves e valores do tipo string.

Cada um implementa uma lógica específica de validação e armazenamento. A ideia é que, embora os dados sejam diferentes, eles compartilham a mesma lógica estrutural de integração no sistema.

### Validação e conformidade

A validação é feita com `isinstance()` e rejeição de valores inválidos. O projeto demonstra um cuidado importante: o dado pode ser um único valor ou uma lista de valores, e a validação precisa suportar ambos os formatos.

Exemplo de regra:

- número válido: 42, 3.14 ou `[1, 2, 3]`;
- texto válido: `'hello'` ou `['a', 'b']`;
- log válido: `{'log_level': 'INFO', 'log_message': 'ok'}`.

Se o dado não passou na validação, o código lança `ValueError`.

### Fluxo de dados (`DataStream`)

A classe `DataStream` funciona como orquestrador. Ela:

- guarda uma lista de processadores registrados;
- recebe uma sequência de dados;
- tenta encontrar um processador compatível com cada item;
- invoca `ingest()` quando a validação passa;
- imprime erro quando nenhum processador consegue processar o valor.

Esse padrão é central para o projeto: o stream não conhece cada tipo de dado em detalhes; ele depende do contrato compartilhado pela interface abstrata.

Isso é um excelente exemplo de polimorfismo em design orientado a objetos.

---

## 2) Exportação e plugins: `Protocol` em vez de herança rígida

No arquivo `data_pipeline.py`, o sistema torna-se mais sofisticado com a introdução de um contrado de plugin de exportação.

### O protocolo `ExportPlugin`

```python
class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass
```

Este é um excelente exemplo de tipagem estrutural. Em Python, um `Protocol` define um “formato” de objeto: qualquer classe que implemente o método `process_output()` pode ser tratada como um exportador compatível, mesmo sem herdar de uma classe base comum.

Isso é importante porque:

- desacopla o núcleo do sistema de plugins específicos;
- permite extensões externas e independentes;
- evita herança desnecessária;
- reduz o acoplamento entre módulos.

### `CSVExportPlugin` e `JSONExportPlugin`

Essas classes implementam a mesma interface sem precisar herdar de `ExportPlugin`. Elas apenas fornecem a assinatura esperada.

- `CSVExportPlugin` imprime uma linha com valores separados por vírgula;
- `JSONExportPlugin` formata os dados como um objeto JSON de chave/valor.

Neste ponto o projeto mostra uma boa transição de um sistema baseado em classes concretas para um sistema de plugins. Ele ilustra uma ideia fundamental da engenharia moderna: preferir contratos e comportamentos a hierarquias rígidas.

---

## 3) Aristocracia de criaturas: modelagem do mundo de combate

Os arquivos em `ex3/` modelam um pequeno universo de criaturas. O foco aqui não é o processamento de dados mas a criação de entidades com diferenças semânticas e comportamentos diversos.

### `Creature` base e comportamento comum

A classe `Creature` é abstrata e define o mínimo que todas as criaturas devem ter:

- `name`
- `element_type`
- método abstrato `attack()`
- método concreto `describe()`

Ele funciona como um contrato para o conjunto de criaturas do sistema.

### Criaturas concretas

As subclasses concretas incluem:

- `Flameling`: representa um ser de fogo básico;
- `Pyrodon`: é uma versão evoluída, também do tipo fogo;
- `Shiftling`: criatura que pode mudar de forma;
- `Morphagon`: criatura evoluída e transformável.

A relação é simples e reflexiva: todas as criaturas herdam de `Creature`, mas apenas algumas possuem uma habilidade específica extra.

---

## 4) Capability pattern e herança múltipla

O ponto mais interessante do sistema de criaturas é a classe `TransformCapability`.

### Por que não colocar transformação na `Creature`?

Se todas as criaturas recebessem um método `transform()`, o modelo ficaria errado e acoplado. Nem toda criatura pode mudar de forma. Isso violaria o Princípio de Segregação de Interface (ISP): um tipo não deve herdar comportamento que não usa.

A solução foi separar a habilidade em uma classe específica:

```python
class TransformCapability(ABC):
    def __init__(self):
        self.is_transformed = False
```

Ela define a interface de transformação e exige que qualquer classe que a implemente forneça:

- `transform()`
- `revert()`

### Herança múltipla

As criaturas transformáveis usam herança múltipla:

```python
class Shiftling(Creature, TransformCapability):
    ...
```

Esse desenho é importante porque:

- a criatura continua sendo uma criatura;
- ela também implementa uma categoria de comportamento especial;
- a lógica de transformação fica separada da lógica de identidade da entidade.

No caso da simulação, o código também faz verificações dinâmicas com `isinstance(entity, TransformCapability)`, permitindo que o sistema detecte capacidades sem depender de classes concretas.

Esse é um exemplo pedagógico de “capability-based design”: a lógica do comportamento depende da presença de uma capacidade, não de uma classe específica.

---

## 5) Fábrica abstrata (`Abstract Factory`)

O diretório `ex3/factories.py` implementa o padrão Abstract Factory.

### A interface `CreatureFactory`

```python
class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass
```

Essa interface define a criação de criaturas em famílias. O cliente não precisa conhecer as classes concretas; ele apenas solicita uma criação “básica” ou “evoluída”.

### Fábricas concretas

- `FlameFactory`: cria `Flameling` e `Pyrodon`;
- `TransformCreatureFactory`: cria `Shiftling` e `Morphagon`.

Isso é exatamente o que o padrão Abstract Factory se propõe a fazer: isolar o cliente da construção específica de objetos e facilitar a criação de famílias relacionadas.

No código do projeto, isso aparece claramente em `battle.py`, onde `test_factory()` e `test_battle()` utilizam a fábrica sem depender de qualquer classe concreta da hierarquia de criaturas.

---

## 6) Estratégia de combate (`Strategy Pattern`)

O módulo `ex4/strategies.py` introduz o padrão Strategy.

### `BattleStrategy`

A interface base define duas operações:

- `is_valid(creature) -> bool`
- `act(creature) -> None`

Ela encapsula a regra de combate em um objeto separado.

### Estratégias concretas

- `NormalStrategy`: aceita qualquer criatura base da hierarquia; executa o ataque padrão.
- `AggressiveStrategy`: exige que a criatura seja uma `TransformCapability`; antes do ataque, ela transforma, ataca e reverte.

### Por que isso importa?

No código da lógica de torneio, a responsabilidade não é “if this creature is transformable then do X”. A decisão fica na própria estratégia.

Isso traz vários ganhos:

- o algoritmo do torneio continua simples;
- o comportamento fica separado em classes específicas;
- novas estratégias podem ser adicionadas sem mexer no núcleo da simulação;
- a regra de compatibilidade fica transparente e verificável.

### Exceção de estratégia inválida

A classe `InvalidStrategyError` é usada para sinalizar que uma criatura não pode ser usada por determinada estratégia.

Isso permite um tratamento explícito e centralizado de erros. Em `tournament.py`, o código tenta aplicar duas estratégias em uma disputa e, se uma for inválida, aborta a rodada com uma mensagem de erro.

---

## 7) Torneio e execução de simulação

O arquivo `tournament.py` reúne as ideias do projeto em uma execução mais complexa.

### Fluxo da lógica

Ele recebe uma lista de pares `(CreatureFactory, BattleStrategy)` e percorre todas as combinações possíveis:

```python
for i in range(len(opponents)):
    for j in range(i + 1, len(opponents)):
```

Para cada duelo:

- cria duas criaturas usando as fábricas;
- exibe a descrição de cada uma;
- aplica a estratégia de cada lado;
- trata corretamente `InvalidStrategyError`.

Isso é um exemplo muito útil de composição de comportamento: cada facção do sistema é responsável por um aspecto do problema:

- criação: fábrica;
- decisão tática: estratégia;
- execução do combate: torneio;
- validação: exceção e guard clauses.

### Raciocínio por pares

A simulação também mostra uma ideia muito importante em design orientado a objetos: combinar componentes pequenos faz com que o sistema se torne mais flexível do que um único “motor de batalha” monolítico.

---

## 8) Arquivos de demonstração e execução

### `battle.py`

Esse arquivo faz uma demonstração simples e direta:

- usa `FlameFactory` e `TransformCreatureFactory`;
- cria uma criatura base e outra evoluída;
- imprime `describe()` e `attack()`;
- faz uma disputa entre duas famílias.

Ele serve como primeira prova prática de que a fábrica desacopla a criação de objetos da lógica de uso.

### `capacitor.py`

Neste arquivo, o foco está na capacidade especial de transformação. A função `exercise_transform()`:

- verifica se o objeto possui métodos como `describe` e `attack`;
- aplica `transform()` quando a entidade suporta `TransformCapability`;
- executa um novo `attack()`;
- chama `revert()` para restaurar o estado original.

Esse script apresenta, em formato didático, a dinâmica do comportamento por capability.

---

## 9) Temas e conceitos importantes explicados

### a) Classes abstratas (`ABC`)

Usadas para definir contratos que não devem ser instanciados diretamente. Elas garantem que implementações concretas sigam uma interface esperada. Exemplos:

- `Creature`
- `CreatureFactory`
- `DataProcessor`
- `BattleStrategy`

### b) Polimorfismo

O sistema lida com objetos diferentes por meio de uma interface comum. Isso aparece em:

- `DataStream` com `DataProcessor`;
- `run_tournament()` com `BattleStrategy`;
- `test_factory()` e `test_battle()` com `CreatureFactory`.

### c) Protocols e duck typing

O módulo mostra o uso de `Protocol` para descrever interfaces estruturais, sem exigir herança direta. Isso é muito útil em arquiteturas de plugin e extensões.

### d) Inversão de dependência

Em vez de cada módulo depender de implementações internas específicas, o código depende de abstrações. Isso reduz o acoplamento e facilita manutenção.

### e) Separação de responsabilidades

Cada tipo tem um papel bem definido:

- `DataProcessor` valida e guarda dados;
- `DataStream` roteia o fluxo;
- `ExportPlugin` serializa saídas;
- `CreatureFactory` cria entidades;
- `BattleStrategy` decide como atacar;
- `tournament.py` coordena as disputas.

### f) Tratamento de erro

O projeto usa exceções para validar estados inválidos e falhas de compatibilidade. Exemplos:

- `ValueError` para dados inválidos;
- `InvalidStrategyError` para uma estratégia incompatível com a criatura.

### g) Testabilidade e extensibilidade

A arquitetura se presta bem a evoluções:

- novos tipos de processadores podem ser adicionados;
- novos plugins de exportação podem entrar sem mexer no sistema central;
- novas criaturas e novas estratégias são simples de inserir.

---

## 10) Como este projeto se encaixa no aprendizado de programação

Este diretório é uma ponte entre dois níveis de abstração:

- nível de dados: estrutura, validação e exportação;
- nível de domínio: entidades, comportamentos e regras de combate.

Isso o torna um ótimo exemplo didático de como os mesmos princípios de design aparecem em diferentes áreas da engenharia de software:

- validação e contratos em sistemas de backend;
- regras de negócio em jogos e simulações;
- plugins e extensões em ferramentas e frameworks;
- composição de objetos em aplicações complexas.

Em outras palavras, este projeto ensina não só “como escrever classes em Python”, mas também “como organizar um sistema de forma que ele continue compreensível quando cresce”.

---

## 11) Conclusão

O diretório `Module06bis` é um estudo prático de padrões de projeto e engenharia de software orientada a objetos em Python.

Ele mostra, de forma didática, como combinar:

- abstração com `ABC`;
- flexibilidade com `Protocol`;
- criação de objetos com `Factory`;
- especialização com `Capability`;
- mudança de comportamento com `Strategy`;
- validação e processamento de dados em pipeline.

Se o objetivo é aprender a pensar em software como um conjunto de contratos, componentes e responsabilidades bem separadas, esse projeto é uma excelente referência.

---

## Execução sugerida

Para rodar cada demonstração, use o ambiente Python do projeto e execute os arquivos isoladamente, por exemplo:

```bash
python battle.py
python capacitor.py
python tournament.py
python data_processor.py
python data_stream.py
python data_pipeline.py
```

Cada script foi construído para funcionar como uma pequena palestra visual do conceito que está sendo ensinado.
