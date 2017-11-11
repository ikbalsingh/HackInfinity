jQuery(document).ready(function($) {

	'use strict';
    //***************************
    // Sticky Header Function
    //***************************
	  jQuery(window).on('scroll', function() {
	      if (jQuery(this).scrollTop() > 170){  
	          jQuery('body').addClass("careplus-sticky");
	      }
	      else{
	          jQuery('body').removeClass("careplus-sticky");
	      }
	  });

    //***************************
    // BannerOne Functions
    //***************************
      jQuery('.careplus-banner-one').slick({
          slidesToShow: 1,
          slidesToScroll: 1,
          autoplay: true,
          autoplaySpeed: 2000,
          infinite: true,
          dots: false,
          arrows: false,
          fade: true,
          responsive: [
                {
                  breakpoint: 1024,
                  settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    infinite: true,
                  }
                },
                {
                  breakpoint: 800,
                  settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                  }
                },
                {
                  breakpoint: 400,
                  settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                  }
                }
              ]
        });
    //***************************
    // fixtureSlider Functions
    //***************************
      jQuery('.sportsmagazine-fixture-slider').slick({
          slidesToShow: 5,
          slidesToScroll: 1,
          autoplay: true,
          autoplaySpeed: 2000,
          infinite: true,
          dots: false,
          prevArrow: "<span class='slick-arrow-left'><i class='fa fa-angle-left'></i></span>",
          nextArrow: "<span class='slick-arrow-right'><i class='fa fa-angle-right'></i></span>",
          responsive: [
                {
                  breakpoint: 1024,
                  settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                    infinite: true,
                  }
                },
                {
                  breakpoint: 800,
                  settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                  }
                },
                {
                  breakpoint: 400,
                  settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                  }
                }
              ]
        });

    //***************************
    // Click to Top Button
    //***************************
    jQuery('.careplus-back-top').on("click", function() {
        jQuery('html, body').animate({
            scrollTop: 0
        }, 800);
        return false;
    });
    //***************************
    // Parent AddClass Function
    //***************************
    jQuery(".sportsmagazine-dropdown-menu,.sportsmagazine-megamenu").parent("li").addClass("subdropdown-addicon");

    //***************************
    // Fancybox Function
    //***************************
    jQuery(".fancybox").fancybox({
      openEffect  : 'elastic',
      closeEffect : 'elastic',
    });
    
    //***************************
    // CartToggle Function
    //***************************
    jQuery('.careplus-user-list li a.fa-shopping-cart').on("click", function(){
          jQuery('.careplus-cart-box').fadeToggle('slow');
          return false;
      });
      jQuery('html').on("click", function() { jQuery(".careplus-cart-box").fadeOut(); });

    //***************************
    // Progressbar Function
    //***************************
    jQuery('.progressbar1').progressBar({
      percentage : false,
      animation : true,
      backgroundColor : "#08364b",
      barColor : "#9bc03c",
      height : "8",
    });

    //***************************
    // Countdown Function
    //***************************
    jQuery(function() {
        var austDay = new Date();
        austDay = new Date(austDay.getFullYear() + 2, 1 - 1, -600);
        jQuery('#sportsmagazine-countdown,#sportsmagazine-game-countdown,#sportsmagazine-banner-countdown').countdown({
            until: austDay
        });
        jQuery('#year').text(austDay.getFullYear());
    });

    //***************************
    // ThumbSlider Functions
    //***************************
    jQuery('.careplus-tabs-thumb,.careplus-tabs-text').slick({
          slidesToShow: 1,
          autoplay: false,
          slidesToScroll: 1,
          arrows: false,
          fade: true,
          asNavFor: '.careplus-tabs-list'
        });
        jQuery('.careplus-tabs-list').slick({
          slidesToShow: 5,
          slidesToScroll: 1,
          autoplay: false,
          asNavFor: '.careplus-tabs-thumb,.careplus-tabs-text',
          dots: false,
          arrows: false,
          vertical: false,
          centerMode: false,
          focusOnSelect: true,
          responsive: [
                {
                  breakpoint: 1024,
                  settings: {
                    slidesToShow: 5,
                    slidesToScroll: 1,
                    infinite: true,
                    vertical: false,
                  }
                },
                {
                  breakpoint: 800,
                  settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                    vertical: false,
                  }
                },
                {
                  breakpoint: 400,
                  settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1,
                    vertical: false,
                  }
                }
              ],
        });
    

});

    //***************************
    // Counter Function
    //***************************
    jQuery('#word-count1').jQuerySimpleCounter({
      end: '64',
      duration: '5000',
    });
    jQuery('#word-count2').jQuerySimpleCounter({
      end: '95',
      duration: '5000',
    });
    jQuery('#word-count3').jQuerySimpleCounter({
      end: '28',
      duration: '5000',
    });
    jQuery('#word-count4').jQuerySimpleCounter({
      end: '09',
      duration: '5000',
    });

//***************************
// FilterAble Function
//***************************
jQuery(window).on('load', function() {
    var $grid = $('.careplus-plane-gallery-filtrable,.careplus-team-modren-filtrable').isotope({
      itemSelector: '.element-item',
      layoutMode: 'fitRows'
    });
    // filter functions
    var filterFns = {
      // show if number is greater than 50
      numberGreaterThan50: function() {
        var number = $(this).find('.number').text();
        return parseInt( number, 10 ) > 50;
      },
      // show if name ends with -ium
      ium: function() {
        var name = $(this).find('.name').text();
        return name.match( /ium$/ );
      }
    };
    // bind filter button click
    $('.filters-button-group,.filters-button-group-two').on( 'click', 'a', function() {
      var filterValue = $( this ).attr('data-filter');
      // use filterFn if matches value
      filterValue = filterFns[ filterValue ] || filterValue;
      $grid.isotope({ filter: filterValue });
    });
    // change is-checked class on buttons
    $('.filters-button-group,.filters-button-group-two').each( function( i, buttonGroup ) {
      var $buttonGroup = $( buttonGroup );
      $buttonGroup.on( 'click', 'a', function() {
        $buttonGroup.find('.is-checked').removeClass('is-checked');
        $( this ).addClass('is-checked');
      });
    });
});
