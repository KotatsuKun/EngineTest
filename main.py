import pygame as pg
import moderngl as mgl
import sys
import screeninfo
from model import *
from camera import Camera



class GraphicsEngine:
    def __init__(self, win_size=(1600/2, 900/2)):
        #init pygame modules
        pg.init()
        #window size
        self.WIN_SIZE = win_size
        #set opengl attributes
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        #create opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)    
        #detect and use the existing context
        self.ctx = mgl.create_context()
        #self.ctx.front_face = 'cw'
        #depth
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        #tracking time
        self.clock = pg.time.Clock()
        self.time = 0
        #delta time
        self.delta_time = 0
        #cam
        self.cam = Camera(self)
        #scene
        #self.scene = Cube(self)


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.scene.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        #clear framebuffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        #scene render
        self.scene.render()
        #swap buffers
        pg.display.flip()

    def get_time(self):
        self.fps = self.clock.get_fps()
        self.time = pg.time.get_ticks() * 0.001
        pg.display.set_caption(f'{self.fps: .1f}')
        

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.cam.update()
            self.render()
            self.delta_time = self.clock.tick(60)
            
            
if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()