# PLN - Projeto 1

A descrição completa do projeto encontra-se no Relatório. Este documento trata
apenas da execução do projeto.

## Equipe

* Alexandre Cisneiros (acaf)
* Pedro Diniz (phrd)
* Rubens Lopes (rlfs)

## Como executar

Para executar, é preciso instalar as bilbiotecas das quais o projeto depende e
baixar a base Reuters para o diretório em que o projeto irá procurá-las. Para
tal, usamos a biblioteca `nltk`, que vai coordenar a instalação e manuseio destes
arquivos.

### Configurando o ambiente

Para configurar o ambiente, recomenda-se o uso de `virtualenv`, evitando misturar
as dependências deste projeto com os pacotes de Python do sistema do usuário.
Caso não use, as dependências serão instaladas globalmente no sistema.

Após instalar o `virtualenv`, criar um ambiente virtual e ativá-lo (ou após 
ignorar tudo isso e desejar instalar globalmente), instale as dependências com:

```
$ pip install -r requirements.txt
```

A seguir, faça o download da base Reuters através da biblioteca `nltk`.

```
$ python -m nltk.downloader reuters
```

### Executando o projeto

Para executar o projeto, rode uma das linhas abaixo:

```
$ ./run
$ ./run <THRESHOLD>
```

O valor de `<THRESHOLD>` (entre `0` e `1`) define o quão estrito o classificador será
ao analisar a pertinência de um documento à classe, conforme explica o Relatório.
Se você não especificar um valor, será usado o valor padrão (`0.93`).

## Exemplo de execução

Abaixo um exemplo da execução esperada ao usar o threshold `0.85`.

```
$ ./run 0.85
[TRAINING] Started training with 6489 documents.
 - Training document #0
 - Training document #500
 - Training document #1000
 - Training document #1500
 - Training document #2000
 - Training document #2500
 - Training document #3000
 - Training document #3500
 - Training document #4000
 - Training document #4500
 - Training document #5000
 - Training document #5500
 - Training document #6000
[TRAINING] Ended training.

[TESTING] Started testing with 2545 documents.
 - Testing document #0
 - Testing document #500
 - Testing document #1000
 - Testing document #1500
 - Testing document #2000
 - Testing document #2500
[TESTING] Ended testing.

[RESULTS] The results are in!
 - Precision: 0.810472
 - Recall: 0.844877
 - Accuracy: 0.957164
 - F1: 0.827317

[INFO] For this execution:
 - User defined threshold: 0.850000
 - Training time: 20.37 s
 - Testing time: 56.67 s
 - Total time: 77.03 s

[THANK YOU] The authors thank you for your time!
 - Alexandre Cisneiros (acaf)
 - Pedro Diniz (phrd)
 - Rubens Lopes (rlfs)
```