# Code Nexus: Abstract Architecture & Design Patterns

## 📖 Visão Geral do Projeto
Bem-vindo ao **Code Nexus**! Este projeto explora conceitos avançados de Arquitetura de Software e Programação Orientada a Objetos (POO) utilizando Python 3.10+. A jornada é dividida em duas fases principais:
1. **Fundamentos (Ex 0 ao 2):** Construção de um pipeline de processamento de dados usando Classes Abstratas, Polimorfismo e Tipagem Estrutural (Protocols).
2. **Padrões de Projeto (Ex 3 e 4):** Desenvolvimento de uma arena de simulação de combate (Sandbox) utilizando *Abstract Factories*, *Capabilities* (Mixins) e o padrão *Strategy*.

O objetivo central é demonstrar como construir sistemas fracamente acoplados, altamente escaláveis e fáceis de manter, respeitando os princípios **SOLID**.

---

## 🧠 Tópicos Aprendidos e Suas Aplicações

### 1. Classes Base Abstratas (ABC) e Sobrescrita de Métodos
* **Conceito:** O módulo `abc` do Python permite criar contratos estritos. Classes abstratas não podem ser instanciadas e forçam as classes filhas a implementarem métodos específicos (`@abstractmethod`).
* **Aplicação (Exercício 0):** Criamos a classe `DataProcessor` com os métodos abstratos `validate` e `ingest`. As classes concretas (`NumericProcessor`, `TextProcessor`, `LogProcessor`) herdaram essa base e implementaram suas próprias lógicas de validação e ingestão, enquanto reaproveitavam o método concreto `output`.

### 2. Polimorfismo
* **Conceito:** A capacidade de tratar objetos de diferentes classes de maneira uniforme, desde que compartilhem a mesma interface (contrato).
* **Aplicação (Exercício 1):** A classe `DataStream` gerencia uma lista de `DataProcessor` genéricos. Ela recebe um fluxo de dados mistos e, através de um loop, chama `.validate()` e `.ingest()` iterando sobre os processadores. O roteamento funciona sem que o `DataStream` precise saber (com `if/else`) qual é o tipo exato do dado ou do processador, respeitando o princípio **Open/Closed (OCP)**.

### 3. Tipagem Estrutural (Duck Typing com Protocols)
* **Conceito:** Em vez de forçar uma classe a herdar de uma classe base (Tipagem Nominal), definimos um formato (Protocol). Se uma classe possui os métodos exigidos com as assinaturas corretas, ela é considerada compatível (Duck Typing estruturado).
* **Aplicação (Exercício 2):** Criamos o `ExportPlugin` como um `Protocol`. Plugins como `CSVExportPlugin` e `JSONExportPlugin` não herdam de nenhuma classe do sistema, apenas implementam `.process_output()`. Isso é ideal para sistemas de plugins, pois terceiros podem criar exportadores sem precisar importar as classes internas do nosso framework.

### 4. Padrão Abstract Factory (Fábrica Abstrata)
* **Conceito:** Um padrão de criação que fornece uma interface para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas.
* **Aplicação (Exercício 3):** Criamos a `CreatureFactory`. O sistema de batalha (`battle.py`) não conhece as classes `Flameling` ou `Morphagon`. Ele apenas pede à fábrica por entidades "base" ou "evoluídas". Isso desacopla a lógica do cliente da criação dos objetos, facilitando a adição de novas famílias de criaturas no futuro.

### 5. Segregação de Interfaces e Capabilities (Mixins)
* **Conceito:** Evitar "classes deus" (God Classes). Se nem todo objeto possui uma habilidade, essa habilidade não deve estar na classe base. (Princípio da Segregação de Interface - ISP).
* **Aplicação (Exercício 3):** Em vez de colocar `.transform()` na classe base `Creature`, criamos a interface isolada `TransformCapability`. Entidades que podem se transformar usam herança múltipla (`Creature`, `TransformCapability`). Isso mantém a hierarquia limpa e permite testes dinâmicos limpos (ex: `isinstance(entity, TransformCapability)`).

### 6. Padrão Abstract Strategy (Estratégia)
* **Conceito:** Um padrão comportamental que permite definir uma família de algoritmos, colocá-los em classes separadas e tornar seus objetos intercambiáveis.
* **Aplicação (Exercício 4):** Removemos a lógica de combate (if/else sobre quem se transforma ou não) do loop do torneio. Em vez disso, criamos as classes `NormalStrategy` e `AggressiveStrategy`. Cada estratégia valida se a criatura é compatível (através da *Capability*) e executa os passos de ataque. O motor do torneio apenas chama `.act()`, delegando a decisão tática para a própria estratégia.

---

## ❓ Respostas às Questões Teóricas do Projeto

* **Por que usar Polimorfismo no DataStream?**
  Permite que o roteador trate tipos diferentes de forma padronizada. Novos processadores podem ser adicionados ao sistema sem precisar alterar ou adicionar condicionais lógicas na classe `DataStream`.

* **Diferença entre ABC e Protocol num sistema de Plugins:**
  `ABC` exige uma relação de herança direta (acoplamento rígido). `Protocol` permite validação estrutural sem herança, tornando-o perfeito para desenvolvimento de plugins de terceiros que não precisam (nem devem) estar acoplados ao núcleo da sua aplicação.

* **O perigo de não usar Capabilities isoladas:**
  Se `transform` e `revert` estivessem em `Creature`, todas as entidades básicas seriam forçadas a carregar métodos inúteis, quebrando o *Princípio da Segregação de Interfaces*. Além disso, você perderia a habilidade de checar, de forma segura, se um objeto realmente foi feito para se transformar.

* **O benefício do Padrão Strategy no Torneio:**
  Ao não verificar a família da classe no torneio, movemos a responsabilidade da decisão de combate para o objeto de estratégia. Se no futuro adicionarmos criaturas voadoras com `FlyCapability`, basta criar uma `AerialStrategy`. O núcleo do `tournament.py` permanecerá exatamente o mesmo.

---

## 🚀 Relevância na Engenharia de Software Moderna
Os padrões abordados neste projeto são os blocos de construção de frameworks reais (como Django, Spring e React), motores de jogos (como Unity e Unreal) e pipelines de dados escaláveis (como Apache Airflow). Eles garantem que seu código possa crescer para milhões de linhas sem se tornar um emaranhado de lógicas condicionais impossível de manter.