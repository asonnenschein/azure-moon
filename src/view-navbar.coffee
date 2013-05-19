root = @
if not root.app? then app = root.app = {} else app = root.app
if not app.views? then app.views = views = {} else views = app.views

class views.headNavbarView extends Backbone.View
  initialize: ->
    @navbarTemplate = _.template $("#headNavbar").html()

  render: ->
    body = @$el
    navbarTemplate = @navbarTemplate

    @collection.forEach (model) ->
      body.append navbarTemplate
        model:model