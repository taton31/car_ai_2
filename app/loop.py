import sys
from app import pygame
from app import window, grid, titles, group_roads, menu, car, buttons, map, clock, cars
from app import draw_fps
from config import WHITE, GRID_SIZE, MENU_HEIGHT, MENU_WIDTH, MENU_ELEMENT_HEIGHT, WINDOW_SIZE, LIGHT_GREY

dragging_road = None

running = True

while running:
    window.fill(LIGHT_GREY)
    grid.draw()
    titles.draw()
    group_roads.draw(window)
    menu.draw()
    buttons.draw()
    
    
    car.update(pygame.key.get_pressed())
    car.draw()

    for c in cars:
        c.update(pygame.key.get_pressed())
        c.draw()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not menu.visible:  # ЛКМ
                for road in group_roads:
                    if road.check_click(event.pos):
                        dragging_road = road
                        dragging_offset = (dragging_road.rect.x - event.pos[0], dragging_road.rect.y - event.pos[1])
                        dragging_road.copy()                        
                        menu.hide()
                        break
            elif event.button == 3:  # ПКМ
                for road in group_roads:
                    if road.check_click(event.pos):
                        menu.show(event.pos, road)
                        break

        elif event.type == pygame.MOUSEBUTTONUP:
            if dragging_road is not None:
                x, y = event.pos[0] + dragging_offset[0], event.pos[1] + dragging_offset[1]
                x = ((x + GRID_SIZE/2) // GRID_SIZE) * GRID_SIZE
                y = ((y + GRID_SIZE/2) // GRID_SIZE) * GRID_SIZE
                dragging_road.move(x, y, save_position=True)
                dragging_road = None
            elif event.button == 1 and menu.visible:  # ЛКМ при видимом меню
                menu_rect = pygame.Rect(menu.position[0], menu.position[1], MENU_WIDTH, MENU_HEIGHT)
                if menu_rect.collidepoint(event.pos):
                    item_index = (event.pos[1] - menu.position[1]) // MENU_ELEMENT_HEIGHT
                    if 0 <= item_index < len(menu.items):
                        menu.handle_action(menu.items[item_index])
                menu.hide()
            elif pygame.Rect(buttons.position[0], buttons.position[1], WINDOW_SIZE[0] - GRID_SIZE, WINDOW_SIZE[1] - MENU_HEIGHT):
                item_index = (event.pos[1] - buttons.position[1]) // MENU_ELEMENT_HEIGHT
                if 0 <= item_index < len(buttons.items):
                    buttons.handle_action(buttons.items[item_index])

        elif event.type == pygame.MOUSEMOTION:
            if dragging_road is not None:
                x = event.pos[0] + dragging_offset[0]
                y = event.pos[1] + dragging_offset[1]
                dragging_road.move(x, y)

            if menu.visible:
                menu_rect = pygame.Rect(menu.position[0], menu.position[1], MENU_WIDTH, MENU_HEIGHT)
                if menu_rect.collidepoint(event.pos):
                    menu.hovered_item = (event.pos[1] - menu.position[1]) // MENU_ELEMENT_HEIGHT
                    if not (0 <= menu.hovered_item < len(menu.items)):
                        menu.hovered_item = None
                else:
                    menu.hovered_item = None

    for c in cars:
        c.check_collision(group_roads)
    car.check_collision(group_roads)

    # for i in group_roads:
    #     a = pygame.mask.from_surface(i.image)
    #     window.blit(a.to_surface(), (i.rect.x, i.rect.y))

    clock.tick(60)
    draw_fps(clock.get_fps(), window)
    pygame.display.flip()

pygame.quit()
sys.exit()
