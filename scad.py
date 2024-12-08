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
        #filter = "with_clamp"

        kwargs["save_type"] = "none"
        #kwargs["save_type"] = "all"
        
        navigation = False
        #navigation = True    

        kwargs["overwrite"] = True
        
        kwargs["modes"] = ["3dpr", "laser", "true"]
        #kwargs["modes"] = ["3dpr"]
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
        p3["extra"] = "shennie_atmega328p_arduino_compatible"
        part["kwargs"] = p3
        part["name"] = "base"
        parts.append(part)


        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["width"] = 4
        p3["height"] = 6
        p3["thickness"] = 3
        p3["extra"] = "shennie_atmega328p_arduino_compatible_breakout_screw_terminal_3_5_mm_pitch"
        part["kwargs"] = p3
        part["name"] = "base"
        parts.append(part)

        


        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["width"] = 6
        p3["height"] = 6
        p3["thickness"] = 3
        p3["extra"] = "shennie_atmega328p_arduino_compatible_breakout_arduino_uno_short_footprint"
        part["kwargs"] = p3
        part["name"] = "base"
        parts.append(part)

        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["width"] = 4
        p3["height"] = 6
        p3["thickness"] = 3
        p3["extra"] = "shennie_atmega328p_arduino_compatible_breakout_arduino_uno_short_footprint_with_clamp"
        part["kwargs"] = p3
        part["name"] = "base"
        parts.append(part)


        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["width"] = 6
        p3["height"] = 7
        p3["thickness"] = 3
        p3["extra"] = "shennie_atmega328p_arduino_compatible_breakout_cnc_shield"
        part["kwargs"] = p3
        part["name"] = "base"
        parts.append(part)
    

        
    #make the parts
    if True:
        for part in parts:
            name = part.get("name", "default")
            extra = part.get("kwargs", {}).get("extra", "")
            if filter in name or filter in extra:
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
    if width == 4 and "with_clamp" in extra:
        p3["holes"] = ["left", "right"]
    else:
        p3["holes"] = "perimeter"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)




    if extra == "shennie_atmega328p_arduino_compatible_breakout_screw_terminal_3_5_mm_pitch":
        thing = add_shennie_atmega328p_arduino_compatible_breakout_screw_terminal_3_5_mm_pitch(thing, **kwargs)
    elif extra == "shennie_atmega328p_arduino_compatible":
        thing = add_shennie_atmega328p_arduino_compatible(thing, **kwargs)
    elif extra == "shennie_atmega328p_arduino_compatible_breakout_arduino_uno_short_footprint":
        thing = add_shennie_atmega328p_arduino_compatible_breakout_arduino_uno_short_footprint(thing, **kwargs)
    elif extra == "shennie_atmega328p_arduino_compatible_breakout_arduino_uno_short_footprint_with_clamp":
        thing = add_shennie_atmega328p_arduino_compatible_breakout_arduino_uno_short_footprint_with_clamp(thing, **kwargs)
    elif extra == "shennie_atmega328p_arduino_compatible_breakout_cnc_shield":
        thing = add_shennie_atmega328p_arduino_compatible_breakout_cnc_shield(thing, **kwargs)



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

def add_shennie_atmega328p_arduino_compatible(thing, **kwargs):
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

def add_shennie_atmega328p_arduino_compatible_breakout_arduino_uno_short_footprint(thing, **kwargs):
        depth = kwargs.get("thickness", 3)
        pos = kwargs.get("pos", [0, 0, 0])
        extra_lift = 3
        #add mounting holes
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "negative"
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

        #add hoels as negative negative
        dep = depth + 3#+ 29 #from with clamp section
        p4 = copy.deepcopy(p3)
        p4["type"] = "negative_negative"
        p4["shape"] = f"oobb_hole"
        p4["radius_name"] = "m3"
        p4["depth"] = dep
        p4["m"] = "#"
        poss2 = copy.deepcopy(poss)
        for pos1 in poss2:
            pos1[2] += dep
        p4["pos"] = poss2
        oobb_base.append_full(thing,**p4)





        #add cylinder lifters
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "positive_positive"
        p3["shape"] = f"oobb_cylinder"
        p3["radius"] = 6/2
        p3["depth"] = extra_lift
        #p3["m"] = "#"
        
        poss = []
        for position in positions:
            pos1 = copy.deepcopy(pos)
            pos1[0] += position[0]
            pos1[1] += position[1]
            pos1[2] += extra_lift + depth/2
            poss.append(pos1)
        p3["pos"] = poss        
        oobb_base.append_full(thing,**p3)


        return thing

def add_shennie_atmega328p_arduino_compatible_breakout_arduino_uno_short_footprint_with_clamp(thing, **kwargs):
        depth = kwargs.get("thickness", 3)
        pos = kwargs.get("pos", [0, 0, 0])
        height = kwargs.get("height", 3)
        width = kwargs.get("width", 3)
        extra_lift = 3
        rot = kwargs.get("rot", [0, 0, 0])
        thing = add_shennie_atmega328p_arduino_compatible_breakout_arduino_uno_short_footprint(thing, **kwargs)

        depth_lift = 20
        #add top clamp plate
        depth_clamp = 9
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["height"] = 1.5
        p3["shape"] = f"oobb_plate"
        p3["depth"] = depth_clamp
        #p3["holes"] = True
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        pos1[1] += (height/2) * 15 - 22.5/2
        pos1[2] += depth + depth_lift
        pos2 = copy.deepcopy(pos)
        pos2[1] += -(height/2) * 15 + 22.5/2
        pos2[2] += depth + depth_lift
        poss = [pos1, pos2]
        p3["pos"] = poss
        oobb_base.append_full(thing,**p3)

        #cube cutout for pcb
        depth_pcb_cutout = 3 + 1.2
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_cube"
        ex = 2
        w = 53 + ex
        h = 58 + ex
        d = depth_pcb_cutout
        size = [w,h,d]
        p3["size"] = size
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        pos1[1] += 0
        pos1[2] += depth + depth_lift 
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

        #add cutouts for clearance
        cubes = []

        #power socket
        w = 9; h = 14; d = depth_clamp
        x_shift = -15.5; y_shift = 22; z_shift = 0
        cubes.append([[x_shift, y_shift, z_shift], [w,h,d]])

        #reset button 3.6,9.0 at -23.7,15.5
        w = 3.6; h = 9; d = depth_clamp
        x_shift = -23.7; y_shift = 15.5; z_shift = 0
        cubes.append([[x_shift, y_shift, z_shift], [w,h,d]])

        #left hand strip 2.54,38.1 at -8.72,7.41
        w = 2.54; h = 38.1; d = depth_clamp
        x_shift = -8.72; y_shift = 7.41; z_shift = 0
        cubes.append([[x_shift, y_shift, z_shift], [w,h,d]])

        #right hand strip 2.54,38.1 at 6.52,7.41
        w = 2.54; h = 38.1; d = depth_clamp
        x_shift = 6.52; y_shift = 7.41; z_shift = 0
        cubes.append([[x_shift, y_shift, z_shift], [w,h,d]])

        #right upper servo connectors 7.62,10.16 at 16.68,21.38
        w = 7.62; h = 10.16; d = depth_clamp
        x_shift = 16.68; y_shift = 21.38; z_shift = 0
        cubes.append([[x_shift, y_shift, z_shift], [w,h,d]])

        #bottom ones
        #left uno header clearance 2.54,15.24 at -23.96,-17.15
        w = 2.54; h = 15.24; d = depth_clamp
        x_shift = -23.96; y_shift = -17.15; z_shift = 0
        cubes.append([[x_shift, y_shift, z_shift], [w,h,d]])

        #left servo connectors 7.62,20.32 at -17.61,-11.64
        w = 7.62; h = 20.32; d = depth_clamp
        x_shift = -17.61; y_shift = -11.64; z_shift = 0
        cubes.append([[x_shift, y_shift, z_shift], [w,h,d]])

        #left lower servo connectors 5.08,7.62 at -7.45,-20.53
        w = 5.08; h = 7.62; d = depth_clamp
        x_shift = -7.45; y_shift = -20.53; z_shift = 0
        cubes.append([[x_shift, y_shift, z_shift], [w,h,d]])

        #power light 5,4 at -13,-27
        w = 5; h = 4; d = depth_clamp
        x_shift = -13; y_shift = -27; z_shift = 0
        cubes.append([[x_shift, y_shift, z_shift], [w,h,d]])

        #weird connectors at bottom 7.62,10.16 at 1.44,-21.8
        w = 7.62; h = 10.16; d = depth_clamp
        x_shift = 1.44; y_shift = -21.8; z_shift = 0
        cubes.append([[x_shift, y_shift, z_shift], [w,h,d]])

        #right hand servo connectors 7.62,10.16 at 16.68,-16.72
        w = 7.62; h = 10.16; d = depth_clamp
        x_shift = 16.68; y_shift = -16.72; z_shift = 0
        cubes.append([[x_shift, y_shift, z_shift], [w,h,d]])

        #right hand uno connector  2.54,20.32 at 24,-14.61
        w = 2.54; h = 20.32; d = depth_clamp
        x_shift = 24; y_shift = -14.61; z_shift = 0
        cubes.append([[x_shift, y_shift, z_shift], [w,h,d]])


        for cube in cubes:
            p3 = copy.deepcopy(kwargs)
            p3["type"] = "n"
            p3["shape"] = f"oobb_cube"
            ex = 1.5
            w = cube[1][0] + ex
            h = cube[1][1] + ex
            d = cube[1][2]
            size = [w,h,d]
            p3["size"] = size
            #p3["m"] = "#"
            pos1 = copy.deepcopy(pos)
            pos1[0] += cube[0][0]
            pos1[1] += cube[0][1]
            pos1[2] += cube[0][2]+depth_lift+depth
            p3["pos"] = pos1
            oobb_base.append_full(thing,**p3)

        #add countersunk linkers
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_screw_countersunk"
        p3["radius_name"] = "m3"
        p3["depth"] = depth_clamp + depth + depth_lift
        p3["nut"] = True
        p3["overhang"] = True
        p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        pos1[2] += 0
        pos11 = copy.deepcopy(pos1)
        pos11[0] += width/2 * 15 - 15
        pos11[1] += height/2 * 15 - 7.5
        pos12 = copy.deepcopy(pos1)
        pos12[0] += -width/2 * 15 + 15
        pos12[1] += height/2 * 15 - 7.5
        pos13 = copy.deepcopy(pos1)
        pos13[0] += width/2 * 15 - 15
        pos13[1] += -height/2 * 15 + 7.5
        pos14 = copy.deepcopy(pos1)
        pos14[0] += -width/2 * 15 + 15
        pos14[1] += -height/2 * 15 + 7.5
        poss = []
        poss.append(pos11)
        poss.append(pos12)
        poss.append(pos13)
        poss.append(pos14)
        p3["pos"] = poss
        rot1 = copy.deepcopy(rot)
        rot1[1] = 180
        p3["rot"] = rot1
        oobb_base.append_full(thing,**p3)

        #locating spheres
        positions = []
        positions.append([-23.96,26.46])
        positions.append([24,24])
        positions.append([-19.5,-26.5])
        positions.append([8.5,-26.5])
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "positive_positive"
        p3["shape"] = f"sphere"
        p3["radius"] = 3/2
        #p3["m"] = "#"
        poss = []
        for shift in positions:
            pos1 = copy.deepcopy(pos)
            pos1[0] += shift[0]
            pos1[1] += shift[1]
            pos1[2] += depth + depth_lift + 3 + 1.2
            poss.append(pos1)
        p3["pos"] = poss
        oobb_base.append_full(thing,**p3)



        return thing


def add_shennie_atmega328p_arduino_compatible_breakout_cnc_shield(thing, **kwargs):
        depth = kwargs.get("thickness", 3)
        pos = kwargs.get("pos", [0, 0, 0])
        rot = kwargs.get("rot", [0, 0, 0])
        extra_lift = 3

        positions = []
        shift_x = 26.75
        shift_y = 32.25
        positions.append([-shift_x,shift_y])
        positions.append([26.75,16.25])
        positions.append([shift_x,-shift_y])
        positions.append([-shift_x,-shift_y])
        
        #add mounting holes
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_screw_countersunk"
        p3["radius_name"] = "m3"
        p3["depth"] = depth + extra_lift
        p3["holes"] = "mounting"
        #p3["m"] = "#"
        poss = []
        for shift in positions:
            pos1 = copy.deepcopy(pos)
            pos1[0] += shift[0]
            pos1[1] += shift[1]
            pos1[2] += 0
            poss.append(pos1)
        p3["pos"] = poss
        rot1= copy.deepcopy(rot)
        rot1[1] = 180
        p3["rot"] = rot1
        #p3["zz"] = "bottom"
        oobb_base.append_full(thing,**p3)

        #add cylinder lifters
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "positive"
        p3["shape"] = f"oobb_cylinder"
        p3["radius"] = 6/2
        p3["depth"] = extra_lift
        #p3["m"] = "#"
        
        poss = []
        for position in positions:
            pos1 = copy.deepcopy(pos)
            pos1[0] += position[0]
            pos1[1] += position[1]
            pos1[2] += extra_lift + depth/2
            poss.append(pos1)
        p3["pos"] = poss        
        oobb_base.append_full(thing,**p3)

        return thing


def add_shennie_atmega328p_arduino_compatible_breakout_screw_terminal_3_5_mm_pitch(thing, **kwargs):
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