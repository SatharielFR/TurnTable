
#from math import sin, cos, pi

#https://docs.blender.org/api/2.61/info_tips_and_tricks.html

def CreateAnim():
    fStart = bpy.data.scenes["Scene"].frame_start
    fEnd = bpy.data.scenes["Scene"].frame_end

    cam = bpy.context.selected_objects[0]
    obj = bpy.context.selected_objects[1] 
    r = 13 

    for i in range(fEnd):
        time = ((((1+i)/24)*pi)*2)/10
        bpy.context.scene.frame_set(fStart + i)
        cam.location[0] = sin(time) * r
        cam.location[1] = cos(time) * r
        cam.keyframe_insert('location', 0)
        cam.keyframe_insert('location', 1)
    
    constraint = cam.constraints.new(type="TRACK_TO")
    constraint.target = obj
    constraint.track_axis = "TRACK_NEGATIVE_Z"
    constraint.up_axis = "UP_Y"

def Test():
    print("test")