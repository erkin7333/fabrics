"use strict";

(function() {
  $(function() {



    // AOS
    AOS.init({
      offset: 100,
      once: true,
      duration: 1100,
      delay: 150
    });
    setTimeout(function() { AOS.refresh(); }, 1);

    //SELECT2
    $(".js-select").select2({
      placeholder: "Выберите...",
      allowClear: false
    });
    $(".js-select.search-hide").select2({
      minimumResultsForSearch: Infinity
    });
    // FANCYBOX
    if ($("[data-fancybox='gallery']").length != 0)
      $("[data-fancybox='gallery']").fancybox({
        afterShow: function(instance, current) {},
        transitionEffect: "zoom-in-out"
      });
    // ELEVATEZOOM
    if (!checkSm())
      var x = $("[data-zoom-image]:not([group])").elevateZoom({
        scrollZoom: true,
        zoomWindowFadeIn: 500,
        zoomWindowFadeOut: 500,
        lensFadeIn: 300,
        lensFadeOut: 300,
        //cursor: 'pointer', 
        tint: true,
        tintColour: '#000',
        tintOpacity: 0.5,
        //zoomType        : "lens",
        //lensShape : "round",
        //lensSize    : 200,
        imageCrossfade: true,
        easing: true
      });


    //MIN-MENU
    var minMenu = $("#min-menu").mmenu({
      extensions: [
        "pagedim-black", // wrapper-bg black
        "theme-dark",
        //"fullscreen",
        //"listview-50",
        //"fx-panels-slide-up",
        //"fx-listitems-drop",
        "border-offset"
        //"position-front",
        //"position-center"
      ],
      navbar: {
        title: "Меню"
      },
      navbars: [{
          height: 2,
          //position: "bottom",
          content: [
            '<div class="close-btn hide close-content bar">' +
            '<a  href="#page" ><span class="icon-bar"></span><span class="icon-bar"></span></a>' +
            '</div>'
          ]
        },
        {
          content: ["prev", "title"]
        }
      ]
    }, {});

    var userPanel = minMenu.find(".user-panel") || null;
    if( userPanel )
      $(".mm-navbars-top").append( userPanel );
    minMenu.after( $(".entry-modal") );
    $(document).on("click", "[href='#"+minMenu.attr("id")+"']", landCarousel)
    
    //FLIKITY
    function flickityPrevNext(className) {
      var carouselWrapper = $(className);
      for (var i = 0; i < carouselWrapper.length; i++) {
        var crs = $(carouselWrapper[i]);
        var carousel = crs.find(".carousel-items");
        var carouselPrevNext = crs.find(".carousel-prev-next");
        var btnNext = carouselPrevNext.find(".next");
        var btnPrev = carouselPrevNext.find(".prev");
        var flkty = carousel.data("flickity");
        var selected;
        console.log(carousel)
        btnNext.on("click", function() {
          carousel.flickity("next", true);
        });

        btnPrev.on("click", function() {
          carousel.flickity("previous", true);
        });
        carousel.on("select.flickity", function() {
          selected = $(flkty.selectedElement);
          selected
            .siblings()
            .addBack()
            .removeClass("is-next is-prev");
          selected.next().addClass("is-next");
          selected.prev().addClass("is-prev");
        });
      }
    }

    var arrowStyle = {
      x0: 10,
      x1: 60,
      y1: 50,
      x2: 70,
      y2: 40,
      x3: 30
    };

    var brandMenu = $('.brands-menu-carousel .carousel-items').flickity({
      imagesLoaded: true,
      autoPlay: false,
      arrowShape: arrowStyle,
      initialIndex: 0,
      prevNextButtons: false,
      draggable: false,
      friction: 1,
      selectedAttraction: 1,
      wrapAround: true,
      pageDots: false,
      contain: true,
      percentPosition: true,
      cellAlign: 'center'
    });

    $('.button-group').on('click', 'li', function() {
      var that = $(this);
      var selector = that.attr('data-selector');
      that.addClass("is-selected");
      that.siblings().removeClass("is-selected");

      console.log($(this).siblings());
      brandMenu.flickity('selectCell', selector);
    });

    //short-partners-carousel
    if ($(".short-partners-carousel .carousel-items figure").length > 3)
      $('.short-partners-carousel .carousel-items').flickity({
        imagesLoaded: true,
        autoPlay: false,
        pauseAutoPlayOnHover: true,
        arrowShape: arrowStyle,
        initialIndex: 2,
        prevNextButtons: true,
        draggable: true,
        wrapAround: true,
        pageDots: false,
        contain: false,
        percentPosition: true,
        cellAlign: 'center'
      });
    //producitons-carousel
    $('.productions-carousel .carousel-items').map(function(i, el) {
      var fct = $(el).flickity({
        imagesLoaded: true,
        autoPlay: false,
        pauseAutoPlayOnHover: true,
        lazyLoad: true,
        arrowShape: arrowStyle,
        setGallerySize: true,
        initialIndex: 1,
        prevNextButtons: true,
        draggable: false,
        resize: false,
        wrapAround: true,
        pageDots: false,
        contain: false,
        percentPosition: true,
        cellAlign: 'left'
      })
      //TODO
      var fctData = fct.data("flickity");
      $(fct).on('ready.flickity', function() {
        console.log('Flickity ready');
      });
      $(document).on("click", "[flickity='resize']", function() {
        setTimeout(function() {
          fct.flickity('resize');
        }, 200)
      })
    })
    //short-reviews-carousel
    if ($(".short-reviews-carousel .carousel-items figure").length > 1)
      $('.short-reviews-carousel .carousel-items').flickity({
        imagesLoaded: true,
        autoPlay: false,
        pauseAutoPlayOnHover: true,
        arrowShape: arrowStyle,
        initialIndex: 1,
        prevNextButtons: false,
        draggable: true,
        wrapAround: false,
        pageDots: false,
        contain: false,
        percentPosition: true,
        cellAlign: 'center'
      });
    flickityPrevNext($('.short-reviews-carousel'));

    //lang-carousel
    function landCarousel(){
      var crs = $(".lang-carousel-items").flickity({
        imagesLoaded: true,
        autoPlay: false,
        pauseAutoPlayOnHover: true,
        arrowShape: arrowStyle,
        initialIndex: 1,
        prevNextButtons: true,
        draggable: checkSm(),
        wrapAround: true,
        pageDots: false,
        contain: false,
        percentPosition: true,
        cellAlign: "center"
      })
      crs.data("flickity");
      crs.flickity("resize");
      
    }
    landCarousel();

    //wholesalers-carousel
    $(".wholesalers-carousel .carousel-items").flickity({
      imagesLoaded: true,
      autoPlay: false,
      pauseAutoPlayOnHover: true,
      arrowShape: arrowStyle,
      initialIndex: 1,
      friction: 1,
      selectedAttraction: 1,
      prevNextButtons: true,
      draggable: checkSm(),
      wrapAround: true,
      pageDots: true,
      contain: false,
      percentPosition: true,
      cellAlign: "center"
    });





    // Стандартный карусель
    window.carouselArticle = function() {
      if ($(".carousel-article").length >= 0) {
        var carouselMain = $(".carousel-article .carousel-main"),
          carouselNav = $(".carousel-article .carousel-nav");

        for (var i = 0; i < carouselMain.length; i++) {
          var crs = $(carouselMain)
            .eq(i)
            .flickity({
              imagesLoaded: true,
              prevNextButtons: false,
              cellAlign: "center",
              bgLazyLoad: 1,
              friction: 1,
              selectedAttraction: 1,
              initialIndex: 0,
              draggable: !checkSm(),
              contain: true,
              pageDots: false
            });
          var flkty = crs.data("flickity");

          //ГК
          crs.on('settle.flickity', function(e) {
            $(flkty.selectedElement).siblings().css("pointer-events", "none");
            var selecedIndex = carouselMain.find(".carousel-cell.is-selected").index() + 1;

            //console.log(this, e);
            var zoomContainer = $(".zoomContainer") || null
            if (!zoomContainer)
              return;
            zoomContainer.removeClass("is-selected");
            zoomContainer.filter("[zoomitem='" + selecedIndex + "']").addClass("is-selected");
            if (!zoomContainer.hasClass("zoom-image"))
              zoomContainer.map(function(i, el) {
                $(el).addClass("zoom-image")
                if (i === 0)
                  $(el).addClass("is-selected")

                //console.log($(el), i)
                $(el).attr("zoomitem", (i + 1))
              })


          })
          crs.on('select.flickity', function(e) {
            $(flkty.selectedElement).css("pointer-events", "");
          })

          var colorList = $('.products-colors .list-inline') || null;
          if( colorList ){
            colorList.find('li').attr("role", "button");
            colorList.on( 'click', 'li', function() {
                var index = $(this).index();
                crs.flickity( 'select', index );
                colorList.find('li').removeClass("active")
                $(this).addClass("active");
            });
          }

          $(carouselNav).eq(i).flickity({
            imagesLoaded: true,
            initialIndex: 0,
            asNavFor: $(carouselMain)[i],
            prevNextButtons: true,
            draggable: true,
            cellAlign: "center",
            adaptiveHeight: true,
            contain: true,
            pageDots: false
          });
        }
      }
    };
    carouselArticle();
    //carouselProducts
    if ($(".products-article").length != 0){
      var productsArticle = $(".products-article").addClass("load");
      if( checkSm() )
        productsArticle.find(".carousel-main a").attr("data-fancybox", "gallery");
    }

    $(".megasubmenu-nav li").hover(function(){
      var megasubmenuItems = $(this).closest(".megasubmenu-nav").siblings(".megasubmenu-items").find(".megasubmenu-item") || null;
      if( !megasubmenuItems ) 
        return;
      megasubmenuItems.add( $(this).siblings() ).removeClass("is-hover");
      megasubmenuItems.eq( $(this).index() ).add( $(this) ).addClass("is-hover");
    },function(){})

    // SMOTHSCROLL-LINK
    smoothScroll.init({
      easing: 'easeInOutCubic'
    });


    // Прибавление-убавление значении
    (function(){
      var form = $("[data-counter]") || null;;
      if( !form )
        return;
      var cntfactor = form.attr("data-counter")*1;

      $("[data-counter-btn]").on("click.cntchange", function(){
        var cntVal;
        var cntInput = $(this).closest( form ).find("[data-counter-input]");
        
        cntVal = (cntInput.val()*1);

        if( $(this).hasClass("plus") )
          cntVal = cntVal + cntfactor;
        if( $(this).hasClass("minus") & cntVal > 0 )
          cntVal = cntVal - cntfactor;
        if( isNaN( cntVal ) || cntVal <= 0) cntVal = 1;
          cntInput.val( cntVal ).attr("value", cntVal)
      })


    })();
    

    // Адаптивное подменю
    (function(){
      var menuBottom = $(".menu-bottom:eq(0)");
      if( menuBottom.length )
        $(".menu-bottom .submenu-maquillage").map(function(i, el){
          el = $(el);
          var menuBottomOffset = menuBottom.offset().left+menuBottom.width();
          var subMenuOffset = el.offset().left+el.width()
          var remainder = menuBottomOffset-subMenuOffset;
          
          if( remainder < 0 )
            el.offset({
              left:  $(el).offset().left+remainder
            })
        })
      })();
      
     // Иконка чекбокса
     (function(){
        window.toggleLabelCheckbox = function( that ){
          $(that).find(".fa-square-o").toggleClass("hide")
          $(that).find(".fa-check-square-o").toggleClass("hide")
        }
      })();
    // Правильное окончание слово "товар"
    (function(){
      var basketText = $(".basket-text") || null;
      var basketCnt = $(".basket-cnt").text() || false;
      if( !basketText || !basketCnt.length )
        return;
      var basketCnt = basketCnt.substring( basketCnt.length-1, basketCnt.length )*1;
      if( basketCnt === 0 )
        basketText.text("товаров");
      else if( basketCnt === 1 )
        basketText.text("товар");
      else if( basketCnt > 1 && basketCnt <= 4 )
        basketText.text("товара ");
      else
        basketText.text("товаров");
    })();


    /*AJAX вход*/
    window.ajaxRequest = function(form, success){
      var data = typeof form == "string" ? form : form.serialize();
      var responce;
      $.ajax({
        type: "POST",
        url: location.href,
        data: data,
        success: success,
        //contentType: "Content-Type:application/json;",
        statusCode: {
          404: function(){alert( "page not found" );}
        },
        complete: function(){}
      });
    };

    /*Вход на сайт
    * TODO
    */
    $("#sign-in-form button").on("click", function(){

      ajaxRequest($("#sign-in-form"), function(responceText, event){
          window.responceText = responceText;          
          if( responceText.match(/<div class="message error">Ошибка/gim) ){
            $("#form-entry").find(".info-err").text( "Ошибка. Неверный логин или пароль" );
            console.log("Ошибка");
          }
          else{
            //$(".authorized").show();
            //$(".unauthorized").hide();
            $("#form-entry").modal("hide");
            location.reload();
          }
      });
    })

    /*Расчёт суммы за продуктов*/
    function recnt(){
      var totalcost = 0;
      var itemsFormCnt = $(".basket-items .products-cnt-form") || null;
      if( !itemsFormCnt )
        return;
      itemsFormCnt.map(function(i, el){
        totalcost = totalcost + ($(el).find("[data-totalcost-item]").attr("data-totalcost-item")*1);
      })
      $(".recalculate-form .price").text(totalcost);
     // $("#PaymentPaycom .price").text(totalcost);
    }
    function productionCntChange(input){
      var quantity;
      var price;
      var id;
      if( !input )
        return;
      id = input.attr("data-id")*1;
      quantity = input.attr("data-quantity", input.attr("value")).attr("data-quantity")*1;
      price = input.attr("data-price");
      input.attr("data-totalcost-item", quantity*price);
      ajaxRequest("bulk="+input.val()+"&id="+id);
      recnt();
    }

    $(".products-cnt-form [data-counter-btn]").on("click.cntchange", function(){
      var input = $(this).closest(".products-cnt-form").find(".cnt-input");
      productionCntChange(input);
    })
    $(".products-cnt-form").find(".cnt-input").on("change", function(){
      var input = $(this);
      $(this).attr( "value", $(this).val() );
      productionCntChange(input);
    })

    /*Пересчёт итоговой оплаты
    window.totalcost = !isNaN($("[data-totalcost]").attr("data-totalcost")*1) ? $("[data-totalcost]").attr("data-totalcost")*1 : false;
    window.mincost = !isNaN($("[data-mincost]").attr("data-mincost")*1) ? $("[data-mincost]").attr("data-mincost")*1 : false;
    
    
      $("[data-delivery]").on("change", function(){
        if( !totalcost )
          return;
        var that = this;
        var delivery = $(that).attr("data-delivery")*1;
        $(".totalcost-content .price").text( intSpace(delivery+totalcost) );
        $(".totalcost-content .delivery").text( intSpace(delivery) );

        $("[data-total-amount]").attr("value", delivery+totalcost).val(delivery+totalcost);
        $("[data-delivery-amount]").attr("value", delivery).val(delivery);
        
      })
    
    window.compareLorder = function( that, delivery, currentMincost ){
      if( !(mincost && totalcost) )
        return;
      currentMincost = currentMincost || mincost;
      if( totalcost <= mincost ){
        $(that).attr("data-delivery", delivery);
        return true;
      }else{
        $(that).attr("data-delivery", "0")[0].checked = true;
        return false;
      }
    }
    if( mincost && totalcost ){
      if( totalcost > mincost )
        $("[data-delivery][data-delivery-perk]").trigger("change")[0].checked = true;
      else
        $("[data-delivery][data-delivery-def]").trigger("change")[0].checked = true;
    }
  */

    function onLoaded() {
      //MASONRY
      if ($(".grid-img").length != 0) {
        var $grid = $(".grid-img").masonry({
          itemSelector: ".grid-img-item",
          columnWidth: ".grid-img-sizer",
          percentPosition: true
        });
      }
    }

    //SCROLL
    var minMenu = $(".header-scroll") || null;
    var headerRange = false;


    $(window).on("scroll", function(e) {

      if ($(window).scrollTop() > 50 && headerRange == false) {

        headerRange = true;
        if (minMenu) minMenu.addClass("scrolled").addClass("down");

      } else if ($(window).scrollTop() < 50 && headerRange == true) {
        headerRange = !true;
        if (minMenu) minMenu.removeClass("scrolled");
      } //.originalEvent.wheelDelta
    });


    $(window).on("mousewheel", function(event) {
      if (!headerRange) return;
      if (event.originalEvent.wheelDelta >= 0) {
        minMenu.removeClass("up");
      } else {
        minMenu.addClass("up");
      }
    });

    window.preLoader = {
      preBox: ".pre-box",
      enter: false,
      status: $(".pre-box").hasClass("in"),

      preToggle: function(bool, func) {
        var endtime = 600;
        if (!this.enter) return;
        if (typeof func === "function")
          setTimeout(function() {
            func();
          }, endtime);
        var preBox = $(this.preBox);

        bool || this.status ?
          preBox.removeClass("in").setTimeout(function() {
            $(preBox).hide();
          }, endtime) :
          preBox
          .show()
          .addClass("in")
          .find(".box-content");

        return (this.status = !this.status);
      },

      preImg: function(img) {
        var images = img || document.images,
          imagesTotalCount = images.length,
          imagesLoadedCount = 0,
          preloadPercent = $(".percent").text("0 %");

        if (imagesTotalCount == 0) {
          preOnload();
          $(preloadPercent).text("100 %");
        }

        for (var i = 0; i < imagesTotalCount; i++) {
          var image_clone = new Image();
          image_clone.onload = image_loaded;
          image_clone.onerror = image_loaded;
          image_clone.src = images[i].src;
        }

        function preOnload() {
          onLoaded();
        }

        function image_loaded() {
          imagesLoadedCount++;

          var per = (100 / imagesTotalCount * imagesLoadedCount) << 0;

          setTimeout(function() {
            //console.log(per);
            $(preloadPercent).text(per + "%");
          }, 1);

          if (imagesLoadedCount >= imagesTotalCount) preOnload();
        }
      }
    };

    preLoader.preImg();




    var revSlider = $('.rev-slider') || null;
    var bannerSlider = $('.rev-slider').hasClass("banner-slider") || null;

    onResized(function() {
      if (revSlider.length != 0)
        revSlider.revolution({
          delay: 6000,
          startwidth: checkSm() ? $(window).width() : checkMd() ? 970 : 1170,
          startheight: checkSm() ? 200 : bannerSlider ? 350 : 400,
          autoHeight: "off",
          fullScreenAlignForce: "off",

          onHoverStop: "on",

          thumbWidth: 100,
          thumbHeight: 50,
          thumbAmount: 3,

          hideThumbsOnMobile: "on",
          hideBulletsOnMobile: "on",
          hideArrowsOnMobile: "on",
          hideThumbsUnderResoluition: 0,

          hideThumbs: -1,
          hideTimerBar: "on",

          keyboardNavigation: "off",

          navigationType: "bullet",
          navigationArrows: "solo", //solo
          navigationStyle: "round",

          navigationHAlign: "center",
          navigationVAlign: "bottom",
          navigationHOffset: 0,
          navigationVOffset: 30,

          soloArrowLeftHalign: "left",
          soloArrowLeftValign: "center",
          soloArrowLeftHOffset: 30,
          soloArrowLeftVOffset: 0,

          soloArrowRightHalign: "right",
          soloArrowRightValign: "center",
          soloArrowRightHOffset: 30,
          soloArrowRightVOffset: 0,


          touchenabled: "off",
          swipe_velocity: "0.7",
          swipe_max_touches: "1",
          swipe_min_touches: "1",
          drag_block_vertical: "false",

          stopAtSlide: -1,
          stopAfterLoops: -1,
          hideCaptionAtLimit: 0,
          hideAllCaptionAtLilmit: 0,
          hideSliderAtLimit: 0,

          fullWidth: "on",
          fullScreen: "off",
          fullScreenOffsetContainer: "#header",

          dottedOverlay: "none",
          forceFullWidth: "off",

          shadow: 0

        })


    });
    if (revSlider.length) {
      var prevnext = $(".tparrows").append('<svg viewBox="0 0 100 100"><path d="M 10,50 L 50,85 L 55,75 L 30,50  L 55,25 L 50,15 Z" class="arrow"></path></svg>')
      $(".arrow-container.container").append(prevnext).css("top", "350");
      $(".arrow-container.container").css("top", "-" + ($(".rev-slider").css("height").match(/(\d+)/gim)[0] / 2) + "px");
    }



  });
})(jQuery);

var isWebkit = /Webkit/i.test(navigator.userAgent),
  isChrome = /Chrome/i.test(navigator.userAgent),
  isMac = /Mac/i.test(navigator.userAgent),
  isMobile = !!("ontouchstart" in window),
  isAndroid = /Android/i.test(navigator.userAgent);

// COMMON FUNCTION

setTimeout(function() {
  //jQuery FUNCITON
  $.fn.onResized = function() {
    onResized(function() {
      this;
    });
    return this;
  };
}, 10);






$(document).on('click', '.zakaz', function(){

    var name = $(this).data("title");
    
    $("#add_name").text(name);
    $(".subject").val(name);  
}); 


/*$(document).ready(function(){ 
         
    $(document).on('click', '.color-link', function() {
        
        var color = $(this).data('color');
        console.log(color);
        
        $('.color-link.'+ color).toggleClass('active');

       
        
    });
 
});*/

function checkSm() {
  return $(document).width() <= 991;
}

function checkMd() {
  return $(document).width() < 1199 && !checkSm();
}

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

function getRandomIntFloat(min, max) {
  return Math.random() * (max - min) + min;
}

function onResized(f) {
  if (typeof f === "function") f();
  $(window).on("resize", function(e) {
    if (typeof f === "function") f();
  });
  return this;
}

function scrolledDiv(el) {
  try {
    var docViewTop = $(window).scrollTop(),
      docViewBottom = docViewTop + $(window).height(),
      elTop = $(el).offset().top,
      elBottom = elTop + $(el).height() / 1.8;
  } catch (err) {
    console.error(err);
  }

  return elBottom <= docViewBottom && elTop >= docViewTop;
}


function intSpace( int, replaceType ){
    var cnt = 0;
    var newInt = "";
    int = int*1;
    replaceType = replaceType || " ";
    if( typeof int === NaN )
      return;
    var arrInt = (int+"").match(/([0-9])/gim).reverse();
    for (var i = 0; i < arrInt.length; i++) {
      cnt++;
      newInt = arrInt[i]+newInt
      if(cnt === 3){
        newInt = replaceType+newInt;
        cnt = 0;
      }
    }
    return newInt;
}













