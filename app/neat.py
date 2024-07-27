import sys
from app import pygame, Car, neat
from app import window, grid, titles, group_roads, menu, buttons, map, clock
from app import draw_fps, is_somebody_alive, draw_score
from config import WHITE, GRID_SIZE, MENU_HEIGHT, MENU_WIDTH, MENU_ELEMENT_HEIGHT, WINDOW_SIZE, LIGHT_GREY, PATH_NEAT_CONFIG


    
starting = False


def eval_genomes(genomes, config):
    global cars, ge, nets, starting

    cars = []
    ge = []
    nets = []

    for genome_id, genome in genomes:
        cars.append(Car((100,45), 14, 4))
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0

    
    dragging_road = None

    running = True

    while running:
        window.fill(LIGHT_GREY)
        if not starting: 
            grid.draw()
            titles.draw()
            
        group_roads.draw(window)
        if not starting: 
            menu.draw()
            buttons.draw()
        
        
        max_fitness = 0
        if starting:
            for i, car in enumerate(cars):
                ge[i].fitness = car.fitness
                max_fitness = max(max_fitness, car.fitness)


                # print(car.fitness)
                if not car.alive:
                    cars.pop(i)
                    ge.pop(i)
                    nets.pop(i)

            for i, car in enumerate(cars):
                # car.img.set_alpha(64)
                # if max_fitness == car.fitness:
                #     car.img.set_alpha(255)


                output = nets[i].activate(car.radars(grid))
                left, right, forward = False, False, False
                if output[0] > 0.5:
                    left = True
                if output[1] > 0.5:
                    right = True
                if output[2] > 0.5:
                    forward = True
                car.update(grid, pygame.key.get_pressed(), map.count_roads, left, right, forward)
                car.draw()

            if not is_somebody_alive(cars) or not cars:
                running = False



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not starting:
                if event.type == pygame.MOUSEBUTTONDOWN:
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
                    elif pygame.Rect(buttons.position[0], buttons.position[1], WINDOW_SIZE[0] - GRID_SIZE, WINDOW_SIZE[1] - MENU_HEIGHT).collidepoint(event.pos):
                        item_index = (event.pos[1] - buttons.position[1]) // MENU_ELEMENT_HEIGHT
                        if 0 <= item_index < len(buttons.items):
                            if buttons.items[item_index] == "Старт":
                                starting = True
                                # grid.blits(group_roads)
                                for road in group_roads:
                                    grid.blit(road.image, (road.rect.x, road.rect.y))
                                
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


        clock.tick()
        draw_fps(clock.get_fps(), window)
        draw_score(max_fitness, window)
        pygame.display.update()
        # pygame.display.flip()


# Setup NEAT Neural Network
def run():
    global pop
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        PATH_NEAT_CONFIG
    )

    # pop = neat.Population(config)
    pop = neat.Checkpointer.restore_checkpoint("neat_checkpoints/one_track_best")

    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    pop.add_reporter(neat.Checkpointer(10, filename_prefix='neat_checkpoints/checkpoint-'))

    return pop.run(eval_genomes, 1000), stats, config



winner, stats, config = run()


from  visualize import visualize
node_names = {-1: 'front', -2: 'front-left', -3: 'left', -4: 'front-right', -5: 'right', -6: 'speed', 0: 'left', 1: 'right', 2: 'forward'}

visualize.draw_net(config, winner, True, node_names=node_names)

visualize.draw_net(config, winner, True, node_names=node_names, prune_unused=True)

visualize.plot_stats(stats, ylog=False, view=True)

visualize.plot_species(stats, view=True)