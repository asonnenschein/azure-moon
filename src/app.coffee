root = @
if not root.app? then app = root.app = {} else app = root.app

headNavbar = [
  new app.models.headNavbarModel
    id:"home"
    display:"Home"
    selected:true
,
  new app.models.headNavbarModel
    id:"blog"
    display:"Blog"
    selected:false
,
  new app.models.headNavbarModel
    id:"returnpolicy"
    display:"Return Policy"
    selected:false
,
  new app.models.headNavbarModel
    id:"shipping"
    display:"Shipping"
    selected:false
,
  new app.models.headNavbarModel
    id:"cart"
    display:"View Cart"
    selected:false
,
  new app.models.headNavbarModel
    id:"about"
    display:"About"
    selected:false
]

app.headNavbarCollection = new app.models.headNavbarCollection headNavbar

app.headNavbar = new app.views.headNavbarView
  el: $(".nav").first()
  collection: app.headNavbarCollection
app.headNavbar.render()