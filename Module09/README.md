# Módulo 09 — Validação de dados com Pydantic

Este módulo introduz a validação de dados em Python com `pydantic` v2, usando uma narrativa espacial para mostrar como modelos, enums e validadores funcionam na prática.

## Objetivo

O projeto é dividido em três exercícios:

- `ex0/space_station.py`: modelos básicos com `BaseModel` e `Field`
- `ex1/alien_contact.py`: enumeração e validação customizada com `@model_validator`
- `ex2/space_crew.py`: modelos aninhados e validação profunda de listas

## Pré-requisitos

- Python 3.10+
- `pydantic` >= 2.0

Instale a dependência com:

```bash
pip install pydantic
```

## Execução

No diretório do módulo, rode cada exercício individualmente:

```bash
python ex0/space_station.py
python ex1/alien_contact.py
python ex2/space_crew.py
```

## Conceitos abordados

### 1. Modelos e campos

`BaseModel` valida automaticamente tipos, conversões e regras definidas em `Field`, como `min_length`, `max_length`, `ge` e `le`.

### 2. Enums e validação de regras de negócio

A classe `AlienContact` usa um `Enum` para restringir valores válidos e um `@model_validator(mode="after")` para aplicar a regra de negócio:

- se `signal_strength > 7.0`, a mensagem não pode estar vazia.

### 3. Modelos aninhados

No exercício final, `SpaceMission` contém uma lista de `CrewMember` e valida regras de segurança do cenário, além de propagação de erros do Pydantic.

## Observação

A ideia central do módulo é demonstrar que validação não é apenas sobre tipos: também é sobre regras de negócio que protegem o sistema contra entradas inconsistentes.
