### Jogo da Cobra em Python com Pygame

Este projeto implementa o clássico jogo da cobra usando Python e Pygame. 

A cobra é representada por segmentos que se movem pela tela, tentando capturar o "Snack" enquanto evita colidir consigo mesma. 

Abaixo estão detalhes importantes sobre o código:

#### Funcionalidades principais:

1. **Classe Cube (Cubo):**
   - Representa cada segmento da cobra.
   - Inicializa com posição, direção e cor.
   - Pode se mover e desenhar seu próprio visual, incluindo olhos opcionais.

2. **Classe Snake (Cobra):**
   - Representa a própria cobra, composta de um segmento de cabeça e uma lista de segmentos do corpo.
   - Gerencia movimento, captura de teclas de direção, crescimento ao capturar lanches e detecção de colisões.

3. **Funções Auxiliares:**
   - **draw_grid:** Desenha uma grade na janela de jogo.
   - **redraw_window:** Atualiza a janela do jogo a cada frame.
   - **random_snack:** Gera um lanche em uma posição aleatória na grade.
   - **message_box:** Exibe uma mensagem quando o jogador perde o jogo.

4. **Função Principal (main):**
   - Inicializa o Pygame e configura a janela do jogo.
   - Cria a cobra e o primeiro lanche.
   - Gerencia o loop principal do jogo, atualizando a tela, movendo a cobra e verificando eventos como captura de lanche ou colisão.

#### Executando o Jogo:

Para executar o jogo, deve-se ter Python instalado, junto com as bibliotecas necessárias, como: Pygame, tkinter. Execute o arquivo e controle a cobra usando as setas do teclado. 

Sinta-se livre para 'forkar' o game e atualiza-lo como quiser 😊

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Snake Game in Python with Pygame

This project implements the classic snake game using Python and Pygame. 

The snake is represented by segments that move across the screen, attempting to capture "snacks" while avoiding collisions with itself. 

Below are key details about the code:

#### Key Features:

1. **Cube Class:**
   - Represents each segment of the snake.
   - Initializes with position, direction, and color.
   - Can move and draw its own appearance, optionally including eyes.

2. **Snake Class:**
   - Represents the snake itself, composed of a head segment and a list of body segments.
   - Manages movement, captures directional input, grows upon capturing snacks, and detects collisions.

3. **Auxiliary Functions:**
   - **draw_grid:** Draws a grid on the game window.
   - **redraw_window:** Updates the game window every frame.
   - **random_snack:** Generates a snack at a random position on the grid.
   - **message_box:** Displays a message when the player loses the game.

4. **Main Function (main):**
   - Initializes Pygame and sets up the game window.
   - Creates the snake and the initial snack.
   - Manages the main game loop, updating the screen, moving the snake, and handling events such as snack capture or collision.

#### Running the Game:

To run the game, ensure Python is installed along with the required modules (Pygame, tkinter). Execute the file and control the snake using the arrow keys.

Feel free to fork and modifid the game as you wish 😊
