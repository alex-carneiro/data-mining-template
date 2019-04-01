# data-mining-template
Template para criação de uma API web com base em um modelo de machine learning.

Use o arquivo _attributes.txt_ para listar os atributos de entrada para seu modelo de machine learning.
Este arquivo pode ser editado com o bloco de notas, wordpad, gedit ou qualquer outro editor de texto.

Use o arquivo _build_model.py_ para testar e salvar seu modelo de machine learning.
Comente uma das duas últimas linhas para escolher se deseja testar ou salvar seu modelo de machine learning.
Para executar o arquivo use o comando: **python build_model.py**

Use o arquivo _server.py_ para criar a API com base em seu modelo de machine learning acessível pela Web.
Acesse a API pela porta 5000 do localhost: http://localhost:5000
Para usar sua API, passe os dados referentes aos atributos na URL: http://localhost:5000/api?sepal_length=1&sepal_width=1&petal_length=1&petal_width=1
Para executar o arquivo use o comando: **python server.py**
