from pygame import font, Color
font = font.SysFont("Arial" , 20 , bold = True)

def draw_fps(clock, window):
    fps = str(int((clock)))
    fps_t = font.render(fps , 1, Color("RED"))
    window.blit(fps_t,(10,10))