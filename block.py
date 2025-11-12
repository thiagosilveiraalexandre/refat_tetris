import pygame
from colors import Colors
from position import Position


class Block:
    def __init__(self, id: int) -> None:
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    def move(self, rows: int, columns: int) -> None:
        self.row_offset += rows
        self.column_offset += columns

    def get_cell_positions(self) -> list[Position]:
        """Retorna lista de posições atualizadas com os offsets atuais"""
        tiles = self.cells[self.rotation_state]
        return [
            Position(
                tile.row + self.row_offset,
                tile.column + self.column_offset
            )
            for tile in tiles
        ]

    def rotate(self) -> None:
        """Avança para o próximo estado de rotação cíclicamente"""
        self.rotation_state = (self.rotation_state + 1) % len(self.cells)

    def undo_rotation(self) -> None:
        """Retorna ao estado anterior de rotação cíclicamente"""
        self.rotation_state = (self.rotation_state - 1) % len(self.cells)

    def draw(self, screen: pygame.Surface, offset_x: int, offset_y: int) -> None:
        """Renderiza o bloco na tela usando as posições calculadas"""
        for tile in self.get_cell_positions():
            rect = pygame.Rect(
                offset_x + tile.column * self.cell_size,
                offset_y + tile.row * self.cell_size,
                self.cell_size - 1,
                self.cell_size - 1
            )
            pygame.draw.rect(screen, self.colors[self.id], rect)