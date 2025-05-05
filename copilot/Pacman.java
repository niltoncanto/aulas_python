package copilot;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.util.Random;
import java.awt.event.KeyEvent;

public class Pacman extends JPanel {
    private static final int SCREEN_WIDTH = 800;
    private static final int SCREEN_HEIGHT = 600;
    private static final int PACMAN_SIZE = 20;
    private static final int GHOST_SIZE = 20;
    private static final int PACMAN_SPEED = 5;
    private static final int GHOST_SPEED = 3;

    private int pacmanX = SCREEN_WIDTH / 2;
    private int pacmanY = SCREEN_HEIGHT / 2;
    private int ghostX;
    private int ghostY;

    private boolean running = true;

    private String[] maze = {
        "############################",
        "#............##............#",
        "#.####.#####.##.#####.####.#",
        "#.####.#####.##.#####.####.#",
        "#.####.#####.##.#####.####.#",
        "#..........................#",
        "#.####.##.########.##.####.#",
        "#.####.##.########.##.####.#",
        "#......##....##....##......#",
        "######.##### ## #####.######",
        "######.##### ## #####.######",
        "######.##          ##.######",
        "######.## ###--### ##.######",
        "######.## #      # ##.######",
        "######.## #      # ##.######",
        "######.## ######## ##.######",
        "######.##          ##.######",
        "######.## ######## ##.######",
        "#............##............#",
        "#.####.#####.##.#####.####.#",
        "#.####.#####.##.#####.####.#",
        "#.####.##..........##.####.#",
        "#.####.##.########.##.####.#",
        "#......##....##....##......#",
        "######.#####.##.#####.######",
        "######.#####.##.#####.######",
        "#............##............#",
        "############################"
    };

    public Pacman() {
        Random rand = new Random();
        ghostX = rand.nextInt(SCREEN_WIDTH - GHOST_SIZE);
        ghostY = rand.nextInt(SCREEN_HEIGHT - GHOST_SIZE);

        addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                if (running) {
                    switch (e.getKeyCode()) {
                        case KeyEvent.VK_LEFT:
                            if (!checkCollision(pacmanX - PACMAN_SPEED, pacmanY)) {
                                pacmanX -= PACMAN_SPEED;
                            }
                            break;
                        case KeyEvent.VK_RIGHT:
                            if (!checkCollision(pacmanX + PACMAN_SPEED, pacmanY)) {
                                pacmanX += PACMAN_SPEED;
                            }
                            break;
                        case KeyEvent.VK_UP:
                            if (!checkCollision(pacmanX, pacmanY - PACMAN_SPEED)) {
                                pacmanY -= PACMAN_SPEED;
                            }
                            break;
                        case KeyEvent.VK_DOWN:
                            if (!checkCollision(pacmanX, pacmanY + PACMAN_SPEED)) {
                                pacmanY += PACMAN_SPEED;
                            }
                            break;
                    }
                }
            }
        });
        setFocusable(true);
    }

    private boolean checkCollision(int x, int y) {
        int xIndex = x / PACMAN_SIZE;
        int yIndex = y / PACMAN_SIZE;
        return maze[yIndex].charAt(xIndex) == '#';
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.BLACK);
        g.fillRect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT);

        drawMaze(g);

        g.setColor(Color.YELLOW);
        g.fillRect(pacmanX, pacmanY, PACMAN_SIZE, PACMAN_SIZE);

        g.setColor(Color.RED);
        g.fillRect(ghostX, ghostY, GHOST_SIZE, GHOST_SIZE);

        moveGhost();

        if (Math.abs(pacmanX - ghostX) < PACMAN_SIZE && Math.abs(pacmanY - ghostY) < PACMAN_SIZE) {
            running = false;
        }

        if (running) {
            repaint();
        }
    }

    private void drawMaze(Graphics g) {
        g.setColor(Color.WHITE);
        for (int y = 0; y < maze.length; y++) {
            for (int x = 0; x < maze[y].length(); x++) {
                if (maze[y].charAt(x) == '#') {
                    g.fillRect(x * PACMAN_SIZE, y * PACMAN_SIZE, PACMAN_SIZE, PACMAN_SIZE);
                }
            }
        }
    }

    private void moveGhost() {
        if (ghostX < pacmanX && !checkCollision(ghostX + GHOST_SPEED, ghostY)) {
            ghostX += GHOST_SPEED;
        }
        if (ghostX > pacmanX && !checkCollision(ghostX - GHOST_SPEED, ghostY)) {
            ghostX -= GHOST_SPEED;
        }
        if (ghostY < pacmanY && !checkCollision(ghostX, ghostY + GHOST_SPEED)) {
            ghostY += GHOST_SPEED;
        }
        if (ghostY > pacmanY && !checkCollision(ghostX, ghostY - GHOST_SPEED)) {
            ghostY -= GHOST_SPEED;
        }
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Pac-man");
        Pacman game = new Pacman();
        frame.add(game);
        frame.setSize(SCREEN_WIDTH, SCREEN_HEIGHT);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}