
 # Turing-Post
	Desenvolvido por: Arthur Henrique Sousa Cruz; Pedro Silveira Lopes; João Pedro Teodoro Silva
   

Programa que converte uma máquina de Turing para uma máquina de Post
A entrada deve ser um arquivo texto com a descriçao da MT seguindo o exemplo do arquivo "exemplo-de-entrada.txt", encontrado no diretório “arquivos”.

Para executar o programa (via terminal) é necessário estar no diretório codigo deste projeto. O comando para a execução é o seguinte:
	python3 Main.py <arquivo-de-entrada> <arquivo-de-saida>.

Onde <arquivo-de-entrada> é o nome do arquivo que contém a Máquina de Turing e <arquivo-de-saida> é o nome do arquivo onde será armazenada a máquina de Post no formato exemplificado no arquivo de texto “exemplo-de-saida.txt”, encontrado no diretório “arquivos”.

O arquivo de entrada deve estar no diretório do projeto, em “arquivos/entradas/”, enquanto o de saída será gerado (sobrescrito caso já exista) também no diretório do projeto, porém agora, em “arquivos/saidas/”.

# Sobre o algoritmo
O algoritmo segue uma ideia recursiva. O caso base é quando todos os estados já foram completados. A função recebe como parâmetro um estado e, quando este é nulo, significa que todos já foram percorridos. 
No caso geral, primeiramente cria-se uma leitura que equivale ao estado. Após tal, busca-se uma transição do estado atual. Feito isso, caso seja encontrada, temos alguns casos:
	O primeiro e mais simples é caso a transição seja um loop. Nesse caso o algoritmo transforma essa transição em um conjunto de leitura, escritas e desvios da máquina de POST e chama recursivamente a função no mesmo estado.
	O segundo caso é: se a transição tiver como destino um estado que já tem um equivalente na máquina de POST, transforma a transição.
	O terceiro é: Se o estado destino não tem um equivalente para POST, então chama a função recursivamente no estado de destino.
	Por fim, se não ocorreu nenhum desses casos, procura-se um estado que ainda tem transições que não foram transformadas.
# Movimentos
Sem dúvidas o movimento é uma peça chave nessa 	transformação e, com toda a certeza, o movimento para a esquerda é o maior desafio da mesma, afinal, o movimento para a direita é praticamente natural, já que a fita se move para a direita. 
Contudo, para gerar o movimento à esquerda é necessário percorrer a fita toda e parar um símbolo antes do atual. Para isso foi inserido em POST um marcador, para identificar que o símbolo anterior ao marcador é o símbolo que será lido após percorrer toda a fita.
Isso significa que quando o marcador for lido o símbolo anterior ao mesmo também já o terá sido. Com isso, o final do movimento à esquerda já se mescla com o inicio da leitura do estado ao qual a transição leva.
Para tratar esses problemas crimaos uma estrutura semalhante à imagem presente no ANEXO_1.jpg para todas as transições para a esquerda.
Vemos neste anexo que, após identificado o movimento a esquerda insere-se o símbolo '&' (identificador utilizado como exemplo) e, após isto, escreve-se um símbolo qualquer que pertence ao alfabeto (este seria o símbolo que deveria ser escrito pela transição). Após isso cria-se uma leitura para cada símbolo presente no alfabeto e, para cada desvio gerado nessa leitura segue-se os seguintes passos:
	1 - Cria-se, para cada símbolo do alfabeto, uma leitura e, em 		seguida, uma escrita do símbolo símbolo lido anteriormentea esses 		passos.
	2 - O destino dessa leitura será a leitura (crianda anteriormente a 		esses passos) cujo símbolo é o mesmo que o do desvio que chegou a 		essa escrita.
	3 - Se o símbolo lido for o símbolo de marcação ('&'), o símbolo 		lido antes deste é o símbolo que seria lido no próximo estado, ou 		seja, é o símbolo que estaria a esquerda após a execução da 		transição.
Caso o símbolo esteja presente em uma transição do estado que seria destino, a parte de leitura dessa transição já foi realizada. Caso contrário significa que a máquina deve parar.
# Parada
Após todas as transições serem criadas, o algoritmo define quais desvios irão para o "estado" aceita quando a máquina parar. Isso é feito com a utilização dos estados finais da máquina de Turing. Se for estado final, quando POST parar, a máquina irá para "aceita", caso contrário, "rejeita".
