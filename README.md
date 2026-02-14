# Bradesco - GenAI Dados

## Configuração de Memória de Agente para Consulta a Dados Otimizado

Este projeto implementa um sistema de memória para agentes de IA com capacidades de armazenamento e recuperação otimizada de dados usando ChromaDB e embeddings vetoriais.

## 📋 Visão Geral

O sistema de memória do agente permite:
- Armazenamento persistente de interações e contextos
- Busca semântica otimizada usando embeddings vetoriais
- Filtragem por metadados e contexto
- Gerenciamento eficiente de histórico de conversações
- Configuração flexível via variáveis de ambiente

## 🚀 Características

- **Armazenamento Vetorial**: Utiliza ChromaDB para armazenamento eficiente de embeddings
- **Busca Semântica**: Recuperação de memórias baseada em similaridade semântica
- **Metadados Estruturados**: Suporte para categorização e filtragem por metadados
- **Configuração Flexível**: Configuração via arquivos `.env`
- **API Simples**: Interface Python intuitiva para operações de memória
- **Otimização de Consultas**: Estratégias de consulta otimizadas para performance

## 📦 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- Chave de API da OpenAI (para embeddings)

### Configuração

1. Clone o repositório:
```bash
git clone https://github.com/igorrodrigz/Bradesco---GenAI-Dados.git
cd Bradesco---GenAI-Dados
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env e adicione sua chave da OpenAI
```

## ⚙️ Configuração

Edite o arquivo `.env` com suas configurações:

```env
# OpenAI API Configuration
OPENAI_API_KEY=your_openai_api_key_here

# ChromaDB Configuration
CHROMA_PERSIST_DIRECTORY=./chroma_db
CHROMA_COLLECTION_NAME=agent_memory

# Agent Configuration
MAX_MEMORY_SIZE=100
MEMORY_RELEVANCE_THRESHOLD=0.7
```

## 💡 Uso

### Exemplo Básico

```python
from src.agent_memory import MemoryStore, AgentMemoryConfig

# Inicializar a configuração
config = AgentMemoryConfig()

# Criar instância do memory store
memory_store = MemoryStore(config)

# Adicionar uma memória
memory_id = memory_store.add_memory(
    content="Cliente interessado em investimentos de renda fixa",
    metadata={"category": "investments", "user_id": "user123"}
)

# Consultar memórias similares
results = memory_store.query_memories(
    query="investimentos",
    n_results=5
)

# Exibir resultados
for result in results:
    print(f"Conteúdo: {result['content']}")
    print(f"Relevância: {result.get('relevance', 'N/A')}")
```

### Exemplos Disponíveis

Execute os exemplos fornecidos:

```bash
# Exemplo básico de uso
python examples/basic_usage.py

# Exemplo de consultas otimizadas
python examples/optimized_queries.py
```

## 📚 Estrutura do Projeto

```
Bradesco---GenAI-Dados/
├── src/
│   ├── agent_memory/
│   │   ├── __init__.py
│   │   ├── config.py           # Configurações do sistema
│   │   └── memory_store.py     # Implementação do armazenamento
│   └── utils/
│       ├── __init__.py
│       └── helpers.py          # Funções auxiliares
├── examples/
│   ├── basic_usage.py          # Exemplo básico
│   └── optimized_queries.py    # Exemplo de consultas otimizadas
├── requirements.txt            # Dependências do projeto
├── .env.example               # Exemplo de configuração
├── .gitignore                 # Arquivos ignorados pelo Git
└── README.md                  # Este arquivo
```

## 🔧 API Principal

### MemoryStore

#### Métodos Principais:

- `add_memory(content, metadata, memory_id)`: Adiciona uma nova memória
- `query_memories(query, n_results, filter_metadata)`: Consulta memórias por similaridade
- `get_memory(memory_id)`: Recupera uma memória específica
- `delete_memory(memory_id)`: Remove uma memória
- `get_all_memories()`: Retorna todas as memórias
- `clear_all_memories()`: Limpa todas as memórias
- `count_memories()`: Retorna o número de memórias armazenadas

## 🎯 Casos de Uso

### 1. Atendimento ao Cliente
Armazene e recupere contexto de interações anteriores para fornecer atendimento personalizado.

### 2. Análise de Comportamento
Mantenha histórico de preferências e comportamentos do usuário para análises.

### 3. Recomendações Personalizadas
Use memórias de interações passadas para gerar recomendações mais relevantes.

### 4. Assistente Virtual
Implemente memória de longo prazo para assistentes virtuais mais contextuais.

## 🔒 Segurança

- Nunca commit suas chaves de API no repositório
- Use variáveis de ambiente para dados sensíveis
- O arquivo `.env` está incluído no `.gitignore`
- Mantenha suas dependências atualizadas

## 📈 Performance

O sistema é otimizado para:
- Consultas rápidas usando índices vetoriais
- Armazenamento eficiente com ChromaDB
- Escalabilidade para grandes volumes de memórias
- Baixa latência em buscas semânticas

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:
1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto é parte de uma entrega para o Bradesco - GenAI.

## 📞 Suporte

Para questões e suporte, por favor abra uma issue no repositório.

## 🙏 Agradecimentos

- OpenAI por fornecer embeddings de alta qualidade
- ChromaDB pela excelente solução de banco de dados vetorial
- LangChain por facilitar a integração com LLMs

---

**Desenvolvido para Bradesco - GenAI Dados**
