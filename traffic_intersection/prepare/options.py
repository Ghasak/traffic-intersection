custom = True
if custom:
    random_simulation = True
    random_seed = 1
    np_random_seed = 1
    save_video = False
    antialias_enabled = False
    speed_up_factor = 3
    dt = 0.2
    duration = 150
    highlight_crossings = False
    create_collision_dictionary = False
    show_boxes = False
    show_tubes = False
    show_honks = True
    show_plates = False
    show_prims = False
    show_traffic_light_walls = False
    new_car_probability = 1
    new_pedestrian_probability = 0.5
    show_axes = False
else:
    random_simulation = True
    seed_random = 1
    seed_np_random = 1
    speed_up_factor = 3
    antialias_enabled = False
    dt = 0.1
    duration = 200
    save_video = False
    highlight_crossings = False
    create_collision_dictionary = False
    show_boxes = False
    show_tubes = False
    show_honks = False
    show_plates = False
    show_prims = False
    show_traffic_light_walls = False
    new_car_probability = 0.1
    new_pedestrian_probability = 0.1
    show_axes = False
