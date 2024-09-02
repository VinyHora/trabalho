#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity
import pygame

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        if self.name == 'Enemy3':
            self.vertical_speed = 2
            self.direction = 1

    def move(self):
        if self.name == 'Enemy3':
            # Movimentação horizontal
            self.rect.centerx -= ENTITY_SPEED[self.name]
            # Movimentação vertical
            self.rect.y += self.vertical_speed * self.direction

            # Lógica de mudança de direção vertical
            if self.rect.top <= 0:
                self.direction = 1
                self.vertical_speed *= 2  # Dobrar a velocidade ao atingir a borda superior
            elif self.rect.bottom >= pygame.display.get_surface().get_height():
                self.direction = -1
                self.vertical_speed = 2  # Redefinir a velocidade ao atingir a borda inferior
        else:
            # Comportamento padrão para inimigos que não são Enemy3
            self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            # Retorna um tiro diferente para Enemy3 se necessário
            # Caso contrário, retorna o tiro padrão
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

