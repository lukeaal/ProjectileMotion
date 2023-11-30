import sys
import matplotlib.pyplot as plt
import numpy as np
import os


"""
modify this to change how the lines momve over time
"""


def projectile_motion_frames(x0, y0, v0, theta_deg, g, num_frames):
    theta_rad = np.radians(theta_deg)
    t_max = 2 * v0 * np.sin(theta_rad) / g
    t_values = np.linspace(0, t_max, num_frames)

    x_values = x0 + v0 * np.cos(theta_rad) * t_values
    y_values = y0 + v0 * np.sin(theta_rad) * t_values - 0.5 * g * t_values**2

    return x_values, y_values


"""
modify this to change how to frames look visually
"""


def save_frames_as_images(x_values, y_values, output_directory='frames'):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for i in range(len(x_values)):
        plt.figure()
        plt.plot(x_values[:i+1], y_values[:i+1], label='Projectile Motion')
        plt.title('Projectile Motion Frame {}'.format(i))
        plt.xlabel('X Position')
        plt.ylabel('Y Position')
        plt.legend()
        plt.xlim(min(x_values) - 5, max(x_values) + 5)
        plt.ylim(0, max(y_values) + 5)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.savefig(os.path.join(output_directory,
                    'frame_{:03d}.jpeg'.format(i)))
        plt.close()


"""
will need to change args of this if you create drag as well
"""


def main_one(x0=0, y0=0, v0=20, theta_deg=45, num_frames=150, g=9.8):

    # Generate projectile motion frames
    x_values, y_values = projectile_motion_frames(
        x0, y0, v0, theta_deg, g, num_frames)

    # Save frames as individual JPEG images
    save_frames_as_images(x_values, y_values, output_directory='static/images')
    return "I have completed"


# your_script.py


def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python ball_moving.py <velocity> <angle>")
        sys.exit(1)

    # Retrieve the arguments
    velocity = float(sys.argv[1])
    angle = float(sys.argv[2])

    # Now you can use 'velocity' and 'angle' in your script
    main_one(v0=velocity, theta_deg=angle)
    print(f"Velocity: {velocity}, Angle: {angle}")


if __name__ == "__main__":
    main()
