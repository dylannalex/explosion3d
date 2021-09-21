# 3D Explosion Animation :bomb: :boom:

<p align="center">
  <img width="400" height="400" src="../media/explosion-demo.gif?raw=true">
</p>

:fire: Amazing explosion animation with Pygame.
<br/>

## :bomb: Explosion physics

An `Explosion` instance is made of a set of `Particle` objects. Those particles are fireballs which behavior is determined by a random generated velocity vector.

#### Particle movement:

```
particle.velocity = [vx, vy, vz]
```

`vx` determines how fast a particle moves to the right or to the left.<br/>
`vy` determines how fast a particle moves up or down.<br/>
`vz` determines how fast a particle moves _closer_ to the screen.

The effect of making a particle going off the screen is achieved by increasing the particle radius and brightening its color.

## :bomb: Explosion parameters

```
explosion = Explosion(
    particle_size, total_particles, x_expansion, y_expansion, screen.window
)
```

`particle_size` sets the initial radius of the explosion particles.<br/>
`total_particles` is the number of fireballs in the explosion.<br/>
`x_expansion` sets how much the explosion expands to the right and to the left.<br/>
`y_expansion` sets how high the explosion expands.

## :bomb: Requirements

This project uses the Pygame module. You can install Pygame with:

```
$ pip install pygame
```

## :bomb: Usage

The main file is `start_explosion.py`. You can run the animation with:

```
$ python -m explosion.start_explosion
```

When you execute the project black screen will be displayed. Just click somewhere in the screen and BOOM:boom::boom:
