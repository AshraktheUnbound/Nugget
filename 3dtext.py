import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# Define the colors of the cube's faces
colors = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1))

# Define the vertices of the cube
vertices = ((-1, -1, -1), (-1, -1, 1), (-1, 1, 1), (-1, 1, -1), (1, -1, -1), (1, -1, 1), (1, 1, 1), (1, 1, -1))

# Define the faces of the cube
faces = ((0, 1, 2, 3), (3, 2, 6, 7), (7, 6, 5, 4), (4, 5, 1, 0), (1, 5, 6, 2), (4, 0, 3, 7))

# Define the angle of rotation
angle = 0


# Define the function to draw the cube
def draw_cube():
    global angle

    # Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Reset the transformation matrix
    glLoadIdentity()

    # Translate the cube away from the camera
    glTranslatef(0, 0, -5)

    # Rotate the cube
    glRotatef(angle, 1, 1, 1)

    # Draw the cube
    glBegin(GL_QUADS)
    for i, face in enumerate(faces):
        #glColor3fv(colors[i])
        glColor3f(1.0, 0.0, 0.0)
        for vertexd a  in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    # Increase the angle of rotation
    angle += 1

    # Swap the buffers
    pygame.display.flip()


# Initialize Pygame and PyOpenGL
pygame.init()
pygame.display.set_mode((640, 480), DOUBLEBUF | OPENGL)

# Set up the projection matrix
gluPerspective(45, 640 / 480, 0.1, 50.0)
glTranslatef(0, 0, -5)

# Enable depth testing
#glEnable(GL_DEPTH_TEST)

# Set up the main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    print('boom')
    draw_cube()
