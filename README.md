# Sistema de Imobiliária

Sistema para cadastro e gerenciamento de Pessoas (Inquilinos e Proprietários) e Imóveis, com aplicação de diversos padrões de projeto.

## Padrões de Projeto Utilizados

### 1. Factory Method
Encapsula a criação de `Proprietario`, `Inquilino` e `Imovel`, facilitando manutenção e extensão.

### 2. Singleton
Garante que apenas uma instância do banco de dados em memória (`Database`) seja utilizada durante a aplicação.

### 3. Facade (Estrutural)
Centraliza operações do sistema imobiliário na classe `ImobiliariaFacade`, facilitando o uso e integração dos componentes.

### 4. Decorator (Estrutural)
Permite adicionar logs e outras funcionalidades às operações sem alterar o código principal, usando o decorator `log_operacao`.

### 5. Strategy (Comportamental)
Permite diferentes estratégias de cálculo do valor do aluguel (`AluguelNormal`, `AluguelComDesconto`, `AluguelComTaxa`), tornando o sistema flexível para promoções, reajustes ou descontos.

### 6. Observer (Comportamental)
Permite que partes do sistema sejam notificadas automaticamente quando um imóvel é alugado, como o `LogAluguelObserver` que registra logs de aluguel.

---

## Como executar

1. Instale o Python 3.x.
2. Clone o repositório.
3. Execute o sistema:
   ```sh
   python main.py
   ```

## Testes

Para rodar os testes unitários:
```
python -m unittest discover tests
```
