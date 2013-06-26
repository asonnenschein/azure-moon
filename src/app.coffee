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

carousel = [
  new app.models.CarouselModel
    id:"pentagrambohemianglassearrings"
    index:'0'
    display:"Pentagram and Bohemian Glass Earrings"
    imgsrc:"media/earrings/pentagram_and_bohemian_glass_earrings.jpg"
    selected:true
,
  new app.models.CarouselModel
    id:"wirewrappedtumbledamethystnecklace"
    index:"1"
    display:"Wire Wrapped Tumbled Amethyst Necklace"
    imgsrc:"media/necklaces/wire_wrapped_tumbled_amethyst.jpg"
    selected:false
,
  new app.models.CarouselModel
    id:"creosotesmudgebundle"
    index:"2"
    display:"Creosote Smudge Bundle"
    imgsrc:"media/scents/creosote_smudge_bundle.jpg"
    selected:false
,
  new app.models.CarouselModel
    id:"hippygypsytearloopearrings"
    index:"3"
    display:"Hippy Gypsy Tear Loop Earrings"
    imgsrc:"media/earrings/hippie_gypsy_tear_loop_earrings.jpg"
    selected:false
,
  new app.models.CarouselModel
    id:"witchesgardensign"
    index:"4"
    display:"Witches Garden"
    imgsrc:"media/signs/witches-garden.jpg"
]

app.headNavbarCollection = new app.models.headNavbarCollection headNavbar

app.carouselCollection = new app.models.CarouselModelCollection carousel

app.headNavbar = new app.views.headNavbarView
  el: $(".nav").first()
  collection: app.headNavbarCollection
app.headNavbar.render()

app.carouselIndicators = new app.views.CarouselIndicatorView
  el: $(".carousel-indicators").first()
  collection: app.carouselCollection
app.carouselIndicators.render()

app.carouselInner = new app.views.CarouselInnerView
  el: $(".carousel-inner").first()
  collection: app.carouselCollection
app.carouselInner.render()

$('.carousel').carousel
  interval: 3000
$('.carousel').carousel 'next'