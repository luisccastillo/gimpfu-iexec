#!/usr/bin/python2.7
from gimpfu import *
import gimpfu

def cartoon_file(filepath, filename, output_directory):
    img = pdb.gimp_file_load(filepath, filepath)
    dodgeLayer = img.layers[0].copy()
    dodgeLayer.mode = DODGE_MODE
    img.add_layer(dodgeLayer, 0)
    pdb.gimp_invert(dodgeLayer)
    pdb.plug_in_vpropagate(img, dodgeLayer, 1, 1, 1, 15, 0, 255)
    pdb.plug_in_vpropagate(img, dodgeLayer, 1, 1, 1, 15, 0, 255)
    pdb.plug_in_vpropagate(img, dodgeLayer, 1, 1, 1, 15, 0, 255)
    layer=pdb.gimp_layer_new(img, img.width, img.height , gimpfu.RGB_IMAGE, "base", 40, gimpfu.LAYER_MODE_LCH_CHROMA)
    pdb.gimp_context_set_foreground((229,21,175))
    img.add_layer(layer,0)
    pdb.gimp_drawable_edit_bucket_fill(layer, 0, 0, 0)
    img.flatten()
    pdb.gimp_file_save(img, img.layers[0], output_directory + "/" + filename, output_directory + "/" + filename)
    pdb.gimp_image_delete(img)

register(
    "python-fu-cartoon",
    "Applies a cartoonish look on an image",
    "Pass the filepath, filename and output directory",
    "Carlos Castillo",
    "Carlos Castillo",
    "2020",
    "RGB*",
    "",
    [
        (PF_STRING, "filepath", "GlobPattern", "*.*"),
        (PF_STRING, "filename", "GlobPattern", "*.*"),
        (PF_STRING, "output_directory", "GlobPattern", "*.*")
    ],  # The parameters for the plug-in's method
    [],  # The results of the plug-in's method
    cartoon_file)  # The name of the method to call in your Python code

main()
