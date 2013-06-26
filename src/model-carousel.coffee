root = @
if not root.app? then app = root.app = {} else app = root.app
if not app.models then models = app.models = {} else models = app.models

class models.CarouselModel extends Backbone.Model
  defaults:
    id:"some id"
    index:"some index"
    imgsrc:"some imgsrc"
    thumblabel:"some thumblabel"
    desc:"some desc"
    selected:"boolean"

    initialize: () ->
      @set "active", @setActive()

    setActive: () ->
      if @get("selected") then active = "active"

class models.CarouselModelCollection extends Backbone.Collection
  model: models.CarouselModel
