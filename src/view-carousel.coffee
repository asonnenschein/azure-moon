root = @
if not root.app? then app = root.app {} else app = root.app
if not app.views? then app.views = views = {} else views = app.views

class views.CarouselIndicatorView extends Backbone.View
  initialize: ->
    @CarouselIndicatorsTemplate =  _.template $("#CarouselIndicators").html()

  render: ->
    body = @$el
    CarouselIndicatorsTemplate = @CarouselIndicatorsTemplate

    @collection.forEach (model) ->
      body.append CarouselIndicatorsTemplate
        model:model

class views.CarouselInnerView extends Backbone.View
  initialize: ->
    @CarouselInnerTemplate = _.template $("#CarouselInner").html()

  render: ->
    body = @$el
    CarouselInnerTemplate = @CarouselInnerTemplate

    @collection.forEach (model) ->
      body.append CarouselInnerTemplate
        model:model