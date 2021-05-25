from typing import List

from matplotlib import pyplot as plt
from matplotlib import animation


class Particle:
    def __init__(self, x, y, ang_vel):
        self.x = x
        self.y = y
        self.ang_vel = ang_vel


class ParticleSimulator:
    def __init__(self, particles: List[Particle]):
        self.particles = particles

    def evolve(self, dt):
        time_step = 0.00001
        n_steps = int(dt / time_step)
        for i in range(n_steps):
            for p in self.particles:
                # 1.) Calculate the direction
                norm = (p.x ** 2 + p.y ** 2) ** 0.5
                v_x = -p.y / norm
                v_y = p.x / norm

                # 2.) Calculate the displacement
                d_x = time_step * p.ang_vel * v_x
                d_y = time_step * p.ang_vel * v_y

                p.x += d_x
                p.y += d_y
                # 3.) Repeat for all of the steps


def visualize(simulator: ParticleSimulator):
    x = [p.x for p in simulator.particles]
    y = [p.y for p in simulator.particles]

    fig = plt.figure()

    plt.clf()

    ax = plt.subplot(111, aspect="equal")
    line, = ax.plot(x, y, "ro")
    # Axis Limits
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    # Runs when the animation starts
    def init():
        line.set_data([], [])
        return line,

    def animate(i):
        simulator.evolve(0.01)
        x = [p.x for p in simulator.particles]
        y = [p.y for p in simulator.particles]

        line.set_data(x, y)

        return line,

    anim = animation.FuncAnimation(
        fig,
        animate,
        init_func=init,
        blit=True,
        interval=10
    )

    plt.show()


def test_visualize():
    particles = [
        Particle(0.3, 0.5, 1),
        Particle(0.0, -0.5, -1),
        Particle(-0.1, -0.4, 3)
    ]

    simulator = ParticleSimulator(particles)

    visualize(simulator)


if __name__ == "__main__":
    test_visualize()
