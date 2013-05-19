root = @
if not root.app? then app = root.app = {} else app = root.app
if not app.models then models = app.models = {} else models = app.models

class models.headNavbarModel extends Backbone.Model
  defaults:
    id:"some id"
    display:"some display"
    selected:"boolean"

  initialize: () ->
    @set "active", @setActive()

  setActive: () ->
    if @get("selected") then active = "active"

class models.headNavbarCollection extends Backbone.Collection
  model: models.headNavbarModel