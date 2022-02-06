# DazHairConverter
## Fork of plugin created by Cinus.
Original:-
https://www.daz3d.com/forums/discussion/445851/hair-converter-add-on-for-blender

Original description:-
install the add-on like you would install any other blender add-on.

The add-on can now convert most hair made of “hair cards”. The hair cards must consist of faces with 4 vertices (quads). It cannot convert hair with triangles or n-gons. It will also fail to convert cards that fold back on themselves or cards that do not start on or near the skull. Toulouse hair is an example of such hair. It will convert the hair, but some cards do not start at the skull, so the generated root particles will be wrong.

Once the add-on is installed, you should see a “DazHairConverter” menu in the right-hand side of your 3D view (assuming you are using the default layout). It should look something like what is depicted in the attached Hair.jpg image.

How to use:

Import a Daz model with hair using either the Diffeomorphic or DazToBlender add-on or whatever other method you prefer. Most of my testing was done with the Diffeo plugin. I am not sure the hair converter will work if you use DazToBlender with the “Size * 100” box checked when importing the model.

You must separate the hair cap from the main hair for the converter to work. It’s the same process that Thomas Larsson documented very well here https://diffeomorphic.blogspot.com/p/hair-version-15.html

Make sure you are in Object mode.

Select the hair mesh.

Switch to Edit mode.

Select any face on the hair cap.

Press Ctrl+L and then press P and then Enter.

A new mesh should have been created. Rename the new mesh to Cap, or “Hair Emitter” or something similar. The name is not important. The “hair cap” will become the particle emitter.

If there is a Subsurface modifier on the hair cap, remove it. It’s not strictly necessary, but I think particle hair looks better without it. Blender seems to have issues if you disconnect and re-connect hair with a subsurface modifier on it.

Once the hair and cap are separated, you can convert the hair.

Switch back to Object mode.

Select the hair mesh and while holding in shift, select the hair cap. It’s important to select the hair mesh first.

Select the “DazHairConverter” menu on the right-hand side of the 3D viewport.

The hair converter has three parameters:

Segments: Number of segments to create per particle. The default is 10. For shorter hair, you should decrease the number. For very curly hair, increase the number. Max is 20, but 14 should work well even for long curly hair.

Single Strand Width (m): This value is used to determine which hair cards will be converted to single particles with no children. If you set the value to 0, then no “single hairs” will be created. If you set the value to the max then most of the hair particles will become “single hairs”. The default value of .001 should work for most hair, but for AprilYsh hair I get the best results by setting it to 0 and then using the Random and Threshold settings under Roughness to add loose hairs.

Strand Radius (m): This value will be used as the child particle radius. If a hair card wider than 2 * Strand Radius is encountered, additional particles will be created in order to fill the card with hair. A value of .008 works well for most hair.

In order to kick off the conversion, click the “Convert Hair” button.

After a few seconds, the converted particle hair should appear.

The converter will hide the original hair mesh once the conversion is done.

You should see a “hair-01” and possibly a “single hairs” particle slot in the Particle Settings panel when the hair cap is selected.

If you want to have all of the particle roots directly on the hair cap, you can use the “Disconnect Hair” and “Connect Hair” option in the particle settings. This will change the look of the hair. It usually lifts the hair up a bit because a lot of hair cards start well below the hair cap.

The converter will create a material for the hair particles called “ParticleHair”. It uses a Principled Hair BSDF shader for Cycles and several nodes for Eevee. In order to change the hair color for Cycles, change the Melanin value. Smaller values for light hair and larger values for dark hair. See this for more info https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/hair_principled.html

For a better hairline, especially for darker hair, use j cade’s node setup. It improves the look of the hairline considerably, but does increase the render time somewhat. You could also use a thinner root than tip as @Krampus suggested, but that will change the look of the hair and you may or may not like it.

For Eevee, change the colors in the Diffuse BSDF and the Glossy BSDF nodes to get the desired color.

You should play around with the hair settings to get the best look. The Clumping section together with the “Radius” under Children can have the biggest impact. I suggest using a “clump curve” that looks something like the one in the attached “Clump Curve.jpg” image.

Changing the Endpoint (under Children->Roughness) to .001 or .002 can improve the look too, but that depends on the type of hair.

To add “loose hairs” for meshes that do not already have a lot of thin cards, use the Random and Threshold settings under Roughness. For most hair, a Random setting of .05 to .07 and a Threshold setting of .6 to .7 works well.

The material for the original hair cap is left in place. Sometimes it looks better without the hair cap. If you do not want to render the hair cap then switch off “Show Emitter” in the particle settings of the first particle slot (can be found in the Viewport Display and Render sub panels)

It is now possible to create several different particle systems for the hair if you choose to do so. If you select a subset of cards before running the conversion, the converter will only convert the selected cards. It will not remove any converted particles, just add new particle slots for the selected cards.

This is handy if the hair has braids. You could first select all the non-braid strands and then run the conversion. Then select all the cards that make up the braids and run it again. You will end up with another particle system for the braids that will allow you to tune the braids to your liking.

This is also handy if you want to create separate particle slots for bangs, etc.

I tested the add-on in Blender 2.83.3 and 2.90.1.

Good luck with your hair conversions. Your computer should not explode when you run this converter, but I make no guarantee :).

