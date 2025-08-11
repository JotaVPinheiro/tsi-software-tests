# Tarefa Avaliativa 5

Nesta tarefa, você irá construir uma suite de testes refinada após capaz de eliminar todos os mutantes sobreviventes gerados pela ferramenta `mutmut` do seguinte cenário.

## Cenário

Imagine que você está desenvolvendo uma funcionalidade para um e-commerce. A função em questão, `validar_voucher`, verifica se o valor de uma compra é elegível para um voucher de desconto.

**Regra de Negócio:** O voucher só é válido para compras com valor entre **R$ 50,00** e **R$ 500,00**, inclusive.

### Função

```py
def validar_voucher(valor: float) -> bool:
    """
    Verifica se um valor de compra é elegível para um voucher.
    Válido para valores entre 50.00 e 500.00 (inclusive).
    """
    return 50.00 <= valor <= 500.00
```

Para concluir a atividade você deve entregar o repositório público do github que contenha todos os testes necessários para a eliminar os mutantes gerados pelo `mutmut`. A avaliação da análise do mutantes se dará através da avaliação da saída do comando `mumut results`.

Dicas

- Crie o projeto.
- Instale o pytest e mutmut.
- Use a estrutura de pastas abordadas na video aula.
- Execute o mutmut
- Veja os resultados com mutmut results
- Crie os testes, preferência use a técnica de Análise de Valor Limite
