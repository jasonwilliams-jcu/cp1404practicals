HEX_COLOURS = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb",
               "antiquewhite2": "#eedfcc", "antiquewhite3": "#cdc0b0 ", "antiquewhite4": "#8b8378",
               "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74"}
print(HEX_COLOURS)

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name, HEX_COLOURS.get(colour_name)))
    colour_name = input("Enter a colour name: ")


