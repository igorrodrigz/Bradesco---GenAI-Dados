# Guia de Uso - Agent Memory Configuration

## Introdução

Este guia fornece instruções detalhadas sobre como usar o sistema de configuração de memória do agente para otimização de consulta a dados.

## Instalação Rápida

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/igorrodrigz/Bradesco---GenAI-Dados.git
cd Bradesco---GenAI-Dados
```

### Passo 2: Executar o Script de Configuração

```bash
chmod +x setup.sh
./setup.sh
```

### Passo 3: Ativar o Ambiente Virtual

```bash
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate    # Windows
```

### Passo 4: Configurar a Chave da API

Edite o arquivo `.env` e adicione sua chave da OpenAI:

```env
OPENAI_API_KEY=sk-your-actual-key-here
```

## Conceitos Principais

### 1. Armazenamento de Memória

O sistema usa ChromaDB para armazenar memórias de forma vetorial, permitindo busca semântica eficiente.

### 2. Embeddings

Utiliza embeddings da OpenAI para converter texto em vetores numéricos que capturam significado semântico.

### 3. Busca Semântica

Permite encontrar memórias relevantes baseado em similaridade de significado, não apenas palavras-chave.

## Exemplos de Uso

### Exemplo 1: Uso Básico

```python
from src.agent_memory import MemoryStore, AgentMemoryConfig

# Criar configuração
config = AgentMemoryConfig()

# Inicializar o store
memory_store = MemoryStore(config)

# Adicionar memória
memory_id = memory_store.add_memory(
    content="Cliente interessado em investimentos",
    metadata={"user_id": "123", "category": "investments"}
)

# Buscar memórias similares
results = memory_store.query_memories("investimentos", n_results=5)

for result in results:
    print(result['content'])
```

### Exemplo 2: Filtragem por Metadados

```python
# Buscar apenas para um usuário específico
results = memory_store.query_memories(
    query="produtos bancários",
    filter_metadata={"user_id": "123"}
)
```

### Exemplo 3: Histórico Contextual

```python
# Obter todas as memórias de um usuário
all_memories = memory_store.get_all_memories()
user_memories = [
    m for m in all_memories 
    if m['metadata'].get('user_id') == "123"
]
```

## Casos de Uso Específicos

### 1. Atendimento ao Cliente com Contexto

```python
# Quando um cliente retorna
customer_id = "cliente_123"

# Recuperar histórico
history = memory_store.query_memories(
    query="últimas interações",
    filter_metadata={"user_id": customer_id}
)

# Usar contexto para personalizar atendimento
for interaction in history:
    print(f"Interação anterior: {interaction['content']}")
```

### 2. Recomendações Personalizadas

```python
# Baseado em interações anteriores
customer_interests = memory_store.query_memories(
    query="preferências do cliente",
    filter_metadata={"user_id": customer_id, "category": "preferences"}
)

# Gerar recomendações
for interest in customer_interests:
    print(f"Cliente demonstrou interesse em: {interest['content']}")
```

### 3. Análise de Padrões

```python
# Obter todas as interações de uma categoria
all_memories = memory_store.get_all_memories()
investment_queries = [
    m for m in all_memories 
    if m['metadata'].get('category') == 'investments'
]

print(f"Total de consultas sobre investimentos: {len(investment_queries)}")
```

## Configurações Avançadas

### Personalizar Threshold de Relevância

```python
config = AgentMemoryConfig()
config.memory_relevance_threshold = 0.8  # Aumentar para resultados mais precisos

memory_store = MemoryStore(config)
```

### Limitar Tamanho da Memória

```python
config = AgentMemoryConfig()
config.max_memory_size = 200  # Armazenar até 200 memórias

memory_store = MemoryStore(config)
```

### Personalizar Local de Armazenamento

```python
config = AgentMemoryConfig()
config.chroma_persist_directory = "/caminho/personalizado/db"

memory_store = MemoryStore(config)
```

## Melhores Práticas

### 1. Organização de Metadados

Sempre inclua metadados estruturados:

```python
metadata = {
    "user_id": "cliente_123",
    "category": "investments",
    "subcategory": "fixed_income",
    "priority": "high",
    "timestamp": "2024-01-15T10:30:00"
}

memory_store.add_memory(content="...", metadata=metadata)
```

### 2. Consultas Eficientes

Use consultas específicas:

```python
# ✓ Boa prática - específico
results = memory_store.query_memories("CDB com liquidez diária", n_results=3)

# ✗ Evitar - muito genérico
results = memory_store.query_memories("produto", n_results=100)
```

### 3. Limpeza Regular

Periodicamente, remova memórias antigas:

```python
# Obter memórias antigas
old_memories = [
    m for m in memory_store.get_all_memories()
    if datetime.fromisoformat(m['metadata']['timestamp']) < cutoff_date
]

# Remover
for mem in old_memories:
    memory_store.delete_memory(mem['id'])
```

### 4. Backup de Dados

Faça backup regular do diretório ChromaDB:

```bash
# Backup
cp -r ./chroma_db ./backups/chroma_db_$(date +%Y%m%d)

# Restauração
cp -r ./backups/chroma_db_20240115 ./chroma_db
```

## Solução de Problemas

### Erro: "No module named 'chromadb'"

**Solução**: Certifique-se de instalar as dependências:
```bash
pip install -r requirements.txt
```

### Erro: "OpenAI API key not found"

**Solução**: Configure a chave no arquivo `.env`:
```env
OPENAI_API_KEY=sk-your-key-here
```

### Memórias não sendo encontradas

**Solução**: 
1. Verifique o threshold de relevância
2. Use consultas mais específicas
3. Verifique se as memórias foram realmente adicionadas

```python
# Verificar total de memórias
count = memory_store.count_memories()
print(f"Total de memórias: {count}")
```

## Recursos Adicionais

### Documentação da API

- **add_memory()**: Adiciona nova memória
- **query_memories()**: Busca por similaridade
- **get_memory()**: Recupera memória específica
- **delete_memory()**: Remove memória
- **get_all_memories()**: Lista todas as memórias
- **clear_all_memories()**: Limpa todas as memórias
- **count_memories()**: Conta memórias armazenadas

### Exemplos Práticos

Execute os exemplos fornecidos:

```bash
# Exemplo básico
python examples/basic_usage.py

# Consultas otimizadas
python examples/optimized_queries.py
```

## Suporte

Para problemas ou dúvidas:
1. Verifique este guia
2. Execute os testes: `python tests/test_structure.py`
3. Abra uma issue no GitHub

## Próximos Passos

1. Explore os exemplos fornecidos
2. Personalize a configuração para seu caso de uso
3. Integre com seus sistemas existentes
4. Monitore performance e ajuste conforme necessário
