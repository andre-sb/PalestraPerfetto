# Demonstrações — Otimizando Pipelines com Tracing de Alta Performance

Este repositório contém exemplos e demonstrações usados na palestra "Otimizando Pipelines com Tracing de Alta Performance" apresentada na Python Brasil 2025.

Página da palestra: https://talks.python.org.br/pythonbrasil-2025/talk/YBYFSN/

Conteúdo
- Scripts de demonstração (ex.: `1-basico.py`, `2-funcoes.py`, `3-pandas.py`) e seus resultados.
- buld.trace.gz: arquivo de trace de uma build do Android Open Surce Project (AOSP) https://source.android.com/

Como usar

1) Crie um ambiente virtual (recomendado) e ative-o:

```bash
python3 -m venv venv
source venv/bin/activate
```

2) Instale os requisitos:

```bash
pip install -r requirements.txt
```

Observações
- O arquivo `requirements.txt` já lista as dependências usadas nas demos (por exemplo, `viztracer`).
- Recomenda-se executar as demos dentro do ambiente virtual criado para evitar poluir o Python do sistema.
