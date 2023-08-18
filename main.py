from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI

load_dotenv()

template_string = """\
Sua tarefa é elaborar um briefing incorporando informações-chave obtidas a partir de uma entrevista com o cliente. Seu briefing deve incluir sugestões relevantes que estejam alinhadas com as respostas fornecidas pelo cliente que estão separadas por três crases.

Não insira nenhum texto adicional além do briefing.

No final formate o conteúdo gerado em um arquivo markdown.

```
Categoria do design: {categoria}
Estética: {estetica}
Cores: {cores}
Informações sobre o público-alvo: {publico_alvo}
Mais informações: {descricao}
```

Observações adicionais:
- Certifique-se de que o briefing de design seja claro, conciso e esteja alinhado com os requisitos do cliente.
- Procure sempre escrever tópicos, ao invés de textos corridos com mais de 2 linhas.
- Sinta-se a vontade de incluir sugestões de conteúdo e de design que o designer pode colocar na imagem.
"""

chat = ChatOpenAI(temperature=0.7)

prompt_template = ChatPromptTemplate.from_template(template_string)

prompt_categoria = "Design de site"
prompt_descricao = "Site de uma empresa que vende roupas femininas"
prompt_estetica = "Moderna"
prompt_cores = "Branco, roxo, vinho e vermelho"
prompt_publico_alvo = "20 a 30 anos"

prompt = prompt_template.format_messages(categoria = prompt_categoria,
                                         descricao = prompt_descricao,
                                         estetica = prompt_estetica,
                                         cores = prompt_cores,
                                         publico_alvo = prompt_publico_alvo)

response = chat(prompt)
with open('response.md', 'w', encoding='utf-8') as file:
    print(response.content, file=file)