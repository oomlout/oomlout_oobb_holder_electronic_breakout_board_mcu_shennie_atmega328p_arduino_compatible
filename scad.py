import copy
import opsc
import oobb
import oobb_base
import yaml
import os

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    # save_type variables
    if True:
        filter = ""
        #filter = "test"

        kwargs["save_type"] = "none"
        kwargs["save_type"] = "all"
        
        navigation = False
        #navigation = True    

        kwargs["overwrite"] = True
        
        #kwargs["modes"] = ["3dpr", "laser", "true"]
        kwargs["modes"] = ["3dpr"]
        #kwargs["modes"] = ["laser"]

    # default variables
    if True:
        kwargs["size"] = "oobb"
        kwargs["width"] = 1
        kwargs["height"] = 1
        kwargs["thickness"] = 3
        
    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        part_default = {} 
        part_default["project_name"] = "test" ####### neeeds setting
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["width"] = 3
        p3["height"] = 5
        p3["thickness"] = 9
        p3["extra"] = "electronic_breakout_board_mcu_shennie_atmega328p_arduino_compatible"
        part["kwargs"] = p3
        part["name"] = "base"
        parts.append(part)


        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["width"] = 4
        p3["height"] = 6
        p3["thickness"] = 3
        p3["extra"] = "electronic_breakout_board_mcu_shennie_atmega328p_arduino_compatible_breakout_screw_terminal_3_5_mm_pitch"
        part["kwargs"] = p3
        part["name"] = "base"
        parts.append(part)

        


        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["width"] = 6
        p3["height"] = 6
        p3["thickness"] = 3
        p3["extra"] = "electronic_breakout_board_mcu_shennie_atmega328p_arduino_compatible_breakout_arduino_uno_footprint"
        part["kwargs"] = p3
        part["name"] = "base"
        parts.append(part)


        
    #make the parts
    if True:
        for part in parts:
            name = part.get("name", "default")
            if filter in name:
                print(f"making {part['name']}")
                make_scad_generic(part)            
                print(f"done {part['name']}")
            else:
                print(f"skipping {part['name']}")


    #generate navigation
    if navigation:
        sort = []
        #sort.append("extra")
        sort.append("width")
        sort.append("height")
        sort.append("thickness")
        
        generate_navigation(sort = sort)

def get_base(thing, **kwargs):

    prepare_print = kwargs.get("prepare_print", False)
    width = kwargs.get("width", 1)
    height = kwargs.get("height", 1)
    depth = kwargs.get("thickness", 3)                    
    rot = kwargs.get("rot", [0, 0, 0])
    pos = kwargs.get("pos", [0, 0, 0])
    extra = kwargs.get("extra", "")
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    #add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_plate"    
    p3["depth"] = depth
    #p3["holes"] = True         uncomment to include default holes
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add holes seperate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_holes"
    p3["both_holes"] = True  
    p3["depth"] = depth
    p3["holes"] = "perimeter"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)




    if extra == "electronic_breakout_board_mcu_shennie_atmega328p_arduino_compatible_breakout_screw_terminal_3_5_mm_pitch":
        thing = add_electronic_breakout_board_mcu_shennie_atmega328p_arduino_compatible_breakout_screw_terminal_3_5_mm_pitch(thing, **kwargs)
    elif extra == "electronic_breakout_board_mcu_shennie_atmega328p_arduino_compatible":
        thing = add_electronic_breakout_board_mcu_shennie_atmega328p_arduino_compatible(thing, **kwargs)
    elif extra == "electronic_breakout_board_mcu_shennie_atmega328p_arduino_compatible_breakout_arduino_uno_footprint":
        thing = add_electronic_breakout_board_mcu_shennie_atmega328p_arduino_compatible_breakout_arduino_uno_footprint(thing, **kwargs)



    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def add_electronic_breakout_board_mcu_shennie_atmega328p_arduino_compatible(thing, **kwargs):
        depth = kwargs.get("thickness", 3)
        pos = kwargs.get("pos", [0, 0, 0])
        #add mounting holes
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_screw_countersunk"
        p3["radius_name"] = "m1_5"
        p3["depth"] = 9
        p3["holes"] = "mounting"
        p3["clearance"] = "top"
        p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        shift_screw = 4
        pos1[2] += -shift_screw
        shift_x = 7.62
        shift_y = 20.32
        pos11 = copy.deepcopy(pos1)
        pos11[0] += shift_x
        pos11[1] += shift_y
        pos12 = copy.deepcopy(pos1)
        pos12[0] += shift_x
        pos12[1] += -shift_y
        pos13 = copy.deepcopy(pos1)
        pos13[0] += -shift_x
        pos13[1] += shift_y
        pos14 = copy.deepcopy(pos1)
        pos14[0] += -shift_x
        pos14[1] += -shift_y
        poss = [pos11, pos12, pos13, pos14]
        p3["pos"] = poss
        p3["zz"] = "bottom"
        oobb_base.append_full(thing,**p3)

        #add cutout cubes
        # icsp
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube"
        w = 9
        h = 6
        d = depth
        size = [w,h,d]
        p3["size"] = size
        #p3["m"] = "#"        
        pos1 = copy.deepcopy(pos)
        pos1[0] += 0
        pos1[1] += 19.5
        pos1[2] += 0        
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

        #usb        
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube"
        w = 12.5
        h = 9
        d = depth
        size = [w,h,d]
        p3["size"] = size
        #p3["m"] = "#"        
        pos1 = copy.deepcopy(pos)
        pos1[0] += 0
        pos1[1] += -18.25
        pos1[2] += 0        
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

        #under usb screw clearance
        #   at plug end
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube"
        w = 18
        h = 4.5
        d = shift_screw
        size = [w,h,d]
        p3["size"] = size
        p3["m"] = "#"        
        pos1 = copy.deepcopy(pos)
        pos1[0] += 0
        pos1[1] += -20.25
        pos1[2] += depth - shift_screw
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

        # at icsp end
        p4 = copy.deepcopy(p3)        
        pos1 = copy.deepcopy(pos1)        
        pos1[1] = pos[1] + 20.32
        p4["pos"] = pos1
        oobb_base.append_full(thing,**p4)

        # extra_usb
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube"
        w = 18
        h = 17
        d = depth
        size = [w,h,d]
        p3["size"] = size
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 0
        pos1[1] += -30.25
        pos1[2] += 0
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

        



        # big one
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube"
        ex = 4
        w = 18
        h = 37
        d = depth + ex
        size = [w,h,d]
        p3["size"] = size
        #p3["m"] = "#"
        x_shift = 0
        pos1 = copy.deepcopy(pos)
        pos1[0] += x_shift
        pos1[1] += 0
        pos1[2] += -ex/2      
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

        return thing

def add_electronic_breakout_board_mcu_shennie_atmega328p_arduino_compatible_breakout_arduino_uno_footprint(thing, **kwargs):
        depth = kwargs.get("thickness", 3)
        pos = kwargs.get("pos", [0, 0, 0])
        extra_lift = 3
        #add mounting holes
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_screw_countersunk"
        p3["radius_name"] = "m3"
        p3["depth"] = depth + extra_lift
        p3["holes"] = "mounting"
        #p3["m"] = "#"
        positions = []
        positions.append([-23.96,26.46])
        positions.append([24,24])
        positions.append([-19.5,-26.5])
        positions.append([8.5,-26.5])
        poss = []
        for position in positions:
            pos1 = copy.deepcopy(pos)
            pos1[0] += position[0]
            pos1[1] += position[1]
            pos1[2] += 0
            poss.append(pos1)        
        p3["pos"] = poss
        rot1 =  [0,180,0]
        p3["rot"] = rot1
        p3["zz"] = "top"
        oobb_base.append_full(thing,**p3)

        #add cylinder lifters
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"oobb_cylinder"
        p3["radius"] = 6/2
        p3["depth"] = depth + extra_lift
        p3["holes"] = "mounting"
        #p3["m"] = "#"
        poss = []
        for position in positions:
            pos1 = copy.deepcopy(pos)
            pos1[0] += position[0]
            pos1[1] += position[1]
            pos1[2] += extra_lift
            poss.append(pos1)
        p3["pos"] = poss        
        oobb_base.append_full(thing,**p3)


        return thing

def add_electronic_breakout_board_mcu_shennie_atmega328p_arduino_compatible_breakout_screw_terminal_3_5_mm_pitch(thing, **kwargs):
        depth = kwargs.get("thickness", 3)
        pos = kwargs.get("pos", [0, 0, 0])
        #add mounting holes
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_screw_countersunk"
        p3["radius_name"] = "m3"
        p3["depth"] = depth
        p3["holes"] = "mounting"
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        pos1[2] += 0
        shift_x = 0
        shift_y = 20.637
        pos11 = copy.deepcopy(pos1)
        pos11[0] += shift_x
        pos11[1] += shift_y
        pos12 = copy.deepcopy(pos1)
        pos12[0] += shift_x
        pos12[1] += -shift_y
        poss = [pos11, pos12]
        p3["pos"] = poss
        p3["zz"] = "bottom"
        oobb_base.append_full(thing,**p3)

        #add cutout cubes
        # little one
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube"
        w = 5
        h = 40
        d = depth
        size = [w,h,d]
        p3["size"] = size
        #p3["m"] = "#"
        x_shift = 7.775
        pos1 = copy.deepcopy(pos)
        pos1[0] += x_shift
        pos1[1] += 0
        pos1[2] += 0
        pos2 = copy.deepcopy(pos)
        pos2[0] += -x_shift
        pos2[1] += 0
        pos2[2] += 0
        poss = [pos1, pos2]
        p3["pos"] = poss
        oobb_base.append_full(thing,**p3)

        # big ones
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube"
        w = 9
        h = 54
        d = depth
        size = [w,h,d]
        p3["size"] = size
        #p3["m"] = "#"
        x_shift = 12.775
        pos1 = copy.deepcopy(pos)
        pos1[0] += x_shift
        pos1[1] += 0
        pos1[2] += 0
        pos2 = copy.deepcopy(pos)
        pos2[0] += -x_shift
        pos2[1] += 0
        pos2[2] += 0
        poss = [pos1, pos2]
        p3["pos"] = poss
        oobb_base.append_full(thing,**p3)

        return thing

###### utilities



def make_scad_generic(part):
    
    # fetching variables
    name = part.get("name", "default")
    project_name = part.get("project_name", "default")
    
    kwargs = part.get("kwargs", {})    
    
    modes = kwargs.get("modes", ["3dpr", "laser", "true"])
    save_type = kwargs.get("save_type", "all")
    overwrite = kwargs.get("overwrite", True)

    kwargs["type"] = f"{project_name}_{name}"

    thing = oobb_base.get_default_thing(**kwargs)
    kwargs.pop("size","")

    #get the part from the function get_{name}"
    func = globals()[f"get_{name}"]    
    # test if func exists
    if callable(func):            
        func(thing, **kwargs)        
    else:            
        get_base(thing, **kwargs)   
    
    folder = f"scad_output/{thing['id']}"

    for mode in modes:
        depth = thing.get(
            "depth_mm", thing.get("thickness_mm", 3))
        height = thing.get("height_mm", 100)
        layers = depth / 3
        tilediff = height + 10
        start = 1.5
        if layers != 1:
            start = 1.5 - (layers / 2)*3
        if "bunting" in thing:
            start = 0.5
        

        opsc.opsc_make_object(f'{folder}/{mode}.scad', thing["components"], mode=mode, save_type=save_type, overwrite=overwrite, layers=layers, tilediff=tilediff, start=start)  

    yaml_file = f"{folder}/working.yaml"
    with open(yaml_file, 'w') as file:
        yaml.dump(part, file)

def generate_navigation(folder="scad_output", sort=["width", "height", "thickness"]):
    #crawl though all directories in scad_output and load all the working.yaml files
    parts = {}
    for root, dirs, files in os.walk(folder):
        if 'working.yaml' in files:
            yaml_file = os.path.join(root, 'working.yaml')
            with open(yaml_file, 'r') as file:
                part = yaml.safe_load(file)
                # Process the loaded YAML content as needed
                part["folder"] = root
                part_name = root.replace(f"{folder}","")
                
                #remove all slashes
                part_name = part_name.replace("/","").replace("\\","")
                parts[part_name] = part

                print(f"Loaded {yaml_file}: {part}")

    pass
    for part_id in parts:
        part = parts[part_id]
        kwarg_copy = copy.deepcopy(part["kwargs"])
        folder_navigation = "navigation"
        folder_source = part["folder"]
        folder_extra = ""
        for s in sort:
            ex = kwarg_copy.get(s, "default")
            folder_extra += f"{s}_{ex}/"

        #replace "." with d
        folder_extra = folder_extra.replace(".","d")            
        folder_destination = f"{folder_navigation}/{folder_extra}"
        if not os.path.exists(folder_destination):
            os.makedirs(folder_destination)
        if os.name == 'nt':
            #copy a full directory
            command = f'xcopy "{folder_source}" "{folder_destination}" /E /I'
            print(command)
            os.system(command)
        else:
            os.system(f"cp {folder_source} {folder_destination}")

if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)