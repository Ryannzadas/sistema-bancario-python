# Sistema bancário com Python

Desafio da formação Python da [DIO](https://www.dio.me/), baseado no
[projeto original](https://github.com/digitalinnovationone/trilha-python-dio/blob/main/00%20-%20Fundamentos/desafio.py).

## Operações

| Opção | Operação  | Regras |
|-------|-----------|--------|
| `d`   | Depositar | Só valores positivos. |
| `s`   | Sacar     | Até 3 saques por dia, de no máximo R$ 500,00 cada, e só com saldo suficiente. |
| `e`   | Extrato   | Lista todas as movimentações e o saldo atual. |
| `q`   | Sair      | Encerra o programa. |

## Como rodar

Precisa do Python 3.8 ou mais novo. Não há dependências.

```bash
python desafio.py
```

## O que mudou em relação ao original

- Cada operação virou uma função (`depositar`, `sacar`, `exibir_extrato`).
- Se a pessoa digitar texto no lugar de um número, o programa avisa em vez de fechar com erro.
- Valores com vírgula (`50,00`) também são aceitos.
- O menu aceita a opção em maiúscula ou com espaços sobrando.
