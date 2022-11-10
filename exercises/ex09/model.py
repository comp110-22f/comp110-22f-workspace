"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730474292" 


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other_point: Point) -> float:
        """Determines the distance between two cells."""
        distance: float = (sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2))
        return distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Runs after each tick to determine recovery of infected cells and to keep track how long a cell has been infected."""
        self.location = self.location.add(self.direction)

        if self.is_infected():
            self.sickness += 1
        if self.sickness >= constants.RECOVERY_PERIOD:
            self.sickness = constants.IMMUNE

    def contract_disease(self) -> None:
        """Changes the cell's sickness status to infected."""
        self.sickness = constants.INFECTED

    def immunize(self) -> None:
        """Makes the cell immune."""
        self.sickness = constants.IMMUNE

    def is_vulnerable(self) -> bool:
        """Reports if a cell is vulnerable to being infected."""
        if self.sickness == constants.VULNERABLE:
            return True
        return False
    
    def is_infected(self) -> bool:
        """Reports if a cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        return False

    def is_immune(self) -> bool:
        """Reports if a cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        return False

    def color(self) -> str: 
        """Determines the color of the cell at any given time in the simulation."""
        if self.is_vulnerable(): 
            return "gray"
        if self.is_infected():
            return "pink"
        if self.is_immune():
            return "medium aquamarine"

    def contact_with(self, other_cell: Cell) -> None:
        """Determines if a cell should become infected based on the status of the two cells in contact."""
        if self.is_vulnerable() and other_cell.is_infected():
            self.contract_disease()
        if other_cell.is_vulnerable() and self.is_infected():
            other_cell.contract_disease()

    
class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0
    infected: int = constants.INFECTEDS

    def __init__(self, cells: int, speed: float, infecteds: int, immunes: int = 0):
        """Initialize the cells with random locations and directions."""
        if infecteds >= cells or immunes > cells or infecteds <= 0 or immunes < 0: 
            raise ValueError(f"The original number of infected cells cannot be 0 and the number of infected and immune cannot exceed the population size, {cells}.")
        if infecteds + immunes > cells:
            raise ValueError(f"The combined number of infected aned immune cells cannot exceed the population size, {cells}.")
        
        self.population = []
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)

        for i in range(infecteds):
            self.population[i].sickness = constants.INFECTED
        
        for i in range(immunes):
            self.population[infecteds + i].sickness = constants.IMMUNE

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0

        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0

        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0

        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Checks the distance between each of the two cells in the population."""
        population_size: int = len(self.population)
        i: int = 0
        while i < population_size:
            for cell in range(i + 1, population_size):
                if self.population[i].location.distance(self.population[cell].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[cell])
            i += 1

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for each in self.population:
            if each.is_infected():
                return False
        return True