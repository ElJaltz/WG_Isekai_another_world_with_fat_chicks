screen gameGallery():
    if Lightbox_image != "":    
        $ lb_image = im.Scale("Escenes/" + Lightbox_image + ".jpg", 2000, 1125) 
        imagebutton:
            idle lb_image
            hover lb_image
            xalign 0.5
            yalign 0.5
            focus_mask True
            action SetVariable("Lightbox_image", "")
    else:
        frame:
            xpos 250
            ypos 100
            background None
            side ("r"):
                area (250, 100, 3840, 2160)
                viewport id "gallery":
                    draggable True mousewheel True
                    vpgrid:
                        cols 4
                        spacing 20

                    for q in galleryList:
                        $ qimage = "Escenes/" + q + ".jpg"
                        $ lb_image = im.Scale(qimage, 640,360)
                        imagebutton:
                            idle lb_image
                            hover lb_image
                            action SetVariable("Lightbox_image", q)